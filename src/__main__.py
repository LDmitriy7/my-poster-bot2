from handlers import HANDLERS
from loader import dp

dp.setup_handlers(HANDLERS)
dp.run()
