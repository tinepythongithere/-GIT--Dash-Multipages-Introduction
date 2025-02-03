import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as bdc
import pandas as pd

dash.register_page(__name__, path_template='/delete-<id_profile>', title='Ajout')

def layout(id_profile=None, **kwargs):
    return html.Div()

@callback(
    Output('url', 'pathname'),
    Input('url', 'pathname'),
    prevent_initial_call=True
)
def delete(path):
    id = int(path[8:])
    db = pd.read_excel('./data/db.xlsx')

    db = db.loc[db['Id']!=id]

    try:
        db.to_excel('./data/db.xlsx', index=False)
    except Exception as e:
        print(e)

    return ''