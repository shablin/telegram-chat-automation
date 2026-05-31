import asyncio

from aiogram import Router, F
from aiogram.types import Message

from llm import ask_llm
from telegram.utils import typing_loop


router = Router()


@router.business_message(F.text)
async def personal_chat_message_handler(message: Message):
    business_id = message.business_connection_id

    stop_event = asyncio.Event()
    typing_task = asyncio.create_task(
        typing_loop(
            message.bot,
            message.chat.id,
            business_id,
            stop_event
        )
    )

    try:
        answer = await ask_llm(message.text)
    finally:
        stop_event.set()
        await typing_task


    await message.bot.send_message(
        chat_id=message.chat.id,
        text=answer,
        business_connection_id=business_id
    )
