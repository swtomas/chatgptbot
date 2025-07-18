from aiogram import Bot, Dispatcher
import asyncio
import os
import database
import commands, callbacks, forms
import logging
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")
logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN) 
dp = Dispatcher()

async def main(): 
   try: 
    dp.include_routers(commands.router, callbacks.router, forms.router)
    await database.init()
    await database.init_userdb()
    await dp.start_polling(bot)
   except Exception as e:
      print(e)

if __name__ == "__main__":
    asyncio.run(main())