import requests
import time
from main import BOT_TOKEN
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F
from random import choice

API_URL = 'https://api.telegram.org/bot'
#BOT_TOKEN = '5424991242:AAGwomxQz1p46bRi_2m3V7kvJlt5RjK9xr0'
URL = 'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1'
CARD_URl = 'https://deckofcardsapi.com/api/deck/<<deck_id>>/draw/?count=1'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def get_deck()->str:
    return requests.get(URL).json()['deck_id']

def get_card():
    response = requests.get(f'https://deckofcardsapi.com/api/deck/{get_deck()}/draw/?count=1').json()
    return response['cards'][0]['image']
#print(get_card())


async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


# Этот хэндлер будет срабатывать на отправку боту фото
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
async def send_echo(message: Message):
    print(message)
    #await message.reply_photo(photo=get_card(),has_spoiler=True,caption='zalupa')


# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_echo)

if __name__ == '__main__':
     dp.run_polling(bot)
