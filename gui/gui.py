import os, sys
sys.path.append(os.getcwd())

import streamlit as st

from chat.chatbot import chatbot_chain

st.title(":blue[Chatbot] :green[by Langchain]")

query = st.chat_input("Enter your query")

if query:
    with st.chat_message("human"):
        st.write(query)

    with st.chat_message("ai"):
        st.write_stream(chatbot_chain.stream(query))