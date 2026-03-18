from aiogram import F, Router
from aiogram.types import CallbackQuery, Message

from bot.keyboards.inline import (
    combo_result_keyboard,
    combo_styles_keyboard,
    decor_result_keyboard,
    decor_styles_keyboard,
    font_result_keyboard,
    font_styles_keyboard,
    text_tools_keyboard,
    verified_menu_keyboard,
)
from bot.services.combo_engine import (
    apply_combo_style,
    get_combo_style_count,
    get_combo_styles,
    is_valid_combo_style,
)
from bot.services.decor_engine import (
    apply_decor_style,
    get_decor_style_count,
    get_decor_styles,
    is_valid_decor_style,
)
from bot.services.font_engine import (
    apply_font_style,
    get_font_style_count,
    get_font_styles,
    is_valid_font_style,
)
from bot.services.join_checker import is_user_joined_required_channel
from bot.services.text_session import (
    get_user_text,
    save_user_text,
    validate_user_text,
)
from bot.services.user_guard import is_on_cooldown, update_user_action
from bot.utils.helpers import (
    is_private_callback,
    is_private_message,
    safe_answer_callback,
    safe_edit_message,
)
from bot.utils.messages import (
    build_combo_result_message,
    build_combo_styles_message,
    build_cooldown_message,
    build_decor_result_message,
    build_decor_styles_message,
    build_empty_text_message,
    build_font_result_message,
    build_font_styles_message,
    build_invalid_action_message,
    build_join_required_short_message,
    build_no_text_found_message,
    build_private_only_message,
    build_text_saved_message,
    build_text_too_long_message,
    build_verified_info_message,
)


router = Router()


async def _ensure_joined_and_text(callback: CallbackQuery) -> tuple[bool, str | None]:
    if not is_private_callback(callback):
        await safe_answer_callback(callback, "Use this bot in private chat.", show_alert=True)
        return False, None

    user = callback.from_user
    if not user:
        await safe_answer_callback(callback, "User not found.", show_alert=True)
        return False, None

    is_joined = await is_user_joined_required_channel(
        bot=callback.bot,
        user_id=user.id,
    )
    if not is_joined:
        await safe_answer_callback(callback, "Join the channel first.", show_alert=True)
        await safe_edit_message(
            callback=callback,
            text=build_join_required_short_message(),
            reply_markup=verified_menu_keyboard(),
            disable_web_page_preview=True,
        )
        return False, None

    saved_text = get_user_text(user.id)
    if not saved_text:
        await safe_answer_callback(callback, "Send text first.", show_alert=True)
        await safe_edit_message(
            callback=callback,
            text=build_no_text_found_message(),
            reply_markup=verified_menu_keyboard(),
            disable_web_page_preview=True,
        )
        return False, None

    return True, saved_text


@router.callback_query(F.data == "verified_info")
async def verified_info_handler(callback: CallbackQuery) -> None:
    if not is_private_callback(callback):
        await safe_answer_callback(callback, "Use this bot in private chat.", show_alert=True)
        return

    await safe_edit_message(
        callback=callback,
        text=build_verified_info_message(),
        reply_markup=verified_menu_keyboard(),
        disable_web_page_preview=True,
    )
    await safe_answer_callback(callback)


@router.callback_query(F.data == "back_to_tools")
async def back_to_tools_handler(callback: CallbackQuery) -> None:
    if not is_private_callback(callback):
        await safe_answer_callback(callback, "Use this bot in private chat.", show_alert=True)
        return

    user = callback.from_user
    if not user:
        await safe_answer_callback(callback, "User not found.", show_alert=True)
        return

    saved_text = get_user_text(user.id)
    if not saved_text:
        await safe_answer_callback(callback, "Send text first.", show_alert=True)
        await safe_edit_message(
            callback=callback,
            text=build_no_text_found_message(),
            reply_markup=verified_menu_keyboard(),
            disable_web_page_preview=True,
        )
        return

    await safe_edit_message(
        callback=callback,
        text=build_text_saved_message(saved_text),
        reply_markup=text_tools_keyboard(),
        disable_web_page_preview=True,
    )
    await safe_answer_callback(callback)


@router.callback_query(F.data == "tool_fonts")
async def open_fonts_menu_handler(callback: CallbackQuery) -> None:
    is_ready, saved_text = await _ensure_joined_and_text(callback)
    if not is_ready or not saved_text:
        return

    styles = get_font_styles()
    await safe_edit_message(
        callback=callback,
        text=build_font_styles_message(saved_text=saved_text, styles=styles, page=0, per_page=6),
        reply_markup=font_styles_keyboard(page=0, per_page=6),
        disable_web_page_preview=True,
    )
    await safe_answer_callback(callback, f"{get_font_style_count()} font styles ready ✅")


@router.callback_query(F.data == "tool_decor")
async def open_decor_menu_handler(callback: CallbackQuery) -> None:
    is_ready, saved_text = await _ensure_joined_and_text(callback)
    if not is_ready or not saved_text:
        return

    styles = get_decor_styles()
    await safe_edit_message(
        callback=callback,
        text=build_decor_styles_message(saved_text=saved_text, styles=styles, page=0, per_page=6),
        reply_markup=decor_styles_keyboard(page=0, per_page=6),
        disable_web_page_preview=True,
    )
    await safe_answer_callback(callback, f"{get_decor_style_count()} decor styles ready ✅")


@router.callback_query(F.data == "tool_combo")
async def open_combo_menu_handler(callback: CallbackQuery) -> None:
    is_ready, saved_text = await _ensure_joined_and_text(callback)
    if not is_ready or not saved_text:
        return

    styles = get_combo_styles()
    await safe_edit_message(
        callback=callback,
        text=build_combo_styles_message(saved_text=saved_text, styles=styles, page=0, per_page=6),
        reply_markup=combo_styles_keyboard(page=0, per_page=6),
        disable_web_page_preview=True,
    )
    await safe_answer_callback(callback, f"{get_combo_style_count()} combo styles ready ✅")


@router.callback_query(F.data.startswith("fonts_page:"))
async def paginate_fonts_handler(callback: CallbackQuery) -> None:
    if not is_private_callback(callback):
        await safe_answer_callback(callback, "Use this bot in private chat.", show_alert=True)
        return

    user = callback.from_user
    if not user:
        await safe_answer_callback(callback, "User not found.", show_alert=True)
        return

    saved_text = get_user_text(user.id)
    if not saved_text:
        await safe_answer_callback(callback, "Send text first.", show_alert=True)
        await safe_edit_message(
            callback=callback,
            text=build_no_text_found_message(),
            reply_markup=verified_menu_keyboard(),
            disable_web_page_preview=True,
        )
        return

    try:
        page = int((callback.data or "fonts_page:0").split(":")[1])
    except (IndexError, ValueError):
        await safe_answer_callback(callback, "Invalid page.", show_alert=True)
        return

    styles = get_font_styles()
    await safe_edit_message(
        callback=callback,
        text=build_font_styles_message(saved_text=saved_text, styles=styles, page=page, per_page=6),
        reply_markup=font_styles_keyboard(page=page, per_page=6),
        disable_web_page_preview=True,
    )
    await safe_answer_callback(callback)


@router.callback_query(F.data.startswith("decor_page:"))
async def paginate_decor_handler(callback: CallbackQuery) -> None:
    if not is_private_callback(callback):
        await safe_answer_callback(callback, "Use this bot in private chat.", show_alert=True)
        return

    user = callback.from_user
    if not user:
        await safe_answer_callback(callback, "User not found.", show_alert=True)
        return

    saved_text = get_user_text(user.id)
    if not saved_text:
        await safe_answer_callback(callback, "Send text first.", show_alert=True)
        await safe_edit_message(
            callback=callback,
            text=build_no_text_found_message(),
            reply_markup=verified_menu_keyboard(),
            disable_web_page_preview=True,
        )
        return

    try:
        page = int((callback.data or "decor_page:0").split(":")[1])
    except (IndexError, ValueError):
        await safe_answer_callback(callback, "Invalid page.", show_alert=True)
        return

    styles = get_decor_styles()
    await safe_edit_message(
        callback=callback,
        text=build_decor_styles_message(saved_text=saved_text, styles=styles, page=page, per_page=6),
        reply_markup=decor_styles_keyboard(page=page, per_page=6),
        disable_web_page_preview=True,
    )
    await safe_answer_callback(callback)


@router.callback_query(F.data.startswith("combo_page:"))
async def paginate_combo_handler(callback: CallbackQuery) -> None:
    if not is_private_callback(callback):
        await safe_answer_callback(callback, "Use this bot in private chat.", show_alert=True)
        return

    user = callback.from_user
    if not user:
        await safe_answer_callback(callback, "User not found.", show_alert=True)
        return

    saved_text = get_user_text(user.id)
    if not saved_text:
        await safe_answer_callback(callback, "Send text first.", show_alert=True)
        await safe_edit_message(
            callback=callback,
            text=build_no_text_found_message(),
            reply_markup=verified_menu_keyboard(),
            disable_web_page_preview=True,
        )
        return

    try:
        page = int((callback.data or "combo_page:0").split(":")[1])
    except (IndexError, ValueError):
        await safe_answer_callback(callback, "Invalid page.", show_alert=True)
        return

    styles = get_combo_styles()
    await safe_edit_message(
        callback=callback,
        text=build_combo_styles_message(saved_text=saved_text, styles=styles, page=page, per_page=6),
        reply_markup=combo_styles_keyboard(page=page, per_page=6),
        disable_web_page_preview=True,
    )
    await safe_answer_callback(callback)


@router.callback_query(F.data.startswith("font_apply:"))
async def apply_font_handler(callback: CallbackQuery) -> None:
    is_ready, saved_text = await _ensure_joined_and_text(callback)
    if not is_ready or not saved_text:
        return

    style_key = (callback.data or "").split(":", maxsplit=1)[1] if ":" in (callback.data or "") else ""
    if not is_valid_font_style(style_key):
        await safe_answer_callback(callback, "Invalid font style.", show_alert=True)
        return

    style_map = {style.key: style for style in get_font_styles()}
    selected_style = style_map.get(style_key)
    if not selected_style:
        await safe_answer_callback(callback, "Invalid font style.", show_alert=True)
        return

    converted_text = apply_font_style(saved_text, style_key)

    await safe_edit_message(
        callback=callback,
        text=build_font_result_message(
            original_text=saved_text,
            styled_text=converted_text,
            style_title=selected_style.title,
        ),
        reply_markup=font_result_keyboard(style_key=style_key),
        disable_web_page_preview=True,
    )
    await safe_answer_callback(callback, "Font applied ✅")


@router.callback_query(F.data.startswith("decor_apply:"))
async def apply_decor_handler(callback: CallbackQuery) -> None:
    is_ready, saved_text = await _ensure_joined_and_text(callback)
    if not is_ready or not saved_text:
        return

    style_key = (callback.data or "").split(":", maxsplit=1)[1] if ":" in (callback.data or "") else ""
    if not is_valid_decor_style(style_key):
        await safe_answer_callback(callback, "Invalid decor style.", show_alert=True)
        return

    style_map = {style.key: style for style in get_decor_styles()}
    selected_style = style_map.get(style_key)
    if not selected_style:
        await safe_answer_callback(callback, "Invalid decor style.", show_alert=True)
        return

    converted_text = apply_decor_style(saved_text, style_key)

    await safe_edit_message(
        callback=callback,
        text=build_decor_result_message(
            original_text=saved_text,
            styled_text=converted_text,
            style_title=selected_style.title,
        ),
        reply_markup=decor_result_keyboard(style_key=style_key),
        disable_web_page_preview=True,
    )
    await safe_answer_callback(callback, "Decor applied ✅")


@router.callback_query(F.data.startswith("combo_apply:"))
async def apply_combo_handler(callback: CallbackQuery) -> None:
    is_ready, saved_text = await _ensure_joined_and_text(callback)
    if not is_ready or not saved_text:
        return

    style_key = (callback.data or "").split(":", maxsplit=1)[1] if ":" in (callback.data or "") else ""
    if not is_valid_combo_style(style_key):
        await safe_answer_callback(callback, "Invalid combo style.", show_alert=True)
        return

    style_map = {style.key: style for style in get_combo_styles()}
    selected_style = style_map.get(style_key)
    if not selected_style:
        await safe_answer_callback(callback, "Invalid combo style.", show_alert=True)
        return

    converted_text = apply_combo_style(saved_text, style_key)

    await safe_edit_message(
        callback=callback,
        text=build_combo_result_message(
            original_text=saved_text,
            styled_text=converted_text,
            style_title=selected_style.title,
        ),
        reply_markup=combo_result_keyboard(style_key=style_key),
        disable_web_page_preview=True,
    )
    await safe_answer_callback(callback, "Combo applied ✅")


@router.message(F.text)
async def receive_user_text(message: Message) -> None:
    if not is_private_message(message):
        await message.answer(build_private_only_message())
        return

    user = message.from_user
    text = (message.text or "").strip()

    if not user:
        return

    if text.startswith("/"):
        return

    if is_on_cooldown(user.id):
        await message.answer(build_cooldown_message())
        return

    update_user_action(user.id)

    is_joined = await is_user_joined_required_channel(
        bot=message.bot,
        user_id=user.id,
    )
    if not is_joined:
        await message.answer(
            text=build_join_required_short_message(),
            reply_markup=verified_menu_keyboard(),
            disable_web_page_preview=True,
        )
        return

    is_valid, reason = validate_user_text(text)
    if not is_valid:
        if reason == "empty":
            await message.answer(build_empty_text_message())
            return
        if reason == "too_long":
            await message.answer(build_text_too_long_message())
            return

        await message.answer(build_invalid_action_message())
        return

    save_user_text(user.id, text)

    await message.answer(
        text=build_text_saved_message(text),
        reply_markup=text_tools_keyboard(),
        disable_web_page_preview=True,
    )
