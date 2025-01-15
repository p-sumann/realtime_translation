import os

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv(override=True)

BASE_URL = os.getenv("BASE_URL")

text = st.text_area("Enter Text")
lang = st.text_input(
    label="Languages that wanna translate to", placeholder="e.g en, fr, de"
)

lang = lang.split(",")
data = {"text": text, "languages": lang}

models_btn = st.button("Translate")
with st.spinner("Translating.....") as spinner:
    if models_btn:
        try:
            res = requests.post(f"{BASE_URL}translate", json=data)
            heloo = res.json()
            st.write(f'Your translation ID is: *{heloo.get('task_id')}*')
        except Exception as e:
            st.error(f"Error fetching translation API: {e}")


translation_id = st.text_input(
    "Check Transition ID", placeholder="Enter translation id"
)
check_status_btn = st.button("Check Status", key="status")

if check_status_btn:
    try:
        url = f"{BASE_URL}translation/{translation_id}"
        res = requests.get(url)
        if res.status_code == 200:
            st.write(res.json()["translations"])
        if res.status_code == 404:
            st.write(f'Translation ID: *{translation_id}* doesn"t exist')
    except Exception as e:
        st.error(f"error processing translation {e}")
