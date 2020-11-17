import asyncio
import os
from datetime import datetime
from pathlib import Path
from telethon.tl.types import InputMessagesFilterDocument
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from userbot import bot
from userbot.utils import *
DELETE_TIMEOUT = 3
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Mr.X"
@bot.on(admin_cmd(pattern=r"snd (?P<shortname>\w+)", outgoing=True))
async def send(event):
    if event.fwd_from:
        return

    message_id = event.message.id
    input_str = event.pattern_match.group(1)
    the_plugin_file = "{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        start = datetime.now()
        pro = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            force_document=True,
            allow_cache=False,
            reply_to=message_id,
        )
        end = datetime.now()
        time_taken_in_ms = (end - start).seconds
        await pro.edit(
            f"__**➥ Plugin Name:- {input_str} .**__\n__**➥ Uploaded in {time_taken_in_ms} seconds.**__\n__**➥ Uploaded by :-**__ {DEFAULTUSER}"
          )
        await asyncio.sleep(DELETE_TIMEOUT)
        await event.delete()
    else:
        await event.edit("`ERROR S0S : File not found`")
