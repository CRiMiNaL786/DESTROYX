from userbot.events import javes05
from userbot import bot, BOTLOG_CHATID
import asyncio
from telethon import events
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import (PeerChat, PeerChannel,ChannelParticipantsAdmins, ChatAdminRights,ChatBannedRights, MessageEntityMentionName,MessageMediaPhoto, ChannelParticipantsBots)
from telethon.tl.types import Channel
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from userbot.events import rekcah05
client = javes = bot 
from telethon.tl.functions.messages import GetCommonChatsRequest
from userbot import JAVES_NAME, JAVES_MSG
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)
from datetime import timedelta
import re, datetime
from telethon.tl import types
from typing import Dict, List, Tuple, Union
from telethon.tl.functions.channels import (EditAdminRequest,EditBannedRequest,EditPhotoRequest)
from telethon.tl.types import UserStatusEmpty, UserStatusLastMonth, UserStatusLastWeek, UserStatusOffline, UserStatusOnline, UserStatusRecently, ChannelParticipantsKicked, ChatBannedRights
from telethon.errors import FloodWaitError
from telethon.tl import functions, types
from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest
from telethon.errors import (BadRequestError, ChatAdminRequiredError,ImageProcessFailedError, PhotoCropSizeSmallError,UserAdminInvalidError)
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from userbot import CMD_HELP


async def get_user_from_event(event):  
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit(f"`{JAVES_NNAME}`: ** Pass the user's username, id or reply!**")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("Failed \n **Error**\n", str(err))           
    return user_obj, extra

async def ban_user(chat_id, i, rights):
    try:
        await javes(functions.channels.EditBannedRequest(chat_id, i, rights))
        return True, None
    except Exception as exc:
        return False, str(exc)


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj
    
    
async def amount_to_secs(amount: tuple) -> int:    
    num, unit = amount
    num = int(num)
    if not unit:
        unit = 's'
    if unit == 's':
        return 60
    elif unit == 'm':
        return num * 60
    elif unit == 'h':
        return num * 60 * 60
    elif unit == 'd':
        return num * 60 * 60 * 24
    elif unit == 'w':
        return num * 60 * 60 * 24 * 7
    elif unit == 'y':
        return num * 60 * 60 * 24 * 7 * 52
    else:
        return 60
        
async def string_to_secs(string: str) -> int:  
    values = regexp.findall(string)
    totalValues = len(values)
    if totalValues == 1:
        return await amount_to_secs(values[0])
    else:
        total = 0
        for amount in values:
            total += await amount_to_secs(amount)
        return total
regexp = re.compile(r"(\d+)(w|d|h|m|s)?")
adminregexp = re.compile(r"\d+(?:w|d|h|m|s)?")


KWARGS = re.compile(
    r'(?<!\S)'  
    r'(?:(?P<q>\'|\")?)(?P<key>(?(q).+?|(?!\d)\w+?))(?(q)(?P=q))'
    r'(?::(?!//)|=)\s?'
    r'(?P<val>\[.+?\]|(?P<q1>\'|\").+?(?P=q1)|\S+)')
ARGS = re.compile(r'(?:(?P<q>\'|\"))(.+?)(?:(?P=q))')
BOOL_MAP = {
    'false': False,
    'true': True,
}
Value = Union[int, str, float, list]
KeywordArgument = Union[Value, range, List[Value]]
async def _parse_arg(val: str) -> Union[int, str, float]:
    val = val.strip()
    if re.match(r'^-?\d+$', val):
        return int(val)
    try:
        return float(val)
    except ValueError:
        pass
    if isinstance(val, str):
        if re.search(r'^\[.*\]$', val):
            val = re.sub(r'[\[\]]', '', val).split(',')
            val = [await _parse_arg(v.strip()) for v in val]
        else:
            val = BOOL_MAP.get(val.lower(), val)
    if isinstance(val, str):
        val = re.sub(r'(?<!\\), ?$', '', val)
    return val
async def parse_arguments(
        arguments: str) -> Tuple[List[Value], Dict[str, KeywordArgument]]:
    keyword_args = {}
    args = []
    for match in KWARGS.finditer(arguments):
        key = match.group('key')
        val = await _parse_arg(re.sub(r'[\'\"]', '', match.group('val')))
        keyword_args.update({key: val})
    arguments = KWARGS.sub('', arguments)
    for val in ARGS.finditer(arguments):
        args.append(await _parse_arg(val.group(2)))
    arguments = ARGS.sub('', arguments)
    for val in re.findall(r'([^\r\n\t\f\v ,]+|\[.*\])', arguments):
        parsed = await _parse_arg(val)
        if parsed:
            args.append(parsed)
    return args, keyword_args




@javes05(outgoing=True, pattern="^\!promote(?: |$)(.*)", groups_only=True)
async def promote(event):
    chat = await event.get_chat()  
    if event.is_private:
       await event.reply("`You can't promote users in private chats.`")
       return
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.edit(f"`{JAVES_NNAME}:` **I haven't got the admin rights to do this.**")
        return
    new_rights = ChatAdminRights(add_admins=False,
                                 invite_users=True,
                                 change_info=False,
                                 ban_users=True,
                                 delete_messages=True,
                                 pin_messages=True)
    await event.edit(f"`{JAVES_NNAME}:` **Promoting User**")
    user, rank = await get_user_from_event(event)
    if not rank:
        rank = "admin"
    if user:
        pass
    else:
        return    
    try:
        await event.client(
            EditAdminRequest(event.chat_id, user.id, new_rights, rank))
        await event.edit(f"`{JAVES_NNAME}:` **Promoted user [{user.first_name}](tg://user?id={user.id}) to admin  Sucessfully in {event.chat.title}**")
    except BadRequestError:
        return await event.edit(f"`{JAVES_NNAME}:`**I don't have sufficient permissions!**")
   
    


@javes.on(rekcah05(pattern=f"promote(?: |$)(.*)", allow_sudo=True))
async def promote(event):
    chat = await event.get_chat()  
    if event.is_private:
       await event.reply("`You can't promote users in private chats.`")
       return
    admin = chat.admin_rights
    creator = chat.creator   
    if not admin and not creator:
        await event.reply(f"`{JAVES_NNAME}:` **I haven't got the admin rights to do this.**")
        return
    new_rights = ChatAdminRights(add_admins=False,
                                 invite_users=True,
                                 change_info=False,
                                 ban_users=True,
                                 delete_messages=True,
                                 pin_messages=True)
    rkp = await event.reply(f"`{JAVES_NNAME}:` **Promoting User**")
    user, rank = await get_user_from_event(event)
    if not rank:
        rank = "admin"
    if user:
        pass
    else:
        return    
    try:
        await event.client(
            EditAdminRequest(event.chat_id, user.id, new_rights, rank))
        await rkp.edit(f"`{JAVES_NNAME}:` **Promoted user [{user.first_name}](tg://user?id={user.id}) to admin  Sucessfully in {event.chat.title}**")
    except BadRequestError:
        return await rkp.edit(f"`{JAVES_NNAME}:`**I don't have sufficient permissions!**")
   








@javes05(outgoing=True, pattern="^\!demote(?: |$)(.*)", groups_only=True)
async def demote(event):
    chat = await event.get_chat()
    if event.is_private:
       await event.reply("`You can't promote users in private chats.`")
       return
    admin = chat.admin_rights
    creator = chat.creator
    await event.edit(f"`{JAVES_NNAME}:`** Demoting user......**")
    rank = "admin" 
    user = await get_user_from_event(event)
    user = user[0]
    if user:
        pass
    else:
        return
    newrights = ChatAdminRights(add_admins=None,
                                invite_users=None,
                                change_info=None,
                                ban_users=None,
                                delete_messages=None,
                                pin_messages=None)
    try:
        await event.client(
            EditAdminRequest(event.chat_id, user.id, newrights, rank))    
    except BadRequestError:
        return await rkp.edit(f"`{JAVES_NNAME}:`**I don't have sufficient permissions!**")
        return
    await event.edit(f"`{JAVES_NNAME}:` **Demoted user [{user.first_name}](tg://user?id={user.id}) to admin  Sucessfully in {event.chat.title}**")
    


@javes.on(rekcah05(pattern=f"demote(?: |$)(.*)", allow_sudo=True))
async def demote(event):
    chat = await event.get_chat()
    if event.is_private:
       await event.reply("`You can't promote users in private chats.`")
       return
    admin = chat.admin_rights
    creator = chat.creator
    rkp = await event.reply(f"`{JAVES_NNAME}:`** Demoting user......**")
    rank = "admin" 
    user = await get_user_from_event(event)
    user = user[0]
    if user:
        pass
    else:
        return
    newrights = ChatAdminRights(add_admins=None,
                                invite_users=None,
                                change_info=None,
                                ban_users=None,
                                delete_messages=None,
                                pin_messages=None)
    try:
        await event.client(
            EditAdminRequest(event.chat_id, user.id, newrights, rank))    
    except BadRequestError:
        return await rkp.edit(f"`{JAVES_NNAME}:`**I don't have sufficient permissions!**")
        return
    await rkp.edit(f"`{JAVES_NNAME}:` **Demoted user [{user.first_name}](tg://user?id={user.id}) to admin  Sucessfully in {event.chat.title}**")
           





@javes05(outgoing=True, pattern="^!ban(?: |$|\n)([\s\S]*)")
async def ban(event):    
    if event.is_private:
        await event.reply("`You can't ban users in private chats.`")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.edit(f"`{JAVES_NNAME}:` **I haven't got the admin rights to do this.**")
        return
    match = event.pattern_match.group(1)  
    args, kwargs = await parse_arguments(match)
    reason = kwargs.get('r', None)
    skipped = []
    banned = []
    error = []
    if not args and event.reply_to_msg_id:
        reply = await event.get_reply_message()
        args.append(reply.sender_id)
    if not args:
        await event.edit(f"`{JAVES_NNAME}:` **I don't know who you're talking about, you're going to need to specify a user...!**")
        return        
    entity = await event.get_chat()
    for user in args:
        if isinstance(user, list):
            continue
        try:
            await client.edit_permissions(entity=entity,
                                          user=user,
                                          view_messages=False)
            banned.append(user)
        except Exception as e:      
            skipped.append(user)
            error.append(str(e))
    if banned:
        text = f"`{JAVES_NNAME}: `**Successfully banned**\n"
        text += ', '.join((f'`{x}`' for x in banned))
        if reason:
            text += f"\n\n**Reason:** `{reason}`"            
        await event.edit(text)
    if skipped:
        text2 = f"`{JAVES_NNAME}: `**Failed to ban **"
        text2 += ', '.join((f'{x}' for x in skipped))
        text = "\n **Error(s)**\n•"
        text += '•'.join((f'{x}\n' for x in error))
        await event.reply(text2)
        await event.reply(text)


@javes.on(rekcah05(pattern=f"ban(?: |$|\n)([\s\S]*)", allow_sudo=True))
async def ban(event):    
    if event.is_private:
        await event.reply("`You can't ban users in private chats.`")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.reply(f"`{JAVES_NNAME}:` **I haven't got the admin rights to do this.**")
        return
    match = event.pattern_match.group(1)  
    args, kwargs = await parse_arguments(match)
    reason = kwargs.get('r', None)
    skipped = []
    banned = []
    error = []
    if not args and event.reply_to_msg_id:
        reply = await event.get_reply_message()
        args.append(reply.sender_id)
    if not args:
        await event.reply(f"`{JAVES_NNAME}:` **I don't know who you're talking about, you're going to need to specify a user...!**")
        return        
    entity = await event.get_chat()
    for user in args:
        if isinstance(user, list):
            continue
        try:
            await client.edit_permissions(entity=entity,
                                          user=user,
                                          view_messages=False)
            banned.append(user)
        except Exception as e:      
            skipped.append(user)
            error.append(str(e))
    if banned:
        text = f"`{JAVES_NNAME}: `**Successfully banned**\n"
        text += ', '.join((f'`{x}`' for x in banned))
        if reason:
            text += f"\n\n**Reason:** `{reason}`"            
        await event.reply(text)
    if skipped:
        text2 = f"`{JAVES_NNAME}: `**Failed to ban **"
        text2 += ', '.join((f'{x}' for x in skipped))
        text = "\n **Error(s)**\n•"
        text += '•'.join((f'{x}\n' for x in error))
        await event.reply(text2)
        await event.reply(text)




@javes05(outgoing=True, pattern="^!unban(?: |$|\n)([\s\S]*)")
async def ban(event):    
    if event.is_private:
        await event.reply("`You can't unban users in private chats.`")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.edit(f"`{JAVES_NNAME}:` **I haven't got the admin rights to do this.**")
        return
    match = event.pattern_match.group(1)  
    args, kwargs = await parse_arguments(match)
    reason = kwargs.get('r', None)
    skipped = []
    banned = []
    error = []
    if not args and event.reply_to_msg_id:
        reply = await event.get_reply_message()
        args.append(reply.sender_id)
    if not args:
        await event.edit(f"`{JAVES_NNAME}:` **I don't know who you're talking about, you're going to need to specify a user...!**")
        return        
    entity = await event.get_chat()
    for user in args:
        if isinstance(user, list):
            continue
        try:
            await client.edit_permissions(entity=entity,
                                          user=user,
                                          send_messages=True)
            banned.append(user)
        except Exception as e:      
            skipped.append(user)
            error.append(str(e))
    if banned:
        text = f"`{JAVES_NNAME}: `**Successfully unbanned**\n"
        text += ', '.join((f'`{x}`' for x in banned))
        if reason:
            text += f"\n`Reason:` `{reason}`"            
        await event.edit(text)
    if skipped:
        text2 = f"`{JAVES_NNAME}: `**Failed to unban **"
        text2 += ', '.join((f'{x}' for x in skipped))
        text = "\n **Error(s)**\n•"
        text += '•'.join((f'{x}\n' for x in error))
        await event.reply(text2)
        await event.reply(text)

@javes.on(rekcah05(pattern=f"unban(?: |$|\n)([\s\S]*)", allow_sudo=True))
async def ban(event):    
    if event.is_private:
        await event.reply("`You can't unban users in private chats.`")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.reply(f"`{JAVES_NNAME}:` **I haven't got the admin rights to do this.**")
        return
    match = event.pattern_match.group(1)  
    args, kwargs = await parse_arguments(match)
    reason = kwargs.get('r', None)
    skipped = []
    banned = []
    error = []
    if not args and event.reply_to_msg_id:
        reply = await event.get_reply_message()
        args.append(reply.sender_id)
    if not args:
        await event.reply(f"`{JAVES_NNAME}:` **I don't know who you're talking about, you're going to need to specify a user...!**")
        return        
    entity = await event.get_chat()
    for user in args:
        if isinstance(user, list):
            continue
        try:
            await client.edit_permissions(entity=entity,
                                          user=user,
                                          send_messages=True)
            banned.append(user)
        except Exception as e:      
            skipped.append(user)
            error.append(str(e))
    if banned:
        text = f"`{JAVES_NNAME}: `**Successfully unbanned**\n"
        text += ', '.join((f'`{x}`' for x in banned))
        if reason:
            text += f"\n`Reason:` `{reason}`"            
        await event.reply(text)
    if skipped:
        text2 = f"`{JAVES_NNAME}: `**Failed to unban **"
        text2 += ', '.join((f'{x}' for x in skipped))
        text = "\n **Error(s)**\n•"
        text += '•'.join((f'{x}\n' for x in error))
        await event.reply(text2)
        await event.reply(text)
        
@javes05(outgoing=True, pattern="^!mute(?: |$|\n)([\s\S]*)")
async def ban(event):    
    if event.is_private:
        await event.reply("`You can't mute users in private chats.`")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.edit(f"`{JAVES_NNAME}:` **I haven't got the admin rights to do this.**")
        return
    match = event.pattern_match.group(1)  
    args, kwargs = await parse_arguments(match)
    reason = kwargs.get('r', None)
    skipped = []
    banned = []
    error = []
    if not args and event.reply_to_msg_id:
        reply = await event.get_reply_message()
        args.append(reply.sender_id)
    if not args:
        await event.edit(f"`{JAVES_NNAME}:` **I don't know who you're talking about, you're going to need to specify a user...!**")
        return        
    entity = await event.get_chat()
    for user in args:
        if isinstance(user, list):
            continue
        try:
            await client.edit_permissions(entity=entity,
                                          user=user,
                                          send_messages=False)
            banned.append(user)
        except Exception as e:      
            skipped.append(user)
            error.append(str(e))
    if banned:
        text = f"`{JAVES_NNAME}: `**Successfully muted**\n"
        text += ', '.join((f'`{x}`' for x in banned))
        if reason:
            text += f"\n`Reason:` `{reason}`"            
        await event.edit(text)
    if skipped:
        text2 = f"`{JAVES_NNAME}: `**Failed to mute **"
        text2 += ', '.join((f'{x}' for x in skipped))
        text = "\n **Error(s)**\n•"
        text += '•'.join((f'{x}\n' for x in error))
        await event.reply(text2)
        await event.reply(text)

@javes.on(rekcah05(pattern=f"mute(?: |$|\n)([\s\S]*)", allow_sudo=True))
async def ban(event):    
    if event.is_private:
        await event.reply("`You can't mute users in private chats.`")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.reply(f"`{JAVES_NNAME}:` **I haven't got the admin rights to do this.**")
        return
    match = event.pattern_match.group(1)  
    args, kwargs = await parse_arguments(match)
    reason = kwargs.get('r', None)
    skipped = []
    banned = []
    error = []
    if not args and event.reply_to_msg_id:
        reply = await event.get_reply_message()
        args.append(reply.sender_id)
    if not args:
        await event.reply(f"`{JAVES_NNAME}:` **I don't know who you're talking about, you're going to need to specify a user...!**")
        return        
    entity = await event.get_chat()
    for user in args:
        if isinstance(user, list):
            continue
        try:
            await client.edit_permissions(entity=entity,
                                          user=user,
                                          send_messages=False)
            banned.append(user)
        except Exception as e:      
            skipped.append(user)
            error.append(str(e))
    if banned:
        text = f"`{JAVES_NNAME}: `**Successfully muted**\n"
        text += ', '.join((f'`{x}`' for x in banned))
        if reason:
            text += f"\n`Reason:` `{reason}`"            
        await event.reply(text)
    if skipped:
        text2 = f"`{JAVES_NNAME}: `**Failed to mute **"
        text2 += ', '.join((f'{x}' for x in skipped))
        text = "\n **Error(s)**\n•"
        text += '•'.join((f'{x}\n' for x in error))
        await event.reply(text2)
        await event.reply(text)


@javes05(outgoing=True, pattern="^!unmute(?: |$|\n)([\s\S]*)")
async def ban(event):    
    if event.is_private:
        await event.reply("`You can't unmute users in private chats.`")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.edit(f"`{JAVES_NNAME}:` **I haven't got the admin rights to do this.**")
        return
    match = event.pattern_match.group(1)  
    args, kwargs = await parse_arguments(match)
    reason = kwargs.get('r', None)
    skipped = []
    banned = []
    error = []
    if not args and event.reply_to_msg_id:
        reply = await event.get_reply_message()
        args.append(reply.sender_id)
    if not args:
        await event.edit(f"`{JAVES_NNAME}:` **I don't know who you're talking about, you're going to need to specify a user...!**")
        return        
    entity = await event.get_chat()
    for user in args:
        if isinstance(user, list):
            continue
        try:
            await client.edit_permissions(entity=entity,
                                          user=user,
                                          send_messages=True)
            banned.append(user)
        except Exception as e:      
            skipped.append(user)
            error.append(str(e))
    if banned:
        text = f"`{JAVES_NNAME}: `**Successfully unmuted**\n"
        text += ', '.join((f'`{x}`' for x in banned))
        if reason:
            text += f"\n`Reason:` `{reason}`"            
        await event.edit(text)
    if skipped:
        text2 = f"`{JAVES_NNAME}: `**Failed to unmute **"
        text2 += ', '.join((f'{x}' for x in skipped))
        text = "\n **Error(s)**\n•"
        text += '•'.join((f'{x}\n' for x in error))
        await event.reply(text2)
        await event.reply(text)


@javes.on(rekcah05(pattern=f"unmute(?: |$|\n)([\s\S]*)", allow_sudo=True))
async def ban(event):    
    if event.is_private:
        await event.reply("`You can't unmute users in private chats.`")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.reply(f"`{JAVES_NNAME}:` **I haven't got the admin rights to do this.**")
        return
    match = event.pattern_match.group(1)  
    args, kwargs = await parse_arguments(match)
    reason = kwargs.get('r', None)
    skipped = []
    banned = []
    error = []
    if not args and event.reply_to_msg_id:
        reply = await event.get_reply_message()
        args.append(reply.sender_id)
    if not args:
        await event.reply(f"`{JAVES_NNAME}:` **I don't know who you're talking about, you're going to need to specify a user...!**")
        return        
    entity = await event.get_chat()
    for user in args:
        if isinstance(user, list):
            continue
        try:
            await client.edit_permissions(entity=entity,
                                          user=user,
                                          send_messages=True)
            banned.append(user)
        except Exception as e:      
            skipped.append(user)
            error.append(str(e))
    if banned:
        text = f"`{JAVES_NNAME}: `**Successfully unmuted**\n"
        text += ', '.join((f'`{x}`' for x in banned))
        if reason:
            text += f"\n`Reason:` `{reason}`"            
        await event.reply(text)
    if skipped:
        text2 = f"`{JAVES_NNAME}: `**Failed to unmute **"
        text2 += ', '.join((f'{x}' for x in skipped))
        text = "\n **Error(s)**\n•"
        text += '•'.join((f'{x}\n' for x in error))
        await event.reply(text2)
        await event.reply(text)


@javes05(outgoing=True, pattern="^!kick(?: |$|\n)([\s\S]*)")
async def ban(event):    
    if event.is_private:
        await event.reply("`You can't kick users in private chats.`")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.edit(f"`{JAVES_NNAME}:` **I haven't got the admin rights to do this.**")
        return
    match = event.pattern_match.group(1)  
    args, kwargs = await parse_arguments(match)
    reason = kwargs.get('r', None)
    skipped = []
    banned = []
    error = []
    if not args and event.reply_to_msg_id:
        reply = await event.get_reply_message()
        args.append(reply.sender_id)
    if not args:
        await event.edit(f"`{JAVES_NNAME}:` **I don't know who you're talking about, you're going to need to specify a user...!**")
        return        
    entity = await event.get_chat()
    for user in args:
        if isinstance(user, list):
            continue
        try:
            await client.kick_participant(entity=entity,
                                          user=user)
            banned.append(user)
        except Exception as e:      
            skipped.append(user)
            error.append(str(e))
    if banned:
        text = f"`{JAVES_NNAME}: `**Successfully kicked**\n"
        text += ', '.join((f'`{x}`' for x in banned))
        if reason:
            text += f"\n`Reason:` `{reason}`"            
        await event.edit(text)
    if skipped:
        text2 = f"`{JAVES_NNAME}: `**Failed to kick **"
        text2 += ', '.join((f'{x}' for x in skipped))
        text = "\n **Error(s)**\n•"
        text += '•'.join((f'{x}\n' for x in error))
        await event.reply(text2)
        await event.reply(text)

@javes.on(rekcah05(pattern=f"kick(?: |$|\n)([\s\S]*)", allow_sudo=True))
async def ban(event):    
    if event.is_private:
        await event.reply("`You can't kick users in private chats.`")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.reply(f"`{JAVES_NNAME}:` **I haven't got the admin rights to do this.**")
        return
    match = event.pattern_match.group(1)  
    args, kwargs = await parse_arguments(match)
    reason = kwargs.get('r', None)
    skipped = []
    banned = []
    error = []
    if not args and event.reply_to_msg_id:
        reply = await event.get_reply_message()
        args.append(reply.sender_id)
    if not args:
        await event.reply(f"`{JAVES_NNAME}:` **I don't know who you're talking about, you're going to need to specify a user...!**")
        return        
    entity = await event.get_chat()
    for user in args:
        if isinstance(user, list):
            continue
        try:
            await client.kick_participant(entity=entity,
                                          user=user)
            banned.append(user)
        except Exception as e:      
            skipped.append(user)
            error.append(str(e))
    if banned:
        text = f"`{JAVES_NNAME}: `**Successfully kicked**\n"
        text += ', '.join((f'`{x}`' for x in banned))
        if reason:
            text += f"\n`Reason:` `{reason}`"            
        await event.reply(text)
    if skipped:
        text2 = f"`{JAVES_NNAME}: `**Failed to kick **"
        text2 += ', '.join((f'{x}' for x in skipped))
        text = "\n **Error(s)**\n•"
        text += '•'.join((f'{x}\n' for x in error))
        await event.reply(text2)
        await event.reply(text)

@javes05(outgoing=True, pattern="^!tmute(?: |$|\n)([\s\S]*)")
async def tmute(event):
    if event.is_private:
        await event.reply("`You can't tmute users in private chats.`")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.edit(f"`{JAVES_NNAME}:` **I haven't got the admin rights to do this.**")
        return
    match = event.pattern_match.group(1)  
    try:
       args, kwargs = await parse_arguments(match)
    except:
    	return await event.edit(f"`{JAVES_NNAME}:`**Error! invalid time format **\n usage !tmute <users> t=<number>h/s/w/m r=<reason>")               
    reason = kwargs.get('r', None)
    period = kwargs.get('t', None)
    if not period:
        return await event.edit(f"`{JAVES_NNAME}:`**Error! invalid time format **\n usage !tmute <user> t=<n>h/s/w/m r=<reason>")               
    try:
       period = await string_to_secs(period)
    except:
    	return await event.edit(f"`{JAVES_NNAME}:`**Error! invalid time format **\n usage !tban <users> t=<number>h/s/w/m r=<reason>")               
    skipped = []
    tmuted = []
    error = []
    if not args and event.reply_to_msg_id:
        reply = await event.get_reply_message()
        args.append(reply.sender_id)
    if not args:
        await event.edit(f"`{JAVES_NNAME}:` **I don't know who you're talking about, you're going to need to specify a user...!**")
        return

    entity = await event.get_chat()
    for user in args:
        if isinstance(user, list):
            continue
        try:
            await client.edit_permissions(entity=entity,
                                          user=user,
                                          until_date=timedelta(seconds=period),
                                          send_messages=False)
            tmuted.append(user)
        except Exception as e:      
            skipped.append(user)
            error.append(str(e))
    if tmuted:
        text = f"`{JAVES_NNAME}: `**Successfully Tmuted**\n"
        text += ', '.join((f'`{x}`' for x in tmuted))
        text += f"\n**Untill**` {timedelta(seconds=period)} hours`"
        if reason:
            text += f"\n**Reason**:` `{reason}`"            
        await event.edit(text)
    if skipped:
        text2 = f"`{JAVES_NNAME}: `**Failed to Tmute **"
        text2 += ', '.join((f'{x}' for x in skipped))
        text = "\n **Error(s)**\n•"
        text += '•'.join((f'{x}\n' for x in error))
        await event.reply(text2)
        await event.reply(text)

    
@javes.on(rekcah05(pattern=f"tmute(?: |$|\n)([\s\S]*)", allow_sudo=True))
async def tmute(event):
    if event.is_private:
        await event.reply("`You can't tmute users in private chats.`")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.reply(f"`{JAVES_NNAME}:` **I haven't got the admin rights to do this.**")
        return
    match = event.pattern_match.group(1)  
    try:
       args, kwargs = await parse_arguments(match)
    except:
    	return await event.reply(f"`{JAVES_NNAME}:`**Error! invalid time format **\n usage !tmute <users> t=<number>h/s/w/m r=<reason>")               
    reason = kwargs.get('r', None)
    period = kwargs.get('t', None)
    if not period:
        return await event.reply(f"`{JAVES_NNAME}:`**Error! invalid time format **\n usage !tmute <user> t=<n>h/s/w/m r=<reason>")               
    try:
       period = await string_to_secs(period)
    except:
    	return await event.reply(f"`{JAVES_NNAME}:`**Error! invalid time format **\n usage !tban <users> t=<number>h/s/w/m r=<reason>")               
    skipped = []
    tmuted = []
    error = []
    if not args and event.reply_to_msg_id:
        reply = await event.get_reply_message()
        args.append(reply.sender_id)
    if not args:
        await event.reply(f"`{JAVES_NNAME}:` **I don't know who you're talking about, you're going to need to specify a user...!**")
        return

    entity = await event.get_chat()
    for user in args:
        if isinstance(user, list):
            continue
        try:
            await client.edit_permissions(entity=entity,
                                          user=user,
                                          until_date=timedelta(seconds=period),
                                          send_messages=False)
            tmuted.append(user)
        except Exception as e:      
            skipped.append(user)
            error.append(str(e))
    if tmuted:
        text = f"`{JAVES_NNAME}: `**Successfully Tmuted**\n"
        text += ', '.join((f'`{x}`' for x in tmuted))
        text += f"\n**Untill**` {timedelta(seconds=period)} hours`"
        if reason:
            text += f"\n**Reason**:` `{reason}`"            
        await event.reply(text)
    if skipped:
        text2 = f"`{JAVES_NNAME}: `**Failed to Tmute **"
        text2 += ', '.join((f'{x}' for x in skipped))
        text = "\n **Error(s)**\n•"
        text += '•'.join((f'{x}\n' for x in error))
        await event.reply(text2)
        await event.reply(text)



@javes05(outgoing=True, pattern="^!tban(?: |$|\n)([\s\S]*)")
async def tmute(event):
    if event.is_private:
        await event.reply("`You can't tban users in private chats.`")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.edit(f"`{JAVES_NNAME}:` **I haven't got the admin rights to do this.**")
        return
    match = event.pattern_match.group(1)  
    try:
       args, kwargs = await parse_arguments(match)
    except:
    	return await event.edit(f"`{JAVES_NNAME}:`**Error! invalid time format **\n usage !tban <users> t=<number>h/s/w/m r=<reason>")               
    reason = kwargs.get('r', None)
    period = kwargs.get('t', None)
    if not period:
        return await event.edit(f"`{JAVES_NNAME}:`**Error! invalid time format **\n usage !tban <user> t=<n>h/s/w/m r=<reason>")       
    try:
       period = await string_to_secs(period)
    except:
    	return await event.edit(f"`{JAVES_NNAME}:`**Error! invalid time format **\n usage !tban <users> t=<number>h/s/w/m r=<reason>")               
    skipped = []
    tmuted = []
    error = []
    if not args and event.reply_to_msg_id:
        reply = await event.get_reply_message()
        args.append(reply.sender_id)
    if not args:
        await event.edit(f"`{JAVES_NNAME}:` **I don't know who you're talking about, you're going to need to specify a user...!**")
        return

    entity = await event.get_chat()
    for user in args:
        if isinstance(user, list):
            continue
        try:
            await client.edit_permissions(entity=entity,
                                          user=user,
                                          until_date=timedelta(seconds=period),
                                          view_messages=False)
            tmuted.append(user)
        except Exception as e:      
            skipped.append(user)
            error.append(str(e))
    if tmuted:
        text = f"`{JAVES_NNAME}: `**Successfully Tbanned**\n"
        text += ', '.join((f'`{x}`' for x in tmuted))
        text += f"\n**Untill** `{timedelta(seconds=period)} hours`"
        if reason:
            text += f"\n**Reason**:`{reason}`"            
        await event.edit(text)
    if skipped:
        text2 = f"`{JAVES_NNAME}: `**Failed to Tban **"
        text2 += ', '.join((f'{x}' for x in skipped))
        text = "\n **Error(s)**\n•"
        text += '•'.join((f'{x}\n' for x in error))
        await event.reply(text2)
        await event.reply(text)



@javes.on(rekcah05(pattern=f"tban(?: |$|\n)([\s\S]*)", allow_sudo=True))
async def tmute(event):
    if event.is_private:
        await event.reply("`You can't tban users in private chats.`")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.reply(f"`{JAVES_NNAME}:` **I haven't got the admin rights to do this.**")
        return
    match = event.pattern_match.group(1)  
    try:
       args, kwargs = await parse_arguments(match)
    except:
    	return await event.reply(f"`{JAVES_NNAME}:`**Error! invalid time format **\n usage !tban <users> t=<number>h/s/w/m r=<reason>")               
    reason = kwargs.get('r', None)
    period = kwargs.get('t', None)
    if not period:
        return await event.reply(f"`{JAVES_NNAME}:`**Error! invalid time format **\n usage !tban <user> t=<n>h/s/w/m r=<reason>")       
    try:
       period = await string_to_secs(period)
    except:
    	return await event.reply(f"`{JAVES_NNAME}:`**Error! invalid time format **\n usage !tban <users> t=<number>h/s/w/m r=<reason>")               
    skipped = []
    tmuted = []
    error = []
    if not args and event.reply_to_msg_id:
        reply = await event.get_reply_message()
        args.append(reply.sender_id)
    if not args:
        await event.reply(f"`{JAVES_NNAME}:` **I don't know who you're talking about, you're going to need to specify a user...!**")
        return

    entity = await event.get_chat()
    for user in args:
        if isinstance(user, list):
            continue
        try:
            await client.edit_permissions(entity=entity,
                                          user=user,
                                          until_date=timedelta(seconds=period),
                                          view_messages=False)
            tmuted.append(user)
        except Exception as e:      
            skipped.append(user)
            error.append(str(e))
    if tmuted:
        text = f"`{JAVES_NNAME}: `**Successfully Tbanned**\n"
        text += ', '.join((f'`{x}`' for x in tmuted))
        text += f"\n**Untill** `{timedelta(seconds=period)} hours`"
        if reason:
            text += f"\n**Reason**:`{reason}`"            
        await event.reply(text)
    if skipped:
        text2 = f"`{JAVES_NNAME}: `**Failed to Tban **"
        text2 += ', '.join((f'{x}' for x in skipped))
        text = "\n **Error(s)**\n•"
        text += '•'.join((f'{x}\n' for x in error))
        await event.reply(text2)
        await event.reply(text)





    
@javes05(outgoing=True, pattern="^!unbanall ?(.*)")
async def _(event):
        if event.fwd_from:
            return
        if event.is_private:
            return False
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
                  return await event.edit(f"`{JAVES_NNAME}:` **I haven't got the admin rights to do this.**")
        input_str = event.pattern_match.group(1)             
        await event.edit(f"`{JAVES_NNAME}: `**Unbanning all users.....**")
        p = 0
        async for i in javes.iter_participants(event.chat_id, filter=ChannelParticipantsKicked, aggressive=True):
            rights = ChatBannedRights(until_date=0,view_messages=False)
            try:
                await javes(functions.channels.EditBannedRequest(event.chat_id, i, rights))
            except FloodWaitError as ex:                
                sleep(ex.seconds)
            except Exception as ex:
                await event.edit(str(ex))
            else:
                p += 1
        await event.edit(f"`{JAVES_NNAME}: `**Successfully Unbanned {p} user(s)**")


@javes.on(rekcah05(pattern=f"unbanall ?(.*)", allow_sudo=True))
async def _(event):
        if event.fwd_from:
            return
        if event.is_private:
            return False
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
                  return await event.reply(f"`{JAVES_NNAME}:` **I haven't got the admin rights to do this.**")
        input_str = event.pattern_match.group(1)             
        rkp = await event.reply(f"`{JAVES_NNAME}: `**Unbanning all users.....**")
        p = 0
        async for i in javes.iter_participants(event.chat_id, filter=ChannelParticipantsKicked, aggressive=True):
            rights = ChatBannedRights(until_date=0,view_messages=False)
            try:
                await javes(functions.channels.EditBannedRequest(event.chat_id, i, rights))
            except FloodWaitError as ex:                
                sleep(ex.seconds)
            except Exception as ex:
                await rkp.edit(str(ex))
            else:
                p += 1
        await rkp.edit(f"`{JAVES_NNAME}: `**Successfully Unbanned {p} user(s)**")




@javes05(outgoing=True, pattern="^!akick ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.is_private:
        return False
    input_str = event.pattern_match.group(1)
    if input_str:
        chat = await event.get_chat()
        if not (chat.admin_rights or chat.creator):
            await event.edit(f"`{JAVES_NNAME}:` **I haven't got the admin rights to do this.**")
            return False
    y = w = o = q = r = m = n = p = b = c = d = 0 ; e = []    
    await event.edit(f"`{JAVES_NNAME}:` **searching users......**")
    async for i in javes.iter_participants(event.chat_id):
        p = p + 1        
        rights = ChatBannedRights(until_date=None,view_messages=True)
        if isinstance(i.status, UserStatusEmpty):
            y = y + 1
            if "y" in input_str:         
                try:       
                   await client.kick_participant(event.chat_id,i)
                   c = c + 1   
                   await event.edit(f"**{JAVES_NNAME}:** `Successfully kicked {c} UserStatusEmpty account(s)`")        
                except Exception as e:      
                    await event.reply(str(e))                                        
        if isinstance(i.status, UserStatusLastMonth):
            m = m + 1
            if "m" in input_str:
                try:       
                   await client.kick_participant(event.chat_id,i)
                   c = c + 1 
                   await event.edit(f"**{JAVES_NNAME}:** `Successfully kicked {c} UserStatusLastMonth account(s)`")        
                except Exception as e:      
                    await event.reply(str(e))  
        if isinstance(i.status, UserStatusLastWeek):
            w = w + 1
            if "w" in input_str:
                try:       
                   await client.kick_participant(event.chat_id,i)
                   c = c + 1
                   await event.edit(f"**{JAVES_NNAME}:** `Successfully kicked {c} UserStatusLastWeek account(s)`")        
                except Exception as e:      
                    await event.reply(str(e))  
        if isinstance(i.status, UserStatusOffline):
            o = o + 1
            if "o" in input_str:
                try:       
                   await client.kick_participant(event.chat_id,i)
                   c = c + 1
                   await event.edit(f"**{JAVES_NNAME}:** `Successfully kicked {c} UserStatusOffline account(s)`")             
                except Exception as e:      
                    await event.reply(str(e))  
        if isinstance(i.status, UserStatusOnline):
            q = q + 1
            if "q" in input_str:
                try:       
                   await client.kick_participant(event.chat_id,i)
                   c = c + 1
                   await event.edit(f"**{JAVES_NNAME}:** `Successfully kicked {c} UserStatusOnline account(s)`")            
                except Exception as e:      
                    await event.reply(str(e))  
        if isinstance(i.status, UserStatusRecently):
            r = r + 1
            if "r" in input_str:
                try:       
                   await client.kick_participant(event.chat_id,i)
                   c = c + 1
                   await event.edit(f"**{JAVES_NNAME}:** `Successfully kicked {c} UserStatusRecently account(s)`")        
                except Exception as e:      
                    await event.reply(str(e))  
        if i.bot:
            b = b + 1
            if "b" in input_str:
                try:       
                   await client.kick_participant(event.chat_id,i)
                   c = c + 1            
                   await event.edit(f"**{JAVES_NNAME}:** `Successfully kicked {c} bot(s)`")        
                except Exception as e:      
                    await event.reply(str(e))  
        elif i.deleted:
            d = d + 1
            if "d" in input_str:
                try:       
                   await client.kick_participant(event.chat_id,i)                           
                   c = c + 1                  
                   await event.edit(f"**{JAVES_NNAME}:** `Successfully kicked {c} deleted account(s)`")        
                except Exception as e:      
                    await event.reply(str(e))                  
        elif i.status is None:
            n = n + 1
    if input_str:      
    	return       
    return await event.edit(                           
                    f"`{JAVES_NNAME}:`   **Current Status**\n\n"
                    f" **Deleted Accounts**: `{d}`\n"
                    f" **UserStatusEmpty**: `{y}`\n"
                    f" **UserStatusLastMonth**: `{m}`\n"                                                                                     
                    f" **UserStatusLastWeek**: `{w}`\n"                   
                    f" **UserStatusOffline**: `{o}`\n"
                    f" **UserStatusOnline**: `{q}`\n"
                    f" **UserStatusRecently**: `{r}`\n"
                    f" **Bots**: `{b}`\n"
                    f" **Unknown** `{n}`")
                    


@javes.on(rekcah05(pattern=f"akick ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if event.is_private:
        return False
    input_str = event.pattern_match.group(1)
    if input_str:
        chat = await event.get_chat()
        if not (chat.admin_rights or chat.creator):
            await event.reply(f"`{JAVES_NNAME}:` **I haven't got the admin rights to do this.**")
            return False
    y = w = o = q = r = m = n = p = b = c = d = 0 ; e = []    
    rkp = await event.reply(f"`{JAVES_NNAME}:` **searching users......**")
    async for i in javes.iter_participants(event.chat_id):
        p = p + 1        
        rights = ChatBannedRights(until_date=None,view_messages=True)
        if isinstance(i.status, UserStatusEmpty):
            y = y + 1
            if "y" in input_str:         
                try:       
                   await client.kick_participant(event.chat_id,i)
                   c = c + 1   
                   await rkp.edit(f"**{JAVES_NNAME}:** `Successfully kicked {c} UserStatusEmpty account(s)`")        
                except Exception as e:      
                    await event.reply(str(e))                                        
        if isinstance(i.status, UserStatusLastMonth):
            m = m + 1
            if "m" in input_str:
                try:       
                   await client.kick_participant(event.chat_id,i)
                   c = c + 1 
                   await rkp.edit(f"**{JAVES_NNAME}:** `Successfully kicked {c} UserStatusLastMonth account(s)`")        
                except Exception as e:      
                    await event.reply(str(e))  
        if isinstance(i.status, UserStatusLastWeek):
            w = w + 1
            if "w" in input_str:
                try:       
                   await client.kick_participant(event.chat_id,i)
                   c = c + 1
                   await rkp.edit(f"**{JAVES_NNAME}:** `Successfully kicked {c} UserStatusLastWeek account(s)`")        
                except Exception as e:      
                    await event.reply(str(e))  
        if isinstance(i.status, UserStatusOffline):
            o = o + 1
            if "o" in input_str:
                try:       
                   await client.kick_participant(event.chat_id,i)
                   c = c + 1
                   await rkp.edit(f"**{JAVES_NNAME}:** `Successfully kicked {c} UserStatusOffline account(s)`")             
                except Exception as e:      
                    await event.reply(str(e))  
        if isinstance(i.status, UserStatusOnline):
            q = q + 1
            if "q" in input_str:
                try:       
                   await client.kick_participant(event.chat_id,i)
                   c = c + 1
                   await rkp.edit(f"**{JAVES_NNAME}:** `Successfully kicked {c} UserStatusOnline account(s)`")            
                except Exception as e:      
                    await event.reply(str(e))  
        if isinstance(i.status, UserStatusRecently):
            r = r + 1
            if "r" in input_str:
                try:       
                   await client.kick_participant(event.chat_id,i)
                   c = c + 1
                   await rkp.edit(f"**{JAVES_NNAME}:** `Successfully kicked {c} UserStatusRecently account(s)`")        
                except Exception as e:      
                    await event.reply(str(e))  
        if i.bot:
            b = b + 1
            if "b" in input_str:
                try:       
                   await client.kick_participant(event.chat_id,i)
                   c = c + 1            
                   await rkp.edit(f"**{JAVES_NNAME}:** `Successfully kicked {c} bot(s)`")        
                except Exception as e:      
                    await event.reply(str(e))  
        elif i.deleted:
            d = d + 1
            if "d" in input_str:
                try:       
                   await client.kick_participant(event.chat_id,i)                           
                   c = c + 1                  
                   await rkp.edit(f"**{JAVES_NNAME}:** `Successfully kicked {c} deleted account(s)`")        
                except Exception as e:      
                    await event.reply(str(e))                  
        elif i.status is None:
            n = n + 1
    if input_str:      
    	return       
    return await rkp.edit(                           
                    f"`{JAVES_NNAME}:`   **Current Status**\n\n"
                    f" **Deleted Accounts**: `{d}`\n"
                    f" **UserStatusEmpty**: `{y}`\n"
                    f" **UserStatusLastMonth**: `{m}`\n"                                                                                     
                    f" **UserStatusLastWeek**: `{w}`\n"                   
                    f" **UserStatusOffline**: `{o}`\n"
                    f" **UserStatusOnline**: `{q}`\n"
                    f" **UserStatusRecently**: `{r}`\n"
                    f" **Bots**: `{b}`\n"
                    f" **Unknown** `{n}`")
                    




@javes05(outgoing=True, pattern="^\!setgpic$", groups_only=True)
async def set_group_photo(gpic):
    if not gpic.is_group:
        await gpic.edit(f"`{JAVES_NNAME}:` **I don't think this is a group.**")
        return
    replymsg = await gpic.get_reply_message()
    chat = await gpic.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    photo = None
    if not admin and not creator:
        await gpic.edit(NO_ADMIN)
        return
    if replymsg and replymsg.media:
        if isinstance(replymsg.media, MessageMediaPhoto):
            photo = await gpic.client.download_media(message=replymsg.photo)
        elif "image" in replymsg.media.document.mime_type.split('/'):
            photo = await gpic.client.download_file(replymsg.media.document)
        else:
            await gpic.edit(INVALID_MEDIA)
    if photo:
        try:
            await gpic.client(
                EditPhotoRequest(gpic.chat_id, await
                                 gpic.client.upload_file(photo)))
            await gpic.edit(CHAT_PP_CHANGED)
        except PhotoCropSizeSmallError:
            await gpic.edit(PP_TOO_SMOL)
        except ImageProcessFailedError:
            await gpic.edit(PP_ERROR)

@javes.on(rekcah05(pattern=f"setgpic$", allow_sudo=True))
async def set_group_photo(gpic):
    if not gpic.is_group:
        await gpic.reply(f"`{JAVES_NNAME}:` **I don't think this is a group.**")
        return
    replymsg = await gpic.get_reply_message()
    chat = await gpic.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    photo = None
    if not admin and not creator:
        await gpic.reply(NO_ADMIN)
        return
    if replymsg and replymsg.media:
        if isinstance(replymsg.media, MessageMediaPhoto):
            photo = await gpic.client.download_media(message=replymsg.photo)
        elif "image" in replymsg.media.document.mime_type.split('/'):
            photo = await gpic.client.download_file(replymsg.media.document)
        else:
            await gpic.reply(INVALID_MEDIA)
    if photo:
        try:
            await gpic.client(
                EditPhotoRequest(gpic.chat_id, await
                                 gpic.client.upload_file(photo)))
            await gpic.reply(CHAT_PP_CHANGED)
        except PhotoCropSizeSmallError:
            await gpic.reply(PP_TOO_SMOL)
        except ImageProcessFailedError:
            await gpic.reply(PP_ERROR)

                  
@javes05(outgoing=True, pattern="^\!pin(?: |$)(.*)", groups_only=True)
async def pin(msg):
    chat = await msg.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await msg.edit(NO_ADMIN)
        return
    to_pin = msg.reply_to_msg_id
    if not to_pin:
        await msg.edit(f"`{JAVES_NNAME}`: ** Reply to a message to pin it.**")
        return
    options = msg.pattern_match.group(1)
    is_silent = True
    if options.lower() == "loud":
        is_silent = False
    try:
        await msg.client(
            UpdatePinnedMessageRequest(msg.to_id, to_pin, is_silent))
    except BadRequestError:
        await msg.edit(NO_PERM)
        return
    await msg.edit(f"`{JAVES_NNAME}`: ** Pinned Successfully !!**")

@javes.on(rekcah05(pattern=f"pin(?: |$)(.*)", allow_sudo=True))
async def pin(msg):
    chat = await msg.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await msg.edit(NO_ADMIN)
        return
    to_pin = msg.reply_to_msg_id
    if not to_pin:
        await msg.reply(f"`{JAVES_NNAME}`: ** Reply to a message to pin it.**")
        return
    options = msg.pattern_match.group(1)
    is_silent = True
    if options.lower() == "loud":
        is_silent = False
    try:
        await msg.client(
            UpdatePinnedMessageRequest(msg.to_id, to_pin, is_silent))
    except BadRequestError:
        await msg.edit(NO_PERM)
        return
    await msg.reply(f"`{JAVES_NNAME}`: ** Pinned Successfully !!**")




@javes05(outgoing=True, pattern=r"^\!lock ?(.*)")
async def locks(event):
    input_str = event.pattern_match.group(1).lower()
    peer_id = event.chat_id
    msg = None
    media = None
    sticker = None
    gif = None
    gamee = None
    ainline = None
    gpoll = None
    adduser = None
    cpin = None
    changeinfo = None
    if input_str == "msg":
        msg = True
        what = "messages"
    elif input_str == "media":
        media = True
        what = "media"
    elif input_str == "sticker":
        sticker = True
        what = "stickers"
    elif input_str == "gif":
        gif = True
        what = "GIFs"
    elif input_str == "game":
        gamee = True
        what = "games"
    elif input_str == "inline":
        ainline = True
        what = "inline bots"
    elif input_str == "poll":
        gpoll = True
        what = "polls"
    elif input_str == "invite":
        adduser = True
        what = "invites"
    elif input_str == "pin":
        cpin = True
        what = "pins"
    elif input_str == "info":
        changeinfo = True
        what = "chat info"
    elif input_str == "all":
        msg = True
        media = True
        sticker = True
        gif = True
        gamee = True
        ainline = True
        gpoll = True
        adduser = True
        cpin = True
        changeinfo = True
        what = "everything"
    else:
        if not input_str:
            await event.edit(f"`{JAVES_NNAME}`: **I can't lock nothing !!**")
            return
        else:
            await event.edit(f"`{JAVES_NNAME}`: Invalid unlock type \n you can lock all , pin , info , game , invite , poll , inline , gif , media , stickers , msg ")
            return

    lock_rights = ChatBannedRights(
        until_date=None,
        send_messages=msg,
        send_media=media,
        send_stickers=sticker,
        send_gifs=gif,
        send_games=gamee,
        send_inline=ainline,
        send_polls=gpoll,
        invite_users=adduser,
        pin_messages=cpin,
        change_info=changeinfo,
    )
    try:
        await event.client(
            EditChatDefaultBannedRightsRequest(peer=peer_id,
                                               banned_rights=lock_rights))
        await event.edit(f"`{JAVES_NNAME}`: **Locked {what} for this chat !!**")
    except BaseException as e:
        await event.edit(
            f"`{JAVES_NNAME}`: **Sorry i can't able to get admin  rights here**\n**Error:** {str(e)}")
        return


@javes05(outgoing=True, pattern=r"^!unlock ?(.*)")
async def rem_locks(event):
    input_str = event.pattern_match.group(1).lower()
    peer_id = event.chat_id
    msg = None
    media = None
    sticker = None
    gif = None
    gamee = None
    ainline = None
    gpoll = None
    adduser = None
    cpin = None
    changeinfo = None
    if input_str == "msg":
        msg = False
        what = "messages"
    elif input_str == "media":
        media = False
        what = "media"
    elif input_str == "sticker":
        sticker = False
        what = "stickers"
    elif input_str == "gif":
        gif = False
        what = "GIFs"
    elif input_str == "game":
        gamee = False
        what = "games"
    elif input_str == "inline":
        ainline = False
        what = "inline bots"
    elif input_str == "poll":
        gpoll = False
        what = "polls"
    elif input_str == "invite":
        adduser = False
        what = "invites"
    elif input_str == "pin":
        cpin = False
        what = "pins"
    elif input_str == "info":
        changeinfo = False
        what = "chat info"
    elif input_str == "all":
        msg = False
        media = False
        sticker = False
        gif = False
        gamee = False
        ainline = False
        gpoll = False
        adduser = False
        cpin = False
        changeinfo = False
        what = "everything"
    else:
        if not input_str:
            await event.edit(f"`{JAVES_NNAME}`: **I can't unlock nothing !!**")
            return
        else:
            await event.edit(f"`{JAVES_NNAME}`: Invalid unlock type \n you can lock all , pin , info , game , invite , poll , inline , gif , media , stickers , msg ")
            return
    unlock_rights = ChatBannedRights(
        until_date=None,
        send_messages=msg,
        send_media=media,
        send_stickers=sticker,
        send_gifs=gif,
        send_games=gamee,
        send_inline=ainline,
        send_polls=gpoll,
        invite_users=adduser,
        pin_messages=cpin,
        change_info=changeinfo,
    )
    try:
        await event.client(
            EditChatDefaultBannedRightsRequest(peer=peer_id,
                                               banned_rights=unlock_rights))
        await event.edit(f"`{JAVES_NNAME}`: **Unlocked {what} for this chat !!**")
    except BaseException as e:
        await event.edit(
            f"`{JAVES_NNAME}`: **Sorry i can't able to get admin rights here`\n**Error:** {str(e)}")
        return







@javes.on(rekcah05(pattern=f"unlock ?(.*)", allow_sudo=True))
async def rem_locks(event):
    input_str = event.pattern_match.group(1).lower()
    peer_id = event.chat_id
    msg = None
    media = None
    sticker = None
    gif = None
    gamee = None
    ainline = None
    gpoll = None
    adduser = None
    cpin = None
    changeinfo = None
    if input_str == "msg":
        msg = False
        what = "messages"
    elif input_str == "media":
        media = False
        what = "media"
    elif input_str == "sticker":
        sticker = False
        what = "stickers"
    elif input_str == "gif":
        gif = False
        what = "GIFs"
    elif input_str == "game":
        gamee = False
        what = "games"
    elif input_str == "inline":
        ainline = False
        what = "inline bots"
    elif input_str == "poll":
        gpoll = False
        what = "polls"
    elif input_str == "invite":
        adduser = False
        what = "invites"
    elif input_str == "pin":
        cpin = False
        what = "pins"
    elif input_str == "info":
        changeinfo = False
        what = "chat info"
    elif input_str == "all":
        msg = False
        media = False
        sticker = False
        gif = False
        gamee = False
        ainline = False
        gpoll = False
        adduser = False
        cpin = False
        changeinfo = False
        what = "everything"
    else:
        if not input_str:
            await event.reply(f"`{JAVES_NNAME}`: **I can't unlock nothing !!**")
            return
        else:
            await event.reply(f"`{JAVES_NNAME}`: Invalid unlock type \n you can lock all , pin , info , game , invite , poll , inline , gif , media , stickers , msg ")
            return
    unlock_rights = ChatBannedRights(
        until_date=None,
        send_messages=msg,
        send_media=media,
        send_stickers=sticker,
        send_gifs=gif,
        send_games=gamee,
        send_inline=ainline,
        send_polls=gpoll,
        invite_users=adduser,
        pin_messages=cpin,
        change_info=changeinfo,
    )
    try:
        await event.client(
            EditChatDefaultBannedRightsRequest(peer=peer_id,
                                               banned_rights=unlock_rights))
        await event.replyt(f"`{JAVES_NNAME}`: **Unlocked {what} for this chat !!**")
    except BaseException as e:
        await event.reply(
            f"`{JAVES_NNAME}`: **Sorry i can't able to get admin rights here`\n**Error:** {str(e)}")
        return



@javes.on(rekcah05(pattern=f"lock ?(.*)", allow_sudo=True))
async def locks(event):
    input_str = event.pattern_match.group(1).lower()
    peer_id = event.chat_id
    msg = None
    media = None
    sticker = None
    gif = None
    gamee = None
    ainline = None
    gpoll = None
    adduser = None
    cpin = None
    changeinfo = None
    if input_str == "msg":
        msg = True
        what = "messages"
    elif input_str == "media":
        media = True
        what = "media"
    elif input_str == "sticker":
        sticker = True
        what = "stickers"
    elif input_str == "gif":
        gif = True
        what = "GIFs"
    elif input_str == "game":
        gamee = True
        what = "games"
    elif input_str == "inline":
        ainline = True
        what = "inline bots"
    elif input_str == "poll":
        gpoll = True
        what = "polls"
    elif input_str == "invite":
        adduser = True
        what = "invites"
    elif input_str == "pin":
        cpin = True
        what = "pins"
    elif input_str == "info":
        changeinfo = True
        what = "chat info"
    elif input_str == "all":
        msg = True
        media = True
        sticker = True
        gif = True
        gamee = True
        ainline = True
        gpoll = True
        adduser = True
        cpin = True
        changeinfo = True
        what = "everything"
    else:
        if not input_str:
            await event.reply(f"`{JAVES_NNAME}`: **I can't lock nothing !!**")
            return
        else:
            await event.reply(f"`{JAVES_NNAME}`: Invalid unlock type \n you can lock all , pin , info , game , invite , poll , inline , gif , media , stickers , msg ")
            return

    lock_rights = ChatBannedRights(
        until_date=None,
        send_messages=msg,
        send_media=media,
        send_stickers=sticker,
        send_gifs=gif,
        send_games=gamee,
        send_inline=ainline,
        send_polls=gpoll,
        invite_users=adduser,
        pin_messages=cpin,
        change_info=changeinfo,
    )
    try:
        await event.client(
            EditChatDefaultBannedRightsRequest(peer=peer_id,
                                               banned_rights=lock_rights))
        await event.reply(f"`{JAVES_NNAME}`: **Locked {what} for this chat !!**")
    except BaseException as e:
        await event.reply(
            f"`{JAVES_NNAME}`: **Sorry i can't able to get admin  rights here**\n**Error:** {str(e)}")
        return





CMD_HELP.update({
    "admin":
    "!promote <username/reply/userid> <adminname>\
\n**Usage:** Provides admin rights to the person in the chat.\
\n\n!demote <username/reply/userid>\
\n**Usage:** Revokes the person's admin permissions in the chat.\
\n\n!ban <username/reply/userid> r=<reason (optional)>\
\n**Usage:** Bans the person off your chat. you can ban multiple user by !ban user1 user2 user3.....etc\
\n\n!tban <username/reply/userid> t=<number>m/h/w r=<reason (optional)>\
\n**Usage:**  temporary Bans the person off your chat. you can ban multiple user by !tban t=5h user1 user2 user3.....etc \
\n\n!tmute <username/reply/userid> t=<number>m/h/w r=<reason (optional)>\
\n**Usage:**  temporary mute the perso in your chat. you can ban multiple user by !mute t=5h user1 user2 user3.....etc \
\n**Example**\
\n !tmute r=scam t=5h @username (mute @username for 5hours)\
\n\n!unban <username/reply/userid>\
\n**Usage:** Removes the ban from the person in the chat. you can unban multiple user by !unban user1 user2....etc\
\n\n!mute <username/reply/userid> r=<reason (optional)>\
\n**Usage:** Mutes the person in the chat, works on admins too.you can mute multiple user by !mute user1 user2....etc\
\n\n!warn <reply to a message > <reason (optional)>\
\n**Usage:** warn the person\
\n\n!resetwarns <reply to a user > \
\n**Usage:** reset the target person's warns\
\n\n!warns <reply to a user > \
\n**Usage:** get warnings of the targeted person\
\n\n!unmute <username/reply/userid>\
\n**Usage:** Removes the person from the muted list.\
\n\n!gban <username/reply/userid> <reason (optional)>\
\n**Usage:** Ban the person in all groups you have in common with them. and block user in your pm too!\
\n\n!ungban <username/reply/userid>\
\n**Usage:** Reply someone's message with !ungban to remove them from the gban list.\
\n\n!delusers\
\n**Usage:** Searches for deleted accounts in a group. Use !delusers clean to remove deleted accounts from the group.\
\n\n!admins\
\n**Usage:** Retrieves a list of admins in the chat.\
\n\n!bots\
\n**Usage:** Retrieves a list of bots in the chat.\
\n\n!users  <Retrieves a list of members in the chat.>\
\n**Usage:** Retrieves all (or queried) users in the chat.\
\n\n!pin <reply to message>\
\n**Usage:** Changes the group's display picture.\
\n\n!akick / !akick <option>\
\n**Usage:** !akick - give users details !akick<option> kick user(Available Options: p - reserved for channel, e - usercount, y - userstatusempty, m - userstatuslastmonth, w - userstatuslastweek, o - userstatusoffline, q - userstatusonline, r - userstatusrecently, b - bot, d - deleted account )\
\n\n!setgpic <reply to image>\
\n**Usage:** Changes the group's display picture.\
\n\n**All commands support sudo type !help sudo for more info** <reply to image>\
"
})








    
    