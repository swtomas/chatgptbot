import aiohttp
import os
import random
import string
import urllib.parse
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("AITOKEN")
referrer = os.getenv("REFERRER")

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
        return f"ошибка API: {e}"
    


async def upload_image(path):
    async with aiohttp.ClientSession() as session:
        with open(path, 'rb') as f:
            data = aiohttp.FormData()
            data.add_field('file', f, filename='image.jpg')
            
            async with session.post(url="https://swtomas.lol/upload", data=data) as response:
                return await response.json()



async def genimage(promt):
 params = {
    "width": 1280,
    "height": 720,
    "seed": 42,
    "model": "gptimage",
    "nologo": "true", 
    "token": token 
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
        print(e)
        return False