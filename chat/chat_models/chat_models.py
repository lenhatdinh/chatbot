import os

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

os.unsetenv("http_proxy")
os.unsetenv("https_proxy")

def create_chatgpt(model, **kwargs):
    return ChatOpenAI(model=model, streaming=True, **kwargs)

def create_gemini(model, **kwargs):
    return ChatGoogleGenerativeAI(model=model, **kwargs)