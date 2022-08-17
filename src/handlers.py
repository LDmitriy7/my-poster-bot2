import callbacks
import events
from groof import Handler

HANDLERS = [
    Handler(events.start, callbacks.test),
]
