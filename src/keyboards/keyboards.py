
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_customer_keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)

customers_keyboard = {
    '🧮 Калькулятор стоимости': 'calc',
    '🔗 Как отправить ссылку': 'get_link',
    '🏷 Получить скидку': 'get_free',
    '📦 Доставка': 'deliver'
}

order_button = InlineKeyboardButton('🛒 Оформить заказ', url='https://t.me/Yan_Elenskiy')
inline_customer_keyboard.add(order_button)

for key, value in customers_keyboard.items():
    inline_customer_keyboard.add(InlineKeyboardButton(key, callback_data=value))

help_button = InlineKeyboardButton('☎️ Задать вопрос / помощь', url='https://t.me/Yan_Elenskiy')
inline_customer_keyboard.add(help_button)

deliver_button = InlineKeyboardButton('Скачать приложение Poizon IOS 🍏', url='https://apps.apple.com/kz/app/得物-有毒的运动-潮流-好物/id1012871328')
inline_customer_keyboard.add(deliver_button)

deliver_button = InlineKeyboardButton('Скачать приложение Poizon Android 📱', url='https://www.anxinapk.com/rj/12201303.html')
inline_customer_keyboard.add(deliver_button)


