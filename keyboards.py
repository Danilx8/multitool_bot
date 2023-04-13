from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_to_voice_input = InlineKeyboardButton('Перейти на голосовые сообщения', callback_data='voice')
button_to_interview = InlineKeyboardButton('Приступить к интервью', callback_data='interview')

main_menu_kb = InlineKeyboardMarkup(row_width=1).add(button_to_voice_input).add(button_to_interview)


leave_voice_input = KeyboardButton("Прервать прослушку!")

leave_voice_input_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(leave_voice_input)