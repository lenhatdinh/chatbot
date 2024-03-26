from queue import Queue
from langchain_core.callbacks import BaseCallbackHandler


class StreamHandler(BaseCallbackHandler):
    def __init__(self):
        self.token_queque = Queue()

    def on_llm_new_token(self, token, **kwargs):
        self.token_queque.put(token)

    def on_llm_end(self, response, **kwargs):
        self.token_queque.put(None)

    def on_llm_error(self, error, **kwargs):
        self.token_queque.put(None)