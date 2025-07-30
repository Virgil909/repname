from itertools import groupby
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px
import os




def interogare():
    POSTGRES_ADDRESS = os.environ["POSTGRES_ADDRESS"]
    POSTGRES_PORT = os.environ["POSTGRES_PORT"]
    POSTGRES_USERNAME = os.environ["POSTGRES_USERNAME"]
    POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
    POSTGRES_DBNAME = os.environ["POSTGRES_DBNAME"]

    postgres_str = ('postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'
                    .format(username=POSTGRES_USERNAME, password=POSTGRES_PASSWORD, ipaddress=POSTGRES_ADDRESS,
                            port=POSTGRES_PORT, dbname=POSTGRES_DBNAME))

    cnx=create_engine(postgres_str)

    return cnx
