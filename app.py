import streamlit as st
from openai import OpenAI
import os

# 🔑 API key from Streamlit secrets
client = OpenAI(api_key=os.getenv("OPENAI_API_KEYsk-proj-tDgL4Xyr_ifz753XBRwjJ08Xc09GcZpd612iwJK9F9XzHIN9vMsNofdfT410zykjCOkdaD-9TYT3BlbkFJB9M-luARCbcyWiRpcl-EEQx-xG1GUhKveaii26VhFJekHMUYP8HvjnTvup3P0VriwSsC_I9cMA"))

# 🧠 Memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.set_page_config(page_title="UON Chatbot", page_icon="🎓")

st.title("🎓 UON Student Assistant")

# 💬 Show chat history
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 🤖 AI chatbot function
def ai_chatbot(user_input):
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful University of Northampton assistant. Include useful links when possible."}
        ] + st.session_state.chat_history
    )

    reply = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": reply})

    return reply

# 💬 Input
user_input = st.chat_input("Ask me anything...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    response = ai_chatbot(user_input)

    with st.chat_message("assistant"):
        st.write(response)

# 🔄 Clear chat button
if st.button("Clear Chat"):
    st.session_state.chat_history = []
