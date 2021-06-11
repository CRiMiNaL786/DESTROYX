

import asyncio
import re
import userbot.modules.sql_helper.blacklist_sql as sql
from telethon import events, utils
from telethon.tl import types, functions
from userbot.events import javes05, rekcah05
from userbot import bot as javes, CMD_HELP





@javes.on(events.NewMessage(incoming=True))
async def on_new_message(event):
    name = event.raw_text
    snips = sql.get_chat_blacklist(event.chat_id)
    for snip in snips:
        pattern = r"( |^|[^\w])" + re.escape(snip) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            try:
                await event.delete()
            except Exception as e:
                await event.reply("I do not have DELETE permission in this chat")
                sql.rm_from_blacklist(event.chat_id, snip.lower())
            break

@javes05(outgoing=True, pattern="^!saveblacklist ((.|\n)*)")
async def on_add_black_list(event):
    text = event.pattern_match.group(1)
    to_blacklist = list(set(trigger.strip() for trigger in text.split("\n") if trigger.strip()))
    for trigger in to_blacklist:
        sql.add_to_blacklist(event.chat_id, trigger.lower())
    await event.edit("Added {} triggers to the blacklist in the current chat".format(len(to_blacklist)))



@javes.on(rekcah05(pattern=f"saveblacklist ((.|\n)*)", allow_sudo=True))
async def on_add_black_list(event):
    text = event.pattern_match.group(1)
    to_blacklist = list(set(trigger.strip() for trigger in text.split("\n") if trigger.strip()))
    for trigger in to_blacklist:
        sql.add_to_blacklist(event.chat_id, trigger.lower())
    await event.reply("Added {} triggers to the blacklist in the current chat".format(len(to_blacklist)))

@javes05(outgoing=True, pattern="^!checkblacklist(?: |$)(.*)")
async def on_view_blacklist(listbl):
    all_blacklisted = sql.get_chat_blacklist(listbl.chat_id)
    OUT_STR = "Blacklists in the Current Chat:\n"
    if len(all_blacklisted) > 0:
        for trigger in all_blacklisted:
            OUT_STR += f"`{trigger}`\n"
    else:
        OUT_STR = "`There are no blacklist in current chat.`"
    if len(OUT_STR) > 4096:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "blacklist.text"
            await listbl.client.send_file(
                listbl.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="BlackLists in the Current Chat",
                reply_to=listbl
            )
            await listbl.delete()
    else:
        await listbl.edit(OUT_STR)
        
        
        
        
        
@javes.on(rekcah05(pattern=f"checkblacklist$", allow_sudo=True))
async def on_view_blacklist(listbl):
    all_blacklisted = sql.get_chat_blacklist(listbl.chat_id)
    OUT_STR = "Blacklists in the Current Chat:\n"
    if len(all_blacklisted) > 0:
        for trigger in all_blacklisted:
            OUT_STR += f"`{trigger}`\n"
    else:
        OUT_STR = "`There are no blacklist in current chat.`"
    if len(OUT_STR) > 4096:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "blacklist.text"
            await listbl.client.send_file(
                listbl.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="BlackLists in the Current Chat",
                reply_to=listbl
            )
            await listbl.delete()
    else:
        await listbl.reply(OUT_STR)
           
        
        
        
@javes05(outgoing=True, pattern="^!clearblacklist ((.|\n)*)")       
async def on_delete_blacklist(event):
    text = event.pattern_match.group(1)
    to_unblacklist = list(set(trigger.strip() for trigger in text.split("\n") if trigger.strip()))
    successful = 0
    for trigger in to_unblacklist:
        if sql.rm_from_blacklist(event.chat_id, trigger.lower()):
            successful += 1
    await event.edit(f"Removed {successful} / {len(to_unblacklist)} from the blacklist")
        

@javes.on(rekcah05(pattern=f"clearblacklist ((.|\n)*)", allow_sudo=True))
async def on_delete_blacklist(event):
    text = event.pattern_match.group(1)
    to_unblacklist = list(set(trigger.strip() for trigger in text.split("\n") if trigger.strip()))
    successful = 0
    for trigger in to_unblacklist:
        if sql.rm_from_blacklist(event.chat_id, trigger.lower()):
            successful += 1
    await event.edit(f"Removed {successful} / {len(to_unblacklist)} from the blacklist")




CMD_HELP.update({
    "blacklist":
    "!checkblacklist\
    \nUsage: Lists all active userbot blacklists in a chat.\
    \n\n!saveblacklist <keyword> <reply text> or reply to a message with !saveblacklist <keyword>\
    \nUsage: Delete then non admins blacklisted wards.\
    \n\n!clearblacklist <ward>\
    \nUsage: Stops the specified blacklist ward."
})




