import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Scott in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://scott_lab10_db_user:WgJgy2PuSOVpBbpA9fBzzfP2L2Usrf4K@dpg-cvl0sdre5dus73bup9qg-a/scott_lab10_db")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect('postgresql://scott_lab10_db_user:WgJgy2PuSOVpBbpA9fBzzfP2L2Usrf4K@dpg-cvl0sdre5dus73bup9qg-a/scott_lab10_db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(225),
            Last varchar(225),
            City varchar(225),
            Name varchar(225),
            Number int
        );
        ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Successfully Created'

