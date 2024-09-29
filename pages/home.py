import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import sqlite3

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1('Criado por:'),
    html.Div('João Pedro Borba Rodrigues do Colégio de Aplicação da UFRGS'),
]) 
def connect_db():
    conn = sqlite3.connect('')
    return conn
def get_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM students")
    students = cursor.fetchall()
    conn.close()
    return students
layout = html.Div([
    html.H3("Marcar Presença de Alunos", style={'textAlign': 'center'}),
    
    html.Label("Selecione o Aluno"),
    dcc.Dropdown(id='student-dropdown', options=[
        {'label': student[1], 'value': student[0]} for student in get_students()
    ], placeholder="Selecione um aluno"),
    
    html.Button('Marcar Presença', id='mark-present', n_clicks=0),
    html.Div(id='attendance-output', style={'marginTop': '20px', 'textAlign': 'center'}),
])
@dash.callback(
    Output('attendance-output', 'children'),
    Input('mark-present', 'n_clicks'),
    Input('student-dropdown', 'value')
)
def mark_attendance(n_clicks, student_id):
    if n_clicks > 0 and student_id:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE students SET present = 1 WHERE id = ?", (student_id,))
        conn.commit()
        conn.close()
        return f"Presença marcada para o aluno de ID {student_id}."
    return "Selecione um aluno e clique para marcar presença." 