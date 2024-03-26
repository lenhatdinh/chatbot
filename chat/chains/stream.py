from threading import Thread

from langchain.chains import (
    ConversationChain,
    LLMChain,
)
from langchain_core.runnables import Runnable

from chat.handlers import StreamHandler


class StreamableChainMixin:
    def stream(self: Runnable, input):
        config = {"callbacks": [handler := StreamHandler(),]}
        Thread(target=self.invoke, args=(input, config)).start()

        while (token := handler.token_queque.get()) is not None:
            yield token


class StreamableConversationChain(
    StreamableChainMixin,
    ConversationChain,
):
    pass


class StreamableLLMChain(
    StreamableChainMixin,
    LLMChain,
):
    pass