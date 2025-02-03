import dash
from dash import html, dcc
import pandas as pd

dash.register_page(__name__, path='', title='Home')
def layout_home():
    db = pd.read_excel('./data/db.xlsx')

    return html.Div([
        html.H1('Liste des élèves', style={'text-align': 'center'}),
        html.A('Ajouter un élève', href='/add-student', className="title-box-animated"),
        html.Hr(),
        html.Table([
            html.Thead([
                html.Tr([
                    html.Th('Id'),
                    html.Th('Prénom'),
                    html.Th('Nom'),
                    html.Th('View')
                ])
            ]),
            html.Tbody([
                html.Tr([
                    html.Td(db.loc[row, ['Id']]),
                    html.Td(db.loc[row, ['Prénom']]),
                    html.Td(db.loc[row, ['Nom']]),
                    html.Td([html.A('View profile', href=f"Profile_{list(db.loc[row, ['Id']])[0]}"),
                             html.A('Supprimer', href=f"delete-{list(db.loc[row, ['Id']])[0]}",
                                    style={'background': 'red'})])
                ])
                for row in db.index])
        ])
    ])

layout = layout_home
