import config
from groof import Bot, Dispatcher, MongoDatabase, DefaultRequestParams

bot = Bot(
    config.TOKEN,
    DefaultRequestParams(parse_mode='HTML', disable_web_page_preview=True),
)

db = MongoDatabase(config.MONGO_DB)
dp = Dispatcher(bot, db)
