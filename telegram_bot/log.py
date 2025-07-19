import main
import os
from dotenv import load_dotenv


bot = main.bot
group = os.getenv("GROUP")

async def gpt(promt, answer, user):
    try:
        await bot.send_message(text=f'Новый запрос:\nОт: {user.id} (<a href="https://t.me/{user.username}">{user.first_name}</a>)\nЗапрос: {promt}\nОтвет: {answer}', parse_mode="HTML", chat_id=group, message_thread_id=9)
    except Exception as e:
        print(e)
async def error(error):
    try:
        await bot.send_message(text=str(error), chat_id=group, message_thread_id=5)
    except Exception as e:
        print(e)    