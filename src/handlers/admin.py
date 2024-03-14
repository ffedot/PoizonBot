from aiogram.dispatcher import FSMContext
from aiogram import types

from src.config import ADMIN_LIST

from src.bot import bot, dp
from src.states import *


@dp.message_handler(commands=['admin'])
async def admin_start(message: types.Message):
    if message.from_user.id in ADMIN_LIST:

        with open('A:\шерлок\Ян_Еленский\src\data\cost.txt', "r", encoding='utf-8') as f:
            cost = f.read()

        await message.answer(f'Курс сейчас:{cost}\n'
                             f'чтобы изменить курс отправьте боту новоё значениe\n'
                             f'Доступно только админу!')

        await ChangeCost.step_1.set()


@dp.message_handler(state= ChangeCost.step_1)
async def calc_get_price(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMIN_LIST:

        with open('A:\шерлок\Ян_Еленский\src\data\cost.txt', "w", encoding='utf-8') as f:
            f.write(message.text)

        await message.answer(f'Курс изменён на:{message.text}\n')
        await state.finish()

