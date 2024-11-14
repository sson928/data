import streamlit as st
import pandas as pd

if "ID" not in st.session_state:
    st.session_state["ID"] = "None"

ID = st.session_state["ID"]
with st.sidebar:
    st.caption(f'{ID}님 접속중')
data = pd.read_csv("light.csv")

st.title('관악구에서 폐건전지와 폐형광등은 어디다 버릴까?')


data = data.copy().fillna(0)
data.loc[:,'size'] = 5*(data['Used battery']+data['Integrated'])
data


color = {'Used battery':'#87CEEB',
         'Integrated':'#FFA500'}
data.loc[:,'color'] = data.copy().loc[:,'운영방식'].map(color)


st.map(data, latitude="위도",
       longitude="경도",
       size="size",
       color="color")
