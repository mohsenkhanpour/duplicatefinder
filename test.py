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

messages_dailystrips = client.get_messages("dailystrips", limit=5)
for message in messages_dailystrips:
        print(message.id, message.message)

messages_dailystrips2 = client.iter_messages("dailystrips", limit=1000)

for message in messages_dailystrips:
        print(message.id, message.message)