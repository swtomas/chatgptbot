from aiogram import Router,F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
import buttons
import database
import forms

router = Router()

@router.callback_query(F.data == "back")
async def menu(callback: CallbackQuery):
  try:
   await callback.message.edit_text(text="Выберите нейросеть:", reply_markup=await buttons.menu())
  except Exception as e:
   print(e)

@router.callback_query(F.data == "chatgpt")
async def chatgpt(callback: CallbackQuery, state: FSMContext):
 try:
  await callback.message.edit_text(text=f"Выбрана нейросеть ChatGPT 4.1. Напишите ваш запрос:\n❗Поддерживает: текст, фото", reply_markup=await buttons.back())
  await database.delete(callback.from_user.id)
  await state.set_state(forms.Form.chatgpt)
 except Exception as e:
  print(e)  

@router.callback_query(F.data == "chatgptsearch")
async def chatgptsearch(callback: CallbackQuery, state: FSMContext):
 try:
  await callback.message.edit_text(text=f"Выбрана нейросеть ChatGPT 4o Mini Search Напишите ваш запрос:\n❗Поддерживает: текст", reply_markup=await buttons.back())
  await database.delete(callback.from_user.id)
  await state.set_state(forms.Form.chatgptsearch) 
 except Exception as e:
  print(e)  

@router.callback_query(F.data == "gptaudio")
async def audio(callback: CallbackQuery, state: FSMContext):
 try:
  await callback.message.edit_text(text=f"Выбрана нейросеть ChatGPT Audio. Напишите ваш запрос:", reply_markup=await buttons.back())
  await database.delete(callback.from_user.id)
  await state.set_state(forms.Form.gptaudio) 
 except Exception as e:
  print(e)    

@router.callback_query(F.data == "chatgpto3")
async def chatgpto3(callback: CallbackQuery, state: FSMContext):
 try:
  await callback.message.edit_text(text=f"Выбрана нейросеть ChatGPT o3. Напишите ваш запрос:\n❗Поддерживает: текст, фото", reply_markup=await buttons.back())
  await database.delete(callback.from_user.id)
  await state.set_state(forms.Form.chatgpto3)
 except Exception as e:
  print(e)      

@router.callback_query(F.data == "gemini")
async def gemini(callback: CallbackQuery, state: FSMContext):
 try:
  await callback.message.edit_text(text=f"Выбрана нейросеть Gemini 2.5. Напишите ваш запрос:\n❗Поддерживает: текст, фото, стриминг ответа (Ответ приходит по мере готовности)", reply_markup=await buttons.back())
  await database.delete(callback.from_user.id)
  await state.set_state(forms.Form.gemini)
 except Exception as e:
  print(e)   

@router.callback_query(F.data == "deepseekr1")
async def deepseekr1(callback: CallbackQuery, state: FSMContext):
 try:
  await callback.message.edit_text(text=f"Выбрана нейросеть Deepseek R1. Напишите ваш запрос:\n❗Поддерживает: текст, рассуждение в начале ответа", reply_markup=await buttons.back())
  await database.delete(callback.from_user.id)
  await state.set_state(forms.Form.deepseekr1)
 except Exception as e:
  print(e)  

@router.callback_query(F.data == "deepseekv3")
async def deepseekv3(callback: CallbackQuery, state: FSMContext):
 try:
  await callback.message.edit_text(text=f"Выбрана нейросеть Deepseek V3. Напишите ваш запрос:", reply_markup=await buttons.back())
  await database.delete(callback.from_user.id)
  await state.set_state(forms.Form.deepseekv3)
 except Exception as e:
  print(e)  

@router.callback_query(F.data == "chatgptimage")
async def chatgptimage(callback: CallbackQuery, state: FSMContext):
 try:
  await callback.message.edit_text(text="Выбран генератор изображений ChatGPT Image. Напишите ваш запрос:\n❗Поддерживает: текст, фото с подписью (ИИ редактор)", reply_markup=await buttons.back())
  await state.set_state(forms.Form.chatgptimage)
 except Exception as e:
  print(e)    