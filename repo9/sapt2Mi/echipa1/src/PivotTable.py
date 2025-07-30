from dash import dash_table
import dash_bootstrap_components as dbc
from dash import html
import pandas as pd
from interogare import interogare


class Pivottable:
    def __init__(self,query , index_col, columns_col):
        self.query=query
        self.index_col = index_col
        self.columns_col = columns_col
        self.pivot_table = None

    def get_dataquery(self, echipe=None):
        query_template = self.query

        if echipe:
            # Asigură-te că e listă, și escape pentru SQL injection (safe-ish pt testare)
            if isinstance(echipe, str):
                echipe = [echipe]
            echipe_sql = ", ".join(f"'{e}'" for e in echipe)
            filter_str = f"AND agile_team IN ({echipe_sql})"
        else:
            filter_str = ""

        if "{aditional_filter}" in query_template:
            query = query_template.replace("{aditional_filter}", filter_str)
        else:
            query = query_template

        engine = interogare()
        with engine.connect() as conn:
            data_grouped = pd.read_sql_query(query, con=conn)

        return data_grouped

    def update_pivot(self, echipa=None):
        df = self.get_dataquery(echipa)
        self.pivot_table = pd.pivot_table(
            df,
            index=self.index_col,
            columns=self.columns_col,
            aggfunc='size',
            fill_value=0
        )
        self.pivot_table['Total'] = self.pivot_table.sum(axis=1)
        total_row = self.pivot_table.sum(numeric_only=True)
        total_row.name = 'Total'
        self.pivot_table = pd.concat([self.pivot_table, pd.DataFrame([total_row])])
        self.pivot_table = self.pivot_table.reset_index()


    def create_pivot(self):
        df = self.get_dataquery()  # nu mai trimiți self.query ca argument
        self.pivot_table = pd.pivot_table(
        df,
        index=self.index_col,
        columns=self.columns_col,
        aggfunc='size',
        fill_value=0
    )
        self.pivot_table['Total'] = self.pivot_table.sum(axis=1)
        total_row = self.pivot_table.sum(numeric_only=True)
        total_row.name = 'Total'
        self.pivot_table = pd.concat([self.pivot_table, pd.DataFrame([total_row])])
        self.pivot_table = self.pivot_table.reset_index()


    def get_columns(self):
        return [{'name': col, 'id': col} for col in self.pivot_table.columns.astype(str)]


    def get_data(self):
        return self.pivot_table.to_dict('records')


def serve_pivot_layout(pivot: Pivottable):
    return dbc.Container([
        html.H3("Open PRs by Priority and Status", style={'textAlign': 'center'}),

        dash_table.DataTable(
            id='pivot_table',
            columns=pivot.get_columns(),
            data=pivot.get_data(),
            page_size=10,
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'center', 'minWidth': '100px', 'maxWidth': '180px', 'whiteSpace': 'normal'},
            style_data_conditional=[
                {
                    'if': {'filter_query': '{Status} = "Total"'},
                    'backgroundColor': 'rgb(240, 255, 255)',
                    'fontWeight': 'bold'
                }
            ],
            sort_action='native',
            page_action='native'
        )
    ])
