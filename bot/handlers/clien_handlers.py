from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


# import openai
# from . import settings
# openai.api_key = settings.OPEN_AI.get('API_KEY')


async def start(message: types.Message):
    await message.answer(text='Привет ска')


# async def start(message: types.Message):
#     await message.answer(text=f"{openai.Completion.create(model=settings.OPEN_AI.get('MODEL'), prompt=message.text,
#     temperature=2, max_tokens=4000).get('choices')[0].get('text')}")


async def new_post(message: types.Message):
    await message.answer('АО, записано')


async def del_post(message: types.Message):
    await message.answer('Запись удалена')


async def my_posts(message: types.Message):
    await message.answer('Вот балять')


async def photo(message: types.Message):
    await message.answer(message.photo[0].file_id)


async def video(message: types.Message):
    await message.answer(message.video.file_id)


async def audio(message: types.Message):
    await message.answer(message.audio.file_id)


async def voice(message: types.Message):
    await message.answer(message.voice.file_id)


def client_register_message_handler(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(start, Text(equals='Начать', ignore_case=True))
    dp.register_message_handler(new_post, commands=['new_post'])
    dp.register_message_handler(new_post, Text(equals='Новая запись', ignore_case=True))
    dp.register_message_handler(del_post, commands=['del_post'])
    dp.register_message_handler(del_post, Text(equals='Удалить запись', ignore_case=True))
    dp.register_message_handler(my_posts, commands=['my_post'])
    dp.register_message_handler(my_posts, Text(equals='Мои записи', ignore_case=True))
    dp.register_message_handler(photo, content_types=['photo'])
    dp.register_message_handler(video, content_types=['video'])
    dp.register_message_handler(audio, content_types=['audio'])
    dp.register_message_handler(voice, content_types=['voice'])
