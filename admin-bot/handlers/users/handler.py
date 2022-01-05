from aiogram import types
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from data.config import ADMINS
from loader import dp, bot
from keyboards.default.keyboard import newuz, newru, newen, tel, profil, telen, telru
from states.personalData import PersonalData
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="O`zbek tili🇺🇿", state=None)
async def send_message(message: types.Message):
    await message.reply("Til muvaffaqiyatli tanlandi👍\nToliq ismingizni kiriting: ")
    await PersonalData.fullName.set()
@dp.message_handler(state=PersonalData.fullName)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data(
        {"name": fullname}
    )
    await message.answer("Email manzil kiriting")
    await PersonalData.next()
@dp.message_handler(state=PersonalData.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(
        {"email": email}
    )
    await message.answer("Telefon raqam kiriting", reply_markup=tel)

    await PersonalData.next()
@dp.message_handler(content_types='contact',state=PersonalData.phoneNum)
async def answer_phone(message: types.Message, state: FSMContext):
    contact = message.contact
    contact2 = message.contact.phone_number
    await state.update_data(
        {"phone": contact2}
    )
    await message.answer("Yashash joyingizni kiriting:")
    await PersonalData.next()
@dp.message_handler(state=PersonalData.location)
async def answer_phone(message: types.Message, state: FSMContext):
    joy = message.text
    await state.update_data(
        {"joy": joy}
    )
    
    data = await state.get_data()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    joy = data.get("joy")
    await message.answer("Raxmat, malumotlar qabul qilindi", reply_markup=profil)
    await message.answer(text=f"Sizning malumotlaringiz:\n\nIsmingiz:{name}\nTelefon raqam: {phone}\nEmail: {email}\nYashash manilingiz:{joy}")
    await message.answer("Xabar adminga yuborildi")
    await bot.send_message(chat_id=ADMINS[0], text=f"Foydalanuvchi: {message.from_user.full_name}\n\nMalumotlari: Ismi:{name}\nTelefon raqami:{phone}\nEmail: {email}\nYashash manzili: {joy}")
    await state.finish()
@dp.message_handler(text="русский язык🇷🇺", state=None)
async def send_message(message: types.Message):
    await message.reply("Язык выбран успешно👍\n\nВведите свое полное имя", reply_markup=newru)
    await PersonalData.nameru.set()
@dp.message_handler(state=PersonalData.nameru)
async def answer_fullname(message: types.Message, state: FSMContext):
    nameru = message.text
    await state.update_data(
        {"nameru": nameru}
    )
    await message.answer("Введите ваш адрес электронной почты")
    await PersonalData.next()
@dp.message_handler(state=PersonalData.emailru)
async def answer_email(message: types.Message, state: FSMContext):
    emailru = message.text
    await state.update_data(
        {"emailru": emailru}
    )
    await message.answer("Введите номер телефона", reply_markup=telru)

    await PersonalData.next()
@dp.message_handler(content_types='contact',state=PersonalData.phoneru)
async def answer_phone(message: types.Message, state: FSMContext):
    contact = message.contact
    contact3 = message.contact.phone_number
    await state.update_data(
        {"phoneru": contact3}
    )
    await message.answer("Укажите ваше место жительства: ")
    await PersonalData.next()
@dp.message_handler(state=PersonalData.locationru)
async def answer_phone(message: types.Message, state: FSMContext):
    locationru = message.text
    await state.update_data(
        {"joyru": locationru}
    )
    
    data = await state.get_data()
    nameru = data.get("nameru")
    emailru = data.get("emailru")
    phoneru = data.get("phoneru")
    joyru = data.get("joyru")
    await message.answer("Спасибо, данные были получены", reply_markup=profil)
    await message.answer(text=f"Ваши данные:\n\nИмя:{nameru}\nТелефонный номер: {phoneru}\nEmail: {emailru}\nАдрес места проживания:{joyru}")
    await message.answer("Сообщение отправлено админу")
    await bot.send_message(chat_id=ADMINS[0], text=f"Пользователь: {message.from_user.full_name}\n\nИнформация:\nИмя:{nameru}\nТелефонный номер:{phoneru}\nEmail: {emailru}\nАдрес места проживания: {joyru}")
    await state.finish()
@dp.message_handler(text="English🇺🇸", state=None)
async def send_message(message: types.Message):
    await message.reply("Language selected successfully👍\n\nInput your full name: ", reply_markup=newen)
    await PersonalData.namen.set()
@dp.message_handler(state=PersonalData.namen)
async def answer_fullname(message: types.Message, state: FSMContext):
    namen = message.text
    await state.update_data(
        {"namen": namen}
    )
    await message.answer("Input your email: ")
    await PersonalData.next()
@dp.message_handler(state=PersonalData.emailen)
async def answer_email(message: types.Message, state: FSMContext):
    emailen = message.text
    await state.update_data(
        {"emailen": emailen}
    )
    await message.answer("Input your phone number", reply_markup=telen)

    await PersonalData.next()
@dp.message_handler(content_types='contact',state=PersonalData.phonen)
async def answer_phone(message: types.Message, state: FSMContext):
    contact = message.contact
    contact4 = message.contact.phone_number
    await state.update_data(
        {"phonen": contact4}
    )
    await message.answer("Input your location:")
    await PersonalData.next()
@dp.message_handler(state=PersonalData.locationen)
async def answer_phone(message: types.Message, state: FSMContext):
    joyen = message.text
    await state.update_data(
        {"joyen": joyen}
    )
    
    data = await state.get_data()
    namen = data.get("namen")
    emailen = data.get("emailen")
    phonen = data.get("phonen")
    joyen = data.get("joyen")
    await message.answer("Thanks, the data has been received", reply_markup=profil)
    await message.answer(text=f"Your informations:\n\nYour name:{namen}\nPhone number: {phonen}\nEmail: {emailen}\nYour location:{joyen}")
    await message.answer("The message was sent to the admin")
    await bot.send_message(chat_id=ADMINS[0], text=f"User: {message.from_user.full_name}\n\Informations:\nName:{namen}\nPhone number:{phonen}\nEmail: {emailen}\nLocation: {joyen}")
    await state.finish()