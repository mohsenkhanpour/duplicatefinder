from telethon import TelegramClient
from telethon.tl.functions.messages import SearchRequest
from telethon.tl.types import InputMessagesFilterEmpty
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import DeleteMessagesRequest
from dotenv import load_dotenv
from datetime import date
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

offid=3500
found_messages = []
while (offid < 4000):
    result = client(GetHistoryRequest(
        peer=000000000000000,      # On which chat/conversation
        offset_date=0,             # Maximum date
        offset_id=offid,           # ID of the message to use as offset
        add_offset=0,              # Additional offset
        limit=1000,                # How many results
        max_id=0,                  # Maximum message ID
        min_id=0,                  # Minimum message ID
        hash=0                     # Who must have sent the message (peer)
    ))

    #print(result.stringify())
    messages = result.messages


    for message in messages:
        if message.media.caption in found_messages:
         print(message.id)
#        client(DeleteMessagesRequest(
#          channel=###################,
#          id=[message.id]
#      ))
    else:
        found_messages.append(message.media.caption)
    offid=offid+100    
print(found_messages)
