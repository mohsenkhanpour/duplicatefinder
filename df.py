import os
from telethon import TelegramClient, events, sync
from dotenv import load_dotenv


# Client configuration
load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
chat_id = os.getenv("CHAT_ID")

# Client connection
client = TelegramClient('DuplicateFinder', api_id, api_hash)
client.start()
print("Connected as:", client.get_me().username)


# Iterate over messages
messages_ds_iter = client.iter_messages(chat_id, limit=1000000, min_id=307522)

unique_messages = []
duplicate_messages = []
duplicate_ids = []

for message in messages_ds_iter:
    if message.message in unique_messages:
        duplicate_messages.append(message.message)
        duplicate_ids.append(message.id)
        print("Duplicate found:", message.id,":", message.message)
    else:
        unique_messages.append(message.message)

print(duplicate_ids, file=open("output_ids.txt", "w"))


def save_to_file(message):
    print(str(message.encode("unicode_escape"), "utf-8"),
          "\n", file=open("output.txt", "a"))


for message in duplicate_messages:
    save_to_file(message)

print(duplicate_ids)

for message in duplicate_ids:
    client.delete_messages(chat_id, message)
    print("Duplicate removed:", message)

print("All duplicates removed.")
