from aiogram.dispatcher.filters.state import State, StatesGroup


class StartingState(StatesGroup):
    wait_for_answer = State()


class VoiceInputState(StatesGroup):
    wait_for_answer = State()


class InterviewState(StatesGroup):
    wait_for_answer = State()
