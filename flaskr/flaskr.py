import os
import sqlite3
import pymysql
import configparser
from flask import Flask, request, session, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

conn = pymysql.connect(host='127.0.0.1',user='root', password='mysql', database='test')
cursor = conn.cursor()
cf = configparser.ConfigParser()
cf.read('flaskr.conf')
app.secret_key = cf['SECRET_KEY']['SECRET_KEY']
def init_db():
    with app.open_resource('schema.sql', mode='r') as f:
        cursor.execute(f.read())
        conn.commit()

@app.route('/index')
def indexpage():
    return '<b>This is indexpage /</b>'

@app.route('/')
def show_entries():
    cursor.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cursor.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    cursor.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    conn.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != cf['USER']['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != cf['USER']['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            print(session)
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


init_db()
if __name__ == '__main__':
    app.debug = True
    app.run(port=18888)