from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, List


@dataclass(frozen=True)
class DecorStyle:
    key: str
    title: str
    preview: str


def _wrap(text: str, left: str, right: str) -> str:
    return f"{left} {text} {right}"


def _surround(text: str, left: str, right: str) -> str:
    return f"{left}{text}{right}"


def _double_wrap(text: str, left: str, center_left: str, center_right: str, right: str) -> str:
    return f"{left} {center_left}{text}{center_right} {right}"


DECOR_FUNCTIONS: Dict[str, Callable[[str], str]] = {
    "sparkles": lambda text: _wrap(text, "✨", "✨"),
    "fire": lambda text: _wrap(text, "🔥", "🔥"),
    "hearts": lambda text: _wrap(text, "💖", "💖"),
    "stars": lambda text: _wrap(text, "🌟", "🌟"),
    "crown": lambda text: _wrap(text, "👑", "👑"),
    "lightning": lambda text: _wrap(text, "⚡", "⚡"),
    "flowers": lambda text: _wrap(text, "🌸", "🌸"),
    "butterfly": lambda text: _wrap(text, "🦋", "🦋"),
    "diamond": lambda text: _wrap(text, "💎", "💎"),
    "music": lambda text: _wrap(text, "🎵", "🎵"),
    "waves": lambda text: _surround(text, "〰️ ", " 〰️"),
    "dots": lambda text: _surround(text, "• ", " •"),
    "brackets_1": lambda text: _surround(text, "『", "』"),
    "brackets_2": lambda text: _surround(text, "【", "】"),
    "brackets_3": lambda text: _surround(text, "《", "》"),
    "royal_box": lambda text: _surround(text, "꧁", "꧂"),
    "star_frame": lambda text: _surround(text, "★ ", " ★"),
    "heart_frame": lambda text: _surround(text, "•♥ ", " ♥•"),
    "flower_frame": lambda text: _double_wrap(text, "✿", "╭", "╮", "✿"),
    "spark_frame": lambda text: _double_wrap(text, "✧", "⟦", "⟧", "✧"),
}


DECOR_STYLES: List[DecorStyle] = [
    DecorStyle(key="sparkles", title="Sparkles", preview="✨ Hello ✨"),
    DecorStyle(key="fire", title="Fire", preview="🔥 Hello 🔥"),
    DecorStyle(key="hearts", title="Hearts", preview="💖 Hello 💖"),
    DecorStyle(key="stars", title="Stars", preview="🌟 Hello 🌟"),
    DecorStyle(key="crown", title="Crown", preview="👑 Hello 👑"),
    DecorStyle(key="lightning", title="Lightning", preview="⚡ Hello ⚡"),
    DecorStyle(key="flowers", title="Flowers", preview="🌸 Hello 🌸"),
    DecorStyle(key="butterfly", title="Butterfly", preview="🦋 Hello 🦋"),
    DecorStyle(key="diamond", title="Diamond", preview="💎 Hello 💎"),
    DecorStyle(key="music", title="Music", preview="🎵 Hello 🎵"),
    DecorStyle(key="waves", title="Waves", preview="〰️ Hello 〰️"),
    DecorStyle(key="dots", title="Dots", preview="• Hello •"),
    DecorStyle(key="brackets_1", title="Brackets 1", preview="『Hello』"),
    DecorStyle(key="brackets_2", title="Brackets 2", preview="【Hello】"),
    DecorStyle(key="brackets_3", title="Brackets 3", preview="《Hello》"),
    DecorStyle(key="royal_box", title="Royal Box", preview="꧁Hello꧂"),
    DecorStyle(key="star_frame", title="Star Frame", preview="★ Hello ★"),
    DecorStyle(key="heart_frame", title="Heart Frame", preview="•♥ Hello ♥•"),
    DecorStyle(key="flower_frame", title="Flower Frame", preview="✿ ╭Hello╮ ✿"),
    DecorStyle(key="spark_frame", title="Spark Frame", preview="✧ ⟦Hello⟧ ✧"),
]


def get_decor_styles() -> List[DecorStyle]:
    return DECOR_STYLES


def get_decor_style_count() -> int:
    return len(DECOR_STYLES)


def is_valid_decor_style(style_key: str) -> bool:
    return style_key in DECOR_FUNCTIONS


def apply_decor_style(text: str, style_key: str) -> str:
    if not text:
        return ""

    style_function = DECOR_FUNCTIONS.get(style_key)
    if style_function is None:
        return text

    return style_function(text)
