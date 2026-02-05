import streamlit as st
import requests

st.set_page_config(page_title="Azure AI Foundry Agent", layout="centered")
st.title("🤖 Azure AI Foundry Multi-Tool Assistant")

user_input = st.text_input("Ask me anything")

if st.button("Send") and user_input:
    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"user_input": user_input}
    )
    st.markdown("### Response")
    st.write(response.json()["response"])
