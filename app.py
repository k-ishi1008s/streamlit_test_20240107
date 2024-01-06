import streamlit as st
import sqlite3
import time

# Streamlitアプリのタイトル
st.title('ユーザー情報入力アプリ')

# データベース接続
conn = sqlite3.connect('data.db')
c = conn.cursor()

# st.session_stateにデータ保存用の辞書を用意
if 'timestamps' not in st.session_state:
    st.session_state.timestamps = {'name': None, 'favorite': None}

# 入力フォーム
name = st.text_input('氏名を入力してください:')
favorite = st.text_input('好きなものを入力してください:')

# 氏名が入力されたときにタイムスタンプを更新
if name:
    st.session_state.timestamps['name'] = time.time()

# 好きなものが入力されたときにタイムスタンプを更新
if favorite:
    st.session_state.timestamps['favorite'] = time.time()

# 保存ボタンがクリックされたときのみデータベースへ保存
if st.button('保存'):
    # 文字列のカンマを取り除いてデータベースへ保存
    name = name.replace(',', '') if name else None
    favorite = favorite.replace(',', '') if favorite else None
    
    # データベースへ保存
    c.execute('INSERT INTO userstime (name, favorite, name_timestamp, favorite_timestamp) VALUES (?, ?, ?, ?)',
              (name, favorite, st.session_state.timestamps['name'], st.session_state.timestamps['favorite']))
    conn.commit()
    st.success('情報が保存されました！')

# データベースからデータを取得
data = c.execute('SELECT * FROM userstime').fetchall()

# データを表示
st.subheader('データベース内のユーザー:')
if data:
    # テーブル形式で表示
    st.table(data)
else:
    st.warning('データベースにはまだ情報がありません。')

# データベースクローズ
conn.close()
