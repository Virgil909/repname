from flask import Flask, render_template
import pandas as pd
from sqlalchemy import create_engine
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
from abc import abstractclassmethod, abstractmethod


class Chart():

    @abstractmethod
    def layout(self):
        pass
    @abstractmethod
    def update_graph(self, *args):
        pass
    @abstractmethod
    def callback(self):
        pass
