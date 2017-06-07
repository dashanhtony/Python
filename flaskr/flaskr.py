import os
import sqlite3
import pymysql
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

app = Flask(__name__)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

conn = pymysql.connect(host='127.0.0.1',user='root', password='mysql', database='test')
cursor = conn.cursor()
def init_db():
    with app.open_resource('schema.sql', mode='r') as f:
        cursor.execute(f.read())
        conn.commit()

init_db()
if __name__ == '__main__':
    app.run(port=8888)