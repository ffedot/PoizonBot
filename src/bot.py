import logging

from aiogram.types import BotCommand

from src.config import TELEGRAM_API_TOKEN

from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram import Bot, Dispatcher, executor

logging.basicConfig(level=logging.INFO)
API_TOKEN = TELEGRAM_API_TOKEN
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, skip_updates=True)

