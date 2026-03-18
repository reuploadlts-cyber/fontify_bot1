from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message

from bot.keyboards.inline import force_join_keyboard
from bot.utils.helpers import is_private_callback, is_private_message, safe_answer_callback, safe_edit_message
from bot.utils.messages import build_private_only_message, build_start_message


router = Router()


@router.message(CommandStart())
async def start_command(message: Message) -> None:
    if not is_private_message(message):
        await message.answer(build_private_only_message())
        return

    text = build_start_message()
    await message.answer(
        text=text,
        reply_markup=force_join_keyboard(),
        disable_web_page_preview=True,
    )


@router.callback_query(F.data == "show_start")
async def show_start_screen(callback: CallbackQuery) -> None:
    if not is_private_callback(callback):
        await safe_answer_callback(callback, "Use this bot in private chat.", show_alert=True)
        return

    text = build_start_message()
    await safe_edit_message(
        callback=callback,
        text=text,
        reply_markup=force_join_keyboard(),
        disable_web_page_preview=True,
    )
    await safe_answer_callback(callback)
