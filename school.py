import streamlit as st
import pandas as pd

st.set_page_config(page_title=
st.set_page_config(pa

st.set_page_confi

st.set_page_c

st.set_p

st.
"지역별 다문화가정 학생수 현황", layout="wide")
st.title(
st.title

st.t
"지역별 다문화가정 학생수 현황")

data = pd.read_csv("다문화가정학생현황.csv")

if "ID" not in st.session_state:
    st.session_state["ID"] = "None"

ID = st.session_state["ID"]

with st.sidebar:
    st.caption(f'{ID}님 접속중')
    
with st.form("input"):
    region = st.multiselect("지역", data['Region'].unique())
    school = st.multiselect("학교", data['School'].unique())
    family = st.multiselect("가정형태", data['Family'].unique())
    submitted = st.form_submit_button("조회")
    
    if submitted:
        name_list = []
        result = data["Year"].drop_duplicates().sort_values().reset_index(drop=True)
        for re in region:
            for sc in school:
                for fa in family:
                    name = f"{re}_{sc}_{fa}"
                    name_list.append(name)
                    selected_df = data[(data['Region'] == re) & (data['School'] == sc)& (data['Family'] == fa)]
                    selected_df = selected_df[["Year","Students"]].rename(columns={"Students": name})
                    result = pd.merge(result, selected_df, on='Year').sort_values('Year')
        
        st.line_chart(data=result, x='Year', y=name_list,use_container_width=True)
        
