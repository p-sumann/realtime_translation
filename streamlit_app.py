
import streamlit as st
import requests

# Define the FastAPI endpoint
url_input = 'http://127.0.0.1:8000/inputs'
model_input = 'http://127.0.0.1:8000/models'


inputs = st.text_area("Enter Text")
st.text_input(label= "Languages that wanna translate to",placeholder='e.g en, fr, de')

models_btn = st.button('Translate')
if models_btn:
    url = f'http://127.0.0.1:8000/models/{inputs}'
    res = response = requests.get(url)
    heloo = str(res.json())
    st.write(heloo)

st.text_input("Check Transition ID", placeholder='Enter translation id')