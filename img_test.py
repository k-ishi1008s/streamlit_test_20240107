import streamlit as st
import numpy as np
from PIL import Image
import time
import asyncio
import datetime

st.title('画像を表示')

sleeptime = 5

blackImg = Image.open('./images/black.png')
showImg = st.empty()
showImg.image(blackImg)

start_time = 0
end_time = 0
index='1'

button_clicked = st.button("表示")

async def display_image(i):
    img = Image.open('./images/'+ i +'.png')
    showImg.image(img)
    await asyncio.sleep(sleeptime)
    showImg.image(blackImg)

if st.button("表示"):
    start_time = start_time + time.time()
    st.write(start_time)
    asyncio.run(display_image(index))

option = st.text_input('何に見える？')

if option:
    end_time = end_time + time.time()
    st.write(end_time)
    elapsed_time = (end_time - start_time).total_seconds()
    st.write(f"ボタンが押されてからエンターキーが押されるまでの時間: {elapsed_time:.2f}秒")
    '入力：',option

