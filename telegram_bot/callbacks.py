from aiogram import Router,F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import buttons
import database

class Form(StatesGroup):
 chatgpt=State()
 chatgptsearch=State()
 chatgpto3 = State()
 deepseekr1 = State()
 deepseekv3 = State()
 chatgptimage = State()

router = Router()

@router.callback_query(F.data == "back")
async def menu(callback: CallbackQuery, state: FSMContext):
  try:
   await callback.message.edit_text(text="Выберите нейросеть:", reply_markup=await buttons.menu())
  except Exception as e:
   print(e)

@router.callback_query(F.data == "chatgpt")
async def chatgpt(callback: CallbackQuery, state: FSMContext):
 try:
  await callback.message.edit_text(text=f"Выбрана нейросеть ChatGPT 4.1. Напишите ваш запрос:", reply_markup=await buttons.back())
  await database.delete(callback.from_user.id)
  await state.set_state(Form.chatgpt)
 except Exception as e:
  print(e)  

@router.callback_query(F.data == "chatgptsearch")
async def chatgptsearch(callback: CallbackQuery, state: FSMContext):
 try:
  await callback.message.edit_text(text=f"ChatGPT 4o Mini Search временно недоступна. Попробуйте позже.", reply_markup=await buttons.back())
  await database.delete(callback.from_user.id)
 # await state.set_state(Form.chatgptsearch) 
 except Exception as e:
  print(e)  

@router.callback_query(F.data == "chatgpto3")
async def chatgpto3(callback: CallbackQuery, state: FSMContext):
 try:
  await callback.message.edit_text(text=f"Выбрана нейросеть ChatGPT o3. Напишите ваш запрос:", reply_markup=await buttons.back())
  await database.delete(callback.from_user.id)
  await state.set_state(Form.chatgpto3)
 except Exception as e:
  print(e)      

@router.callback_query(F.data == "deepseekr1")
async def deepseekr1(callback: CallbackQuery, state: FSMContext):
 try:
  await callback.message.edit_text(text=f"Выбрана нейросеть Deepseek R1. Напишите ваш запрос:", reply_markup=await buttons.back())
  await database.delete(callback.from_user.id)
  await state.set_state(Form.deepseekr1)
 except Exception as e:
  print(e)  

@router.callback_query(F.data == "deepseekv3")
async def deepseekv3(callback: CallbackQuery, state: FSMContext):
 try:
  await callback.message.edit_text(text=f"Выбрана нейросеть Deepseek V3. Напишите ваш запрос:", reply_markup=await buttons.back())
  await database.delete(callback.from_user.id)
  await state.set_state(Form.deepseekv3)
 except Exception as e:
  print(e)  

@router.callback_query(F.data == "chatgptimage")
async def chatgptimage(callback: CallbackQuery, state: FSMContext):
 try:
  await callback.message.edit_text(text="Выбран генератор изображений ChatGPT Image. Напишите ваш запрос:", reply_markup=await buttons.back())
  await state.set_state(Form.chatgptimage)
 except Exception as e:
  print(e)    