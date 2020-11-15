import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd
from userbot import bot as javes
@javes.on(admin_cmd(pattern="sti ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("```Reply to sticker message```")
       return
    chat = "stickers_to_image_bot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    await event.edit("```Making a sticker to image```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=611085086))
              response2 = conv.wait_event(events.NewMessage(incoming=True,from_users=611085086))
              response3 = conv.wait_event(events.NewMessage(incoming=True,from_users=611085086))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
              response = await response2 
              response = await response3 
          except YouBlockedUserError: 
              await event.reply("```Please unblock (stickers_to_image_bot) ```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```Can you kindly disable your forward privacy settings```")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
