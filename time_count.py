import streamlit as st
import time

def main():
    st.title('時間を測る')

    time_between_buttons = 0
    start_time = 0
    start_time_button = 0
    end_time = 0

    button1 = st.button("スタート")
    if button1:
        time_between_buttons = 0
        start_time = 0
        end_time = 0
        st.write("スタートした")
        start_time_button = time.time()
        st.write(start_time_button)

    start_time = start_time + start_time_button
    st.write(start_time)

    button2 = st.button("ストップ")
    if button2:
        st.write("ストップした")
        end_time = end_time + time.time()
        st.write(end_time)
        st.write(start_time)
        time_between_buttons = end_time - start_time
        # human_readable_time = format_time(time_between_buttons)
        st.write(f"時間：{time_between_buttons}")

# def format_time(seconds):
#     minutes, seconds = divmod(seconds, 60)
#     hours, minutes = divmod(minutes, 60)
#     return "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))

if __name__ == "__main__":
    main()
