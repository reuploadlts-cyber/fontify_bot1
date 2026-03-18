import asyncio

from bot.loader import bot, dp


async def main():
    print("🚀 Bot is running in polling mode...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
