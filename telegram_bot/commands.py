from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
import buttons
import dict
import database

router = Router()

@router.message(Command("start"))
async def start(message: Message):
  try:
    await database.add_user(user_id=message.from_user.id)
    await message.answer(text=f"Привет, {message.from_user.first_name} {message.from_user.last_name if message.from_user.last_name else ""} {dict.hello}")
  except Exception as e:
    print(e)

@router.message(Command("new"))
async def new(message: Message):
  try:
    await message.answer("Выберите нейросеть:", reply_markup=await buttons.menu())
  except Exception as e:
    print(e)  

@router.message(Command("clear"))
async def check(message: Message):
   try: 
    await database.delete(message.from_user.id)
    await message.answer("✅ Контекст очищен \n /new - поменять нейросеть")    
   except Exception as e:
     print(e) 