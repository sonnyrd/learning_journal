# Simple logic multi page

import streamlit as st
from PIL import Image
import numpy as np

#####
st.sidebar.title('select a page')

selected = st.sidebar.selectbox("page : ",["Data Visualization","Hypothesis Testing"])

if selected == "Data Visualization":
    col1, col2, col3 = st.columns(3)
    img = Image.open('2-4.jpg')

    st.title('eiffel Tower')
    st.image(img, caption='eiffel tower')

    with col1:
        st.write("ini kolom 1")
        st.image(img, caption='eiffel tower')

    with col2:
        st.write("ini kolom 2")
        st.image(img, caption='eiffel tower')

    with col3:
        st.write("ini kolom 3")
        st.image(img, caption='eiffel tower')

else :
    st.title('Hypothesis testing')
    st.write('demo hypothesis testing')