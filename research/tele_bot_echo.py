import logging
from aiogram import Bot,Dispatcher,executor,types
from dotenv import load_dotenv
import os

load_dotenv()

Api_Token=os.getenv('bot_token')

#print(Api_Token)

#Configure_Logging

logging.basicConfig(level=logging.INFO)

#intialize bot and dispatcher
bot= Bot(token=Api_Token)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def command_start_handler(message:types.Message) -> None:
    await message.answer(f'Hello , I am ECho Bot !')

@dp.message_handler()
async def command_start_handler(message:types.Message) -> None:
    await message.answer(message.text)
if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)


