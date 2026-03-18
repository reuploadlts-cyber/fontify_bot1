from aiogram import Bot
from aiogram.enums import ChatMemberStatus

from bot.config import settings


ALLOWED_MEMBER_STATUSES = {
    ChatMemberStatus.CREATOR,
    ChatMemberStatus.ADMINISTRATOR,
    ChatMemberStatus.MEMBER,
}


async def is_user_joined_required_channel(bot: Bot, user_id: int) -> bool:
    try:
        member = await bot.get_chat_member(
            chat_id=settings.channel_username,
            user_id=user_id,
        )
        return member.status in ALLOWED_MEMBER_STATUSES
    except Exception:
        return False
