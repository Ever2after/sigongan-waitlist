import streamlit as st 
import pandas as pd 

df = pd.read_csv("./data.csv", index_col=0)
df['timeStamp'] = pd.to_datetime(df['timeStamp']+9*3600, unit='s')

pwd = st.text_input("토큰 입력")
btn = st.button("완료")
if btn or pwd:
    if pwd=="^gongan2^":
        st.dataframe(df)