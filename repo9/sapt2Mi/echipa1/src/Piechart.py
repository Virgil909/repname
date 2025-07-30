from flask import Flask, render_template
import pandas as pd
from sqlalchemy import create_engine
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
from abc import abstractclassmethod, abstractmethod
from Chart import Chart
from config import list_call
from config import dropdown_configs, list_call


from interogare import interogare


class PieChart(Chart):
    def __init__(self, app, query, id_graph, up_val, up_tit, up_names, up_height, up_width,
                 hole=0, filter_dropdown_ids=None, color_scheme=None):
        self.app = app
        self.query = query
        self.id_graph = id_graph
        self.up_val = up_val
        self.up_tit = up_tit
        self.up_names = up_names
        self.up_height = up_height
        self.up_width = up_width
        self.hole = hole
        self.filter_dropdown_ids = filter_dropdown_ids or []  # ex: ['echipe_dropdown'], sau ['domain_dropdown']
        self.color_scheme = color_scheme or ['#FFA500', 'blue', 'purple', 'yellow', 'pink', 'brown']

        self.callback()

    def get_dataquery(self, filter_values=None):
        engine = interogare()

        filter_clauses = []

        for drop_id, values in (filter_values or {}).items():
            if values:
                if not isinstance(values, list):
                    values = [values]
                col_name = drop_id.replace("_dropdown", "")  # ex: echipe_dropdown → echipe
                values_quoted = ", ".join(f"'{v}'" for v in values)
                if drop_id == "test_level_dropdown":
                    filter_clauses.append(f"c.test_level IN ({values_quoted})")

                elif drop_id == "requirement_level_dropdown":
                    filter_clauses.append(f"c.requirement_level IN ({values_quoted})")

                else:
                    # fallback, coloane fara alias
                    col_name = drop_id.replace("_dropdown", "")
                    filter_clauses.append(f"{col_name} IN ({values_quoted})")

        if filter_clauses:
            filter_sql = " AND " + " AND ".join(filter_clauses)
        else:
            filter_sql = ""

        if "{aditional_filter}" in self.query:
            query = self.query.replace("{aditional_filter}", filter_sql)
        else:
            query = self.query

        with engine.connect() as conn:
            df = pd.read_sql_query(query, con=conn)

        return df

    def layout(self):
        return html.Div([
            dcc.Graph(id=self.id_graph)
        ])

    def update_graph(self, filter_values):
        df = self.get_dataquery(filter_values)

        fig = px.pie(
            data_frame=df,
            values=self.up_val,
            names=self.up_names,
            title=self.up_tit,
            color_discrete_sequence=self.color_scheme,
            hole=self.hole,
            height=self.up_height,
            width=self.up_width
        )

        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            annotations=[dict(
                text="Total<br>{}".format(df[self.up_val].sum()),
                x=0.5,
                y=0.5,
                font_size=20,
                showarrow=False
            )]
        )

        return fig

    def callback(self):
        if not self.filter_dropdown_ids:
            return  # Dacă nu există dropdownuri, nu creez callback

        @self.app.callback(
            Output(self.id_graph, 'figure'),
            [Input(drop_id, 'value') for drop_id in self.filter_dropdown_ids]
        )
        def update(*values):
            filters = {drop_id: val for drop_id, val in zip(self.filter_dropdown_ids, values)}
            return self.update_graph(filters)
