from aiogram.enums import ChatType
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery, Message


def is_private_message(message: Message) -> bool:
    return message.chat.type == ChatType.PRIVATE


def is_private_callback(callback: CallbackQuery) -> bool:
    return bool(callback.message and callback.message.chat.type == ChatType.PRIVATE)


async def safe_edit_message(
    callback: CallbackQuery,
    text: str,
    reply_markup=None,
    disable_web_page_preview: bool = True,
) -> bool:
    if callback.message is None:
        return False

    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=reply_markup,
            disable_web_page_preview=disable_web_page_preview,
        )
        return True
    except TelegramBadRequest:
        try:
            await callback.message.answer(
                text=text,
                reply_markup=reply_markup,
                disable_web_page_preview=disable_web_page_preview,
            )
            return True
        except TelegramBadRequest:
            return False


async def safe_answer_callback(
    callback: CallbackQuery,
    text: str | None = None,
    show_alert: bool = False,
) -> None:
    try:
        await callback.answer(text=text, show_alert=show_alert)
    except TelegramBadRequest:
        return
