from aiogram import Router, Bot
from aiogram.types import Message, FSInputFile
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import gpt
import os
import dict
import asyncio
import database
import re
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")
bot = Bot(token=BOT_TOKEN) 
router = Router()
promt = dict.promt

class Form(StatesGroup):
 chatgpt=State()
 chatgptsearch=State()
 chatgpto3 = State()
 deepseekr1 = State()
 deepseekv3 = State()
 chatgptimage = State()

@router.message(StateFilter(None))
async def nostate(message: Message):
 await message.answer("У вас нет активного диалога.\n / new ")
 return

@router.message(Form.chatgpt)
async def chatgpt(message: Message, state: FSMContext):
 try:
  if message.photo:
   try: 
    sent=await message.answer("⌛")
    await asyncio.sleep(0,5)
    await bot.send_chat_action(chat_id=message.chat.id, action="upload_photo")
    photo = message.photo[-1]  
    file = await bot.get_file(photo.file_id)
    file_path = f"telegram_bot/photos/{file.file_id}.jpg"
    await bot.download_file(file.file_path, file_path)
    image_url = await gpt.upload_image(file_path)
    messages=[
    {
      "role": "user",
      "content": [
        { "type": "text", "text": message.caption if message.caption else "Опиши изображения или сделай задания если они есть. Не используй MathJax и форматирование" },
        {
          "type": "image_url",
          "image_url": {"url": image_url}
        }
      ]
    }
  ]
    answer = await gpt.request(messages=messages, model="openai-large")  
    await sent.delete()
    await message.reply(answer)                
    await state.set_state(Form.chatgpt)
    return
   except Exception as e:
    print(e)
    return 
  else: 
   sent=await message.answer("⌛")
   history_messages = await database.get(user_id=message.from_user.id)
   messages = [
    {"role": "system", "content": promt}, 
   *[{"role": role, "content": content} for role, content in history_messages],
    {"role": "user", "content": message.text}
            ]        
   await asyncio.sleep(0,4)
   await bot.send_chat_action(chat_id=message.chat.id, action="TYPING")
   answer=await gpt.request(messages=messages, model="openai-large") 
   await sent.delete()
   await message.reply(text=answer, parse_mode="Markdown")
   await database.save(message.from_user.id, "user", message.text)
   await database.save(message.from_user.id, "assistant", answer)
   await state.set_state(Form.chatgpt)
 except Exception as e:
  await message.answer(f"Произошла ошибка: {e}")
  await message.reply(text=answer)
  await state.set_state(Form.chatgpt)

@router.message(Form.chatgptsearch)
async def chatgptsearch(message: Message, state: FSMContext):
 try:
  if message.photo:
   await message.answer("ChatGPT Search не поддерживает обработку фото")
   await state.set_state(Form.chatgptsearch)
  else: 
   sent=await message.answer("⌛")
   history_messages = await database.get(user_id=message.from_user.id)
   messages = [
    {"role": "system", "content": promt}, 
   *[{"role": role, "content": content} for role, content in history_messages],
    {"role": "user", "content": message.text}
            ]        
   await asyncio.sleep(0,4)
   await bot.send_chat_action(chat_id=message.chat.id, action="TYPING")
   answer=await gpt.request(messages=messages, model="elixposearch") 
   await sent.delete()
   await message.reply(text=answer, parse_mode="Markdown")
   await database.save(message.from_user.id, "user", message.text)
   await database.save(message.from_user.id, "assistant", answer)
   await state.set_state(Form.chatgptsearch)
 except Exception as e:
  await message.answer(f"Произошла ошибка: {e}")  
  await message.reply(text=answer)
  await state.set_state(Form.chatgptsearch)

@router.message(Form.chatgpto3)
async def chatgpto3(message: Message, state: FSMContext):
 try:
  if message.photo:
   try: 
    sent=await message.answer("⌛")
    await asyncio.sleep(0,5)
    await bot.send_chat_action(chat_id=message.chat.id, action="upload_photo")
    photo = message.photo[-1]  
    file = await bot.get_file(photo.file_id)
    file_path = f"telegram_bot/photos/{file.file_id}.jpg"
    await bot.download_file(file.file_path, file_path)
    image_url = await gpt.upload_image(file_path)
    messages=[
    {
      "role": "user",
      "content": [
        { "type": "text", "text": message.caption if message.caption else "Опиши изображения или сделай задания если они есть. Не используй MathJax и форматирование" },
        {
          "type": "image_url",
          "image_url": {"url": image_url}
        }
      ]
    }
  ]
    answer = await gpt.request(messages=messages, model="o3")  
    await sent.delete()
    await message.reply(answer)                
    await state.set_state(Form.chatgpto3)
    return
   except Exception as e:
    print(e)
    return 
  else: 
   sent=await message.answer("⌛")
   history_messages = await database.get(user_id=message.from_user.id)
   messages = [
    {"role": "system", "content": promt}, 
   *[{"role": role, "content": content} for role, content in history_messages],
    {"role": "user", "content": message.text}
            ]        
   await asyncio.sleep(0,4)
   await bot.send_chat_action(chat_id=message.chat.id, action="TYPING")
   answer=await gpt.request(messages=messages, model="o3") 
   await sent.delete()
   await message.reply(text=answer, parse_mode="Markdown")
   await database.save(message.from_user.id, "user", message.text)
   await database.save(message.from_user.id, "assistant", answer)
   await state.set_state(Form.chatgpto3)
 except Exception as e:
  await message.answer(f"Произошла ошибка: {e}")
  await message.reply(text=answer) 
  await state.set_state(Form.chatgpto3)

@router.message(Form.deepseekr1)
async def deepseekr1(message: Message, state: FSMContext):
 try:
  if message.photo:
   try: 
    await message.answer("Deepseek R1 не поддерживает обработку фото.")
    await state.set_state(Form.deepseekr1)
   except Exception as e:
    print(e)
    return 
  else: 
   sent=await message.answer("⌛")
   history_messages = await database.get(user_id=message.from_user.id)
   messages = [
    {"role": "system", "content": "Не используй MathJax и форматирование текста"}, 
   *[{"role": role, "content": content} for role, content in history_messages],
    {"role": "user", "content": message.text}
            ]        
   await asyncio.sleep(0,4)
   await bot.send_chat_action(chat_id=message.chat.id, action="TYPING")
   answer=await gpt.request(messages=messages, model="deepseek-reasoning")
   filtered = re.sub(r'<(/?)(think)\b', r'<\1blockquote', answer, flags=re.IGNORECASE) 
   await sent.delete()
   await message.reply(text=filtered, parse_mode="HTML")
   await database.save(message.from_user.id, "user", message.text)
   await database.save(message.from_user.id, "assistant", answer)
   await state.set_state(Form.chatgpto3)
 except Exception as e:
  await message.answer(f"Произошла ошибка: {e}")
  await message.reply(text=filtered)   

@router.message(Form.chatgptimage)
async def gptimage(message: Message, state: FSMContext):
 try:
   if message.photo:
     if message.caption == None:
      await message.reply("Пожалуйста, укажите что нужно сделать в подписи к фотографии")
      return
     sent=await message.answer("⌛")
     await asyncio.sleep(0,5)
     await bot.send_chat_action(chat_id=message.chat.id, action="upload_photo")
     photo = message.photo[-1]  
     file = await bot.get_file(photo.file_id)
     file_path = f"telegram_bot/photos/{file.file_id}.jpg"
     await bot.download_file(file.file_path, file_path)
     image_url = await gpt.upload_image(file_path)
     image = await gpt.redimage(promt=message.caption, image_url=image_url)
     if image == False:
      await message.answer("Что-то пошло не так. Попробуйте позже.")
      return
     photo = FSInputFile(image)
     await sent.delete()
     await message.answer_photo(photo=photo)
     os.remove(image)
   else:
    sent = await message.answer("🎨")
    image = await gpt.genimage(promt=message.text)
    sent.delete()
    if image == False:
     await message.answer("Что-то пошло не так. Попробуйте позже.")
     return
    photo = FSInputFile(image)
    await sent.delete()
    await message.answer_photo(photo=photo)
    os.remove(image)
    
 except Exception as e:
  print(e)