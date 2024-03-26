from functools import partial
from .chat_models import (
    create_gemini,
    create_chatgpt,
)

chat_model_creators = {
    "gpt-3.5-turbo": partial(create_chatgpt, "gpt-3.5-turbo"),
    "gpt-4-turbo": partial(create_chatgpt, "gpt-4-0125-preview"),
    "gemini-pro": partial(create_gemini, "gemini-pro"),
    # "gemini-vision": partial(create_gemini, "gemini-vision"),
}