import streamlit as st
from PIL import Image
import numpy as np

### Set page config
### Jika multi page simpan di main page saja
st.set_page_config(
    page_title="Sonny Stream Lite",
    page_icon="💲",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.google.com',
        'Report a bug': 'https://github.com/sonnyrd',
        'About': "# Practice Streamlite"
    }
)

### load image
img = Image.open('2-4.jpg')

st.title('eiffel Tower')
st.image(img, caption='eiffel tower')

### Make Column
col1, col2, col3 = st.columns(3)

with col1:
    st.write("ini kolom 1")
    st.image(img, caption='eiffel tower')

with col2:
    st.write("ini kolom 2")
    st.image(img, caption='eiffel tower')

with col3:
    st.write("ini kolom 3")
    st.image(img, caption='eiffel tower')

## Make Colum with ratio
col_1, col_2 = st.columns([3,1])

data = np.random.rand(10,1)

col_1.write("kolom pertama")
col_1.line_chart(data)

col_2.write("kolom kedua")
col_2.image("https://static.streamlit.io/examples/dog.jpg")

### Container with Notation
st.title('container with notaion')

with st.container():
    st.write('this is inside container')
    st.bar_chart(np.random.randn(50,3))

st.write('this is outside container')

### Container using variable
st.title("Container Using Variable")

cont = st.container()
cont.write("this is inside container 1")

st.write("this is outside container")

cont.write('this is inside coutnaner 2')

#### Expander
st.title("expander")
st.line_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
  st.write("""
     The chart above shows some numbers I picked for you.
     I rolled actual dice for these, so they're *guaranteed* to
     be random.
  """)

  st.image("https://static.streamlit.io/examples/dice.jpg")

 
