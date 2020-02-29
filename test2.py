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

duplicate_ids = [171824]

for message in duplicate_ids:
    client.delete_messages("dailystrips", message)
    print("duplicate removed:", message)