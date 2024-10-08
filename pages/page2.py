import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import sqlite3

# Registrar a página
dash.register_page(__name__, path='/registrar-alunos')

# Função para conectar ao banco de dados
def connect_db():
    conn = sqlite3.connect('students.db')
    return conn

# Layout da página Home
layout = html.Div([
    html.H2("Registrar Novo Aluno", style={'textAlign': 'center'}),

    dcc.Input(id='name', type='text', placeholder='Nome', required=True),
    dcc.Input(id='age', type='number', placeholder='Idade', required=True),
    dcc.Input(id='course', type='text', placeholder='Curso', required=True),
    html.Button('Registrar', id='submit', n_clicks=0),
    
    html.Div(id='output', style={'marginTop': '20px', 'textAlign': 'center'}),
])

# Callback para registrar um aluno no banco de dados
@dash.callback(
    Output('output', 'children'),
    Input('submit', 'n_clicks'),
    [State('name', 'value'), State('age', 'value'), State('course', 'value')]
)
def register_student(n_clicks, name, age, course):
    if n_clicks > 0:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
        conn.commit()
        conn.close()
        return f"Aluno {name} registrado com sucesso!"
    return ""