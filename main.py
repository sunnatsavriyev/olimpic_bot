from aiogram import Bot, Dispatcher, types, executor
import logging
from aiogram.types import  ReplyKeyboardMarkup
from medaltable import fetch_data1
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from boshqa_oyinlar import fetch_data3



TOKEN = '7336574102:AAEhLD72qDsOSpJ-oD9k9NaAiZvaJLliVjQ'
# Set up logging
logging.basicConfig(level=logging.INFO)

# Retrieve the bot token from environment variable



# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
scheduler = AsyncIOScheduler()

def get_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    button1 = types.KeyboardButton("Medallar Jadvali🏆")
    button3 = types.KeyboardButton("Sport turlari ro'yhati🎗")
    keyboard.add(button1, button3)
    return keyboard

def send_long_message(chat_id, text):
    # Telegram's limit is 4096 characters per message
    MAX_LENGTH = 4096
    for i in range(0, len(text), MAX_LENGTH):
        part = text[i:i+MAX_LENGTH]
        bot.send_message(chat_id, part)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Olimpiada 2024 nima haqida bilmoqchisiz? 👇", reply_markup=get_keyboard())

@dp.message_handler(lambda message: message.text == "/start")
async def handle_start(message: types.Message):
    await send_welcome(message)
    


@dp.message_handler(lambda message: message.text == "Medallar Jadvali🏆")
async def handle_medals(message: types.Message):
    api_url = 'https://apis.codante.io/olympic-games/countries'  # Url kiritish
    data = fetch_data1(api_url)
    response_message = f"Medallar Jadvali: \n {data}" if data else "Bu qism uchun malumot yo'q afsus!"
    await bot.send_message(message.chat.id, response_message)



@dp.message_handler(lambda message: message.text == "Sport turlari ro'yhati🎗")
async def handle_sports(message: types.Message):
    api_url = 'https://apis.codante.io/olympic-games/disciplines'  # Url kiritish
    data = fetch_data3(api_url)
    response_message = f"Barcha sport turlari: \n {data}" if data else "Bu qism uchun malumot yo'q afsus!"
    await bot.send_message(message.chat.id, response_message)


# Function to send daily reminder
async def send_daily_reminder():
    chat_ids = [] 
    api_url = 'https://apis.codante.io/olympic-games/countries'  # Url kiritish
    data = fetch_data1(api_url)
    response_message = f"Medallar Jadvali Bugungi: \n {data}" if data else "Bu qism uchun malumot yo'q afsus!"
    for chat_id in chat_ids:
        await bot.send_message(chat_id, response_message)

# Schedule the daily reminder
scheduler.add_job(send_daily_reminder, CronTrigger(hour=9, minute=28, second=0, timezone='UTC'))

# Start the scheduler
scheduler.start()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




