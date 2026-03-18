from html import escape

from bot.config import settings
from bot.services.combo_engine import ComboStyle, get_combo_style_count
from bot.services.decor_engine import DecorStyle, get_decor_style_count
from bot.services.font_engine import FontStyle, get_font_style_count
from bot.services.text_session import MAX_TEXT_LENGTH


def build_start_message() -> str:
    return (
        "✨ <b>Welcome to FontifyBot</b>\n\n"
        "Turn your plain text into stylish font designs, emoji decor, and combo outputs in one tap.\n\n"
        "🔒 <b>Access Requirement</b>\n"
        f"Join our required channel first: {settings.channel_username}\n\n"
        "📌 <b>How to continue:</b>\n"
        "1. Tap <b>Join Channel</b>\n"
        "2. Join the channel\n"
        "3. Come back and tap <b>Verify Join</b>\n\n"
        "🚀 After verification, send your text and start styling."
    )


def build_force_join_failed_message() -> str:
    return (
        "❌ <b>Verification Failed</b>\n\n"
        f"You still need to join: {settings.channel_username}\n\n"
        "Please:\n"
        "1. Tap <b>Join Channel</b>\n"
        "2. Join completely\n"
        "3. Tap <b>Verify Join</b> again\n\n"
        "🔒 Access stays locked until channel join is confirmed."
    )


def build_force_join_success_message(first_name: str | None) -> str:
    display_name = escape(first_name or "there")

    return (
        f"✅ <b>Verification Successful, {display_name}!</b>\n\n"
        "Your access is now unlocked.\n\n"
        "📝 <b>Next step:</b>\n"
        f"Send any text up to <b>{MAX_TEXT_LENGTH}</b> characters and choose a style.\n\n"
        "🎉 You are ready to use FontifyBot."
    )


def build_verified_info_message() -> str:
    return (
        "📝 <b>How to use FontifyBot</b>\n\n"
        "1. Send any text you want to style\n"
        "2. I will save only your current text\n"
        "3. Choose one of these sections:\n"
        "   • <b>Fonts</b>\n"
        "   • <b>Decor</b>\n"
        "   • <b>Combo Styles</b>\n\n"
        f"🎨 <b>Fonts ready:</b> {get_font_style_count()} styles\n"
        f"✨ <b>Decor ready:</b> {get_decor_style_count()} styles\n"
        f"🔥 <b>Combo ready:</b> {get_combo_style_count()} styles\n"
        f"📏 <b>Text limit:</b> {MAX_TEXT_LENGTH} characters\n\n"
        "⚡ Sending new text automatically replaces the old one."
    )


def build_join_required_short_message() -> str:
    return (
        "🔒 <b>Channel Join Required</b>\n\n"
        f"Please join {settings.channel_username} first, then tap <b>Verify Join</b>.\n\n"
        "After that, send your text and continue."
    )


def build_no_text_found_message() -> str:
    return (
        "⚠️ <b>No text found</b>\n\n"
        "You have not sent any text yet.\n\n"
        "📨 Send your text first, then choose Fonts, Decor, or Combo Styles."
    )


def build_text_too_long_message() -> str:
    return (
        "⚠️ <b>Text is too long</b>\n\n"
        f"Please send text under <b>{MAX_TEXT_LENGTH}</b> characters.\n\n"
        "Shorter text will work better with stylish Unicode output."
    )


def build_empty_text_message() -> str:
    return (
        "⚠️ <b>Empty text not allowed</b>\n\n"
        "Please send some actual text to continue."
    )


def build_private_only_message() -> str:
    return (
        "🔒 <b>Private Chat Only</b>\n\n"
        "Please use this bot in a private chat, not in groups or channels."
    )


def build_cooldown_message() -> str:
    return "⏳ Please slow down a little and try again."


def build_invalid_action_message() -> str:
    return (
        "⚠️ <b>Invalid or expired action</b>\n\n"
        "Please send your text again or reopen the menu."
    )


def build_text_saved_message(user_text: str, selected_tool: str | None = None) -> str:
    safe_text = escape(user_text)
    heading = "✅ <b>Your text is ready</b>"
    extra_info = ""

    if selected_tool:
        heading = f"✅ <b>{escape(selected_tool)} selected</b>"

    if selected_tool == "Fonts":
        extra_info = f"\n🎨 <b>Available font styles:</b> {get_font_style_count()}\n"
    elif selected_tool == "Decor":
        extra_info = f"\n✨ <b>Available decor styles:</b> {get_decor_style_count()}\n"
    elif selected_tool == "Combo Styles":
        extra_info = f"\n🔥 <b>Available combo styles:</b> {get_combo_style_count()}\n"

    return (
        f"{heading}\n\n"
        f"📝 <b>Current text:</b>\n"
        f"<code>{safe_text}</code>\n"
        f"{extra_info}\n"
        "Choose what you want to do next:\n"
        "• <b>Fonts</b> for Unicode font styles\n"
        "• <b>Decor</b> for emoji and symbol decoration\n"
        "• <b>Combo Styles</b> for ready-made mixed outputs\n\n"
        "🔄 Send a new text anytime to replace this one."
    )


def build_font_styles_message(
    saved_text: str,
    styles: list[FontStyle],
    page: int,
    per_page: int,
) -> str:
    safe_text = escape(saved_text)
    total = len(styles)
    total_pages = max(1, (total + per_page - 1) // per_page)
    safe_page = max(0, min(page, total_pages - 1))
    start_index = safe_page * per_page
    end_index = min(start_index + per_page, total)

    preview_lines = []
    for index, style in enumerate(styles[start_index:end_index], start=start_index + 1):
        preview_lines.append(
            f"{index}. <b>{escape(style.title)}</b> — <code>{escape(style.preview)}</code>"
        )

    preview_block = "\n".join(preview_lines) if preview_lines else "No styles found."

    return (
        "🎨 <b>Choose a Font Style</b>\n\n"
        f"📝 <b>Current text:</b>\n<code>{safe_text}</code>\n\n"
        f"📚 <b>Page:</b> {safe_page + 1}/{total_pages}\n"
        f"🎯 <b>Total styles:</b> {total}\n\n"
        "<b>Preview styles on this page:</b>\n"
        f"{preview_block}\n\n"
        "Tap any button below to apply that font."
    )


def build_decor_styles_message(
    saved_text: str,
    styles: list[DecorStyle],
    page: int,
    per_page: int,
) -> str:
    safe_text = escape(saved_text)
    total = len(styles)
    total_pages = max(1, (total + per_page - 1) // per_page)
    safe_page = max(0, min(page, total_pages - 1))
    start_index = safe_page * per_page
    end_index = min(start_index + per_page, total)

    preview_lines = []
    for index, style in enumerate(styles[start_index:end_index], start=start_index + 1):
        preview_lines.append(
            f"{index}. <b>{escape(style.title)}</b> — <code>{escape(style.preview)}</code>"
        )

    preview_block = "\n".join(preview_lines) if preview_lines else "No decor styles found."

    return (
        "✨ <b>Choose a Decor Style</b>\n\n"
        f"📝 <b>Current text:</b>\n<code>{safe_text}</code>\n\n"
        f"📚 <b>Page:</b> {safe_page + 1}/{total_pages}\n"
        f"🎯 <b>Total decor styles:</b> {total}\n\n"
        "<b>Preview styles on this page:</b>\n"
        f"{preview_block}\n\n"
        "Tap any button below to apply that decor."
    )


def build_combo_styles_message(
    saved_text: str,
    styles: list[ComboStyle],
    page: int,
    per_page: int,
) -> str:
    safe_text = escape(saved_text)
    total = len(styles)
    total_pages = max(1, (total + per_page - 1) // per_page)
    safe_page = max(0, min(page, total_pages - 1))
    start_index = safe_page * per_page
    end_index = min(start_index + per_page, total)

    preview_lines = []
    for index, style in enumerate(styles[start_index:end_index], start=start_index + 1):
        preview_lines.append(
            f"{index}. <b>{escape(style.title)}</b> — <code>{escape(style.preview)}</code>"
        )

    preview_block = "\n".join(preview_lines) if preview_lines else "No combo styles found."

    return (
        "🔥 <b>Choose a Combo Style</b>\n\n"
        f"📝 <b>Current text:</b>\n<code>{safe_text}</code>\n\n"
        f"📚 <b>Page:</b> {safe_page + 1}/{total_pages}\n"
        f"🎯 <b>Total combo styles:</b> {total}\n\n"
        "<b>Preview styles on this page:</b>\n"
        f"{preview_block}\n\n"
        "Tap any button below to apply that combo style."
    )


def build_font_result_message(
    original_text: str,
    styled_text: str,
    style_title: str,
) -> str:
    return (
        f"✅ <b>{escape(style_title)} Applied</b>\n\n"
        f"📝 <b>Original text:</b>\n<code>{escape(original_text)}</code>\n\n"
        f"✨ <b>Styled output:</b>\n<code>{escape(styled_text)}</code>\n\n"
        "You can copy the styled text above and use it anywhere."
    )


def build_decor_result_message(
    original_text: str,
    styled_text: str,
    style_title: str,
) -> str:
    return (
        f"✅ <b>{escape(style_title)} Decor Applied</b>\n\n"
        f"📝 <b>Original text:</b>\n<code>{escape(original_text)}</code>\n\n"
        f"✨ <b>Decorated output:</b>\n<code>{escape(styled_text)}</code>\n\n"
        "You can copy the decorated text above and use it anywhere."
    )


def build_combo_result_message(
    original_text: str,
    styled_text: str,
    style_title: str,
) -> str:
    return (
        f"✅ <b>{escape(style_title)} Combo Applied</b>\n\n"
        f"📝 <b>Original text:</b>\n<code>{escape(original_text)}</code>\n\n"
        f"🔥 <b>Combo output:</b>\n<code>{escape(styled_text)}</code>\n\n"
        "You can copy the combo styled text above and use it anywhere."
    )
