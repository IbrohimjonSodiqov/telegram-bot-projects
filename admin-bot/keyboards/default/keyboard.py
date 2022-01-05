from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

til = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text='O`zbek tili🇺🇿'),
        KeyboardButton(text='русский язык🇷🇺'),
        KeyboardButton(text='English🇺🇸'),
    ],
    ],
    resize_keyboard=True
)
newuz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Orqaga🔙")
        ],
    ],
    resize_keyboard=True
)
newru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Назад🔙")
        ],
    ],
    resize_keyboard=True
)

newen = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Back🔙")
        ],
    ],
    resize_keyboard=True
)
tel = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="📱Telefon raqamni yuborish",
                                                      request_contact=True)
                                   ]
                               ])
telru = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="📱Отправить номер телефона",
                                                      request_contact=True)
                                   ]
                               ])
telen = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="📱Send a phone number",
                                                      request_contact=True)
                                   ]
                               ])
profil = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/start")
        ],
    ],
    resize_keyboard=True
)