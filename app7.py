# app.py
import streamlit as st
import sqlite3
import time
import os
from datetime import datetime
import pandas as pd
from PIL import Image
import asyncio

# タイトル
st.title("20240106TEST")

# ユーザー名入力フォーム
user_name = st.text_input('ユーザー名をアルファベットで入力してください:')

# データベース接続
conn = sqlite3.connect('data_timestamp.db')
c = conn.cursor()

# ユーザーごとのテーブルを作成
c.execute(f'''
    CREATE TABLE IF NOT EXISTS {user_name}(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        image_number INTEGER,
        input_text TEXT,
        time REAL
    )
''')
conn.commit()

# 画像表示のための準備
imgsum = 3
sleeptime = 5  # 表示時間
image_folder = './images/'
blackImg = Image.open(image_folder + 'black.png')

# st.session_stateに解答時間を用意する
if 'timestamps' not in st.session_state:
    st.session_state.timestamps = {f'{i+1}': {'start': None, 'save': None} for i in range(imgsum)}
    
# 一定時間のみ画像を表示する関数
async def display_image(i):
    img = Image.open(image_folder + f'{imgIndex}.png')
    showImg.image(img)
    await asyncio.sleep(sleeptime)
    showImg.image(blackImg)

try:
    for imgIndex in range(1, imgsum + 1):
        showImg = st.empty()
        # はじめは黒画像
        showImg.image(blackImg)
        
        if st.button(f'{imgIndex}.pngを表示'):
            # 表示ボタンがクリックされたときにタイムスタンプを更新
            st.session_state.timestamps[f'{imgIndex}']['start'] = time.time()
            # 画像を表示
            asyncio.run(display_image(imgIndex))

        # 入力フォーム
        input_text = st.text_input(f'({imgIndex})何に見えますか？')

        if st.button(f'解答を保存({imgIndex})'):
            # タイムスタンプを更新
            st.session_state.timestamps[f'{imgIndex}']['save'] = time.time()

            # 解答にかかった時間を計算
            elapsed_time = st.session_state.timestamps[f'{imgIndex}']['save'] - st.session_state.timestamps[f'{imgIndex}']['start']

            #データベースへ保存
            c.execute(f'INSERT INTO {user_name}(image_number,input_text,time) VALUES (?, ?, ?)',
                    (imgIndex, input_text, elapsed_time))
            conn.commit()
            st.success('保存完了')
            
    # データベースからデータを取得
    data = c.execute(f'SELECT * FROM {user_name}').fetchall()
    
    # データを表示
    st.subheader('只今の入力情報:')
    if data:
        #　テーブル形式で表示
        st.table(data)
    else:
        st.warning('データベースにはまだ情報がありません')
    
    #終了ボタンがクリックされた時にエクセルファイルを出力
    if st.button('終了'):
        # データベースから全データを取得
        all_data = c.execute(f'SELECT * FROM {user_name}').fetchall()
        
        # DataFrameに変換
        df = pd.DataFrame(all_data, columns=['id', 'image_number', 'input_text', 'time'])
        
        # カレントディレクトリを取得
        current_directory = os.getcwd()
        
        # 日時を取得してフォーマット
        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        
        # ファイル名に日時を含めて書き込み
        excel_filename = f'{user_name}_user_data_{current_time}.xlsx'
        relative_filepath = os.path.join('./data', excel_filename)
        df.to_excel(relative_filepath, index=False)
        st.success(f'エクセルファイルが {relative_filepath} に出力されました！')
    

finally:
    # データベースクローズ
    conn.close()
