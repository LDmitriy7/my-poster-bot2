from . import types
from .bot import Bot
from .database import MongoDatabase
from .handler import Handler


class Dispatcher:
    def __init__(self, bot: Bot, db: MongoDatabase):
        self._bot = bot
        self._db = db
        self._handlers: list[Handler] = []
        self._updates: list[types.Update] = []

    def setup_handlers(self, handlers: list[Handler]):
        self._handlers.extend(handlers)

    @property
    def _updates_offset(self) -> int | None:
        if updates := self._updates:
            return updates[-1].update_id + 1

    def _get_updates(self):
        self._updates = self._bot.get_updates(offset=self._updates_offset)

    def _process_updates(self):
        print(self._updates)

    def run(self):
        while True:
            self._get_updates()
            self._process_updates()
