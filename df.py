import os
import json
import datetime
import asyncio
from datetime import timedelta
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import SearchRequest
from telethon.tl.types import InputMessagesFilterEmpty
from telethon.tl.functions.messages import GetHistoryRequest
from dotenv import load_dotenv
load_dotenv()

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
channel_name = os.getenv("CHANNEL_NAME")


client = TelegramClient('DuplicateFinder', api_id, api_hash)
client.start()
print(client.get_me().stringify())

result = client(GetHistoryRequest(
    peer=channel_name,  # On which chat/conversation
    offset_date=datetime.date(2018, 6, 2),       # Maximum date
    offset_id=0,            # ID of the message to use as offset
    add_offset=0,           # Additional offset
    limit=1000000,                # How many results
    max_id=0,               # Maximum message ID
    min_id=0,               # Minimum message ID
    hash=0                  # Who must have sent the message (peer)
))

#print(result.stringify())
messages = result.messages

found_messages = []
for message in messages:
    if message.message in found_messages:
        print(message.id)
    else:
        found_messages.append(message.message)

print(found_messages)
