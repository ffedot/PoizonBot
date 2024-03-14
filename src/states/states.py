from aiogram.dispatcher.filters.state import State, StatesGroup


class GetPrice(StatesGroup):
    step_1 = State()
    step_2 = State()


class ChangeCost(StatesGroup):
    step_1 = State()
    step_2 = State()