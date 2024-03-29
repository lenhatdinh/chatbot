from langchain.memory import (
    FileChatMessageHistory,
    ConversationBufferWindowMemory,
    ConversationBufferMemory,
)

def create_buffer_memory(**kwargs):
    return ConversationBufferMemory(
        chat_memory=FileChatMessageHistory(r"C:\PySpace\llm_projects\chatbot\chat\chat_history.json"),
        return_messages=True,
        **kwargs,
    )

def create_window_memory(k, **kwargs):
    return ConversationBufferWindowMemory(
        chat_memory=FileChatMessageHistory(r"C:\PySpace\llm_projects\chatbot\chat\chat_history.json"),
        return_messages=True,
        k=k,
        **kwargs,
    )