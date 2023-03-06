from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


async def start(message: types.Message):
    await message.answer(text='Привет баля')


async def new_post(message: types.Message):
    await message.answer('АО, записано')


async def del_post(message: types.Message):
    await message.answer('Запись удалена')


async def my_posts(message: types.Message):
    await message.answer('Вот балять')


def client_register_message_handler(dp: Dispatcher):
    dp.register_message_handler(start, content_types=['text'])
    dp.message_handler(new_post)
    dp.message_handler(del_post)
    dp.message_handler(my_posts)
