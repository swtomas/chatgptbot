import aiosqlite
import os

DB_NAME = "telegram_bot/chat.db"
DB_USNAME = "telegram_bot/users.db"


async def init():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''CREATE TABLE IF NOT EXISTS history
                          (user_id INT, role TEXT, content TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        await db.commit()

async def get(user_id, limit=5):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute('''SELECT role, content FROM history 
                                   WHERE user_id = ? 
                                   ORDER BY timestamp DESC LIMIT ?''', (user_id, limit))
        history = await cursor.fetchall()
        return reversed(history)   

async def save(user_id, role, content):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''INSERT INTO history (user_id, role, content) 
                          VALUES (?, ?, ?)''', (user_id, role, content))
        await db.commit()

async def delete(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''DELETE FROM history WHERE user_id = ?''', (user_id,))
        await db.commit()        

async def init_userdb():
    async with aiosqlite.connect(DB_USNAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY
            )
        """)
        await db.commit()

async def add_user(user_id: int):
    async with aiosqlite.connect(DB_USNAME) as db:
        await db.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
        await db.commit()        