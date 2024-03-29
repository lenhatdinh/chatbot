from chat.chains import StreamableConversationChain
from chat.chat_models import chat_model_creators
from chat.memories import memory_creators

chatbot_chain = StreamableConversationChain(
    llm=chat_model_creators["gpt-3.5-turbo"](),
    memory=memory_creators["10-window"](),
)

if __name__ == "__main__":
    while True:
        query = input("\n>> ")
        if query.lower() == "q":
            break

        for output in chatbot_chain.stream(query):
            print(output, end="")