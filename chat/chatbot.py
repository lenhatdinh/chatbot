from chat.chains import StreamableConversationChain
from chat.chat_models import chat_model_creators
from chat.memories import memory_creators

chain = StreamableConversationChain(
    llm=chat_model_creators["gpt-3.5-turbo"](),
    memory=memory_creators["0-window"](),
)

while True:
    query = input("\n>> ")
    if query.lower() == "q":
        break

    for output in chain.stream(query):
        print(output, end="")