from aiogram import F, Router
from aiogram.types import CallbackQuery

from bot.keyboards.inline import force_join_keyboard, verified_menu_keyboard
from bot.services.join_checker import is_user_joined_required_channel
from bot.utils.helpers import is_private_callback, safe_answer_callback, safe_edit_message
from bot.utils.messages import (
    build_force_join_failed_message,
    build_force_join_success_message,
)


router = Router()


@router.callback_query(F.data == "verify_join")
async def verify_join_handler(callback: CallbackQuery) -> None:
    if not is_private_callback(callback):
        await safe_answer_callback(callback, "Use this bot in private chat.", show_alert=True)
        return

    user = callback.from_user
    if not user:
        await safe_answer_callback(callback, "User not found.", show_alert=True)
        return

    is_joined = await is_user_joined_required_channel(
        bot=callback.bot,
        user_id=user.id,
    )

    if is_joined:
        await safe_edit_message(
            callback=callback,
            text=build_force_join_success_message(first_name=user.first_name),
            reply_markup=verified_menu_keyboard(),
            disable_web_page_preview=True,
        )
        await safe_answer_callback(callback, "Verification successful ✅")
        return

    await safe_edit_message(
        callback=callback,
        text=build_force_join_failed_message(),
        reply_markup=force_join_keyboard(),
        disable_web_page_preview=True,
    )
    await safe_answer_callback(callback, "You must join the channel first.", show_alert=True)
