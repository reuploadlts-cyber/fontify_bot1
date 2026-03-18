from typing import Dict


_user_current_text: Dict[int, str] = {}

MAX_TEXT_LENGTH = 300


def save_user_text(user_id: int, text: str) -> None:
    _user_current_text[user_id] = text


def get_user_text(user_id: int) -> str | None:
    return _user_current_text.get(user_id)


def clear_user_text(user_id: int) -> None:
    _user_current_text.pop(user_id, None)


def validate_user_text(text: str) -> tuple[bool, str | None]:
    cleaned = text.strip()

    if not cleaned:
        return False, "empty"

    if len(cleaned) > MAX_TEXT_LENGTH:
        return False, "too_long"

    return True, None
