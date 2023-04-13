from aiogram.dispatcher.filters.state import State, StatesGroup


class MainMenuState(StatesGroup):
    wait_for_answer = State()


class VoiceInputState(StatesGroup):
    wait_for_answer = State()


class InterviewState(StatesGroup):
    name_input = State()
    age_input = State()
    height_input = State()
