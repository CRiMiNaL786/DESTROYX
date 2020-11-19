import re
import hashlib
import asyncio
import datetime
import logging
from userbot import CMD_HELP
import os
import math
import html
import os.path
import sys
import time
from typing import Tuple, Union
from userbot import bot
from telethon import errors 
from telethon import events
from telethon.tl import types
from telethon.tl.functions.channels import (EditAdminRequest,
                                            EditBannedRequest,
                                            EditPhotoRequest)
from telethon.utils import get_display_name
from telethon.tl.functions.messages import GetPeerDialogsRequest
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator, ChatBannedRights
import userbot.modules.sql_helper.warns_sql as sql
from userbot.events import javes05
async def is_admin(chat_id, user_id):
    req_jo = await bot(GetParticipantRequest(channel=chat_id,user_id=user_id))
    chat_participant = req_jo.participant
    if isinstance(chat_participant, ChannelParticipantCreator) or isinstance(chat_participant, ChannelParticipantAdmin):
        return True
    return False

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)
javes = bot
from userbot.events import rekcah05

@javes05(outgoing=True, pattern="^!warn(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    try:
      chat = await event.get_chat()
      admin = chat.admin_rights
      creator = chat.creator
      warn_reason = event.pattern_match.group(1)
      reply_message = await event.get_reply_message()
    except:
    	return await event.edit("`Sorry canot warn users here`")
    if not admin and not creator:
        return await event.edit("`I have to be admin to warn people.`")
    if await is_admin(event.chat_id, reply_message.from_id):
        return await event.edit("`I'm not going to warn an admin!`")

    limit, soft_warn = sql.get_warn_setting(event.chat_id)
    num_warns, reasons = sql.warn_user(reply_message.from_id, event.chat_id, warn_reason)
    if num_warns >= limit:        
        if soft_warn:
            reply = "{} warnings, <u><a href='tg://user?id={}'>user</a></u> has been muted!".format(limit, reply_message.from_id)
            await event.client.edit_permissions(chat, reply_message.from_id, until_date=None, send_messages=False)
        else:        	
            await event.client.edit_permissions(chat, reply_message.from_id, until_date=None, view_messages=False)
            reply = "{} warnings, <u><a href='tg://user?id={}'>user</a></u> has been banned!".format(limit, reply_message.from_id)
    else:
        reply = "<u><a href='tg://user?id={}'>user</a></u> has {}/{} warnings... watch out!".format(reply_message.from_id, num_warns, limit)
        if warn_reason:
            reply += "\nReason for last warn:\n{}".format(html.escape(warn_reason))
    #
    await event.edit(reply, parse_mode="html")



@javes.on(rekcah05(pattern=f"warn(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
      chat = await event.get_chat()
      admin = chat.admin_rights
      creator = chat.creator
      warn_reason = event.pattern_match.group(1)
      reply_message = await event.get_reply_message()
    except:
    	return await event.reply("`Sorry canot warn users here`")
    if not admin and not creator:
        return await event.reply("`I have to be admin to warn people.`")
    if await is_admin(event.chat_id, reply_message.from_id):
        return await event.reply("`I'm not going to warn an admin!`")

    limit, soft_warn = sql.get_warn_setting(event.chat_id)
    num_warns, reasons = sql.warn_user(reply_message.from_id, event.chat_id, warn_reason)
    if num_warns >= limit:        
        if soft_warn:
            reply = "{} warnings, <u><a href='tg://user?id={}'>user</a></u> has been muted!".format(limit, reply_message.from_id)
            await event.client.edit_permissions(chat, reply_message.from_id, until_date=None, send_messages=False)
        else:        	
            await event.client.edit_permissions(chat, reply_message.from_id, until_date=None, view_messages=False)
            reply = "{} warnings, <u><a href='tg://user?id={}'>user</a></u> has been banned!".format(limit, reply_message.from_id)
    else:
        reply = "<u><a href='tg://user?id={}'>user</a></u> has {}/{} warnings... watch out!".format(reply_message.from_id, num_warns, limit)
        if warn_reason:
            reply += "\nReason for last warn:\n{}".format(html.escape(warn_reason))
    #
    await event.reply(reply, parse_mode="html")






@javes05(outgoing=True, pattern="^!warns(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    result = sql.get_warns(reply_message.from_id, event.chat_id)
    if result and result[0] != 0:
        num_warns, reasons = result
        limit, soft_warn = sql.get_warn_setting(event.chat_id)
        if reasons:
            text = "This user has {}/{} warnings, for the following reasons:".format(num_warns, limit)
            text += "\r\n"
            text += reasons
            await event.edit(text)
        else:
            await event.edit("This user has {} / {} warning, but no reasons for any of them.".format(num_warns, limit))
    else:
        await event.edit("This user hasn't got any warnings!")


@javes.on(rekcah05(pattern=f"warns(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    result = sql.get_warns(reply_message.from_id, event.chat_id)
    if result and result[0] != 0:
        num_warns, reasons = result
        limit, soft_warn = sql.get_warn_setting(event.chat_id)
        if reasons:
            text = "This user has {}/{} warnings, for the following reasons:".format(num_warns, limit)
            text += "\r\n"
            text += reasons
            await event.reply(text)
        else:
            await event.reply("This user has {} / {} warning, but no reasons for any of them.".format(num_warns, limit))
    else:
        await event.reply("This user hasn't got any warnings!")



@javes05(outgoing=True, pattern="^!setwarnmode(?: |$)(.*)")
async def set_warn_strength(event):
    try:
      chat = await event.get_chat()
      admin = chat.admin_rights
      creator = chat.creator
      args = event.pattern_match.group(1)     
    except:
    	return await event.edit("`Error`")

    
    if args:
        if args in ("ban"):
            sql.set_warn_strength(event.chat_id, False)
            await event.edit("Warn mode Set To Ban User.")
            return

        elif args in ("mute"):
            sql.set_warn_strength(event.chat_id, True)
            await event.edit("Warn mode Set To Kick User.")
            return
       
        else:
            await event.edit("`Error usage !setwarnmode kick or mute`")
    else:
        limit, soft_warn = sql.get_warn_setting(event.chat_id)
        if soft_warn:
            await event.edit("I Am **muting** User's For Now.")
        else:
            await event.edit("I Am **Baning** User's For Now.")
    return ""


@javes.on(rekcah05(pattern=f"setwarnmode(?: |$)(.*)", allow_sudo=True))
async def set_warn_strength(event):
    try:
      chat = await event.get_chat()
      admin = chat.admin_rights
      creator = chat.creator
      args = event.pattern_match.group(1)     
    except:
    	return await event.reply("`Error`")

    
    if args:
        if args in ("ban"):
            sql.set_warn_strength(event.chat_id, False)
            await event.reply("Warn mode Set To Ban User.")
            return

        elif args in ("mute"):
            sql.set_warn_strength(event.chat_id, True)
            await event.reply("warn mode Set To Kick User.")
            return
       
        else:
            await event.reply("`Error usage !setwarnmode kick or mute`")
    else:
        limit, soft_warn = sql.get_warn_setting(event.chat_id)
        if soft_warn:
            await event.reply("I Am **muting** User's For Now.")
        else:
            await event.reply("I Am **Baning** User's For Now.")
    return ""


@javes05(outgoing=True, pattern="^!setwarnlimit(?: |$)(.*)")
async def set_warn_limit(event):
    try:
     chat = await event.get_chat()
     admin = chat.admin_rights
     creator = chat.creator
     input_str = event.pattern_match.group(1)
    except:
    	return await event.edit("`Error`")
    
    if input_str:
        if int(input_str) < 3:
            await event.edit("`The minimum warn limit is 3!`")
        else:
            sql.set_warn_limit(event.chat_id, int(input_str))
            await event.edit("`Updated the warn limit to` {}".format(input_str))
            return
        
    else:
        limit, soft_warn = sql.get_warn_setting(event.chat_id)
        await event.edit("`The current warn limit is {}`".format(limit))
    return ""        


@javes.on(rekcah05(pattern=f"setwarnlimit(?: |$)(.*)", allow_sudo=True))
async def set_warn_limit(event):
    try:
     chat = await event.get_chat()
     admin = chat.admin_rights
     creator = chat.creator
     input_str = event.pattern_match.group(1)
    except:
    	return await event.reply("`Error`")
    
    if input_str:
        if int(input_str) < 3:
            await event.reply("`The minimum warn limit is 3!`")
        else:
            sql.set_warn_limit(event.chat_id, int(input_str))
            await event.reply("`Updated the warn limit to` {}".format(input_str))
            return
        
    else:
        limit, soft_warn = sql.get_warn_setting(event.chat_id)
        await event.reply("`The current warn limit is {}`".format(limit))
    return ""        

@javes05(outgoing=True, pattern="^!resetwarns(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    sql.reset_warns(reply_message.from_id, event.chat_id)
    await event.edit("Warnings have been reset!") 

@javes.on(rekcah05(pattern=f"resetwarns(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    sql.reset_warns(reply_message.from_id, event.chat_id)
    await event.reply("Warnings have been reset!") 



CMD_HELP.update({
    "warn":
    "!warn\
\nUsage: Warn a user.\
\n\n!warns \
\nUsage: See a user's warnings.\
\n\n!setwarnmode <ban/mute>\
\nUsage: Set the chat's warn mode. \
\n\n!setwarnlimit <number>\
\nUsage: Set the number of warnings before users are punished. \
\n\n!resetwarns \
\nUsage: Reset all of a user's warnings to 0. \
\n\nAll commands support Sudo ( type !help sudo for more info)\
"
})




