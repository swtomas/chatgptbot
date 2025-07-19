from aiogram.utils.keyboard import InlineKeyboardBuilder

async def menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="👁️ ChatGPT 4.1", callback_data="chatgpt")
    builder.button(text="🔍 ChatGPT Search", callback_data="chatgptsearch")
    builder.button(text="🧐 ChatGPT o3 | вычисления", callback_data="chatgpto3")
    builder.button(text="👾 Gemini 2.5 | стриминг", callback_data="gemini")
    builder.button(text="🤖 Deepseek R1 | мышление", callback_data="deepseekr1")
    builder.button(text="🎨 Генератор | редактор фото", callback_data="chatgptimage")
    builder.adjust(1,1,1,1,1,1,1)
    return builder.as_markup()

async def back():
    builder = InlineKeyboardBuilder()
    builder.button(text="◀️ К другим моделям", callback_data="back")
    builder.adjust(1,1)
    return builder.as_markup()
