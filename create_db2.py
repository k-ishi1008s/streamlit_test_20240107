import sqlite3

# データベース接続
conn = sqlite3.connect('data_timestamp.db')
c = conn.cursor()

# テーブルが存在しない場合は作成
c.execute('''
    CREATE TABLE IF NOT EXISTS userstime2 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        input_text TEXT,
        time REAL
    )
''')

# データベースクローズ
conn.close()
