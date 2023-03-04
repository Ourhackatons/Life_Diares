from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


async def start(message: types.Message):
    await message.answer(text='Привет баля')


def client_register_message_handler(dp: Dispatcher):
    dp.register_message_handler(start, content_types=['text'])
