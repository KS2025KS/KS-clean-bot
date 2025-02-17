import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType
from aiogram.utils import executor
from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Привіт! Надішли фото, щоб відправити звіт чистоти ☕️")

@dp.message_handler(content_types=ContentType.PHOTO)
async def handle_photo(message: types.Message):
    photo = message.photo[-1].file_id
    caption = f"Фотозвіт від {message.from_user.full_name} ({message.from_user.id})"

    GROUP_CHAT_ID = -123456789  # Замінити на ID групи
    await bot.send_photo(chat_id=GROUP_CHAT_ID, photo=photo, caption=caption)

    await message.reply("Фото прийнято! ✅")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)