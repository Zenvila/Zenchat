from app import create_app
import sqlite3

def init_db():
    conn = sqlite3.connect('chat.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            msg TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.close()

app = create_app()

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)

