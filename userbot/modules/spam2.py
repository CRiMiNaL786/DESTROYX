# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#Added Sudo control By @CrimiNaL786

import asyncio
from asyncio import wait
from telethon import events
from userbot import bot as borg
from userbot import bot
borg = bot
from userbot.events import rekcah05, javes
from userbot.events import javes05
from userbot import BOTLOG_CHATID, JAVES_NAME, JAVES_MSG, CMD_HELP
from userbot.events import register

@javes.on(rekcah05(pattern=f"tspam(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^.tspam(?: |$)(.*)")
async def tmeme(e):
    tspam = str(e.text[7:])
    message = tspam.replace(" ", "")
    for letter in message:
        await e.respond(letter)
    await e.delete()



@javes.on(rekcah05(pattern=f"picspam(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^.picspam(?: |$)(.*)")        
async def tiny_pic_spam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        text = message.split()
        counter = int(text[1])
        link = str(text[2])
        for i in range(1, counter):
            await e.client.send_file(e.chat_id, link)
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP,
                "#PICSPAM \n\n"
                "PicSpam was executed successfully"
                )

@javes.on(rekcah05(pattern=f"delayspam(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^.delayspam(?: |$)(.*)")
async def spammer(e):
    spamDelay = float(e.pattern_match.group(1).split(' ', 2)[0])
    counter = int(e.pattern_match.group(1).split(' ', 2)[1])
    spam_message = str(e.pattern_match.group(1).split(' ', 2)[2])
    await e.delete()
    for i in range(1, counter):
        await e.respond(spam_message)
        await sleep(spamDelay)
    if LOGGER:
        await e.client.send_message(
            LOGGER_GROUP, "#DelaySPAM\n"
            "DelaySpam was executed successfully")
        
@javes.on(rekcah05(pattern=f"mspam(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^.mspam(?: |$)(.*)")            

async def tiny_pic_spam(e):

  sender = await e.get_sender() ; me = await e.client.get_me()

  if not sender.id == me.id and not FULL_SUDO:

       return await e.reply("`Sorry sudo users cant access this command..`")

  try:

       await e.delete()

  except:

    	pass
    
  try:

    counter = int(e.pattern_match.group(1).split(' ', 1)[0])

    reply_message = await e.get_reply_message() 

    if not reply_message or not e.reply_to_msg_id or not reply_message.media or not reply_message.media:

       return await e.edit("```Reply to a pic/sticker/gif/video message```")

    message = reply_message.media

    for i in range(1, counter):

        await e.client.send_file(e.chat_id, message)

  except:      

        return await e.reply(f"**Error**\nUsage `!mspam <count> reply to a sticker/gif/photo/video`")

#Spam removed coz javes spammer is there
