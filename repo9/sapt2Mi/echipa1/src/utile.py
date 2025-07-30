from flask import Flask, render_template
import pandas as pd
from sqlalchemy import create_engine
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
from abc import abstractclassmethod, abstractmethod



def create_dropdown(id_dropdown, label="Selectează:", **kwargs):

    return html.Div([
        html.Label(label),
        dcc.Dropdown(
            id=id_dropdown,
            **kwargs

        )
        ], style={"margin-bottom": "20px"})

