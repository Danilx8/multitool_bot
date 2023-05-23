from aiogram.dispatcher.filters.state import State, StatesGroup


class MainMenuState(StatesGroup):
    wait_for_answer = State()


class VoiceInputState(StatesGroup):
    wait_for_answer = State()


class InterviewState(StatesGroup):
    name_input = State()
    age_input = State()
    height_input = State()


class QuestionState(StatesGroup):
    wait_for_answer = State()


class ScheduleState(StatesGroup):
    subject_input = State()
    students_input = State()


class ChatState(StatesGroup):
    wait_for_answer = State();
