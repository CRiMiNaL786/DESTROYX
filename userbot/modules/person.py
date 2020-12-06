from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.messages import ReportSpamRequest
from telethon.tl.types import User
import datetime, asyncio, os, json, subprocess, time, math, sys, pytz, spamwatch, os, asyncio, html
from asyncio import sleep
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from random import choice, randint
from telethon.events import StopPropagation
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins, MessageEntityMentionName
from userbot import AFKREASON, COUNT_MSG, CMD_HELP, ISAFK, BOTLOG, BOTLOG_CHATID, USERS, PM_AUTO_BAN, bot, TEMP_DOWNLOAD_DIRECTORY, LOGS
from userbot.events import javes05, javess, rekcah05
from telethon.errors import rpcbaseerrors
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot import CMD_HELP, BOTLOG_CHATID
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.utils import get_input_location
from speedtest import Speedtest
from telethon import functions
from os import remove, execle, path, makedirs, getenv, environ
from shutil import rmtree
from pySmartDL import SmartDL
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.tl.types import DocumentAttributeVideo
#from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from userbot import CMD_HELP, bot, HEROKU_APIKEY, HEROKU_APPNAME, UPSTREAM_REPO_URL
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which
from os import remove
from telethon import version
from userbot import ALIVE_NAME, PM_MESSAGE, JAVES_NAME, JAVES_MSG, ORI_MSG, AFK_MESSAGE, AFK_MSG, BLOCK_MSG, BLOCK_MESSAGE
W_CHAT = set(int(x) for x in os.environ.get("WHITE_CHATS", "").split())
import time as t
from datetime import datetime
x = math.inf
counter = 0
start=t.time()
from sqlalchemy.exc import IntegrityError
from userbot import (COUNT_PM, CMD_HELP, BOTLOG, BOTLOG_CHATID, PM_AUTO_BAN,LASTMSG, LOGS)
from userbot import CMD_HELP, ALIVE_NAME, PM_MESSAGE, JAVES_NAME, JAVES_MSG, ORI_MSG
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)
BLOCK_MMSG = str(BLOCK_MESSAGE) if BLOCK_MESSAGE else str(BLOCK_MSG)
AFK_MMSG = str(AFK_MESSAGE) if AFK_MESSAGE else str(AFK_MSG)
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
PM_MESSAGE = str(PM_MESSAGE) if PM_MESSAGE else str(ORI_MSG)
javes = bot
UNAPPROVED_MSG = (
   f"`{JAVES_NNAME}:`**{PM_MESSAGE}**")
swapi = os.environ.get("SPAMWATCH_API_KEY", None)
SPAMWATCH_SHOUT = os.environ.get("SPAMWATCH_SHOUT", None)
    
if PM_AUTO_BAN:
 @javess(incoming=True, disable_edited=True, disable_errors=True)
 async def permitpm(event):    
    if PM_AUTO_BAN:
        self_user = await event.client.get_me()
        if event.is_private and event.chat_id != 710844948 and event.chat_id != self_user.id and not (
                await event.get_sender()).bot:
            try:
                from userbot.modules.sql_helper.pm_permit_sql import is_approved
                from userbot.modules.sql_helper.globals import gvarstatus
            except AttributeError:
                return
            apprv = is_approved(event.chat_id)
            notifsoff = gvarstatus("NOTIF_OFF")            
            if not apprv and event.text != UNAPPROVED_MSG:
                if event.chat_id in LASTMSG:
                    prevmsg = LASTMSG[event.chat_id]                    
                    if event.text != prevmsg:
                        async for message in event.client.iter_messages(
                                event.chat_id,
                                from_user='me',
                                search=UNAPPROVED_MSG):
                            await message.delete()                        
                    LASTMSG.update({event.chat_id: event.text})
                else:
                    await event.reply(UNAPPROVED_MSG)
                    LASTMSG.update({event.chat_id: event.text})
                if notifsoff:
                    await event.client.send_read_acknowledge(event.chat_id)
                if event.chat_id not in COUNT_PM:
                    COUNT_PM.update({event.chat_id: 1})
                else:
                    COUNT_PM[event.chat_id] = COUNT_PM[event.chat_id] + 1
                if COUNT_PM[event.chat_id] == 3:
                    await event.respond(
                             f"`{JAVES_NNAME}`: ** Dont spam my master's pm this is your last warning!!**")
                if COUNT_PM[event.chat_id] > 3:
                    await event.respond(
                             f"`{JAVES_NNAME}`: ** {BLOCK_MMSG} **")                        
                    try:
                        del COUNT_PM[event.chat_id]
                        del LASTMSG[event.chat_id]
                    except KeyError:
                        if BOTLOG:
                            await event.client.send_message(
                                BOTLOG_CHATID,
                                "Count PM is seemingly going retard, plis restart bot!",
                            )                       
                        return
                    await event.client(BlockRequest(event.chat_id))
                    await event.client(ReportSpamRequest(peer=event.chat_id))
                    if BOTLOG:
                        name = await event.client.get_entity(event.chat_id)
                        name0 = str(name.first_name)
                        await event.client.send_message(
                            BOTLOG_CHATID,
                            "[" + name0 + "](tg://user?id=" +
                            str(event.chat_id) + ")" +
                            " blocked  for spam your PM",
                        )

if PM_AUTO_BAN:
 @javess(disable_edited=True, outgoing=True, disable_errors=True)
 async def auto_accept(event):    
    if not PM_AUTO_BAN:
        return
    self_user = await event.client.get_me()
    if event.is_private and event.chat_id != 777000 and event.chat_id != self_user.id and not (
            await event.get_sender()).bot:
        try:
            from userbot.modules.sql_helper.pm_permit_sql import is_approved
            from userbot.modules.sql_helper.pm_permit_sql import approve
        except AttributeError:
            return
        chat = await event.get_chat()
        if isinstance(chat, User):
            if is_approved(event.chat_id) or chat.bot:
                return
            async for message in event.client.iter_messages(event.chat_id,
                                                            reverse=True,
                                                            limit=1):
                if message.message is not UNAPPROVED_MSG and message.from_id == self_user.id:
                    try:
                        approve(event.chat_id)
                    except IntegrityError:
                        return

                if is_approved(event.chat_id) and BOTLOG:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        "#AUTO-APPROVED\n" + "User: " +
                        f"[{chat.first_name}](tg://user?id={chat.id})",
                    )

async def get_full_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            ruser = await event.client(
                GetFullUserRequest(
                    previous_message.forward.from_id or previous_message.forward.channel_id
                )
            )
            return ruser, None
        else:
            ruser = await event.client(
                GetFullUserRequest(
                    previous_message.from_id
                )
            )
            return ruser, None
    else:
        input_str = None
        try:
            input_str = event.pattern_match.group(1)
        except IndexError as e:
            return None, e
        if event.message.entities :
            mention_entity = event.message.entities
            probable_user_mention_entity = mention_entity[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                ruser = await event.client(GetFullUserRequest(user_id))
                return ruser, None
            else:
                try:
                    user_object = await event.client.get_entity(input_str)
                    user_id = user_object.id
                    ruser = await event.client(GetFullUserRequest(user_id))
                    return ruser, None
                except Exception as e:
                    return None, e
        elif event.is_private:
            try:
                user_id = event.chat_id
                ruser = await event.client(GetFullUserRequest(user_id))
                return ruser, None
            except Exception as e:
                return None, e
        else:
            try:
                user_object = await event.client.get_entity(int(input_str))
                user_id = user_object.id
                ruser = await event.client(GetFullUserRequest(user_id))
                return ruser, None
            except Exception as e:
                return None, e


@javes05(outgoing=True, pattern="^\!notifoff$")
async def notifoff(noff_event):  
    try:
        from userbot.modules.sql_helper.globals import addgvar
    except AttributeError:
        await noff_event.edit("`Running on Non-SQL mode!`")
        return
    addgvar("NOTIF_OFF", True)
    await noff_event.edit("`Notifications from unapproved PM's are silenced!`")


@javes05(outgoing=True, pattern="^\!notifon$")
async def notifon(non_event):    
    try:
        from userbot.modules.sql_helper.globals import delgvar
    except AttributeError:
        await non_event.edit("`Running on Non-SQL mode!`")
        return
    delgvar("NOTIF_OFF")
    await non_event.edit("`Notifications from unapproved PM's unmuted!`")


@javes05(outgoing=True, pattern="^\!allow$")
async def approvepm(apprvpm):    
    try:
        from userbot.modules.sql_helper.pm_permit_sql import approve
    except AttributeError:
        await apprvpm.edit("`Running `")
        return
    if apprvpm.reply_to_msg_id:
        reply = await apprvpm.get_reply_message()
        ruser = await apprvpm.client.get_entity(reply.from_id)
        aname = ruser.id
        name0 = str(ruser.first_name)
        uid = ruser.id
    else:
        aname = await apprvpm.client.get_entity(apprvpm.chat_id)
        name0 = str(aname.first_name)
        uid = apprvpm.chat_id
    try:
        approve(uid)
    except IntegrityError:
        await apprvpm.edit("You allowed to pm!")
        return
    await apprvpm.edit(f"[{name0}](tg://user?id={uid}) `approved to PM!`")
    async for message in apprvpm.client.iter_messages(apprvpm.chat_id,
                                                      from_user='me',
                                                      search=UNAPPROVED_MSG):
        await message.delete()
    if BOTLOG:
        await apprvpm.client.send_message(
            BOTLOG_CHATID,
            "#APPROVED\n" + "User: " + f"[{name0}](tg://user?id={uid})",
        )


@javes05(outgoing=True, pattern="^\!disallow$")
async def disapprovepm(disapprvpm):
    try:
        from userbot.modules.sql_helper.pm_permit_sql import dissprove
    except BaseException:
        await disapprvpm.edit("`Running on Non-SQL mode!`")
        return
    if disapprvpm.reply_to_msg_id:
        reply = await disapprvpm.get_reply_message()
        ruser = await disapprvpm.client.get_entity(reply.from_id)
        aname = ruser.id
        name0 = str(ruser.first_name)
        dissprove(ruser.id)
    else:
        dissprove(disapprvpm.chat_id)
        aname = await disapprvpm.client.get_entity(disapprvpm.chat_id)
        name0 = str(aname.first_name)
    await disapprvpm.edit(
        f"[{name0}](tg://user?id={disapprvpm.chat_id}) ` Disaproved to PM!`")
    if BOTLOG:
        await disapprvpm.client.send_message(
            BOTLOG_CHATID,
            f"[{name0}](tg://user?id={disapprvpm.chat_id})"
            " was disapproved to PM you.",
        )


@javes05(outgoing=True, pattern="^\!block$")
async def blockpm(block):
    """ For .block command, block people from PMing you! """
    if block.reply_to_msg_id:
        reply = await block.get_reply_message()
        ruser = await block.client.get_entity(reply.from_id)
        aname = ruser.id
        name0 = str(ruser.first_name)
        await block.client(BlockRequest(ruser.id))
        await block.edit(f"`{JAVES_NNAME}: You've been blocked!`")
        uid = ruser.id
    else:
        await block.client(BlockRequest(block.chat_id))
        aname = await block.client.get_entity(block.chat_id)
        await block.edit(f"`{JAVES_NNAME}: You've been blocked!`")
        name0 = str(aname.first_name)
        uid = block.chat_id
    try:
        from userbot.modules.sql_helper.pm_permit_sql import dissprove
        dissprove(uid)
    except AttributeError:
        pass

    if BOTLOG:
        await block.client.send_message(
            BOTLOG_CHATID,
            "#BLOCKED\n" + "User: " + f"[{name0}](tg://user?id={uid})",
        )


@javes05(outgoing=True, pattern="^\!unblock$")
async def unblockpm(unblock):
    """ For .unblock command, let people PMing you again! """
    if unblock.reply_to_msg_id:
        reply = await unblock.get_reply_message()
        ruser = await unblock.client.get_entity(reply.from_id)
        name0 = str(ruser.first_name)
        await unblock.client(UnblockRequest(ruser.id))
        await unblock.edit(f"`{JAVES_NNAME}: You have been unblocked.`")
    if BOTLOG:
        await unblock.client.send_message(
            BOTLOG_CHATID,
            f"[{name0}](tg://user?id={ruser.id})"
            " was unblocked!.",
        )



try:
    from userbot.modules.sql_helper.globals import gvarstatus, addgvar, delgvar
    afk_db = True
except AttributeError:
    afk_db = False
AFKSTR = [f"`{JAVES_NNAME}:` ** {AFK_MMSG} **"]
global USER_AFK  
global afk_time  
global afk_start
global afk_end
USER_AFK = {}
afk_time = None
afk_start = {}


@javes05(outgoing=True, pattern="^!afk(?: |$)(.*)", disable_errors=True)
async def set_afk(afk_e):    
    message = afk_e.text
    string = afk_e.pattern_match.group(1)
    global ISAFK
    global AFKREASON
    global USER_AFK  
    global afk_time  
    global afk_start
    global afk_end
    global reason
    USER_AFK = {}
    afk_time = None
    afk_end = {}
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    if string:
        AFKREASON = string
        await afk_e.edit(f"Going To Afk!\
        \nReason: `{string}`")
    else:
        await afk_e.edit("Going To Afk!")
    if BOTLOG:
        await afk_e.client.send_message(BOTLOG_CHATID, "#AFK\nYou went AFK!")
    ISAFK = True
    afk_time = datetime.now()  
    raise StopPropagation


@javes05(outgoing=True)
async def type_afk_is_not_true(notafk):    
  global ISAFK
  if ISAFK:
    global COUNT_MSG
    global USERS
    global AFKREASON
    global USER_AFK  
    global afk_time  
    global afk_start
    global afk_end
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)
    if ISAFK:
        ISAFK = False
        msg = await notafk.respond("I'm no longer AFK.")
        time.sleep(3)
        await msg.delete()
        if BOTLOG:
            await notafk.client.send_message(
                BOTLOG_CHATID,
                "You've recieved " + str(COUNT_MSG) + " messages from " +
                str(len(USERS)) + " chats while you were away",
            )
            for i in USERS:
                name = await notafk.client.get_entity(i)
                name0 = str(name.first_name)
                await notafk.client.send_message(
                    BOTLOG_CHATID,
                    "[" + name0 + "](tg://user?id=" + str(i) + ")" +
                    " sent you " + "`" + str(USERS[i]) + " messages`",
                )
        COUNT_MSG = 0
        USERS = {}
        AFKREASON = None


@javes05(incoming=True, disable_edited=True)
async def mention_afk(mention):
 global ISAFK
 if ISAFK:
  if not mention.chat_id in W_CHAT:   
    global COUNT_MSG
    global USERS    
    global USER_AFK  
    global afk_time  
    global afk_start
    global afk_end
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    afk_since = "a while ago"
    if mention.message.mentioned and not (await mention.get_sender()).bot:        
            now = datetime.now()
            datime_since_afk = now - afk_time  # pylint:disable=E0602
            time = float(datime_since_afk.seconds)
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                afk_since = "Yesterday"
            elif days > 1:
                if days > 6:
                    date = now + \
                        datet.timedelta(
                            days=-days, hours=-hours, minutes=-minutes)
                    afk_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datet.timedelta(days=-days)
                    afk_since = wday.strftime('%A')
            elif hours > 1:
                afk_since = f" {int(hours)}h {int(minutes)}m ago"
            elif minutes > 0:
                afk_since = f"{int(minutes)}m {int(seconds)}s ago"
            else:   
                afk_since = f"{int(seconds)}s ago"
            if mention.sender_id not in USERS:
                if AFKREASON:
                    await mention.reply(f"`{JAVES_NNAME}:`**{AFK_MMSG}**\
                    \n\n`Reason:` **{AFKREASON}**\n`Since :` **{afk_since}**")
                else:
                    await mention.reply(str(choice(AFKSTR)))
                USERS.update({mention.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif mention.sender_id in USERS:
                if USERS[mention.sender_id] % randint(2, 4) == 0:
                    if AFKREASON:
                        await mention.reply(
                            f"`{JAVES_NNAME}: ` **In case you didn't notice,  My master Still Offline**\
                        \n\n`Reason:` **{AFKREASON}**\n`Since :` **{afk_since}**")
                    else:
                        await mention.reply(str(choice(AFKSTR)))
                    USERS[mention.sender_id] = USERS[mention.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                else:
                    USERS[mention.sender_id] = USERS[mention.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1


@javes05(incoming=True, disable_errors=True)
async def afk_on_pm(sender):   
  global ISAFK
  if ISAFK:
    global USERS
    global COUNT_MSG
    global COUNT_MSG
    global USERS
    global USER_AFK  
    global afk_time  
    global afk_start
    global afk_end
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    afk_since = "a while ago"
    if sender.is_private and sender.sender_id != 710844948 and not (
            await sender.get_sender()).bot:
        if PM_AUTO_BAN:
            try:
                from userbot.modules.sql_helper.pm_permit_sql import is_approved
                apprv = is_approved(sender.sender_id)
            except AttributeError:
                apprv = True
        else:
            apprv = True
        if apprv and ISAFK:
            now = datetime.now()
            datime_since_afk = now - afk_time  # pylint:disable=E0602
            time = float(datime_since_afk.seconds)
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                afk_since = "Yesterday"
            elif days > 1:
                if days > 6:
                    date = now + \
                        datet.timedelta(
                            days=-days, hours=-hours, minutes=-minutes)
                    afk_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datet.timedelta(days=-days)
                    afk_since = wday.strftime('%A')
            elif hours > 1:
                afk_since = f"{int(hours)}h {int(minutes)}m ago"
            elif minutes > 0:
                afk_since = f"{int(minutes)}m {int(seconds)}s ago"
            else:
                afk_since = f"{int(seconds)}s ago"
            if sender.sender_id not in USERS:
                if AFKREASON:
                    await sender.reply(f"`{JAVES_NNAME}:`**{AFK_MMSG}**\
                    \n\n`Reason:` **{AFKREASON}**\n`Since :`**{afk_since}**")
                else:
                    await sender.reply(str(choice(AFKSTR)))
                USERS.update({sender.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif apprv and sender.sender_id in USERS:
                if USERS[sender.sender_id] % randint(2, 4) == 0:
                    if AFKREASON:
                        await sender.reply(
                            f"`{JAVES_NNAME}: ` **In case you didn't notice,  My master Still Offline**\
                        \n\n`Reason:` **{AFKREASON}**\n`Since :`**{afk_since}**")
                    else:
                        await sender.reply(str(choice(AFKSTR)))
                    USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                else:
                    USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1

@javes.on(rekcah05(pattern=f"userinfo(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^\!userinfo(?: |$)(.*)")
async def _(event):
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing`")
    else:
    	rkp = await event.edit("`processing`")  
    if event.fwd_from:
        return
    ruser, rdhs = await get_full_user(event)
    if ruser is None:
        await rkp.edit("Error please mention user")
        return False
    ruser_profile_photos = await event.client(GetUserPhotosRequest(
        user_id=ruser.user.id,
        offset=42,
        max_id=0,
        limit=80
    ))
    ruser_profile_photos_count = "f"
    try:
        ruser_profile_photos_count = ruser_profile_photos.count
    except AttributeError as e:
        pass
    user_id = ruser.user.id  
    first_name = html.escape(ruser.user.first_name)    
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")    
    user_bio = ruser.about
    if user_bio is not None:
        user_bio = html.escape(ruser.about)
    spamw =  "[Add Apikey](https://t.me/javes05/157)" ; sreason = {}
    try:
       cas_url = f"https://api.cas.chat/check?user_id={user_id}"
       r = get(cas_url, timeout=3)
       data = r.json()
    except BaseException:    
    	pass
    spambot = data = None
    if data:
        if data and data['ok']:
           reason = f"[Banned by Combot Anti Spam](https://combot.org/cas/query?u={check_user.id})"
           spambot = True      
    if spambot:
         sbot = "Yes"
         sn = reason
    else:
         sbot = "No"
         sn = {}                      
    if swapi:
        sw = spamwatch.Client(swapi)        
        sswatch = sw.get_ban(user_id) 
        if sswatch:
            spamw = "`Yes`"
            sreason = sswatch.reason
        else:
            spamw = "`No`"
            sreason = {}
    try:
        dc_id, location = get_input_location(ruser.profile_photo)
    except Exception as e:
        dc_id = "Need a Profile Picture to check **this**"
        location = str(e)    
    caption = """**About** [{}](tg://user?id={})
    
** User ID:** `{}`
** First Name:** `{}`
** Last Name:** `{}`
** UserName:** `@{}`
** Bio:** `{}`
** Number of Profile Pics:** `{}`
** Scam:** `{}`
** Restricted:** `{}`
 **Reason:** `{}`
** Banned in SpamWatch:** {}
** Reason:** `{}`
** Banned in CAS:** {} [?](http://cas.chat)
** Reason:** `{}`
** Verified by Telegram:** `{}`
** Bot** `{}`
** Deleted:** `{}`

""".format(
        first_name, user_id,
        user_id,
        ruser.user.first_name, ruser.user.last_name,
        ruser.user.username,
        user_bio,
        ruser_profile_photos_count,
        ruser.user.scam,
        ruser.user.restricted,
        ruser.user.restriction_reason,
        spamw,
        sreason,
        sbot,
        sn,
        ruser.user.verified,
        ruser.user.bot,
        ruser.user.contact,
        ruser.user.deleted
        
    )  
    await rkp.edit (caption)





@javes05(pattern="^\!whois(?: |$)(.*)", outgoing=True)
@javes.on(rekcah05(pattern=f"whois(?: |$)(.*)", allow_sudo=True))
async def who(event):
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing`")
    else:
    	rkp = await event.edit("`processing`")   
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    ruser = await get_user(event)
    try:
        photo, caption = await fetch_info(ruser, event)
    except AttributeError:
        rkp.edit("`Could not fetch info of that user.`")
        return
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(event.chat_id,
                                     photo,
                                     caption=caption,
                                     link_preview=False,
                                     force_document=False,
                                     reply_to=message_id_to_reply,
                                     parse_mode="html")
        if not photo.startswith("http"):
            os.remove(photo)
        await rkp.delete()
    except TypeError:
        await event.edit(caption, parse_mode="html")
async def get_user(event):    
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        previous_message = await event.get_reply_message()
        ruser = await event.client(
            GetFullUserRequest(previous_message.from_id))
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                ruser = await event.client(GetFullUserRequest(user_id))
                return ruser
        try:
            user_object = await event.client.get_entity(user)
            ruser = await event.client(
                GetFullUserRequest(user_object.id))
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return ruser
async def fetch_info(ruser, event):
    ruser_profile_photos = await event.client(
        GetUserPhotosRequest(user_id=ruser.user.id,
                             offset=42,
                             max_id=0,
                             limit=80))
    ruser_profile_photos_count = "Person needs help with uploading profile picture."
    try:
        ruser_profile_photos_count = ruser_profile_photos.count
    except AttributeError as e:
        pass
    user_id = ruser.user.id
    first_name = ruser.user.first_name
    last_name = ruser.user.last_name
    try:
        dc_id, location = get_input_location(ruser.profile_photo)
    except Exception as e:
        dc_id = "Couldn't fetch DC ID!"
        location = str(e)
    common_chat = ruser.common_chats_count
    username = ruser.user.username
    user_bio = ruser.about
    is_bot = ruser.user.bot
    restricted = ruser.user.restricted
    verified = ruser.user.verified
    photo = await event.client.download_profile_photo(user_id,
                                                      TEMP_DOWNLOAD_DIRECTORY +
                                                      str(user_id) + ".jpg",
                                                      download_big=True)
    first_name = first_name.replace(
        "\u2060", "") if first_name else ("This User has no First Name")
    last_name = last_name.replace(
        "\u2060", "") if last_name else ("This User has no Last Name")
    username = "@{}".format(username) if username else (
        "This User has no Username")
    user_bio = "This User has no About" if not user_bio else user_bio
    caption = "<b>USER INFO:</b>\n\n"
    caption += f"First Name: {first_name}\n"
    caption += f"Last Name: {last_name}\n"
    caption += f"Username: {username}\n"
    caption += f"Data Centre ID: {dc_id}\n"
    caption += f"Number of Profile Pics: {ruser_profile_photos_count}\n"
    caption += f"Is Bot: {is_bot}\n"
    caption += f"Is Restricted: {restricted}\n"
    caption += f"Is Verified by Telegram: {verified}\n"
    caption += f"ID: <code>{user_id}</code>\n\n"
    caption += f"Bio: \n<code>{user_bio}</code>\n\n"
    caption += f"Common Chats with this user: {common_chat}\n"
    caption += f"<a href=\"tg://user?id={user_id}\">{first_name}</a>"    
    return photo, caption



@javes05(outgoing=True, pattern="^\!purge$")
@javes.on(rekcah05(pattern=f"purge$", allow_sudo=True))
async def fastpurger(purg):   
    chat = await purg.get_input_chat()
    msgs = []
    itermsg = purg.client.iter_messages(chat, min_id=purg.reply_to_msg_id)
    count = 0
    if purg.reply_to_msg_id is not None:
        async for msg in itermsg:
            msgs.append(msg)
            count = count + 1
            msgs.append(purg.reply_to_msg_id)
            if len(msgs) == 100:
                await purg.client.delete_messages(chat, msgs)
                msgs = []
    else:
        await purg.reply("`I need a mesasge to start purging from.`")
        return
    if msgs:
        await purg.client.delete_messages(chat, msgs)
    done = await purg.client.send_message(
        purg.chat_id, f"`Fast purge complete!`\
        \nPurged {str(count)} messages")
    return

@javes05(outgoing=True, pattern="^\!purgeme")
@javes.on(rekcah05(pattern=f"purgeme", allow_sudo=True))
async def purgeme(delme):    
    message = delme.text
    count = int(message[9:])
    i = 1
    async for message in delme.client.iter_messages(delme.chat_id,
                                                    from_user='me'):
        if i > count + 1:
            break
        i = i + 1
        await message.delete()
    smsg = await delme.client.send_message(
        delme.chat_id,
        "`Purge complete!` Purged " + str(count) + " messages.",
    )
    return


@javes05(outgoing=True, pattern="^\!del$")
@javes.on(rekcah05(pattern=f"del$", allow_sudo=True))
async def delete_it(delme):    
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await msg_src.delete()
            await delme.delete()
            return
        except rpcbaseerrors.BadRequestError:
            return

@javes05(outgoing=True, pattern="^\!edit")
async def editer(edit):    
    message = edit.text
    chat = await edit.get_input_chat()
    self_id = await edit.client.get_peer_id('me')
    string = str(message[6:])
    i = 1
    async for message in edit.client.iter_messages(chat, self_id):
        if i == 2:
            await message.edit(string)
            await edit.delete()
            break
        i = i + 1
    if BOTLOG:
        await edit.client.send_message(BOTLOG_CHATID,
                                       "Edit query was executed successfully")


@javes05(outgoing=True, pattern="^\!sd")
async def selfdestruct(destroy):
    message = destroy.text
    counter = int(message[4:6])
    text = str(destroy.text[6:])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(counter)
    await smsg.delete()
    return



CMD_HELP.update({
    "person":
    "**         pm protecter**\
\n**Usage:** protect your pm from unknown scammers\
\nFor on !set var PM_PROTECTOR True For off !del var PM_PROTECTOR\
\n\n!allow <reply to a user>\
\n**Usage:** Approves the mentioned/replied person to PM...\
\n\n!disallow <reply to a user>\
\n**Usage:** Disapproves the mentioned/replied person to PM. \
\n\n!block <reply to a user>\
\n**Usage:** Blocks the person. \
\n\n!unblock <reply to a user>\
\n**Usage:** UnBlocks the person.. \
\n\n!notifoff \
\n**Usage:** Clears/Disables any notifications of unapproved PMs. \
\n\n!notifon \
\n**Usage:** Allows notifications for unapproved PMs. \
\n\n     **AFK**\
\n\n!afk <reason>\
\n**Usage:** Sets you as afk.\nReplies to anyone who tags/PM's you telling them that you are AFK(reason).\nSwitches off AFK when you type back anything, anywhere.\
\n\n!purge \
\n**Usage:** Purges all messages starting from the reply. \
\n\n!purgeme \
\n**Usage:** Deletes x amount of your latest messages.. \
\n\n!del \
\n**Usage:** Deletes the message you replied to. \
\n\n!edit <newmessage>\
\n**Usage:** Replace your last message with <newmessage>. \
\n\n!sd <x> <message> \
\n**Usage:** Creates a message that selfdestructs in x seconds. \
\n\n!userinfo / !whois <user/reply to a message> \
\n**Usage:** get userinfo. \
\n\n**Sudo Commands purge, purgeme , del, userinfo whois**\
"
})








