import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import sqlite3
dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1('Criado por:'),
    html.Div('João Pedro Borba Rodrigues do Colégio de Aplicação da UFRGS'),
]) 
