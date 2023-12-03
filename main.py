import asyncio
from aiogram import Bot, Dispatcher
from settings import settings
from handlers.handlers import router, state_router
# from handlers.post_handlers import


bot = Bot(token=settings.BOT_TOKEN.get_secret_value())
dp = Dispatcher()

async def main():




    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
