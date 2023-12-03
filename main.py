import asyncio
from aiogram import Bot, Dispatcher
from settings import settings
from handlers.handlers import router
from handlers.post_handlers import state_router, dispatcher




async def main():
    bot = Bot(token=settings.BOT_TOKEN.get_secret_value())
    dp = Dispatcher()

    dp.include_router(router)
    dp.include_router(state_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
