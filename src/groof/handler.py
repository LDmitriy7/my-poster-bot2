from . import types
from .event import Event


class Handler:
    def __init__(self, event: Event, callback: types.Callback):
        self._event = event
        self._callback = callback
