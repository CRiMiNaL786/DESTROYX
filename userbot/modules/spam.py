

import asyncio, os
from asyncio import wait, sleep
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.events import javes05, rekcah05
from userbot import client as javes
FULL_SUDO = os.environ.get("FULL_SUDO", None)


@javes.on(rekcah05(pattern=f"(?:scam|ssc)\s(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern=r"^\!(?:scam|ssc)\s(.*)")
async def scam(e):
    if not e.is_private:
              chat = await e.get_chat() ; admin = chat.admin_rights ; creator = chat.creator
              if not admin and not creator and chat.id == -1001288555028:
                     	return
    try:
       await e.delete()
    except:
    	pass
    options = ('typing', 'game' , 'voice', 'round', 'video' , 'photo', 'document')
    input_str = e.pattern_match.group(1)
    args = input_str.split()  
    if len(args) == 2:  
        scam_action = str(args[1]).lower()
        if not scam_action in options:
           return await e.reply(f"Failed \n\n •**Error:** Invalid Action\n\n You can use one of this \n{options}")
        try:
            scam_time = int(args[0])
        except:      
             return await e.reply("Failed \n\n •**Error:** Invalid Time.....")
    else:
        return await e.reply(f"**Error**\nusage `!scam <time in seconds> <action>`")
    try:
        if (scam_time > 0):            
            async with e.client.action(e.chat_id, scam_action):
                await sleep(scam_time)
    except Exception as e:      
        return await e.reply(f"**Error**\nusage `!scam <time in seconds> <action>`")


@javes.on(rekcah05(pattern=f"(?:rspam|rsp)\s(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern=r"^\!(?:rspam|rsp)\s(.*)")
async def repeat(e):
  sender = await e.get_sender() ; me = await e.client.get_me()
  if not sender.id == me.id and not FULL_SUDO:
       return await e.reply("`Sorry normal sudo users cant access this command..`")
  try:
       await e.delete()
  except:
    	pass
  try:
    cnt, txt = e.pattern_match.group(1).split(' ', 1)
    replyCount = int(cnt)
    toBeRepeated = txt
    replyText = toBeRepeated + "\n"
    for i in range(0, replyCount - 1):
        replyText += toBeRepeated + "\n"
    await e.reply(replyText)
  except:      
        return await e.reply(f"**Error**\nusage `! repeatspam <count> <text>`")


@javes.on(rekcah05(pattern=f"(?:cspam|csp)\s(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern=r"^\!(?:cspam|csp)\s(.*)")
async def tmeme(e):
  sender = await e.get_sender() ; me = await e.client.get_me()
  if not sender.id == me.id and not FULL_SUDO:
       return await e.reply("`Sorry normal sudo users cant access this command..`")
  try:
       await e.delete()
  except:
    	pass
  try:
    cspam = str(e.pattern_match.group(1))
    message = cspam.replace(" ", "")
    for letter in message:
        await e.respond(letter)
  except:      
        return await e.reply(f"**Error**\nusage `!cspam <text>`")

@javes.on(rekcah05(pattern=f"(?:wspam|wsp)\s(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern=r"^\!(?:wspam|wsp)\s(.*)")
async def tmeme(e):
  sender = await e.get_sender() ; me = await e.client.get_me()
  if not sender.id == me.id and not FULL_SUDO:
       return await e.reply("`Sorry normal sudo users cant access this command..`")
  try:
       await e.delete()
  except:
    	pass
  try:
    wspam = str(e.pattern_match.group(1))
    message = wspam.split()
    for word in message:
        await e.respond(word)
  except:      
        return await e.reply(f"**Error**\nusage `!wspam  <text> <text> <text>`")

@javes.on(rekcah05(pattern=f"(?:spam|sp)\s(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern=r"^\!(?:spam|sp)\s(.*)")
async def spammer(e):
  sender = await e.get_sender() ; me = await e.client.get_me()
  if not sender.id == me.id and not FULL_SUDO:
       return await e.reply("`Sorry normal sudo users cant access this command..`")
  try:
       await e.delete()
  except:
    	pass
  try:
    counter = int(e.pattern_match.group(1).split(' ', 1)[0])
    spam_message = str(e.pattern_match.group(1).split(' ', 1)[1])
    await asyncio.wait([e.respond(spam_message) for i in range(counter)])
  except:      
        return await e.reply(f"**Error**\nusage `!spam <time in seconds> <text>`")

@javes.on(rekcah05(pattern=f"(?:mspam|msp)\s(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern=r"^\!(?:mspam|msp)\s(.*)")
async def tiny_pic_spam(e):
  sender = await e.get_sender() ; me = await e.client.get_me()
  if not sender.id == me.id and not FULL_SUDO:
       return await e.reply("`Sorry normal sudo users cant access this command..`")
  try:
       await e.delete()
  except:
    	pass
  try:
    counter = int(e.pattern_match.group(1).split(' ', 1)[0])
    reply_message = await e.get_reply_message() 
    if not reply_message or not e.reply_to_msg_id or not reply_message.media or not reply_message.media:
       return await e.edit("```Reply to a media message```")
    message = reply_message.media
    for i in range(1, counter):
        await e.client.send_file(e.chat_id, message)
  except:      
        return await e.reply(f"**Error**\nusage `!dspam <count> reply to a media/photo/video`")

@javes.on(rekcah05(pattern=f"(?:dmspam|dmsp)\s(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern=r"^\!(?:dmspam|dmsp)\s(.*)")
async def tiny_pic_spam(e):
  sender = await e.get_sender() ; me = await e.client.get_me()
  if not sender.id == me.id and not FULL_SUDO:
       return await e.reply("`Sorry normal sudo users cant access this command..`")
  try:
       await e.delete()
  except:
    	pass
  try:
    spamDelay = float(e.pattern_match.group(1).split(' ', 2)[0])
    counter = int(e.pattern_match.group(1).split(' ', 2)[1])
    reply_message = await e.get_reply_message() 
    if not reply_message or not e.reply_to_msg_id or not reply_message.media or not reply_message.media:
       return await e.edit("```Reply to a media message```")
    message = reply_message.media
    for i in range(1, counter):
        await e.client.send_file(e.chat_id, message)
        await sleep(spamDelay)
  except:      
        return await e.reply(f"**Error**\nusage `!ddspam <time in seconds> <count> reply to a media/photo/video`")

@javes.on(rekcah05(pattern=f"(?:delayspam|dsp)\s(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern=r"^\!(?:delayspam|dsp)\s(.*)")
async def spammer(e):
  sender = await e.get_sender() ; me = await e.client.get_me()
  if not sender.id == me.id and not FULL_SUDO:
       return await e.reply("`Sorry normal sudo users cant access this command..`")
  try:
       await e.delete()
  except:
    	pass
  try:
    spamDelay = float(e.pattern_match.group(1).split(' ', 2)[0])
    counter = int(e.pattern_match.group(1).split(' ', 2)[1])
    spam_message = str(e.pattern_match.group(1).split(' ', 2)[2])
    for i in range(1, counter):
        await e.respond(spam_message)
        await sleep(spamDelay)
  except:      
        return await e.reply(f"**Error**\nusage `!dealyspam <time in seconds> <count> <text>`")


CMD_HELP.update({
    "spam":
    "⚠️ Spam at your own risk !!\
\n\n`!spam/!sp` <count> <text>\
\n**Usage:**  Floods text in the chat !!\
\n\n`!scam/!sc` <time in seconds> <action>\
\n**Usage:**  Scam by fake actions like typing, sending photo......!!\
\n\n`!cspam/!csp` <text>\
\n**Usage:**  Spam the text letter by letter.\
\n\n`!rspam/!rsp` <count> <text>\
\n**Usage:**  Repeats the text for a number of times.\
\n\n`!wspam/!wsp` <text>\
\n**Usage:**  Spam the text word by word.\
\n\n`!mspam/!msp` <count> <reply to a media message>\
\n**Usage:**  As if text spam was not enough !!\
\n\n`!delayspam/!dsp` <delay> <count> <text>\
\n**Usage:**  spam with custom delay.\
\n\n`!dmspam/!dmsp` <delay> <count> <reply to a media message>\
\n**Usage:**  mspam with custom delay.\
\n\n**Spam_protect**\
\n**Usage:**  Protect your groups from scammers.\
\nFor on `!set var SPAM_PROTECT True` , for off `!del var SPAM_PROTECT`\
\n You need to set up api key for that\
\n More information click [here](https://t.me/javes05/157)\
\n\n**All commands support sudo , type !help sudo for more info**\
"
})
