from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# Импорт классов InlineKeyboardMarkup, InlineKeyboardButton  из aiogram.types

import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         input_field_placeholder='Выберите пункт меню.')
button1 = KeyboardButton('Рассчитать')
button2= KeyboardButton('Информация')
kb.row(button1,button2)

kb_in1 = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text='Расчитать норму калорий',callback_data='calories')
button2 = InlineKeyboardButton(text='Формулы расчёта',callback_data='formulas')
kb_in1.add(button1,button2)

start_menu=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Для мужчин'),KeyboardButton(text='Для женщин')
         ]
    ],resize_keyboard=True
)

class UserState(StatesGroup):
    '''
    UserState  для определения группы состояний пользователя в Telegram-боте
    Объекты класса State
    age возраст
    groth рост
    weght вес
    '''
    age: int = State()
    growth: int = State()
    weight: int = State()
    gender: str = State()

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.',reply_markup=kb)

@dp.message_handler(text=['Информация'])
async def start_message(message):
    await message.answer('Рассчёт суточной нормы калорий \n'
                         'по упрощённой формулу Миффлина - Сан Жеора.')



@dp.message_handler(text=['Рассчитать'])
@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.',reply_markup=kb_in1)


@dp.callback_query_handler(text=['formulas'])
async def formulas_info(call_in):
    await call_in.message.answer(f'Для мужчин:\n\t'
                                 f'10*вес + 6.25*рост - 5*возраст + 5\n'
                                 f'Для женщин:\n\t'
                                 f'10*вес + 6.25*рост - 5*возраст -161')
    await call_in.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call_in):
     await call_in.message.answer('Введите свой возраст:')
     # @dp.message_handler выводит сообщение Telegram-бот
     await UserState.age.set()
     await call_in.answer()


@dp.message_handler(state=UserState.age)
# Обернунуть set_age(message) в message_handler,
# который реагирует на текстовое сообщение
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_growth(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def set_gender(message, state):
    await state.update_data(weight=message.text)
    await message.answer('Выбрать категорию',reply_markup=start_menu)
    await UserState.gender.set()

@dp.message_handler(state=UserState.gender)
async def set_gender(message, state):
     # расчёт калорий для категорий мужчина.женщина
    await state.update_data(gender=message.text)
    data_quest = await state.get_data()

    if data_quest['gender'] == 'Для мужчин':
        result = 10 * int(data_quest['weight']) + \
                 6.25 * int(data_quest['growth']) - \
                 5 * int(data_quest['age']) + 5
        gend = data_quest['gender'].lower()

    elif data_quest['gender'] == 'Для женщин':
        result = 10 * int(data_quest['weight']) + \
        6.25 * int(data_quest['growth']) - \
        5 * int(data_quest['age']) - 161

        gend = data_quest['gender'].lower()

    await message.answer(f'Ваша норма калорий: {result} ккал в сутки {gend}',
                         reply_markup=ReplyKeyboardRemove())

    await state.finish()

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
