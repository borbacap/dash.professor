import dash
from dash import Dash, html, dcc
import sqlite3
import dash_bootstrap_components as dbc
def create_table():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    # Criar a tabela 'students' se ela ainda não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL,
            present BOOLEAN DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()
app = Dash(__name__, use_pages=True)
app.layout = html.Div([
    html.H1('Multi-page app with Dash Pages'),
    dash.page_container,
])
html.Div(id="nav-bar", children=[
    dcc.Input(id="nav-toggle", type="checkbox")
]),
html.Div(id="nav-header", children=[
    html.A(id="nav-title", href="https://codepen.io", target="_blank", children=[
        html.I(className="fab fa-codepen", children="DEPEN"),
        html.L(
            htmlFor=("nav-toggle", html.Span(id="nav-toggle-burger"))
        )
    ]) 
])
html.Div(id="nav-content", children=[html.I(className="fas fa-palette")])
html.Div(id="nav-button"), html.I(className="fas fa-images"), html.Span("Assets")
#Código da Sidebar, diretamente roubado do chat gpt
if __name__ == '__main__':
    app.run(debug=True)