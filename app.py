from dash import dash, html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dcc.Location(id='url'),
    dash.page_container
])

if __name__=='__main__':
    app.run_server(debug=False)