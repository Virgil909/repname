import pandas as pd

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px


# === Încarcă datele ===
df = pd.read_csv("sales_data.csv")

# === Creează aplicația Dash ===
app = dash.Dash(__name__)

# === Layout-ul aplicației ===
app.layout = html.Div([
    html.H2("Sales per Category"),

    html.Div([
        html.Label("Select Region:"),
        dcc.Dropdown(
            id="reg_drop",
            options=[{'label': r, 'value': r} for r in sorted(df['Region'].unique())],
            value=df['Region'][1],
            multi=False,
            placeholder="Select a region",
            style={"width": "50%"}
        )
    ], style={"margin-bottom": "20px"}),

    html.Div([
        html.Label("Select Category:"),
        dcc.Dropdown(
            id="cat_drop",
            options=[{'label': c, 'value': c} for c in sorted(df['Category'].dropna().unique())],
            value=[],
            multi=True,
            placeholder="Select category/categories",
            style={"width": "50%"}
        )
    ], style={"margin-bottom": "20px"}),

    dcc.Graph(id='bar_chart')
])

# === Callback pentru actualizarea graficului ===
@app.callback(
    Output('bar_chart', 'figure'),
    Input('reg_drop', 'value'),
    Input('cat_drop', 'value')
)
def update_bar_chart(selected_region, selected_categories):
    dff = df.copy()

    # Filtrare după regiune (dacă e selectată)
    if selected_region:
        dff = dff[dff['Region'] == selected_region]

    # Filtrare după categorii (dacă sunt selectate)
    if selected_categories:
        dff = dff[dff['Category'].isin(selected_categories)]

    # Grupare și numărare vânzări per categorie
    grouped = dff.groupby('Category')['Sales'].sum().reset_index(name='Total Sales')
    #grouped = dff.groupby('Category')['Sales'].sum()

    # Graficul bară
    if grouped.empty:
        fig = px.bar(title="No data to display")
    else:
        fig = px.bar(
            grouped,
            x='Category',
            y='Total Sales',
            title="Number of Sales per Category",
            labels={'Sales Count': 'Number of Sales'}
        )

    return fig

# === Pornește serverul Dash ===
if __name__ == '__main__':
    app.run(debug=True)

