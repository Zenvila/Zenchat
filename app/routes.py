from flask import Blueprint, request, render_template, redirect
import sqlite3
from datetime import datetime

chat = Blueprint('chat', __name__)

def get_db():
    conn = sqlite3.connect('chat.db')
    return conn

@chat.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        msg = request.form['msg']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        db = get_db()
        db.execute('INSERT INTO messages (username, msg, timestamp) VALUES (?, ?, ?)', (username, msg, timestamp))
        db.commit()
        db.close()
        return redirect('/')

    db = get_db()
    messages = db.execute('SELECT username, msg, timestamp FROM messages ORDER BY id DESC').fetchall()
    db.close()
    return render_template('index.html', messages=messages)

