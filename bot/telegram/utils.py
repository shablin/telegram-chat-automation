import asyncio
from aiogram.enums import ChatAction
from aiogram import Bot

async def typing_loop(
    bot: Bot,
    chat_id,
    business_id,
    stop_event: asyncio.Event
):
    while not stop_event.is_set():
        await bot.send_chat_action(
            chat_id=chat_id,
            business_connection_id=business_id,
            action=ChatAction.TYPING
        )

        await asyncio.sleep(3)