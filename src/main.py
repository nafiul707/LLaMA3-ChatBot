import os
import json
import requests
import streamlit as st

# configuring Groq API key
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))
GROQ_API_KEY = config_data["GROQ_API_KEY"]

# configuring streamlit page settings
st.set_page_config(
    page_title="LLaMA3 Chat",
    page_icon="🦙",
    layout="centered"
)

# initialize chat session in streamlit if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# streamlit page title
st.title("🤖 LLaMA3 - ChatBot")

# display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# input field for user's message
user_prompt = st.chat_input("Ask LLaMA3...")

if user_prompt:
    # add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # send user's message to Groq LLaMA3 and get a response
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama3-70b-8192",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant"},
                *st.session_state.chat_history
            ]
        }
    )

    # parse and display response
    if response.status_code == 200:
        assistant_response = response.json()["choices"][0]["message"]["content"]
    else:
        assistant_response = f"❌ Error: {response.text}"

    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)
