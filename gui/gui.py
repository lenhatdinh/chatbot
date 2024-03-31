import os, sys
sys.path.append(os.getcwd())

import streamlit as st

from chat.chatbot import chatbot_chain

st.set_page_config(
    page_title="General Chat",
    layout="centered",
)
st.title(":blue[Chatbot] :green[by Langchain]")

chat_window = st.container(border=True, height=500)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


for chat_round in st.session_state.chat_history[-20:]:
    with chat_window.chat_message("human"):
        st.text(chat_round["query"])

    with chat_window.chat_message("ai"):
        st.write(chat_round["response"])


if query := st.chat_input("Enter your query"):
    with chat_window.chat_message("human"):
        st.text(query)

    with chat_window.chat_message("ai"):
        with st.spinner("Generating..."):
            full_response = st.write_stream(chatbot_chain.stream(query))

    st.session_state.chat_history.append({
        "query": query,
        "response": full_response,
    })


if not st.session_state.chat_history:
    chat_window.info("Hello!👋  \nHow can I help you today?")


with st.sidebar:
    if "chat_name" not in st.session_state:
        st.session_state.chat_name = "New chat"

    st.page_link(page="gui.py", label=st.session_state.chat_name)

    st. divider()

    st.button(
        "Clear chat history",
        use_container_width=True,
        on_click=st.session_state.chat_history.clear,
    )

    with st.expander("Edit chat name"):
        col1, col2 = st.columns([1.5, 1])
        new_name = col1.text_input(
            label="Chat Name",
            value=st.session_state.chat_name,
            label_visibility="collapsed",
        )
        apply_button = col2.button("Apply")

        if new_name and apply_button:
            st.session_state.chat_name = new_name
            st.rerun()