import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd

dash.register_page(__name__, path='/add-student', title='Ajout')

layout = html.Div([
    html.H1('Ajout'),

    html.H3('Prénom : '),
    dcc.Input(id='prenom', type='text'),

    html.H3('Nom : '),
    dcc.Input(id='nom', type='text'),

    html.H3('Âge : '),
    dcc.Input(id='age', type='number', min=14, max=40),

    html.H3('Classe'),
    dcc.Dropdown(['C1', 'C2'],id='classe'),

    html.H3('Note français'),
    dcc.Input(id='fr', type='number', min=0, max=20),

    html.H3('Note Anglais'),
    dcc.Input(id='en', type='number', min=0, max=20),

    html.H3('Note Math'),
    dcc.Input(id='math', type='number', min=0, max=20),
    html.Br(),
    dbc.Button('Ajouter',id='btn')
], className="profile-container")

@callback(
    Output('url', 'pathname',allow_duplicate=True),
    Input('btn','n_clicks'),
    State('prenom','value'),
    State('nom','value'),
    State('age','value'),
    State('classe','value'),
    State('fr','value'),
    State('en','value'),
    State('math','value'),
    prevent_initial_call=True
)
def ajouter(btn,prenom,nom,age,classe,fr,en,math):
    if btn:
        db = pd.read_excel('./data/db.xlsx')
        new_ligne=pd.DataFrame([{'Id':db['Id'].max()+1,
                   'Prénom':prenom,
                   'Nom':nom,
                   'Âge':age,
                   'Classe': classe,
                   'Note français':fr,
                   'Note Anglais':en,
                   'Note Math':math}])
        db = pd.concat([db,new_ligne],ignore_index=True)
        db.to_excel('./data/db.xlsx', index=False)

        return ''
