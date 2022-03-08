import streamlit as st
import numpy as np

def app():
    st.title('container with notaion')

    with st.container():
        st.write('this is inside container')
        st.bar_chart(np.random.randn(50,3))

