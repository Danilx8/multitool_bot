from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_to_voice_input = InlineKeyboardButton('Перейти на голосовые сообщения', callback_data='voice')
button_to_interview = InlineKeyboardButton('Приступить к интервью', callback_data='interview')
button_to_api = InlineKeyboardButton('Задать вопрос оракулу', callback_data='api')
button_to_schedule = InlineKeyboardButton('Записать сегодняшнюю посещаемость', callback_data='schedule')

main_menu_kb = InlineKeyboardMarkup(row_width=1).add(button_to_voice_input).add(button_to_interview).add(button_to_api).add(button_to_schedule)


leave_input = leave_question_input = KeyboardButton('Выйти из выбранного режима')

leave_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(leave_question_input)

delete_keyboard = ReplyKeyboardRemove()
