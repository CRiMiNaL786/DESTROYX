



import asyncio, random, math, os, requests, zipfile, datetime, re, html, bs4, requests, asyncio, textwrap
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.events import javes05, rekcah05, progress, humanbytes, time_formatter
from userbot import CMD_HELP, ALIVE_NAME, PM_MESSAGE, JAVES_NAME, JAVES_MSG, ORI_MSG, bot as javes
from io import BytesIO
from PIL import Image
from datetime import datetime
THUMB_IMAGE_PATH = "./thumb_image.jpg"
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pySmartDL import SmartDL
from telethon.tl.types import DocumentAttributeVideo
from userbot import (TEMP_DOWNLOAD_DIRECTORY, CMD_HELP, bot)
from collections import defaultdict
from telethon.errors.rpcerrorlist import StickersetInvalidError
from telethon.errors import MessageNotModifiedError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import (DocumentAttributeFilename, DocumentAttributeSticker, InputMediaUploadedDocument, InputPeerNotifySettings, InputStickerSetID, InputStickerSetShortName, MessageMediaPhoto)

    


def is_message_image(message):
    if message.media:
        if isinstance(message.media, MessageMediaPhoto):
            return True
        if message.media.document:
            if message.media.document.mime_type.split("/")[0] == "image":
                return True
        return False
    return False
    
async def silently_send_message(conv, text):
    await conv.send_message(text)
    response = await conv.get_response()
    await conv.mark_read(message=response)
    return response


EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+")


def deEmojify(inputString: str) -> str:
    return re.sub(EMOJI_PATTERN, '', inputString)




@javes.on(rekcah05(pattern=f"song2(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!song2(?: |$)(.*)")
async def _(event):
  sender = await event.get_sender() ; me = await event.client.get_me()
  if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
  else:
    	rkp = await event.edit("`processing...`")    
  try:
    reply_message = event.pattern_match.group(1)
    if not reply_message:
       reply_message = await event.get_reply_message() 
       if reply_message:
           if reply_message.media:
       	    return await rkp.edit("`Reply to a text message`")
    if not reply_message:
          return await rkp.edit("`Error\n**Usage** song2 <song> or reply to a message`")
    chat = "@vkmusic_bot"   
    async with event.client.conversation(chat, timeout=7) as conv:
          try:                   
              await conv.send_message(reply_message)
              response = await conv.get_response()
          except YouBlockedUserError: 
              await rkp.edit("`Please unblock @iLyricsBot and try again`")
              return
          try:
           await response.click(1, 1) 
          except:
             return await rkp.edit(f"`Failed to find {reply_message}`")    
          test = await conv.get_response()
          await rkp.delete()
          await event.client.send_file(event.chat_id, test, caption=f"`{reply_message} song`", reply_to=event.message.reply_to_msg_id)          
  except Exception as e:
        error = str(e)
        if not error:
            error = f"No response from {chat}"
        return await rkp.edit(f"**Error**\n\n{error}")
          




@javes.on(rekcah05(pattern=f"info(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!info(?: |$)(.*)")
async def _(event):
  sender = await event.get_sender() ; me = await event.client.get_me()
  if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
  else:
    	rkp = await event.edit("`processing...`")    
  try:
    reply_message = await event.get_reply_message() 
    if not event.reply_to_msg_id:
       return await rkp.edit("`reply to a user  message`")
    chat = "@getidsbot"   
    async with event.client.conversation(chat, timeout=7) as conv:
          try:     
              test = conv.wait_event(events.NewMessage(incoming=True,from_users=186675376))
              await event.client.forward_messages(chat, reply_message)
              response = await test
          except YouBlockedUserError: 
                return await rkp.edit("`Please unblock @getidsbot_bot and try again`")
          return await rkp.edit(f"**Info**\n\n{response.text}")
  except Exception as e:
        error = str(e)
        if not error:
            error = f"No response from {chat}"
        return await rkp.edit(f"**Error**\n\n{error}")
          









@javes.on(rekcah05(pattern=f"lyrics2(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!lyrics2(?: |$)(.*)")
async def _(event):
  sender = await event.get_sender() ; me = await event.client.get_me()
  if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
  else:
    	rkp = await event.edit("`processing...`")    
  try:
    reply_message = event.pattern_match.group(1)
    if not reply_message:
       reply_message = await event.get_reply_message() 
       if reply_message:
           if reply_message.media:
       	    return await rkp.edit("`Reply to a text message`")
    if not reply_message:
          return await rkp.edit("`Error\n**Usage** lyrics2 <song> or reply to a message`")
    chat = "@iLyricsBot"   
    async with event.client.conversation(chat, timeout=7) as conv:
          try:     
              test = conv.wait_event(events.MessageEdited(incoming=True,from_users=232268607))
              await event.client.send_message(chat, reply_message)
              response = await test
          except YouBlockedUserError: 
              await rkp.edit("`Please unblock @iLyricsBot and try again`")
              return          
          return await rkp.edit(response.text)          
  except Exception as e:
        error = str(e)
        if not error:
            error = f"No response from {chat}"
        return await rkp.edit(f"**Error**\n\n{error}")
          


@javes.on(rekcah05(pattern=f"fry(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!fry(?: |$)(.*)")
async def _(event):
  sender = await event.get_sender() ; me = await event.client.get_me()
  if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
  else:
    	rkp = await event.edit("`processing...`")    
  try:    
       reply_message = await event.get_reply_message() 
       if reply_message:
           if not reply_message.media:
       	    return await rkp.edit("`Reply to a photo/sticker`")
       if not reply_message:
          return await rkp.edit("**Error**\n**Usage** fry  reply to a non animated sticker / photo")
       chat = "@image_deepfrybot"   
       async with event.client.conversation(chat, timeout=7) as conv:
          try:     
              test = conv.wait_event(events.NewMessage(incoming=True,from_users=432858024))
              await event.client.forward_messages(chat, reply_message)
              response = await test
          except YouBlockedUserError: 
              await rkp.edit("`Please unblock @image_deepfrybot and try again`")
              return
          await rkp.delete()
          return await event.client.send_file(event.chat_id, response.message.media, reply_to=event.message.reply_to_msg_id)     
  except Exception as e:
        error = str(e)
        if not error:
            error = f"No response from {chat}"
        return await rkp.edit(f"**Error**\n\n{error}")



@javes.on(rekcah05(pattern=f"ss2(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!ss2(?: |$)(.*)")
async def _(event):
  sender = await event.get_sender() ; me = await event.client.get_me()
  if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
  else:
    	rkp = await event.edit("`processing...`")    
  try:    
       reply_message = await event.get_reply_message() 
       if reply_message:
           if not reply_message.media:
       	    return await rkp.edit("`Reply to a photo`")
       if not reply_message:
          return await rkp.edit("**Error**\n**Usage** ss2 reply to a  photo")
       chat = "@BuildStickerBot"   
       async with event.client.conversation(chat, timeout=7) as conv:
          try:     
              test = conv.wait_event(events.NewMessage(incoming=True,from_users=164977173))
              await event.client.forward_messages(chat, reply_message)
              response = await test
          except YouBlockedUserError: 
              return await rkp.edit("`Please unblock @BuildStickerBot and try again`")
          if response.text.startswith("🔸"):   
              return  await rkp.edit("`Failed to convert`")
          await rkp.delete()
          return await event.client.send_file(event.chat_id, response.message.media, reply_to=event.message.reply_to_msg_id)     
  except Exception as e:
        error = str(e)
        if not error:
            error = f"No response from {chat}"
        return await rkp.edit(f"**Error**\n\n{error}")
          



          


@javes.on(rekcah05(pattern=f"ss3(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!ss3(?: |$)(.*)")
async def _(event):
  sender = await event.get_sender() ; me = await event.client.get_me()
  if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
  else:
    	rkp = await event.edit("`processing...`")    
  try:    
       reply_message = await event.get_reply_message() 
       if reply_message:
           if not reply_message.media:
       	    return await rkp.edit("`Reply to a photo`")
       if not reply_message:
          return await rkp.edit("**Error**\n**Usage** ss2 reply to a  photo")
       chat = "@Stickerdownloadbot"   
       async with event.client.conversation(chat, timeout=7) as conv:
          try:     
              test = conv.wait_event(events.NewMessage(incoming=True,from_users=220255550))
              await event.client.forward_messages(chat, reply_message)
              response = await test
          except YouBlockedUserError: 
              return await rkp.edit("`Please unblock @Stickerdownloadbot and try again`")
          if response.text.startswith("I"):   
              return  await rkp.edit("`Failed to convert`")
          await rkp.delete()
          return await event.client.send_file(event.chat_id, response.message.media, reply_to=event.message.reply_to_msg_id)     
  except Exception as e:
        error = str(e)
        if not error:
            error = f"No response from {chat}"
        return await rkp.edit(f"**Error**\n\n{error}")
          



@javes.on(rekcah05(pattern=f"ss4(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!ss4(?: |$)(.*)")
async def _(event):
  sender = await event.get_sender() ; me = await event.client.get_me()
  if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
  else:
    	rkp = await event.edit("`processing...`")    
  try:    
       reply_message = await event.get_reply_message() 
       if reply_message:
           if not reply_message.media:
       	    return await rkp.edit("`Reply to a photo`")
       if not reply_message:
          return await rkp.edit("**Error**\n**Usage** ss2 reply to a  photo")
       chat = "@stickerator_bot"   
       async with event.client.conversation(chat, timeout=7) as conv:
          try:     
              test = conv.wait_event(events.NewMessage(incoming=True,from_users=384614990))
              await event.client.forward_messages(chat, reply_message)
              response = await test
          except YouBlockedUserError: 
              return await rkp.edit("`Please unblock @stickerator_bot and try again`")
          if response.text.startswith("274"):   
              return  await rkp.edit("`Failed to convert`")
          await rkp.delete()
          return await event.client.send_file(event.chat_id, response.message.media, reply_to=event.message.reply_to_msg_id)     
  except Exception as e:
        error = str(e)
        if not error:
            error = f"No response from {chat}"
        return await rkp.edit(f"**Error**\n\n{error}")
          


          

@javes.on(rekcah05(pattern=f"mask(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!mask(?: |$)(.*)")
async def _(event):
  sender = await event.get_sender() ; me = await event.client.get_me()
  if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
  else:
    	rkp = await event.edit("`processing...`")    
  try:    
       reply_message = await event.get_reply_message() 
       if reply_message:
           if not reply_message.media:
       	    return await rkp.edit("`Reply to a photo/sticker`")
       if not reply_message:
          return await rkp.edit("**Error**\n**Usage** fry  reply to a non animated sticker / photo")
       chat = "@hazmat_suit_bot"   
       async with event.client.conversation(chat, timeout=7) as conv:
          try:     
              test = conv.wait_event(events.NewMessage(incoming=True,from_users=905164246))
              await event.client.forward_messages(chat, reply_message)
              response = await test
          except YouBlockedUserError: 
              await rkp.edit("`Please unblock @hazmat_suit_bot and try again`")
              return
          await rkp.delete()
          return await event.client.send_file(event.chat_id, response.message.media, reply_to=event.message.reply_to_msg_id)     
  except Exception as e:
        error = str(e)
        if not error:
            error = f"No response from {chat}"
        return await rkp.edit(f"**Error**\n\n{error}")
          

@javes.on(rekcah05(pattern=f"ushort(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!ushort(?: |$)(.*)")
async def _(event):
  sender = await event.get_sender() ; me = await event.client.get_me()
  if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
  else:
    	rkp = await event.edit("`processing...`")    
  try:
    reply_message = event.pattern_match.group(1)
    if not reply_message:
       reply_message = await event.get_reply_message() 
       if reply_message:
           if reply_message.media:
       	    return await rkp.edit("`Reply to a link`")
    if not reply_message:
          return await rkp.edit("`Error\n**Usage** ushort <link> or reply to a link`")
    chat = "@LinkGeneratorBot"   
    async with event.client.conversation(chat, timeout=7) as conv:
          try:     
              test = conv.wait_event(events.NewMessage(incoming=True,from_users=355705793))
              await event.client.send_message(chat, reply_message)
              response = await test
          except YouBlockedUserError: 
              await rkp.edit("`Please unblock @LinkGeneratorBot and try again`")
              return          
          return await rkp.edit(response.text)          
  except Exception as e:
        error = str(e)
        if not error:
            error = f"No response from {chat}"
        return await rkp.edit(f"**Error**\n\n{error}")
          

        
          

@javes.on(rekcah05(pattern=f"ss(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!ss(?: |$)(.*)")
async def _(event):
  sender = await event.get_sender() ; me = await event.client.get_me()
  if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
  else:
    	rkp = await event.edit("`processing...`")    
  try:    
       reply_message = await event.get_reply_message() 
       if reply_message:
           if reply_message.media:
       	    return await rkp.edit("`Reply to a text`")
       if not reply_message:
          return await rkp.edit("**Error**\n**Usage** ss reply to a text")
       chat = "@QuotLyBot"   
       async with event.client.conversation(chat, timeout=7) as conv:
          try:     
              test = conv.wait_event(events.NewMessage(incoming=True,from_users=1031952739))
              await event.client.forward_messages(chat, reply_message)
              response = await test
          except YouBlockedUserError: 
              await rkp.edit("`Please unblock @QuotLyBot and try again`")
              return
          await rkp.delete()
          return await event.client.send_file(event.chat_id, response.message.media, reply_to=event.message.reply_to_msg_id)     
  except Exception as e:
        error = str(e)
        if not error:
            error = f"No response from {chat}"
        return await rkp.edit(f"**Error**\n\n{error}")
          



CMD_HELP.update({
    "bot":
"\n\n!info <reply to a message>\
\n**Usage**: get message, user information  \
\n\n!lyrics2 <song name>\
\n**Usage**: for get lyrics   \
\n\n!fry <reply to a non animated sticker/photo>\
\n**Usage**: fry given img/sticker  \
\n\n!ss <reply to a message>\
\n**Usage**: change given text to cool img  \
\n\n!ss2 <reply to a photo>\
\n**Usage**: chang img to sticker  \
\n\n!ss3 <reply to a photo/sticker>\
\n**Usage**: convert the img/sticker  \
\n\n!ss4 <reply to a photo/sticker>\
\n**Usage**: convert the img/sticker  \
\n\n!mask <reply to a photo/sticker>\
\n**Usage**: save your sticker/photo from covid-19  \
\n\n!ushort <link>\
\n**Usage**: shorted the url  \
\n\n **All Commands support sudo** \
"
})

