import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.keyboard import til
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    await message.answer(f"Assalomu alaykum hurmatli{name}\nBotimizga hush kelipsiz\nKerakli tilni tanlang🔽\n\nHello dear{name}\nWelcome to our bot\nChoose the desired language🔽\n\nЗдравствуйте,дорогой{name}\nДобро пожаловать к нашему боту\nВыберите желаемый язык🔽", reply_markup=til)
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)