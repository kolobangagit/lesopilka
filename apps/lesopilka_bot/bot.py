import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6569461259:AAEu8HfH6vohmD3QK93CUkDKX6D5nLuRzV4")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

# Запуск процесса поллинга новых апдейтов


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
