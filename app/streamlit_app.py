
import streamlit as st
import requests

url = 'http://127.0.0.1:8000/translate'

text = st.text_area("Enter Text")
lang = st.text_input(label= "Languages that wanna translate to",placeholder='e.g en, fr, de')
lang = lang.split(',')
data = {
    'text' : text,
    'languages' : lang
}

models_btn = st.button('Translate')
if models_btn:
    res = response = requests.post(url, json=data)
    heloo = str(res.json())
    st.write(heloo)

# st.text_input("Check Transition ID", placeholder='Enter translation id')
# col1, col2 = st.columns(2)

# with col1:
#     check_status_btn = col1.button('Check Status', key='status')

# with col2:
#     check_translation_btn = col2.button('Check Translation', key='translation')

# if check_status_btn:
#     st.write("Status button clicked")

# if check_translation_btn:
#     st.write("Translation button clicked")