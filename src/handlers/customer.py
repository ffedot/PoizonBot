from aiogram.types import Message, BotCommand
from aiogram import types
from aiogram.dispatcher import FSMContext

from src.bot import bot, dp
from src.keyboards import inline_customer_keyboard
from src.states import *



@dp.message_handler(commands=['start'])
async def customer_start(message: types.Message):
    try:
            await message.answer("Добро Пожаловать в бот группы Poizon Order", reply_markup=inline_customer_keyboard)
            bot_commands = [
                BotCommand(command="/start", description="Перезапустить бота")
            ]
            await bot.set_my_commands(bot_commands)
    except Exception as Eror:
        await message.answer('Произошла ошибка ⚠️, попробуйте ещё раз', reply_markup=inline_customer_keyboard)


@dp.callback_query_handler(lambda cb: cb.data == 'calc', state='*')
async def calc(callback_query: types.CallbackQuery, state: FSMContext, object = None):
    try:
        await callback_query.message.edit_text('📊 Отправьте боту сумму в юанях¥, на которую хотите оформить заказ')
        await GetPrice.step_1.set()
    except Exception as Eror:
        await state.finish()
        await callback_query.message.answer('Произошла ошибка ⚠️, попробуйте ещё раз', reply_markup=inline_customer_keyboard)


@dp.message_handler(state= GetPrice.step_1)
async def calc_get_price(message: types.Message, state: FSMContext):
    try:

        with open('A:\шерлок\Ян_Еленский\src\data\cost.txt', "r", encoding='utf-8') as f:
            cost = f.read()
        summ = float(message.text)/float(cost)
        commision = 450
        if summ >= 10001  and summ <= 19000:
            commision = 900
        elif summ >= 19001  and summ <= 27000:
            commision = 1500
        elif summ >= 27001  and summ <= 40000:
            commision = 2300
        elif summ >= 40001  and summ <= 100000:
            commision = 3500
        elif summ > 100000:
            commision = 5500

        await message.answer(f"Цена: {round(summ + commision)}₽\nБез учёта доставки", reply_markup=inline_customer_keyboard)
        await state.finish()
    except ValueError as Eror:
        await state.finish()
        await message.answer("Это не число, попробуйте заного", reply_markup=inline_customer_keyboard)


@dp.callback_query_handler(lambda cb: cb.data == 'get_link', state='*')
async def link(callback_query: types.CallbackQuery, state: FSMContext):
    try:

        photo1 = open('A:\шерлок\Ян_Еленский\src\data\photo_2024-03-11_23-33-02.jpg', 'rb')
        photo2 = open('A:\шерлок\Ян_Еленский\src\data\photo_2024-03-14_15-02-03.jpg', 'rb')

        await callback_query.message.answer_photo(photo2)
        await callback_query.message.answer_photo(photo1)

        await bot.send_message(callback_query.message.chat.id, '1. Открываем приложение Poizon (dewu) на своем смартфоне и нажимаем на иконку "пакетика" в нижней строке\n'
                                                '2. В поисковой строке вводим название нужного товара на английском языке\n'
                                                '3. Кликаем на желаемый товар и попадаем в карточку товарa\n'
                                                '4. Находясь в карточке товара кликаем на зеленую иконку отмеченную на скриншоте\n'
                                                '5. Далее, кликаем на иконку копирования\n'
                                                'Готово! Теперь вы сможете поделиться ссылкой и получить расчет по стоимости.', reply_markup=inline_customer_keyboard)

    except Exception as Eror:
        await state.finish()
        await callback_query.message.answer('Произошла ошибка ⚠️, попробуйте ещё раз', reply_markup=inline_customer_keyboard)


@dp.callback_query_handler(lambda cb: cb.data == 'get_free', state='*')
async def link(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await callback_query.message.edit_text('- При 3-третьем и последующих заказах предоставляется скидка 10% на комиссию.\n'
                                                '-За приведенного друга скидка 300 рублей', reply_markup=inline_customer_keyboard)

    except Exception as Eror:
        await state.finish()
        await callback_query.message.answer('Произошла ошибка ⚠️, попробуйте ещё раз', reply_markup=inline_customer_keyboard)


@dp.callback_query_handler(lambda cb: cb.data == 'deliver', state='*')
async def link(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await callback_query.message.edit_text("""
• Доставка товара до Владивостока в течение 9 дней с момента оформления заказа.\n 
• Стоимость 370кг. 🚛 \n
• Если вес заказа меньше 1 кг, то сумма заказа будет рассчитываться по цене за грамм. \n
• Доставка с Владивостока по России до вашего адреса осуществляется любым удобным для вас способом""", reply_markup=inline_customer_keyboard)

    except Exception as Eror:
        await state.finish()
        await callback_query.message.answer('Произошла ошибка ⚠️, попробуйте ещё раз', reply_markup=inline_customer_keyboard)

