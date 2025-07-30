from flask import Flask, render_template
import pandas as pd
from sqlalchemy import create_engine
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import os
import dash_bootstrap_components as dbc

from dashboard import create_layout,register_callback

#-----------------------------ZONA PORNIRE FLASK/DASH-----------------------------------------
flask_server = Flask(__name__)
@flask_server.route('/')
def home():
    return render_template('index.html')


dash_app = dash.Dash(
    __name__,
    server=flask_server,
    url_base_pathname='/dash/',
    external_stylesheets=[dbc.themes.BOOTSTRAP]

)

dash_app.layout = create_layout(dash_app)
register_callback(dash_app)

flask_server.run(debug=True)

# register_callbacks(dash_app)


