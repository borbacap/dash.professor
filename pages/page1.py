import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import sqlite3

# Registrar a página
dash.register_page(__name__, path='/presenca')

# Função para conectar ao banco de dados
def connect_db():
    conn = sqlite3.connect('students.db')
    return conn

# Função para obter a lista de alunos
def get_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM students")
    students = cursor.fetchall()
    conn.close()
    return students

# Layout da página de Presença
layout = html.Div([
    html.H3("Marcar Presença de Alunos", style={'textAlign': 'center'}),
    
    html.Label("Selecione o Aluno"),
    dcc.Dropdown(id='student-dropdown', options=[
        {'label': student[1], 'value': student[0]} for student in get_students()
    ], placeholder="Selecione um aluno"),
    
    html.Button('Marcar Presença', id='mark-present', n_clicks=0),
    html.Div(id='attendance-output', style={'marginTop': '20px', 'textAlign': 'center'}),
])

# Callback para marcar presença do aluno
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
