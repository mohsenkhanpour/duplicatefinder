import os
from telethon import TelegramClient, events, sync
from dotenv import load_dotenv
load_dotenv()

# Client configuration
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

client = TelegramClient('DuplicateFinder', api_id, api_hash)
client.start()
print("Connected as:", client.get_me().username)

""" messages_ds_get = client.get_messages("dailystrips", limit=5)
for message in messages_ds_get:
        print(message.id, message.message) """

messages_ds_iter = client.iter_messages("dailystrips", limit=10000000)

unique_messages = []
duplicate_messages = []
for message in messages_ds_iter:
    if message.message in unique_messages:
        duplicate_messages.append(message.message)
    else:
        unique_messages.append(message.message)

""" print(unique_messages) """

def save_to_file(message):
        print(str(message.encode("unicode_escape"),"utf-8"), "\n", file=open("output.txt", "a")) 
        
for message in duplicate_messages:
        save_to_file(message)
        print(message)
