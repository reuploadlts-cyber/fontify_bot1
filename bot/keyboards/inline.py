from math import ceil

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.config import settings
from bot.services.combo_engine import get_combo_styles
from bot.services.decor_engine import get_decor_styles
from bot.services.font_engine import get_font_styles


def force_join_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📢 Join Channel",
                    url=f"https://t.me/{settings.channel_username.lstrip('@')}",
                )
            ],
            [
                InlineKeyboardButton(
                    text="✅ Verify Join",
                    callback_data="verify_join",
                )
            ],
        ]
    )


def verified_menu_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📝 How To Use",
                    callback_data="verified_info",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔄 Back to Start",
                    callback_data="show_start",
                )
            ],
        ]
    )


def text_tools_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎨 Fonts",
                    callback_data="tool_fonts",
                ),
                InlineKeyboardButton(
                    text="✨ Decor",
                    callback_data="tool_decor",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔥 Combo Styles",
                    callback_data="tool_combo",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔄 Send New Text",
                    callback_data="verified_info",
                )
            ],
        ]
    )


def font_styles_keyboard(page: int = 0, per_page: int = 6) -> InlineKeyboardMarkup:
    styles = get_font_styles()
    total_pages = max(1, ceil(len(styles) / per_page))
    safe_page = max(0, min(page, total_pages - 1))
    start_index = safe_page * per_page
    end_index = start_index + per_page
    current_items = styles[start_index:end_index]

    rows = []
    for style in current_items:
        rows.append(
            [
                InlineKeyboardButton(
                    text=f"🎨 {style.title}",
                    callback_data=f"font_apply:{style.key}",
                )
            ]
        )

    nav_row = []
    if safe_page > 0:
        nav_row.append(
            InlineKeyboardButton(
                text="⬅️ Previous",
                callback_data=f"fonts_page:{safe_page - 1}",
            )
        )
    if safe_page < total_pages - 1:
        nav_row.append(
            InlineKeyboardButton(
                text="Next ➡️",
                callback_data=f"fonts_page:{safe_page + 1}",
            )
        )
    if nav_row:
        rows.append(nav_row)

    rows.append([InlineKeyboardButton(text="🔙 Back to Tools", callback_data="back_to_tools")])

    return InlineKeyboardMarkup(inline_keyboard=rows)


def decor_styles_keyboard(page: int = 0, per_page: int = 6) -> InlineKeyboardMarkup:
    styles = get_decor_styles()
    total_pages = max(1, ceil(len(styles) / per_page))
    safe_page = max(0, min(page, total_pages - 1))
    start_index = safe_page * per_page
    end_index = start_index + per_page
    current_items = styles[start_index:end_index]

    rows = []
    for style in current_items:
        rows.append(
            [
                InlineKeyboardButton(
                    text=f"✨ {style.title}",
                    callback_data=f"decor_apply:{style.key}",
                )
            ]
        )

    nav_row = []
    if safe_page > 0:
        nav_row.append(
            InlineKeyboardButton(
                text="⬅️ Previous",
                callback_data=f"decor_page:{safe_page - 1}",
            )
        )
    if safe_page < total_pages - 1:
        nav_row.append(
            InlineKeyboardButton(
                text="Next ➡️",
                callback_data=f"decor_page:{safe_page + 1}",
            )
        )
    if nav_row:
        rows.append(nav_row)

    rows.append([InlineKeyboardButton(text="🔙 Back to Tools", callback_data="back_to_tools")])

    return InlineKeyboardMarkup(inline_keyboard=rows)


def combo_styles_keyboard(page: int = 0, per_page: int = 6) -> InlineKeyboardMarkup:
    styles = get_combo_styles()
    total_pages = max(1, ceil(len(styles) / per_page))
    safe_page = max(0, min(page, total_pages - 1))
    start_index = safe_page * per_page
    end_index = start_index + per_page
    current_items = styles[start_index:end_index]

    rows = []
    for style in current_items:
        rows.append(
            [
                InlineKeyboardButton(
                    text=f"🔥 {style.title}",
                    callback_data=f"combo_apply:{style.key}",
                )
            ]
        )

    nav_row = []
    if safe_page > 0:
        nav_row.append(
            InlineKeyboardButton(
                text="⬅️ Previous",
                callback_data=f"combo_page:{safe_page - 1}",
            )
        )
    if safe_page < total_pages - 1:
        nav_row.append(
            InlineKeyboardButton(
                text="Next ➡️",
                callback_data=f"combo_page:{safe_page + 1}",
            )
        )
    if nav_row:
        rows.append(nav_row)

    rows.append([InlineKeyboardButton(text="🔙 Back to Tools", callback_data="back_to_tools")])

    return InlineKeyboardMarkup(inline_keyboard=rows)


def font_result_keyboard(style_key: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🎨 Try Another Font", callback_data="tool_fonts")],
            [
                InlineKeyboardButton(text="✨ Decor", callback_data="tool_decor"),
                InlineKeyboardButton(text="🔥 Combo", callback_data="tool_combo"),
            ],
            [InlineKeyboardButton(text="🔙 Back to Tools", callback_data="back_to_tools")],
        ]
    )


def decor_result_keyboard(style_key: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="✨ Try Another Decor", callback_data="tool_decor")],
            [
                InlineKeyboardButton(text="🎨 Fonts", callback_data="tool_fonts"),
                InlineKeyboardButton(text="🔥 Combo", callback_data="tool_combo"),
            ],
            [InlineKeyboardButton(text="🔙 Back to Tools", callback_data="back_to_tools")],
        ]
    )


def combo_result_keyboard(style_key: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔥 Try Another Combo", callback_data="tool_combo")],
            [
                InlineKeyboardButton(text="🎨 Fonts", callback_data="tool_fonts"),
                InlineKeyboardButton(text="✨ Decor", callback_data="tool_decor"),
            ],
            [InlineKeyboardButton(text="🔙 Back to Tools", callback_data="back_to_tools")],
        ]
    )
