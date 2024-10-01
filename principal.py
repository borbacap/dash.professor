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

    #Código da Sidebar, diretamente roubado do chat gpt
    
    html.Div(
        [
            html.H2("Menu", className="display-4"),
            html.Hr(),
            html.P("Navegação", className="lead"),
            dbc.Nav(
                [
                    dbc.NavLink("Página 1", href="/", active="exact", className="nav-item"),
                    dbc.NavLink("Página 2", href="/page-2", active="exact", className="nav-item"),
                    dbc.NavLink("Página 3", href="/page-3", active="exact", className="nav-item"),
                ],
                vertical=True,
                pills=True,
            ),
        ],
        style={
            "position": "fixed",
            "top": 0,
            "left": 0,
            "bottom": 0,
            "width": "16rem",
            "padding": "2rem 1rem",
            "background-color": "#f8f9fa",
        },
    ),
])
if __name__ == '__main__':
    app.run(debug=True)