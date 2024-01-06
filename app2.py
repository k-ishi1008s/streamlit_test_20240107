# app.py
import streamlit as st
import sqlite3
import time
import os
from datetime import datetime
import pandas as pd

# Streamlitアプリのタイトル
st.title('タイムスタンプつきユーザー情報入力アプリ')

# データベース接続
conn = sqlite3.connect('data_timestamp.db')
c = conn.cursor()

# st.session_stateにデータ保存用の辞書を用意
if 'timestamps' not in st.session_state:
    st.session_state.timestamps = {'start': None, 'save': None}

# スタートボタンがクリックされたときにタイムスタンプを更新
if st.button('スタート'):
    st.session_state.timestamps['start'] = time.time()

# 入力フォーム
input_text = st.text_input('入力してください:')

# 保存ボタンがクリックされたときのみデータベースへ保存
if st.button('保存'):
    # タイムスタンプを更新
    st.session_state.timestamps['save'] = time.time()

    # 解答にかかった時間を計算
    elapsed_time = st.session_state.timestamps['save'] - st.session_state.timestamps['start']

    # データベースへ保存
    c.execute('INSERT INTO userstime2 (input_text, time) VALUES (?, ?)',
              (input_text, elapsed_time))
    conn.commit()
    st.success('情報が保存されました！')

# データベースからデータを取得
data = c.execute('SELECT * FROM userstime2').fetchall()

# データを表示
st.subheader('データベース内のユーザー:')
if data:
    # テーブル形式で表示
    st.table(data)
else:
    st.warning('データベースにはまだ情報がありません。')

# 終了ボタンがクリックされたときにエクセルファイルを出力
if st.button('終了'):
    # データベースから全データを取得
    all_data = c.execute('SELECT * FROM userstime2').fetchall()

    # DataFrameに変換
    df = pd.DataFrame(all_data, columns=['id', 'input_text', 'time'])

    # カレントディレクトリを取得
    current_directory = os.getcwd()

    # 日時を取得してフォーマット
    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    # ファイル名に日時を含めて書き込み
    excel_filename = f'user_data_{current_time}.xlsx'
    relative_filepath = os.path.join('./data', excel_filename)
    df.to_excel(relative_filepath, index=False)
    st.success(f'エクセルファイルが {relative_filepath} に出力されました！')

# データベースクローズ
conn.close()
