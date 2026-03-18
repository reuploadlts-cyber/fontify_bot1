from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"


def _build_translation_map(
    lower: str | None = None,
    upper: str | None = None,
    digits: str | None = None,
    extra: Dict[str, str] | None = None,
) -> Dict[str, str]:
    mapping: Dict[str, str] = {}

    if lower:
        for source, target in zip(LOWER, lower):
            mapping[source] = target

    if upper:
        for source, target in zip(UPPER, upper):
            mapping[source] = target

    if digits:
        for source, target in zip(DIGITS, digits):
            mapping[source] = target

    if extra:
        mapping.update(extra)

    return mapping


def _apply_mapping(text: str, mapping: Dict[str, str]) -> str:
    return "".join(mapping.get(char, char) for char in text)


BOLD_MAP = _build_translation_map(
    lower="𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇",
    upper="𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭",
    digits="𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵",
)

ITALIC_MAP = _build_translation_map(
    lower="𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻",
    upper="𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡",
)

BOLD_ITALIC_MAP = _build_translation_map(
    lower="𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯",
    upper="𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕",
)

SCRIPT_MAP = _build_translation_map(
    lower="𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏",
    upper="𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵",
)

BOLD_SCRIPT_MAP = _build_translation_map(
    lower="𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃",
    upper="𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩",
)

FRAKTUR_MAP = _build_translation_map(
    lower="𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷",
    upper="𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ",
)

DOUBLE_MAP = _build_translation_map(
    lower="𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫",
    upper="𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ",
    digits="𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡",
)

MONOSPACE_MAP = _build_translation_map(
    lower="𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣",
    upper="𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉",
    digits="𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿",
)

SMALL_CAPS_MAP = {
    "a": "ᴀ",
    "b": "ʙ",
    "c": "ᴄ",
    "d": "ᴅ",
    "e": "ᴇ",
    "f": "ғ",
    "g": "ɢ",
    "h": "ʜ",
    "i": "ɪ",
    "j": "ᴊ",
    "k": "ᴋ",
    "l": "ʟ",
    "m": "ᴍ",
    "n": "ɴ",
    "o": "ᴏ",
    "p": "ᴘ",
    "q": "ǫ",
    "r": "ʀ",
    "s": "s",
    "t": "ᴛ",
    "u": "ᴜ",
    "v": "ᴠ",
    "w": "ᴡ",
    "x": "x",
    "y": "ʏ",
    "z": "ᴢ",
}
SMALL_CAPS_MAP.update({char.upper(): value for char, value in SMALL_CAPS_MAP.items()})

BUBBLE_MAP = _build_translation_map(
    lower="ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ",
    upper="ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ",
    digits="⓪①②③④⑤⑥⑦⑧⑨",
)

SQUARE_MAP = _build_translation_map(
    lower="🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉",
    upper="🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉",
)

WIDE_MAP = _build_translation_map(
    lower="ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ",
    upper="ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ",
    digits="０１２３４５６７８９",
)

TINY_MAP = {
    "a": "ᵃ",
    "b": "ᵇ",
    "c": "ᶜ",
    "d": "ᵈ",
    "e": "ᵉ",
    "f": "ᶠ",
    "g": "ᵍ",
    "h": "ʰ",
    "i": "ᶦ",
    "j": "ʲ",
    "k": "ᵏ",
    "l": "ˡ",
    "m": "ᵐ",
    "n": "ⁿ",
    "o": "ᵒ",
    "p": "ᵖ",
    "q": "ᑫ",
    "r": "ʳ",
    "s": "ˢ",
    "t": "ᵗ",
    "u": "ᵘ",
    "v": "ᵛ",
    "w": "ʷ",
    "x": "ˣ",
    "y": "ʸ",
    "z": "ᶻ",
    "A": "ᴬ",
    "B": "ᴮ",
    "D": "ᴰ",
    "E": "ᴱ",
    "G": "ᴳ",
    "H": "ᴴ",
    "I": "ᴵ",
    "J": "ᴶ",
    "K": "ᴷ",
    "L": "ᴸ",
    "M": "ᴹ",
    "N": "ᴺ",
    "O": "ᴼ",
    "P": "ᴾ",
    "R": "ᴿ",
    "T": "ᵀ",
    "U": "ᵁ",
    "V": "ⱽ",
    "W": "ᵂ",
    "0": "⁰",
    "1": "¹",
    "2": "²",
    "3": "³",
    "4": "⁴",
    "5": "⁵",
    "6": "⁶",
    "7": "⁷",
    "8": "⁸",
    "9": "⁹",
}

FANCY_1_MAP = {
    "a": "α",
    "b": "Ⴆ",
    "c": "ƈ",
    "d": "ԃ",
    "e": "ҽ",
    "f": "ϝ",
    "g": "ɠ",
    "h": "ԋ",
    "i": "ι",
    "j": "ʝ",
    "k": "ƙ",
    "l": "ʅ",
    "m": "ɱ",
    "n": "ɳ",
    "o": "σ",
    "p": "ρ",
    "q": "ϙ",
    "r": "ɾ",
    "s": "ʂ",
    "t": "ƚ",
    "u": "υ",
    "v": "ʋ",
    "w": "ɯ",
    "x": "x",
    "y": "ყ",
    "z": "ȥ",
    "A": "Λ",
    "B": "β",
    "C": "Ƈ",
    "D": "D",
    "E": "Ɛ",
    "F": "F",
    "G": "G",
    "H": "H",
    "I": "I",
    "J": "J",
    "K": "K",
    "L": "L",
    "M": "M",
    "N": "И",
    "O": "Θ",
    "P": "P",
    "Q": "Q",
    "R": "R",
    "S": "Ƨ",
    "T": "Ƭ",
    "U": "Ц",
    "V": "V",
    "W": "Щ",
    "X": "X",
    "Y": "Y",
    "Z": "Z",
}

FANCY_2_MAP = {
    "a": "ค",
    "b": "๒",
    "c": "ς",
    "d": "๔",
    "e": "є",
    "f": "Ŧ",
    "g": "ﻮ",
    "h": "ђ",
    "i": "เ",
    "j": "ן",
    "k": "к",
    "l": "l",
    "m": "๓",
    "n": "ภ",
    "o": "๏",
    "p": "ק",
    "q": "ợ",
    "r": "г",
    "s": "ร",
    "t": "Շ",
    "u": "ย",
    "v": "ש",
    "w": "ฬ",
    "x": "א",
    "y": "ץ",
    "z": "չ",
    "A": "Λ",
    "B": "ß",
    "C": "₡",
    "D": "Đ",
    "E": "Ɇ",
    "F": "₣",
    "G": "₲",
    "H": "Ħ",
    "I": "Ɨ",
    "J": "J",
    "K": "Ҡ",
    "L": "Ł",
    "M": "M",
    "N": "₦",
    "O": "Ø",
    "P": "P",
    "Q": "Q",
    "R": "₹",
    "S": "Ş",
    "T": "Ŧ",
    "U": "Ʉ",
    "V": "V",
    "W": "₩",
    "X": "Ж",
    "Y": "¥",
    "Z": "Ƶ",
}

FANCY_3_MAP = {
    "a": "å",
    "b": "ß",
    "c": "¢",
    "d": "Ð",
    "e": "ê",
    "f": "£",
    "g": "ğ",
    "h": "h",
    "i": "ï",
    "j": "j",
    "k": "k",
    "l": "l",
    "m": "m",
    "n": "ñ",
    "o": "ø",
    "p": "þ",
    "q": "q",
    "r": "r",
    "s": "§",
    "t": "†",
    "u": "µ",
    "v": "v",
    "w": "w",
    "x": "x",
    "y": "¥",
    "z": "ž",
    "A": "Ä",
    "B": "ß",
    "C": "Ç",
    "D": "Ð",
    "E": "Ë",
    "F": "F",
    "G": "Ğ",
    "H": "H",
    "I": "Ï",
    "J": "J",
    "K": "K",
    "L": "Ł",
    "M": "M",
    "N": "Ñ",
    "O": "Ö",
    "P": "Þ",
    "Q": "Q",
    "R": "R",
    "S": "Š",
    "T": "Ť",
    "U": "Ü",
    "V": "V",
    "W": "Ŵ",
    "X": "X",
    "Y": "Ÿ",
    "Z": "Ž",
}


def _underline_style(text: str) -> str:
    underline_mark = "\u0332"
    return "".join(f"{char}{underline_mark}" if char != " " else " " for char in text)


def _strike_style(text: str) -> str:
    strike_mark = "\u0336"
    return "".join(f"{char}{strike_mark}" if char != " " else " " for char in text)


def _aesthetic_style(text: str) -> str:
    converted = _apply_mapping(text, WIDE_MAP)
    return " ".join(list(converted))


STYLE_FUNCTIONS = {
    "bold": lambda text: _apply_mapping(text, BOLD_MAP),
    "italic": lambda text: _apply_mapping(text, ITALIC_MAP),
    "bold_italic": lambda text: _apply_mapping(text, BOLD_ITALIC_MAP),
    "script": lambda text: _apply_mapping(text, SCRIPT_MAP),
    "bold_script": lambda text: _apply_mapping(text, BOLD_SCRIPT_MAP),
    "fraktur": lambda text: _apply_mapping(text, FRAKTUR_MAP),
    "double": lambda text: _apply_mapping(text, DOUBLE_MAP),
    "monospace": lambda text: _apply_mapping(text, MONOSPACE_MAP),
    "small_caps": lambda text: _apply_mapping(text, SMALL_CAPS_MAP),
    "bubble": lambda text: _apply_mapping(text, BUBBLE_MAP),
    "square": lambda text: _apply_mapping(text, SQUARE_MAP),
    "wide": lambda text: _apply_mapping(text, WIDE_MAP),
    "tiny": lambda text: _apply_mapping(text, TINY_MAP),
    "underline": _underline_style,
    "strike": _strike_style,
    "aesthetic": _aesthetic_style,
    "fancy_1": lambda text: _apply_mapping(text, FANCY_1_MAP),
    "fancy_2": lambda text: _apply_mapping(text, FANCY_2_MAP),
    "fancy_3": lambda text: _apply_mapping(text, FANCY_3_MAP),
}


@dataclass(frozen=True)
class FontStyle:
    key: str
    title: str
    preview: str


FONT_STYLES: List[FontStyle] = [
    FontStyle(key="bold", title="Bold", preview="𝗛𝗲𝗹𝗹𝗼"),
    FontStyle(key="italic", title="Italic", preview="𝘏𝘦𝘭𝘭𝘰"),
    FontStyle(key="bold_italic", title="Bold Italic", preview="𝙃𝙚𝙡𝙡𝙤"),
    FontStyle(key="script", title="Script", preview="𝒣𝑒𝓁𝓁𝑜"),
    FontStyle(key="bold_script", title="Bold Script", preview="𝓗𝓮𝓵𝓵𝓸"),
    FontStyle(key="fraktur", title="Fraktur", preview="𝔋𝔢𝔩𝔩𝔬"),
    FontStyle(key="double", title="Double", preview="ℍ𝕖𝕝𝕝𝕠"),
    FontStyle(key="monospace", title="Monospace", preview="𝙷𝚎𝚕𝚕𝚘"),
    FontStyle(key="small_caps", title="Small Caps", preview="ʜᴇʟʟᴏ"),
    FontStyle(key="bubble", title="Bubble", preview="Ⓗⓔⓛⓛⓞ"),
    FontStyle(key="square", title="Square", preview="🄷🄴🄻🄻🄾"),
    FontStyle(key="wide", title="Wide", preview="Ｈｅｌｌｏ"),
    FontStyle(key="tiny", title="Tiny", preview="ʰᵉˡˡᵒ"),
    FontStyle(key="underline", title="Underline", preview="H̲e̲l̲l̲o̲"),
    FontStyle(key="strike", title="Strike", preview="H̶e̶l̶l̶o̶"),
    FontStyle(key="aesthetic", title="Aesthetic", preview="Ｈ ｅ ｌ ｌ ｏ"),
    FontStyle(key="fancy_1", title="Fancy 1", preview="ԋҽʅʅσ"),
    FontStyle(key="fancy_2", title="Fancy 2", preview="ђєll๏"),
    FontStyle(key="fancy_3", title="Fancy 3", preview="hêllø"),
]


def get_font_styles() -> List[FontStyle]:
    return FONT_STYLES


def get_font_style_count() -> int:
    return len(FONT_STYLES)


def is_valid_font_style(style_key: str) -> bool:
    return style_key in STYLE_FUNCTIONS


def apply_font_style(text: str, style_key: str) -> str:
    if not text:
        return ""

    style_function = STYLE_FUNCTIONS.get(style_key)
    if style_function is None:
        return text

    return style_function(text)
