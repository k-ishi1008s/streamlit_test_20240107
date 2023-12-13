import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('progressbar')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration:{i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done!!'

left_column, right_column = st.columns(2) #pythonのバージョンが古すぎてbeta_columnsをcolumnsにした
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')


expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')


#text  = st.text_input('あなたの趣味を教えてください')
#condition = st.slider('あなたの今の調子は', 0, 100, 50)

#'あなたの趣味：' , text ,'です'
#'コンディション：',condition

#if st.checkbox('show Image'):
#    img = Image.open('./images/1.png')
#   st.image(img, caption='ちいかわ', use_column_width=False)

