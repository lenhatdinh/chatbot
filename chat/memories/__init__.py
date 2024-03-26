from functools import partial

from .buffers import (
    create_buffer_memory,
    create_window_memory,
)

memory_creators = {
    "buffer": create_buffer_memory,
    "window": create_window_memory,
    "0-window": partial(create_window_memory, k=0),
    "10-window": partial(create_window_memory, k=10),
}