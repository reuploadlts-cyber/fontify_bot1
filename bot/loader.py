from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.config import settings
from bot.handlers.force_join import router as force_join_router
from bot.handlers.start import router as start_router
from bot.handlers.text import router as text_router


bot = Bot(
    token=settings.bot_token,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)

dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(force_join_router)
dp.include_router(text_router)
