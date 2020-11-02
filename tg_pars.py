# coding-utf-8
from telethon import TelegramClient, events
import os
from pars_conf import account, list_all
api_id = os.environ.get('apiid0')
api_hash = os.environ.get('api_hash0')
SESSION_STRING = os.environ.get('SESSION_STRING0')
client = TelegramClient('my_account', StringSession(SESSION_STRING), api_id, api_hash)
@client.on(events.NewMessage)
async def my_event_handler(event):
        if event.chat.username in list_all:
                chat = await event.get_input_chat()
                msg = await client.get_messages(chat.channel_id, limit=1)
                await client.forward_messages(int(account[2]), msg)
                print("busted")
client.start()
client.run_until_disconnected()
