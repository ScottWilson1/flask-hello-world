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
