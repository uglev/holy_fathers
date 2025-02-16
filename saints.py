import pickle
import random
import os
from telebot import TeleBot
from dotenv import find_dotenv, load_dotenv, set_key

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

ID_MESSAGE = os.getenv('ID_MESSAGE')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

bot = TeleBot(TELEGRAM_TOKEN)

def send_message(message):
    if ID_MESSAGE != 0:
        try:
            bot.delete_message(chat_id=CHAT_ID, message_id=ID_MESSAGE)
        except:
            print(f"Error deleting message {ID_MESSAGE}")
    new_id_message = bot.send_message(chat_id=CHAT_ID, text=message)
    set_key(dotenv_file, 'ID_MESSAGE', str(new_id_message.id))

with open('saints.pickle', 'rb') as f:
    data_new = pickle.load(f)
number = random.randint(0, len(data_new)-1)
result = f'Братие, послание святаго отца нашего, {data_new[number][0]}, чтение.\n\n {data_new[number][1]}'
send_message(result)