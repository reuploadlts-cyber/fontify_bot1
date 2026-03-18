from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, List

from bot.services.decor_engine import apply_decor_style
from bot.services.font_engine import apply_font_style


@dataclass(frozen=True)
class ComboStyle:
    key: str
    title: str
    preview: str


def _build_combo(font_key: str | None = None, decor_key: str | None = None) -> Callable[[str], str]:
    def apply(text: str) -> str:
        result = text

        if font_key:
            result = apply_font_style(result, font_key)

        if decor_key:
            result = apply_decor_style(result, decor_key)

        return result

    return apply


COMBO_FUNCTIONS: Dict[str, Callable[[str], str]] = {
    "bold_sparkles": _build_combo(font_key="bold", decor_key="sparkles"),
    "script_hearts": _build_combo(font_key="script", decor_key="hearts"),
    "mono_brackets": _build_combo(font_key="monospace", decor_key="brackets_1"),
    "double_crown": _build_combo(font_key="double", decor_key="crown"),
    "bubble_stars": _build_combo(font_key="bubble", decor_key="stars"),
    "wide_fire": _build_combo(font_key="wide", decor_key="fire"),
    "smallcaps_diamond": _build_combo(font_key="small_caps", decor_key="diamond"),
    "fancy1_flower": _build_combo(font_key="fancy_1", decor_key="flowers"),
    "fancy2_lightning": _build_combo(font_key="fancy_2", decor_key="lightning"),
    "fancy3_music": _build_combo(font_key="fancy_3", decor_key="music"),
    "boldscript_royal": _build_combo(font_key="bold_script", decor_key="royal_box"),
    "italic_waves": _build_combo(font_key="italic", decor_key="waves"),
    "fraktur_star": _build_combo(font_key="fraktur", decor_key="star_frame"),
    "tiny_spark": _build_combo(font_key="tiny", decor_key="spark_frame"),
    "underline_butterfly": _build_combo(font_key="underline", decor_key="butterfly"),
    "strike_dots": _build_combo(font_key="strike", decor_key="dots"),
    "aesthetic_brackets": _build_combo(font_key="aesthetic", decor_key="brackets_2"),
    "square_flowerframe": _build_combo(font_key="square", decor_key="flower_frame"),
    "bolditalic_heartframe": _build_combo(font_key="bold_italic", decor_key="heart_frame"),
    "script_brackets3": _build_combo(font_key="script", decor_key="brackets_3"),
}


COMBO_STYLES: List[ComboStyle] = [
    ComboStyle(key="bold_sparkles", title="Bold Sparkles", preview="✨ 𝗛𝗲𝗹𝗹𝗼 ✨"),
    ComboStyle(key="script_hearts", title="Script Hearts", preview="💖 𝒣𝑒𝓁𝓁𝑜 💖"),
    ComboStyle(key="mono_brackets", title="Mono Brackets", preview="『𝙷𝚎𝚕𝚕𝚘』"),
    ComboStyle(key="double_crown", title="Double Crown", preview="👑 ℍ𝕖𝕝𝕝𝕠 👑"),
    ComboStyle(key="bubble_stars", title="Bubble Stars", preview="🌟 Ⓗⓔⓛⓛⓞ 🌟"),
    ComboStyle(key="wide_fire", title="Wide Fire", preview="🔥 Ｈｅｌｌｏ 🔥"),
    ComboStyle(key="smallcaps_diamond", title="Small Caps Diamond", preview="💎 ʜᴇʟʟᴏ 💎"),
    ComboStyle(key="fancy1_flower", title="Fancy Flower", preview="🌸 ԋҽʅʅσ 🌸"),
    ComboStyle(key="fancy2_lightning", title="Fancy Lightning", preview="⚡ ђєll๏ ⚡"),
    ComboStyle(key="fancy3_music", title="Fancy Music", preview="🎵 hêllø 🎵"),
    ComboStyle(key="boldscript_royal", title="Royal Script", preview="꧁𝓗𝓮𝓵𝓵𝓸꧂"),
    ComboStyle(key="italic_waves", title="Italic Waves", preview="〰️ 𝘏𝘦𝘭𝘭𝘰 〰️"),
    ComboStyle(key="fraktur_star", title="Fraktur Star", preview="★ 𝔋𝔢𝔩𝔩𝔬 ★"),
    ComboStyle(key="tiny_spark", title="Tiny Spark", preview="✧ ⟦ʰᵉˡˡᵒ⟧ ✧"),
    ComboStyle(key="underline_butterfly", title="Underline Butterfly", preview="🦋 H̲e̲l̲l̲o̲ 🦋"),
    ComboStyle(key="strike_dots", title="Strike Dots", preview="• H̶e̶l̶l̶o̶ •"),
    ComboStyle(key="aesthetic_brackets", title="Aesthetic Brackets", preview="【Ｈ ｅ ｌ ｌ ｏ】"),
    ComboStyle(key="square_flowerframe", title="Square Flower Frame", preview="✿ ╭🄷🄴🄻🄻🄾╮ ✿"),
    ComboStyle(key="bolditalic_heartframe", title="Bold Italic Hearts", preview="•♥ 𝙃𝙚𝙡𝙡𝙤 ♥•"),
    ComboStyle(key="script_brackets3", title="Script Brackets", preview="《𝒣𝑒𝓁𝓁𝑜》"),
]


def get_combo_styles() -> List[ComboStyle]:
    return COMBO_STYLES


def get_combo_style_count() -> int:
    return len(COMBO_STYLES)


def is_valid_combo_style(style_key: str) -> bool:
    return style_key in COMBO_FUNCTIONS


def apply_combo_style(text: str, style_key: str) -> str:
    if not text:
        return ""

    style_function = COMBO_FUNCTIONS.get(style_key)
    if style_function is None:
        return text

    return style_function(text)
