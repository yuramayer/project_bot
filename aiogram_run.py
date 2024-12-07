import asyncio
from create_bot import bot, dp
from handlers import start, test, dummy


async def main():
    dp.include_routers(start.start_router, test.test_router, dummy.dummy_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
