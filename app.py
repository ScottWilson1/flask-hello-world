import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Scott in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect('postgresql://scott_lab10_db_user:WgJgy2PuSOVpBbpA9fBzzfP2L2Usrf4K@dpg-cvl0sdre5dus73bup9qg-a/scott_lab10_db')
    conn.close()
    return 'Database Connection Successful'

@app.route('/db_create')
def creating():
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

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect('postgresql://scott_lab10_db_user:WgJgy2PuSOVpBbpA9fBzzfP2L2Usrf4K@dpg-cvl0sdre5dus73bup9qg-a/scott_lab10_db')
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawahi', 'Leonard', 'Los Angeles', 'Clippers', 2),
        ('Scott', 'Wilson', 'CU Boulder', 'Buffaloes', 3308);
        ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Successfully Populated'

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect('postgresql://scott_lab10_db_user:WgJgy2PuSOVpBbpA9fBzzfP2L2Usrf4K@dpg-cvl0sdre5dus73bup9qg-a/scott_lab10_db')
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
        ''')
    records = cur.fetchall()
    conn.close()
    response_string=''
    response_string+='<table>'
    for player in records:
        response_string+='<tr>'
        for info in player:
            response_string+='<td>{}</td>'.format(info)
        response_string+='<tr>'
    response_string+='<table>'
    return response_string

@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect('postgresql://scott_lab10_db_user:WgJgy2PuSOVpBbpA9fBzzfP2L2Usrf4K@dpg-cvl0sdre5dus73bup9qg-a/scott_lab10_db')
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
        ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Successfully Dropped'


