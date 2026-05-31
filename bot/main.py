import asyncio

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from telegram.handlers import router


async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    print("bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())