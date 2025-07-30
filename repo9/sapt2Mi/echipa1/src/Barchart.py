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
from interogare import interogare



class BarChart(Chart):
    def __init__(self, app,query, id_graph, up_val, up_tit, up_names, up_height, up_width):
        self.app = app
        self.query=query
        self.id_graph = id_graph
        self.up_val = up_val
        self.up_tit = up_tit
        self.up_names = up_names
        self.up_height = up_height
        self.up_width = up_width

        self.query=query
        self.callback()

    def get_dataquery(self,query):
        engine = interogare()
        with engine.connect() as conn:
            data_grouped = pd.read_sql_query(query, con=conn)
        return data_grouped


    def layout(self):
        return html.Div([
            dcc.Graph(id=self.id_graph)
        ])


    def update_graph(self, *args):
        dff = self.get_dataquery(self.query)


        barchart = px.bar(
            data_frame=dff,
            x=self.up_names,
            y=self.up_val,
            title=self.up_tit,
            labels={'Sales Count': 'Number of Sales'}

        )
        return barchart



    def callback(self):
        @self.app.callback(
            Output(component_id=self.id_graph, component_property='figure'),
            [Input(component_id=self.id_graph, component_property='id')])
        def update(chart_id):
            return self.update_graph(chart_id)
