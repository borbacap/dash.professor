import dash
from dash import Dash, html, dcc
import sqlite3
app = Dash(__name__, use_pages=True)
app.layout = html.Div([
    html.H1('Multi-page app with Dash Pages'),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
    dash.page_container
])
def connect_db():
    conn = sqlite3.connect('students.db')
    return conn
    conn.commit()
    conn.close()
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      name TEXT NOT NULL, 
                      age INTEGER NOT NULL, 
                      course TEXT NOT NULL
                    present BOOLEAN DEFAULT 0)''')
create_table() 
if __name__ == '__main__':
    app.run(debug=True)