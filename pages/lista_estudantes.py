import dash
from dash import html, Output, Input
import sqlite3

# Registrar a página
dash.register_page(__name__, path='/list-students')

# Função para conectar ao banco de dados
def connect_db():
    conn = sqlite3.connect('students.db')
    return conn

# Layout da página de Listagem de Alunos
layout = html.Div([
    html.H3("Lista de Alunos Registrados", style={'textAlign': 'center'}),
    html.Ul(id='student-list', style={'textAlign': 'center', 'listStyleType': 'none'}),
])

# Callback para carregar a lista de alunos ao acessar a página
@dash.callback(
    Output('student-list', 'children'),
    Input('student-list', 'id')
)
def display_students(_):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()

    return [html.Li(f"{student[1]} - {student[2]} anos - Curso: {student[3]}") for student in students]
