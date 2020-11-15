import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd
from userbot import bot as javes
@javes.on(admin_cmd(pattern="ssti?(.*)"))
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
    chat = "Stickerdownloadbot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    await event.edit("```Making a sticker to image```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=220255550))
              respond = conv.wait_event(events.NewMessage(incoming=True,from_users=220255550))
              responds = conv.wait_event(events.NewMessage(incoming=True,from_users=220255550))

              await event.client.forward_messages(chat, reply_message)
              response = await response 
              responds = await responds 
              respond = await respond 
          except YouBlockedUserError: 
              await event.reply("```Please unblock (@Stickerdownloadbot) ```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```Can you kindly disable your forward privacy settings```")
          else: 

             await event.client.send_message(event.chat_id, response.message)
             await event.client.send_message(event.chat_id, respond.message)
             await event.client.send_message(event.chat_id, responds.message)

@javes.on(admin_cmd(pattern="sati ?(.*)"))
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
    chat = "Stickerdownloadbot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    await event.edit("```Making a sticker to image```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=220255550))
              respond = conv.wait_event(events.NewMessage(incoming=True,from_users=220255550))
              responds = conv.wait_event(events.NewMessage(incoming=True,from_users=220255550))
              respo = conv.wait_event(events.NewMessage(incoming=True,from_users=220255550))
              res = conv.wait_event(events.NewMessage(incoming=True,from_users=220255550))
              resp = conv.wait_event(events.NewMessage(incoming=True,from_users=220255550))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
              respond = await respond 
              responds = await responds 
              respo = await respo 
              res = await res 
              resp= await resp 
          except YouBlockedUserError: 
              await event.reply("```Please unblock (@Stickerdownloadbot) ```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```Can you kindly disable your forward privacy settings```")
          else: 

             await event.client.send_message(event.chat_id, response.message)
             await event.client.send_message(event.chat_id, respond.message)
             await event.client.send_message(event.chat_id, responds.message)
             await event.client.send_message(event.chat_id, respo.message)
             await event.client.send_message(event.chat_id, res.message)
             await event.client.send_message(event.chat_id, resp.message)
@javes.on(admin_cmd(pattern="iti ?(.*)"))
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
    chat = "Stickerdownloadbot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    await event.edit("```Making a sticker to image```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=220255550))
              respond = conv.wait_event(events.NewMessage(incoming=True,from_users=220255550))
              
              await event.client.forward_messages(chat, reply_message)
              response = await response 
              respond = await respond 
             
          except YouBlockedUserError: 
              await event.reply("```Please unblock (@Stickerdownloadbot) ```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```Can you kindly disable your forward privacy settings```")
          else: 

             await event.client.send_message(event.chat_id, response.message)
             await event.client.send_message(event.chat_id, respond.message)
@javes.on(admin_cmd(pattern="sa2ti ?(.*)"))
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
    chat = "Stickerdownloadbot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    await event.edit("```Making a sticker to image```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=220255550))
              respond = conv.wait_event(events.NewMessage(incoming=True,from_users=220255550))
              responds = conv.wait_event(events.NewMessage(incoming=True,from_users=220255550))
              respo = conv.wait_event(events.NewMessage(incoming=True,from_users=220255550))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
              respond = await respond 
              responds = await responds 
              respo = await respo 
          except YouBlockedUserError: 
              await event.reply("```Please unblock (@Stickerdownloadbot) ```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```Can you kindly disable your forward privacy settings```")
          else: 
             await event.client.send_message(event.chat_id, response.message)
             await event.client.send_message(event.chat_id, respond.message)
             await event.client.send_message(event.chat_id, responds.message)
             await event.client.send_message(event.chat_id, respo.message)





