from __future__ import annotations

import typing
from dataclasses import dataclass

ParseMode = typing.Literal['HTML', 'MarkdownV2']
Callback = typing.Callable[[], typing.Any]


@dataclass
class Message:
    message_id: int
    text: str


@dataclass
class Update:
    update_id: int
    # message: Message


UpdateType = typing.Literal[
    'message',
    'edited_message',
    'channel_post',
    'edited_channel_post',
    'inline_query',
    'chosen_inline_result',
    'callback_query',
    'shipping_query',
    'pre_checkout_query',
    'poll',
    'poll_answer',
    'my_chat_member',
    'chat_member',
    'chat_join_request',
]
