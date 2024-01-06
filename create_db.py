import sqlite3

# データベース接続
conn = sqlite3.connect('data.db')
c = conn.cursor()

# テーブル作成
c.execute('''
    CREATE TABLE IF NOT EXISTS userstime (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        favorite TEXT,
        name_timestamp REAL,
        favorite_timestamp REAL
    )
''')
conn.commit()

# データベースクローズ
conn.close()
