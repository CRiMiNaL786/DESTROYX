

#Telegram javes05


import asyncio, time, io, math, os, logging, asyncio, shutil, re, subprocess, json
from datetime import datetime
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from base64 import b64decode
from pySmartDL import SmartDL
from telethon.tl.types import DocumentAttributeVideo, DocumentAttributeAudio
from userbot.javes_main.commands import progress, humanbytes, time_formatter, admin_cmd
from userbot import client, TEMP_DOWNLOAD_DIRECTORY, CMD_HELP, COUNTRY, TZ_NUMBER
thumb_image_path = TEMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"
from userbot.events import javes05, rekcah05, progress
javes = client
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
FULL_SUDO = os.environ.get("FULL_SUDO", None)
from telethon.tl import functions, types
from userbot import client, BOTLOG_CHATID, CMD_HELP, BOTLOG, BOTLOG_CHATID, YOUTUBE_API_KEY, TEMP_DOWNLOAD_DIRECTORY, CHROME_DRIVER, GOOGLE_CHROME_BIN, bot
from telethon.tl.functions.messages import GetHistoryRequest, CheckChatInviteRequest, GetFullChatRequest
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.errors import FloodWaitError
from bs4 import BeautifulSoup
from time import sleep
from html import unescape
from urllib.parse import quote_plus
from urllib.error import HTTPError
from telethon import events
from requests import get
from googleapiclient.errors import HttpError
from googletrans import LANGUAGES, Translator
from gtts import gTTS
from gtts.lang import tts_langs
from emoji import get_emoji_regexp
from youtube_dl import YoutubeDL
from youtube_dl.utils import (DownloadError, ContentTooShortError,
                              ExtractorError, GeoRestrictedError,
                              MaxDownloadsReached, PostProcessingError,
                              UnavailableVideoError, XAttrMetadataError)
from html import unescape
from re import findall
from asyncio import sleep
from datetime import datetime as dt
from pytz import country_names as c_n, country_timezones as c_tz, timezone as tz
def deEmojify(inputString):   
    return get_emoji_regexp().sub(u'', inputString)
from telethon.errors.rpcerrorlist import YouBlockedUserError
import random

CARBONLANG = "auto"
TRT_LANG = TTS_LANG = "en"


try:
   from youtubesearchpython import SearchVideos 
except:
	os.system("pip install pip install youtube-search-python")
	from youtubesearchpython import SearchVideos 
	pass

async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.reply("`This is a private channel/group or I am banned from there`")
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError) as err:
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info

async def get_tz(con):
    """ Get time zone of the given country. """
    if "(Uk)" in con:
        con = con.replace("Uk", "UK")
    if "(Us)" in con:
        con = con.replace("Us", "US")
    if " Of " in con:
        con = con.replace(" Of ", " of ")
    if "(Western)" in con:
        con = con.replace("(Western)", "(western)")
    if "Minor Outlying Islands" in con:
        con = con.replace("Minor Outlying Islands", "minor outlying islands")
    if "Nl" in con:
        con = con.replace("Nl", "NL")

    for c_code in c_n:
        if con == c_n[c_code]:
            return c_tz[c_code]
    try:
        if c_n[con]:
            return c_tz[con]
    except KeyError:
        return


def make_mention(user):
    if user.username:
        return f"@{user.username}"
    else:
        return inline_mention(user)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = ' '.join(names)
    return full_name
 





@javes05(outgoing=True, pattern="^!reupload (.*)")
@javes.on(rekcah05(pattern=f"reupload (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    thumb = None
    if os.path.exists(thumb_image_path):
        thumb = thumb_image_path    
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
    else:
    	rkp = await event.edit("`processing...`")
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        start = datetime.now()
        end = datetime.now()
        file_name = input_str
        reply_message = await event.get_reply_message()
        to_download_directory = TEMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await client.download_media(
            reply_message,
            downloaded_file_name,
            )
        ms_one = (end - start).seconds
        if os.path.exists(downloaded_file_name):
            c_time = time.time()
            await client.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=True,
                supports_streaming=False,
                allow_cache=False,
                reply_to=event.message.id,
                thumb=thumb,
                )
            end_two = datetime.now()
            os.remove(downloaded_file_name)
            ms_two = (end_two - end).seconds
            await rkp.edit("Downloaded in {} seconds. Uploaded in {} seconds.".format(ms_one, ms_two))
        else:
            await rkp.edit("File Not Found {}".format(input_str))
    else:
        await rkp.edit("Syntax // !reupload file.name as reply to a Telegram media")




@javes05(outgoing=True, pattern="^!search (.*)")
@javes.on(rekcah05(pattern=f"search (.*)", allow_sudo=True))
async def telethon_search(event):
 if event.is_private:
     return await rk.reply("`**Error! Permission Denied.**") 
 query = event.pattern_match.group(1)
 group = event.chat.title
 gr = (await client.get_entity(group))
 (await client.send_message(event.input_chat, f"**Search Query:** `{query}`\n\n**Results**\n\nMsg~> " + "\nMsg~> ".join(map(lambda x:f"[{x}](tg://privatepost?channel={gr.id}&post={x})", [msg.id for msg in await client.get_messages(group, search=query, limit=25) if msg.entities and [e for e in msg.entities if isinstance(e, (types.MessageEntityCode, types.MessageEntityPre))]])), link_preview=False, reply_to=event.reply_to_msg_id))
 await event.delete()



@javes.on(rekcah05(pattern=f"stats(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern=r"^!stats(?: |$)(.*)") 
async def stats(event: NewMessage.Event) -> None:  
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
    else:
    	rkp = await event.edit("`processing...`")
    if not sender.id == me.id and not FULL_SUDO:
       return await rkp.edit("`Sorry normal sudo users cant access this command..`")
    try:
       await e.delete()
    except:
    	pass    
    waiting_message = await rkp.edit('`Collecting.........`')
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    largest_group_member_count = 0
    largest_group_with_admin = 0
    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):           
            if entity.broadcast:
                broadcast_channels += 1
                if entity.creator or entity.admin_rights:
                    admin_in_broadcast_channels += 1
                if entity.creator:
                    creator_in_channels += 1
            elif entity.megagroup:
                groups += 1
                if entity.creator or entity.admin_rights:                    
                    admin_in_groups += 1
                if entity.creator:
                    creator_in_groups += 1
        elif isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1
        elif isinstance(entity, Chat):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1
        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    stop_time = time.time() - start_time
    full_name = inline_mention(await event.client.get_me())
    response = f' **Stats for {full_name}** \n\n'
    response += f'**Private Chats:** {private_chats} \n'
    response += f'   • `Users: {private_chats - bots}` \n'
    response += f'   • `Bots: {bots}` \n'
    response += f'**Groups:** {groups} \n'
    response += f'**Channels:** {broadcast_channels} \n'
    response += f'**Admin in Groups:** {admin_in_groups} \n'
    response += f'   • `Creator: {creator_in_groups}` \n'
    response += f'   • `Admin Rights: {admin_in_groups - creator_in_groups}` \n'
    response += f'**Admin in Channels:** {admin_in_broadcast_channels} \n'
    response += f'   • `Creator: {creator_in_channels}` \n'
    response += f'   • `Admin Rights: {admin_in_broadcast_channels - creator_in_channels}` \n'
    response += f'**Unread:** {unread} \n'
    response += f'**Unread Mentions:** {unread_mentions} \n\n'
    response += f'__It Took:__ {stop_time:.02f}s \n'
    await waiting_message.edit(response)










@javes05(pattern="!inviteall(?: |$)(.*)", outgoing=True)
@javes.on(rekcah05(pattern=f"inviteall(?: |$)(.*)", allow_sudo=True))
async def get_users(event):   
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
    else:
    	rkp = await event.edit("`processing...`")
    rk1 = await get_chatinfo(event) ; chat = await event.get_chat()
    if event.is_private:
              return await rkp.edit("`Sorry, Can add users here`")    
    s = 0 ; f = 0 ; error = 'None'   
  
    await rkp.edit("**TerminalStatus**\n\n`Collecting Users.......`")
    async for user in event.client.iter_participants(rk1.full_chat.id):
                try:
                    if error.startswith("Too"):
                        return await rkp.edit(f"**Terminal Finished With Error**\n(`May Got Limit Error from telethon Please try agin Later`)\n**Error** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people")
                    await event.client(functions.channels.InviteToChannelRequest(channel=chat,users=[user.id]))
                    s = s + 1                                                    
                    await rkp.edit(f"**Terminal Running...**\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people\n\n**× LastError:** `{error}`")                
                except Exception as e:
                    error = str(e) ; f = f + 1             
    return await rkp.edit(f"**Terminal Finished** \n\n• Successfully Invited `{s}` people \n• failed to invite `{f}` people")
    



@javes05(pattern="!inviteall2(?: |$)(.*)", outgoing=True)
async def get_users(event):   
    rk1 = await get_chatinfo(event) ; chat = await event.get_chat()
    if event.is_private:
              return await event.edit("`Sorry, Can add users here`")
    if not BOTLOG_CHATID:
	         return await event.edit (f"`Failed to Channed Bot log Chat \nPlease add bot log chat to use this`")
    s = 0 ; f = 0 ; error = 'None'   
    await event.delete()    
    test = "**TerminalStatus**\n\n`Collecting Users.......`"
    rkp = await client.send_message(BOTLOG_CHATID, test)
    async for user in event.client.iter_participants(rk1.full_chat.id):
                try:
                    if error.startswith("Too"):
                        return await rkp.edit(f"**Terminal Finished With Error**\n(`May Got Limit Error from telethon Please try agin Later`)\n**Error** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people")
                    await event.client(functions.channels.InviteToChannelRequest(channel=chat,users=[user.id]))
                    s = s + 1                                                    
                    await rkp.edit(f"**Terminal Running...**\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people\n\n**× LastError:** `{error}`")                
                except Exception as e:
                    error = str(e) ; f = f + 1             
    return await rkp.edit(f"**Terminal Finished** \n\n• Successfully Invited `{s}` people \n• failed to invite `{f}` people")
    
    
@javes05(outgoing=True, pattern="^!tagall$")
@javes.on(rekcah05(pattern=f"tagall$", allow_sudo=True))
async def _(event):
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
    else:
    	rkp = await event.edit("`processing...`")
    if event.is_private:
              return await rkp.edit("`Sorry, Can tag users here`")
    mentions = "@tagedall"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, 100):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()


@javes05(outgoing=True, pattern="^!crblang (.*)")
@javes.on(rekcah05(pattern=f"crblang (.*)", allow_sudo=True))
async def setlang(prog):
    try:
       await prog.delete()
    except:
       pass      
    global CARBONLANG
    CARBONLANG = prog.pattern_match.group(1)
    await prog.reply(f"Language for carbon.now.sh set to {CARBONLANG}")


 

 


 
@javes05(outgoing=True, pattern=r"^!tts2(?: |$)([\s\S]*)")
@javes.on(rekcah05(pattern=f"tts2(?: |$)([\s\S]*)", allow_sudo=True))
async def text_to_speech(query):    
    sender = await query.get_sender() ; me = await query.client.get_me()
    if not sender.id == me.id:
        rkp = await query.reply("`processing...`")
    else:
    	rkp = await query.edit("`processing...`")
    
    textx = await query.get_reply_message()
    message = query.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await rkp.edit(
            "`Give a text or reply to a message for Text-to-Speech!`")
 
    try:
        gTTS(message, lang=TTS_LANG)
    except AssertionError:
        return await rkp.edit(
            'The text is empty.\n'
            'Nothing left to speak after pre-precessing, tokenizing and cleaning.'
        )
    except ValueError:
        return await rkp.edit('Language is not supported.')
    except RuntimeError:
        return await rkp.edit('Error loading the languages dictionary.')
    tts = gTTS(message, lang=TTS_LANG)
    tts.save("tts.mp3")
    with open("tts.mp3", "rb") as audio:
        linelist = list(audio)
        linecount = len(linelist)
    if linecount == 1:
        tts = gTTS(message, lang=TTS_LANG)
        tts.save("tts.mp3")
    with open("tts.mp3", "r"):
        await query.client.send_file(query.chat_id, "tts.mp3", voice_note=True)
        os.remove("tts.mp3")
        return

@javes05(outgoing=True, pattern=r"^!trt(?: |$)([\s\S]*)")
@javes.on(rekcah05(pattern=f"trt(?: |$)([\s\S]*)", allow_sudo=True))
async def translateme(trans):   
    sender = await trans.get_sender() ; me = await trans.client.get_me()
    if not sender.id == me.id:
        rkp = await trans.reply("`processing...`")
    else:
    	rkp = await trans.edit("`processing...`")    
    translator = Translator()
    textx = await trans.get_reply_message()
    message = trans.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await rkp.edit("`Give a text or reply to a message to translate!`")
    try:
        reply_text = translator.translate(deEmojify(message), dest=TRT_LANG)
    except ValueError:
        return await rkp.edit("Invalid destination language.")
    source_lan = LANGUAGES[f'{reply_text.src.lower()}']
    transl_lan = LANGUAGES[f'{reply_text.dest.lower()}']
    reply_text = f"From **{source_lan.title()}**\nTo **{transl_lan.title()}:**\n\n{reply_text.text}" 
    return await rkp.edit(reply_text)
    
 
 
@javes05(pattern="!lang (trt|tts) (.*)", outgoing=True)
@javes.on(rekcah05(pattern=f"lang (trt|tts) (.*)", allow_sudo=True))
async def lang(value):
    sender = await value.get_sender() ; me = await value.client.get_me()
    if not sender.id == me.id:
        rkp = await value.reply("`processing...`")
    else:
    	rkp = await value.edit("`processing...`")    
    util = value.pattern_match.group(1).lower()
    if util == "trt":
        scraper = "Translator"
        global TRT_LANG
        arg = value.pattern_match.group(2).lower()
        if arg in LANGUAGES:
            TRT_LANG = arg
            LANG = LANGUAGES[arg]
        else:
            return await rkp.edit(
                f"`Invalid Language code !!`\n`Available language codes for TRT`:\n\n`{LANGUAGES}`"
            )
    elif util == "tts":
        scraper = "Text to Speech"
        global TTS_LANG
        arg = value.pattern_match.group(2).lower()
        if arg in tts_langs():
            TTS_LANG = arg
            LANG = tts_langs()[arg]
        else:
            return await rkp.edit(
                f"`Invalid Language code !!`\n`Available language codes for TTS`:\n\n`{tts_langs()}`"
            )
    return await rkp.edit(f"`Language for {scraper} changed to {LANG.title()}.`")
    





 
 
@javes05(outgoing=True, pattern=r"!get (audio|video) (.*)")
@javes.on(rekcah05(pattern=f"get (audio|video) (.*)", allow_sudo=True))
async def download_video(v_url):
    sender = await v_url.get_sender() ; me = await v_url.client.get_me()
    if not sender.id == me.id:
        rkp = await v_url.reply("`processing...`")
    else:
    	rkp = await v_url.edit("`processing...`")    
    url = v_url.pattern_match.group(2)
    type = v_url.pattern_match.group(1).lower()
    await rkp.edit("`Preparing to download...`")
    if type == "audio":
        opts = {
            'format':
            'bestaudio',
            'addmetadata':
            True,
            'key':
            'FFmpegMetadata',
            'writethumbnail':
            True,
            'prefer_ffmpeg':
            True,
            'geo_bypass':
            True,
            'nocheckcertificate':
            True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'outtmpl':
            '%(id)s.mp3',
            'quiet':
            True,
            'logtostderr':
            False
        }
        video = False
        song = True
 
    elif type == "video":
        opts = {
            'format':
            'best',
            'addmetadata':
            True,
            'key':
            'FFmpegMetadata',
            'prefer_ffmpeg':
            True,
            'geo_bypass':
            True,
            'nocheckcertificate':
            True,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }],
            'outtmpl':
            '%(id)s.mp4',
            'logtostderr':
            False,
            'quiet':
            True
        }
        song = False
        video = True
 
    try:
        await rkp.edit("`Fetching data, please wait..`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        return await rkp.edit(f"`{str(DE)}`")
    except ContentTooShortError:
        return await rkp.edit("`The download content was too short.`")
    except GeoRestrictedError:
        return await rkp.edit(
            "`Video is not available from your geographic location "
            "due to geographic restrictions imposed by a website.`"
        )
    except MaxDownloadsReached:
        return await rkp.edit("`Max-downloads limit has been reached.`")
    except PostProcessingError:
        return await rkp.edit("`There was an error during post processing....`")
    except UnavailableVideoError:
        return await rkp.edit("`Media is not available in the requested format.`")
    except XAttrMetadataError as XAME:
        return await rkp.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
    except ExtractorError:
        return await rkp.edit("`There was an error during info extraction.`")
    except Exception as e:
        return await rkp.edit(f"{str(type(e)): {str(e)}}")
    c_time = time.time()
    if song:
        await rkp.edit(
            f"`Preparing to upload audio:`\n**{rip_data['title']}**")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp3",
            supports_streaming=True,
            attributes=[
                DocumentAttributeAudio(duration=int(rip_data['duration']),
                                       title=str(rip_data['title']),
                                       performer=str(rip_data['uploader']))
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading..",
                         f"{rip_data['title']}.mp3")))
        os.remove(f"{rip_data['id']}.mp3")
        await v_url.delete()
    elif video:
        await rkp.edit(
            f"`Preparing to upload video:`\n**{rip_data['title']}**")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp4",
            supports_streaming=True,
            caption=rip_data['title'],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading..",
                         f"{rip_data['title']}.mp4")))
        os.remove(f"{rip_data['id']}.mp4")
        await v_url.delete()
 

@javes05(outgoing=True, pattern=r"^\!tts(?: |$)([\s\S]*)")
@javes.on(rekcah05(pattern=f"tts(?: |$)([\s\S]*)", allow_sudo=True))
async def _(event):
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
    else:
    	rkp = await event.edit("`processing...`")   
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str
    elif "|" in input_str:
        lan, text = input_str.split("|")        
    else:
        await rkp.edit("Error usage tts <langcode> <reply to a message>")
        return
    text = text.strip()
    lan = lan.strip()
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    required_file_name = TEMP_DOWNLOAD_DIRECTORY + "voice.tts"
    try:
        tts = gTTS(text, lang=lan)
        tts.save(required_file_name)
        command_to_execute = [
            "ffmpeg",
            "-i",
             required_file_name,
             "-map",
             "0:a",
             "-codec:a",
             "libopus",
             "-b:a",
             "100k",
             "-vbr",
             "on",
             required_file_name + ".opus"
        ]
        try:
            t_response = subprocess.check_output(command_to_execute, stderr=subprocess.STDOUT)
        except (subprocess.CalledProcessError, NameError, FileNotFoundError) as exc:
            await rkp.edit(str(exc))            
        else:
            os.remove(required_file_name)
            required_file_name = required_file_name + ".opus"
        end = datetime.now()
        ms = (end - start).seconds
        await bot.send_file( event.chat_id, required_file_name, reply_to=event.message.reply_to_msg_id, allow_cache=False, voice_note=True )
        os.remove(required_file_name)
        await rkp.edit("Processed {} ({}) in {} seconds!".format(text[0:97], lan, ms))
        await asyncio.sleep(5)
        await rkp.delete()
    except Exception as e:
        await rkp.edit(str(e))



@javes05(outgoing=True, pattern="^!time(?: |$)(.*)(?<![0-9])(?: |$)([0-9]+)?")
@javes.on(rekcah05(pattern=f"time(?: |$)(.*)(?<![0-9])(?: |$)([0-9]+)?", allow_sudo=True))
async def time_func(tdata):
    sender = await tdata.get_sender() ; me = await tdata.client.get_me()
    if not sender.id == me.id:
        rkp = await tdata.reply("`processing...`")
    else:
    	rkp = await tdata.edit("`processing...`")
    
    con = tdata.pattern_match.group(1).title()
    tz_num = tdata.pattern_match.group(2)
    t_form = "%H:%M"
    c_name = None
    if len(con) > 4:
        try:
            c_name = c_n[con]
        except KeyError:
            c_name = con
        timezones = await get_tz(con)
    elif COUNTRY:
        c_name = COUNTRY
        tz_num = TZ_NUMBER
        timezones = await get_tz(COUNTRY)
    else:
        await rkp.edit(f"`It's`  **{dt.now().strftime(t_form)}**  `here.`")
        return
    if not timezones:
        await rkp.edit("`Invaild country.`")
        return
    if len(timezones) == 1:
        time_zone = timezones[0]
    elif len(timezones) > 1:
        if tz_num:
            tz_num = int(tz_num)
            time_zone = timezones[tz_num - 1]
        else:
            return_str = f"`{c_name} has multiple timezones:`\n\n"
            for i, item in enumerate(timezones):
                return_str += f"`{i+1}. {item}`\n"
            return_str += "\n`Choose one by typing the number "
            return_str += "in the command.`\n"
            return_str += f"`Example: !time {c_name} 2`"
            await rkp.edit(return_str)
            return
    dtnow = dt.now(tz(time_zone)).strftime(t_form)
    if c_name != COUNTRY:
        await rkp.edit(
            f"`It's`  **{dtnow}**  `in {c_name}({time_zone} timezone).`")
        return
    elif COUNTRY:
        await rkp.edit(f"`It's`  **{dtnow}**  `here, in {COUNTRY}"
                         f"({time_zone} timezone).`")
        return


@javes05(outgoing=True, pattern="^!date(?: |$)(.*)(?<![0-9])(?: |$)([0-9]+)?")
@javes.on(rekcah05(pattern=f"date(?: |$)(.*)(?<![0-9])(?: |$)([0-9]+)?", allow_sudo=True))
async def date_func(dat):
    sender = await dat.get_sender() ; me = await dat.client.get_me()
    if not sender.id == me.id:
        rkp = await dat.reply("`processing...`")
    else:
    	rkp = await dat.edit("`processing...`")   
    con = dat.pattern_match.group(1).title()
    tz_num = dat.pattern_match.group(2)
    d_form = "%d/%m/%y - %A"
    c_name = ''
    if len(con) > 4:
        try:
            c_name = c_n[con]
        except KeyError:
            c_name = con
        timezones = await get_tz(con)
    elif COUNTRY:
        c_name = COUNTRY
        tz_num = TZ_NUMBER
        timezones = await get_tz(COUNTRY)
    else:
        await rkp.edit(f"`It's`  **{dt.now().strftime(d_form)}**  `here.`")
        return
    if not timezones:
        await rkp.edit("`Invaild country.`")
        return
    if len(timezones) == 1:
        time_zone = timezones[0]
    elif len(timezones) > 1:
        if tz_num:
            tz_num = int(tz_num)
            time_zone = timezones[tz_num - 1]
        else:
            return_str = f"`{c_name} has multiple timezones:`\n"
            for i, item in enumerate(timezones):
                return_str += f"`{i+1}. {item}`\n"
            return_str += "\n`Choose one by typing the number "
            return_str += "in the command.`\n"
            return_str += f"Example: !date {c_name} 2"
            await rkp.edit(return_str)
            return
    dtnow = dt.now(tz(time_zone)).strftime(d_form)
    if c_name != COUNTRY:
        await rkp.edit(
            f"`It's`  **{dtnow}**  `in {c_name}({time_zone} timezone).`")
        return
    elif COUNTRY:
        await rkp.edit(f"`It's`  **{dtnow}**  `here, in {COUNTRY}"
                       f"({time_zone} timezone).`")
        return


@javes05(outgoing=True, pattern="^!carbon ?(.*)")
@javes.on(rekcah05(pattern=f"carbon ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
    else:
    	rkp = await event.edit("`processing...`")   
    input_str = event.pattern_match.group(1)
    to_rip_mesg = event
    if event.reply_to_msg_id and (not input_str or input_str == "reply"):
        rep_mesg = await event.get_reply_message()
        input_str = rep_mesg.message
        to_rip_mesg = rep_mesg
    chat = "@CarbonNowShBot"
    chat_e = await event.client.get_entity(chat)
    await rkp.edit("creating a carbon")
    async with event.client.conversation(chat_e, timeout=180) as conv:
        try:
            await conv.send_message(input_str)
            response = await conv.wait_event(events.MessageEdited(
                incoming=True,
                from_users=chat_e.id
            ))          
            row = random.randint(0, 8)
            column = random.randint(0, 2)
            await response.click(row, column)
            response = await conv.wait_event(events.NewMessage(
                incoming=True,
                from_users=chat_e.id
            ))
            response_caption = response.message.message
            response_caption_sp = response_caption.split("\n")           
            response_caption = "\n".join(response_caption_sp[0:2])
            carbon_media = response.message.media
            await to_rip_mesg.reply(response_caption, file=carbon_media)          
            await rkp.delete()
        except YouBlockedUserError:
            await rkp.reply("Please unblock me (@CarbonNowShBot)")
            return


@javes.on(rekcah05(pattern=f"song (.*)", allow_sudo=True))
@javes05(outgoing=True, pattern=r"!song (.*)")
async def download_video(v_url):  
    lazy = v_url ; sender = await lazy.get_sender() ; me = await lazy.client.get_me()
    if not sender.id == me.id:
        rkp = await lazy.reply("`processing...`")
    else:
    	rkp = await lazy.edit("`processing...`")   
    url = v_url.pattern_match.group(1)
    if not url:
         return await rkp.edit("`Error \nusage song <song name>`")
    search = SearchVideos(url, offset = 1, mode = "json", max_results = 1)
    test = search.result()
    p = json.loads(test)
    q = p.get('search_result')
    try:
       url = q[0]['link']
    except:
    	return await rkp.edit("`failed to find`")
    type = "audio"
    await rkp.edit("`Preparing to download...`")
    if type == "audio":
        opts = {
            'format':
            'bestaudio',
            'addmetadata':
            True,
            'key':
            'FFmpegMetadata',
            'writethumbnail':
            True,
            'prefer_ffmpeg':
            True,
            'geo_bypass':
            True,
            'nocheckcertificate':
            True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'outtmpl':
            '%(id)s.mp3',
            'quiet':
            True,
            'logtostderr':
            False
        }
        video = False
        song = True    
    try:
        await rkp.edit("`Fetching data, please wait..`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await rkp.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await rkp.edit("`The download content was too short.`")
        return
    except GeoRestrictedError:
        await rkp.edit(
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`"
        )
        return
    except MaxDownloadsReached:
        await rkp.edit("`Max-downloads limit has been reached.`")
        return
    except PostProcessingError:
        await rkp.edit("`There was an error during post processing.`")
        return
    except UnavailableVideoError:
        await rkp.edit("`Media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        await rkp.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await rkp.edit("`There was an error during info extraction.`")
        return
    except Exception as e:
        await rkp.edit(f"{str(type(e)): {str(e)}}")
        return
    c_time = time.time()
    if song:
        await rkp.edit(f"`Preparing to upload song:`\
        \n**{rip_data['title']}**\
        \nby *{rip_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp3",
            supports_streaming=True,
            attributes=[
                DocumentAttributeAudio(duration=int(rip_data['duration']),
                                       title=str(rip_data['title']),
                                       performer=str(rip_data['uploader']))
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading..",
                         f"{rip_data['title']}.mp3")))
        os.remove(f"{rip_data['id']}.mp3")
        await v_url.delete()
    elif video:
        await rkp.edit(f"`Preparing to upload song :`\
        \n**{rip_data['title']}**\
        \nby *{rip_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp4",
            supports_streaming=True,
            caption=url,
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading..",
                         f"{rip_data['title']}.mp4")))
        os.remove(f"{rip_data['id']}.mp4")
        await rkp.delete()

@javes.on(rekcah05(pattern=f"vsong (.*)", allow_sudo=True))
@javes05(outgoing=True, pattern=r"!vsong (.*)")
async def download_video(v_url):  
    lazy = v_url ; sender = await lazy.get_sender() ; me = await lazy.client.get_me()
    if not sender.id == me.id:
        rkp = await lazy.reply("`processing...`")
    else:
    	rkp = await lazy.edit("`processing...`")   
    url = v_url.pattern_match.group(1)
    if not url:
         return await rkp.edit("`Error \nusage song <song name>`")
    search = SearchVideos(url, offset = 1, mode = "json", max_results = 1)
    test = search.result()
    p = json.loads(test)
    q = p.get('search_result')
    try:
       url = q[0]['link']
    except:
    	return await rkp.edit("`failed to find`")
    type = "audio"
    await rkp.edit("`Preparing to download...`")
    if type == "audio":
        opts = {
            'format':
            'best',
            'addmetadata':
            True,
            'key':
            'FFmpegMetadata',
            'prefer_ffmpeg':
            True,
            'geo_bypass':
            True,
            'nocheckcertificate':
            True,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }],
            'outtmpl':
            '%(id)s.mp4',
            'logtostderr':
            False,
            'quiet':
            True
        }
        song = False
        video = True
    try:
        await rkp.edit("`Fetching data, please wait..`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await rkp.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await rkp.edit("`The download content was too short.`")
        return
    except GeoRestrictedError:
        await rkp.edit(
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`"
        )
        return
    except MaxDownloadsReached:
        await rkp.edit("`Max-downloads limit has been reached.`")
        return
    except PostProcessingError:
        await rkp.edit("`There was an error during post processing.`")
        return
    except UnavailableVideoError:
        await rkp.edit("`Media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        await rkp.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await rkp.edit("`There was an error during info extraction.`")
        return
    except Exception as e:
        await rkp.edit(f"{str(type(e)): {str(e)}}")
        return
    c_time = time.time()
    if song:
        await rkp.edit(f"`Preparing to upload song `\
        \n**{rip_data['title']}**\
        \nby *{rip_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp3",
            supports_streaming=True,
            attributes=[
                DocumentAttributeAudio(duration=int(rip_data['duration']),
                                       title=str(rip_data['title']),
                                       performer=str(rip_data['uploader']))
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading..",
                         f"{rip_data['title']}.mp3")))
        os.remove(f"{rip_data['id']}.mp3")
        await v_url.delete()
    elif video:
        await rkp.edit(f"`Preparing to upload video song :`\
        \n**{rip_data['title']}**\
        \nby *{rip_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp4",
            supports_streaming=True,
            caption=rip_data['title'],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading..",
                         f"{rip_data['title']}.mp4")))
        os.remove(f"{rip_data['id']}.mp4")
        await rkp.delete()





CMD_HELP.update({
    "tools":
    "`!reupload <customname>`\
\n**Usage:** Reply to a media / video / photo to reupload with your custom name\
\n\n`!search <keyword>`\
\n**Usage:** Search given keyword in group and give results\
\n\n`!stats `\
\n**Usage:** Command to get stats about your account\
\n\n`!carbon <text>`\
\n**Usage:** Beautify your text\
\n\n`!inviteall <chatusername/chatid>`\
\n**Usage:** Invite all the members to current chat from given group/channel\
\n\n`!tagall`\
\n**Usage:** Tag all people in group\
\n\n`!tts2 <text> (or reply) **or** `!tts` <langcode> <reply to a media>`\
\n**Usage:** Translates text to speech for the language which is set.\n`!lang tts <language code>` to set language for trt. (Default is English)\
\n\n`!trt <text> (or reply)` \
\n**Usage:** Translates text to the language which is set..\n`!lang trt <language code>` to set language for trt. (Default is English)\
\n\n`!get video <url> or get audio <url>`\
\n**Usage:** Download video or audio from YouTube , facebook, Yahoo , [many other sites](https://ytdl-org.github.io/youtube-dl/supportedsites.html)\
\n\n`!time <country name/code> <timezone number>`\
\n**Usage:** Get the time of a country. If a country has multiple timezones it will list all of them and let you select one.\
\n\n`!date <country name/code> <timezone number>`\
\n**Usage:** Get the date of a country. \
\n\n**All Commands Support Sudo type !help sudo fore more info**\
"
})







