import dash
from dash import html
import dash_daq as daq
import sqlite3
from dash import Input, Output

def connect_db():
    conn = sqlite3.connect('students.db')
    return conn

dash.register_page(__name__, path='/regitro-de-presencas')

def get_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM students")
    students = cursor.fetchall()
    conn.close()
    return students

layout = html.Div([
    html.H1('Registro de presenças'),
    html.Div('Registre aqui as presenças e faltas dos alunos'),
     daq.BooleanSwitch(id='Presente?', on=False),
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