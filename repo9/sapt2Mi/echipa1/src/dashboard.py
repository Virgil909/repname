from dash import html
import dash_bootstrap_components as dbc
from dash.dcc import Dropdown

from PivotTable import Pivottable, serve_pivot_layout
import pandas as pd
from Piechart import PieChart
from config import priority_input, status_input, severity_input, table_input, dropdown_query,require_input ,require_stats_input,feature_status_input,dropdown_traceability_configs,\
    crd_input, list_call, dropdown_configs
# from app import flask_server,dash_app
from dash.dependencies import Input, Output
from interogare import interogare
from config import feature_status_query
from utile import create_dropdown


def get_dataquery(query):
    engine = interogare()
    with engine.connect() as conn:
        data_grouped = pd.read_sql_query(query, con=conn)
    return data_grouped


def create_layout(dash_app, dropdowns_traceability=None):
    chart = PieChart(dash_app, **priority_input)
    chart1 = PieChart(dash_app, **status_input)
    chart2 = PieChart(dash_app, **severity_input)
    chart3 = PieChart(dash_app, **feature_status_input)
    chart4 = PieChart(dash_app, **crd_input)
    chartreq=PieChart(dash_app, **require_input)
    chartreqstats=PieChart(dash_app, **require_stats_input)
    pivot = Pivottable(**table_input)
    pivot.create_pivot()

    # Generează toate dropdown-urile
    dropdowns = [
        create_dropdown(
            id_dropdown=conf["id"],
            label=conf["label"],
            options=[],
            value=None,
            placeholder=conf["label"],
            multi=True
        ) for conf in dropdown_configs
    ]
    dropdown_traceability =  [
        create_dropdown(
            id_dropdown=conf["id"],
            label=conf["label"],
            options=[],
            value=None,
            placeholder=conf["label"],
            multi=True
        ) for conf in dropdown_traceability_configs
    ]

    layout = dbc.Container([
        dbc.Row([dbc.Col(dropdown, width=4) for dropdown in dropdowns]),
        dbc.Row([dbc.Col(chart.layout(), width=4),
                 dbc.Col(chart1.layout(), width=4),
                 dbc.Col(chart2.layout(), width=4)], className='mb-4'),

        dbc.Row([dbc.Col(chart3.layout(), width=4),
                dbc.Col(serve_pivot_layout(pivot), width=8)]),

        dbc.Row([dbc.Col(dropdown, width=4) for dropdown in dropdown_traceability]),

        dbc.Row([
                dbc.Col(chart4.layout(), width=4),
                dbc.Col(chartreq.layout(), width=4),
                dbc.Col(chartreqstats.layout(), width=4)
        ])
    ], fluid=True, className="px-4", style={"backgroundColor": "#a6a6a6", "minHeight": "100vh"})

    return layout

def register_callback(dash_app):
    for dropdown in dropdown_configs+dropdown_traceability_configs:
        @dash_app.callback(
            Output(dropdown["id"], "options"),
            Output(dropdown["id"], "value"),
            Input(dropdown["id"], "id"),
        )
        def update_options(_id, query=dropdown["query"]):
            from interogare import interogare
            engine = interogare()
            with engine.connect() as conn:
                df = pd.read_sql_query(query, con=conn)
            col = df.columns[0]
            options = [{'label': val, 'value': val} for val in df[col].dropna().unique()]
            return options, None

    @dash_app.callback(
        Output('pivot_table', 'data'),
        Output('pivot_table', 'columns'),
        [Input(drop_id, 'value') for drop_id in list_call]
    )
    def update_pivot_table(*dropdown_values):
        selected_filters = {drop_id: val for drop_id, val in zip(list_call, dropdown_values)}


        echipe = selected_filters.get('agile_team_dropdown', None)
        pivot = Pivottable(**table_input)
        pivot.update_pivot(echipe)
        return pivot.get_data(), pivot.get_columns()




