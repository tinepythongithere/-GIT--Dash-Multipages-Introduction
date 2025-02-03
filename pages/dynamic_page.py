import dash
from dash import html, dcc
import dash_bootstrap_components as bdc
import pandas as pd

dash.register_page(__name__, path_template='/Profile_<id_profile>', title='dynamic page')

def set_profile(id_profile):
    db = pd.read_excel('./data/db.xlsx')
    return html.Div([
        html.H1("Profile"),
        html.H3(
            f"Prénom et Nom : {db.loc[db['Id'] == int(id_profile)]['Prénom'].iloc[0]} {db.loc[db['Id'] == int(id_profile)]['Nom'].iloc[0]}"),
        html.H3(f"Âge : {db.loc[db['Id'] == int(id_profile)]['Âge'].iloc[0]} ans"),
        html.H3(f"Classe : {db.loc[db['Id'] == int(id_profile)]['Classe'].iloc[0]}"),
        html.H3(f"Note Français: {db.loc[db['Id'] == int(id_profile)]['Note français'].iloc[0]}"),
        html.H3(f"Note Math : {db.loc[db['Id'] == int(id_profile)]['Note Math'].iloc[0]}"),
        html.H3(f"Note Anglais : {db.loc[db['Id'] == int(id_profile)]['Note Anglais'].iloc[0]}"),

    ], className="profile-container")


def layout(id_profile=None, **kwargs):
    return set_profile(id_profile)




