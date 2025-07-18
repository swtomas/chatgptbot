from aiogram.utils.keyboard import InlineKeyboardBuilder

async def menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="👁️ ChatGPT 4.1", callback_data="chatgpt")
    builder.button(text="🔍 ChatGPT Search", callback_data="chatgptsearch")
    builder.button(text="🧐 ChatGPT o3", callback_data="chatgpto3")
    builder.button(text="🤖 Deepseek R1", callback_data="deepseekr1")
  # builder.button(text="🐟 Deepseek V3", callback_data="deepseekv3")
    builder.button(text="👩‍🎨 ChatGPT Image", callback_data="chatgptimage")
    builder.adjust(1,1,1,1,1,1)
    return builder.as_markup()

async def back():
    builder = InlineKeyboardBuilder()
    builder.button(text="◀️ К другим моделям", callback_data="back")
    builder.adjust(1,1)
    return builder.as_markup()
