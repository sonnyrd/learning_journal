import dataviz
import hypottest
import uber
import streamlit as st

PAGES = {
    "Data Visualization": dataviz,
    "Hypothesis Testing": hypottest
}

st.sidebar.title('Navigation')
selected = st.sidebar.selectbox('select a page', list(PAGES.keys()))
page = PAGES[selected]

page.app()