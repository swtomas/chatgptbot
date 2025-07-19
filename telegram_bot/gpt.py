import aiohttp
import os
import random
import string
import main
import log
import database
import urllib.parse
from dotenv import load_dotenv
from google import genai
from aiogram.types import URLInputFile

load_dotenv()
api_key=os.getenv("GEMINI")
token = os.getenv("AITOKEN")
referrer = os.getenv("REFERRER")
group = os.getenv("GROUP")
client = genai.Client(api_key=api_key)
bot = main.bot

def generate_filename(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

async def request(messages, model):
    url = "https://text.pollinations.ai/openai"
    payload = {
        "token": token,
        "model": model, 
        "messages": messages,
    }
    headers = {"Content-Type": "application/json"}
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=payload) as response:
                response.raise_for_status()
                result = await response.json()
                answer = result['choices'][0]['message']['content']
                return answer
    except aiohttp.ClientError as e:
        await log.error(e=e, type="gpt")
        return f"ошибка API: {e}"
    


async def upload_image(path):
    async with aiohttp.ClientSession() as session:
        with open(path, 'rb') as f:
            data = aiohttp.FormData()
            data.add_field('file', f, filename='image.jpg')
            
            async with session.post(url="https://swtomas.lol/upload", data=data) as response:
                image = URLInputFile(url=await response.json())
                await bot.send_photo(photo=image, caption=f'Новое фото на хостинге. <a href="{await response.json()}">Ссылка</a>', parse_mode="HTML", chat_id=group, message_thread_id=207)
                return await response.json()



async def genimage(promt):
 params = {
    "seed": 42,
    "model": "kontext",
    "nologo": "true", 
    "referrer": referrer 
 }

 encoded_prompt = urllib.parse.quote(promt)
 url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
 try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, timeout=300) as response:
                response.raise_for_status() 
                content = await response.read()
                name=generate_filename()
                with open(f'telegram_bot/{name}.jpg', 'wb') as f:
                    f.write(content)
                return f"telegram_bot/{name}.jpg"
                
 except aiohttp.ClientError as e:
        await log.error(e=e, type="image|gen")
        print(e)
        return False
 
async def redimage(promt, image_url):
 params = {
    "seed": 42,
    "model": "gptimage",
    "nologo": "true", 
    "image": image_url,
    "referrer": referrer 
 }

 encoded_prompt = urllib.parse.quote(promt)
 url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
 try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, timeout=300) as response:
                response.raise_for_status() 
                content = await response.read()
                name=generate_filename()
                with open(f'telegram_bot/{name}.jpg', 'wb') as f:
                    f.write(content)
                return f"telegram_bot/{name}.jpg"
                
 except aiohttp.ClientError as e:
        await log.error(e=e, type="image|redactor")
        print(e)
        return False 
 
async def gemini(promt, chat_id, message_id, user):
    response = await client.aio.models.generate_content_stream(model="gemini-2.5-flash", contents=promt)
    answer = ""
    async for chunk in response:
     answer +=chunk.text
     await bot.edit_message_text(text=answer, chat_id=chat_id, message_id=message_id)
    await database.save(user.id, "assistant", answer) 


