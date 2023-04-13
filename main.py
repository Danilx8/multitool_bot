from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove

from Token import TOKEN
from states import MainMenuState, VoiceInputState, InterviewState
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def initialize(message: types.Message, state:FSMContext):
    await bot.send_message(text='Приветствую в многофункциональном боте! Выберите функцию, с которой хотели'
                                ' бы поработать!', reply_markup=kb.main_menu_kb, chat_id=message.chat.id)


@dp.callback_query_handler(text='voice')
async def query_handle(call: types.callback_query):
    await VoiceInputState.wait_for_answer.set()
    await bot.send_message(text='Теперь я реагирую только на голосовые сообщения. Скажи что-нибудь!',
                           reply_markup=kb.leave_voice_input_kb, chat_id=call.message.chat.id)


@dp.message_handler(content_types=types.ContentType.ANY, state=VoiceInputState.wait_for_answer)
async def audio_handler(message: types.Message, state=FSMContext):
    if message.voice:
        await message.reply('Слышу тебя! Приём.')
    elif message.text != 'Прервать прослушку!':
        await message.reply('Не понимаю тебя. Запиши голосовое!')
    else:
        await state.finish()
        delete_keyboard = ReplyKeyboardRemove()
        await message.reply('Хорошо поговорили!', reply_markup=delete_keyboard)
        await bot.send_message(text='Можешь посмотреть и другие режимы, доступные в этом боте', chat_id=message.chat.id,
                            reply_markup=kb.main_menu_kb)


@dp.callback_query_handler(text='interview')
async def interview_begin(call: types.CallbackQuery, state: FSMContext):
    await InterviewState.age_input.set()
    await call.message.reply('Давай знакомиться! Как тебя зовут?')


@dp.message_handler(state=InterviewState.age_input)
async def name_parse(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await state.update_data({"name": message.text})
        await InterviewState.name_input.set()
        await message.reply(f'Приятно познакомиться, {message.text}!\n\nТеперь скажи, сколько тебе лет?')
    else:
        await message.reply('Просто введи уже своё имя')


@dp.message_handler(state=InterviewState.name_input)
async def age_parse(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data({"age": message.text})
        age = (await state.get_data())['age']
        word = "лет"
        if (age % 10 == 1):
            word = "год"
        elif (age % 10 > 1 and age % 10 < 5):
            word = "года"
        await message.reply(f'Итак, тебе {age} {word}. И какого ты роста?')
        await InterviewState.height_input.set()
    else:
        await message.reply('Не похоже на возраст...')


@dp.message_handler(state=InterviewState.height_input)
async def height_parse(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data({"height": message.text})
        print(await state.get_data())
        name = (await state.get_data())['name']
        age = (await state.get_data())['age']
        height = (await state.get_data())['height']
        word = "лет"
        if (age % 10 == 1):
            word = "год"
        elif (age % 10 > 1 and age % 10 < 5):
            word = "года"
        await bot.send_message(text=f'Супер! Подытожим, {name}\nТебе {age} {word}\nТвой рост - '
                            f'{height}\nТеперь я знаю о тебе чуть больше.\n\nМожешь посмотреть и другие '
                            f'режимы, доступные в этом боте!', reply_markup=kb.main_menu_kb, chat_id=message.chat.id)
        await state.finish()
    else:
        await message.reply('Не похоже на рост...')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
