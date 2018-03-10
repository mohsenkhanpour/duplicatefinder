from telethon import TelegramClient
from telethon.tl.functions.messages import SearchRequest
from telethon.tl.types import InputMessagesFilterEmpty
from telethon.tl.functions.messages import GetHistoryRequest
from dotenv import load_dotenv
load_dotenv()
import json
import os

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

client = TelegramClient('DuplicateFinder', api_id, api_hash)
client.start()
print(client.get_me().stringify())

result = client(GetHistoryRequest(
    peer=################,    # On which chat/conversation
    offset_date=None,       # Maximum date
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
    if message.media.caption in found_messages:
        print(message.id)
    else:
        found_messages.append(message.media.caption)
    
print(found_messages)
