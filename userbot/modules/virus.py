
#telegram javes05

import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.events import javes05, rekcah05
import json, os
a = 0
try:
  from virustotal_python import Virustotal ; a = 1
except:
  a = 2 ; pass
Vapi = os.environ.get("VTOTAL_API", None)
from userbot import CMD_HELP, ALIVE_NAME, PM_MESSAGE, JAVES_NAME, JAVES_MSG, ORI_MSG, bot, TEMP_DOWNLOAD_DIRECTORY, BOTLOG, BOTLOG_CHATID
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)
javes = bot
from pathlib import Path

import json, os, subprocess, time, math, asyncio
from pySmartDL import SmartDL
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.tl.types import DocumentAttributeVideo
from userbot import LOGS, CMD_HELP, TEMP_DOWNLOAD_DIRECTORY

text = "scanning"

async def progress(current, total, event, start, type_of_ps, file_name=None):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "[{0}{1}] {2}%\n".format(
            ''.join(["█" for i in range(math.floor(percentage / 10))]),
            ''.join(["░" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2))
        tmp = progress_str + \
            "{0} of {1}\nETA: {2}".format(
                humanbytes(current),
                humanbytes(total),
                time_formatter(estimated_total_time)
            )
        if file_name:
            await event.edit("{}\nFile Name: `{}`\n{}".format(
                type_of_ps, file_name, tmp))
        else:
            await event.edit("{}\n{}".format(type_of_ps, tmp))
            
def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def time_formatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " day(s), ") if days else "") + \
        ((str(hours) + " hour(s), ") if hours else "") + \
        ((str(minutes) + " minute(s), ") if minutes else "") + \
        ((str(seconds) + " second(s), ") if seconds else "") + \
        ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    return tmp[:-2]




@javes05(pattern=r"^\!scan(?: |$)(.*)", outgoing=True)
async def vt(event):
    await event.edit(f"Analyzing Datas......")
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if "|" in input_str:
        url, file_name = input_str.split("|")
        url = url.strip()      
        file_name = file_name.strip()
        head, tail = os.path.split(file_name)
        if head:
            if not os.path.isdir(os.path.join(TEMP_DOWNLOAD_DIRECTORY, head)):
                os.makedirs(os.path.join(TEMP_DOWNLOAD_DIRECTORY, head))
                file_name = os.path.join(head, tail)
        downloaded_file_name = TEMP_DOWNLOAD_DIRECTORY + "" + file_name
        downloader = SmartDL(url, downloaded_file_name, progress_bar=False)
        downloader.start(blocking=False)
        c_time = time.time()
        display_message = None
        while not downloader.isFinished():
            status = downloader.get_status().capitalize()
            total_length = downloader.filesize if downloader.filesize else None
            downloaded = downloader.get_dl_size()
            now = time.time()
            diff = now - c_time
            percentage = downloader.get_progress() * 100
            speed = downloader.get_speed()
            elapsed_time = round(diff) * 1000
            progress_str = "[{0}{1}] {2}%".format(
                ''.join(["█" for i in range(math.floor(percentage / 10))]),
                ''.join(["░"
                         for i in range(10 - math.floor(percentage / 10))]),
                round(percentage, 2))
            estimated_total_time = downloader.get_eta(human=True)
            try:
                current_message = f"{status}..\
                \nURL: {url}\
                \nFile Name: {file_name}\
                \n{progress_str}\
                \n{humanbytes(downloaded)} of {humanbytes(total_length)}\
                \nETA: {estimated_total_time}"

                if round(diff %
                         10.00) == 0 and current_message != display_message:
                    await event.edit(current_message)
                    display_message = current_message
            except Exception as e:
                LOGS.info(str(e))
        if downloader.isSuccessful():
            await event.edit(f"{text} \n\nDownloaded  successfully !!")
        else:
            await event.edit("Incorrect URL\n{}".format(url))
    elif event.reply_to_msg_id:
        try:
            c_time = time.time()
            downloaded_file_name = await event.client.download_media(
                await event.get_reply_message(),
                TEMP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop(
                ).create_task(
                    progress(d, t, event, c_time, f"{text} \n\nDownloading...")))
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
        else:
            await event.edit(f"{text} \n\nDownloaded successfully !!")
    else:
        return await event.edit(f"Error\n`Reply to a file to scan.`")
    await event.edit(" `Scanning......`")
    vscan = downloaded_file_name
    if a ==2:
		      return await event.edit("`You need to Update Javes to use this command.......`")
    if not vscan:
		     return await event.edit("`Unknown command type !help virus_scan for more info`")            
    try:
         vtotal = Virustotal(Vapi)
    except:
          return await event.edit("Failed to connect virus total , is api key added? type `!help virus_scan` for more info")
    try:
      vr = vtotal.file_scan(vscan)
    except:
      return await event.edit("`Unknown command type !help virus_scan for more info")            
    test = vr['json_resp'] ; link = test['permalink'] ; scan_id = test['scan_id'] ; response_code = test['response_code']
    return await event.edit(""                 
                    f"• **Virus Total Response Code:** `{response_code}`\n"                                 
                    f"• **Scan Results:** [ClickHere]({link}) ")
                    
                    
                    
                    

@javes.on(rekcah05(pattern=f"scan(?: |$)(.*)", allow_sudo=True))
async def vt(event):
    rkp = await event.reply(f"Analyzing Datas......")
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if "|" in input_str:
        url, file_name = input_str.split("|")
        url = url.strip()      
        file_name = file_name.strip()
        head, tail = os.path.split(file_name)
        if head:
            if not os.path.isdir(os.path.join(TEMP_DOWNLOAD_DIRECTORY, head)):
                os.makedirs(os.path.join(TEMP_DOWNLOAD_DIRECTORY, head))
                file_name = os.path.join(head, tail)
        downloaded_file_name = TEMP_DOWNLOAD_DIRECTORY + "" + file_name
        downloader = SmartDL(url, downloaded_file_name, progress_bar=False)
        downloader.start(blocking=False)
        c_time = time.time()
        display_message = None
        while not downloader.isFinished():
            status = downloader.get_status().capitalize()
            total_length = downloader.filesize if downloader.filesize else None
            downloaded = downloader.get_dl_size()
            now = time.time()
            diff = now - c_time
            percentage = downloader.get_progress() * 100
            speed = downloader.get_speed()
            elapsed_time = round(diff) * 1000
            progress_str = "[{0}{1}] {2}%".format(
                ''.join(["█" for i in range(math.floor(percentage / 10))]),
                ''.join(["░"
                         for i in range(10 - math.floor(percentage / 10))]),
                round(percentage, 2))
            estimated_total_time = downloader.get_eta(human=True)
            try:
                current_message = f"{status}..\
                \nURL: {url}\
                \nFile Name: {file_name}\
                \n{progress_str}\
                \n{humanbytes(downloaded)} of {humanbytes(total_length)}\
                \nETA: {estimated_total_time}"

                if round(diff %
                         10.00) == 0 and current_message != display_message:
                    await rkp.edit(current_message)
                    display_message = current_message
            except Exception as e:
                LOGS.info(str(e))
        if downloader.isSuccessful():
            await rkp.edit(f"{text} \n\nDownloaded  successfully !!")
        else:
            await rkp.edit("Incorrect URL\n{}".format(url))
    elif event.reply_to_msg_id:
        try:
            c_time = time.time()
            downloaded_file_name = await event.client.download_media(
                await event.get_reply_message(),
                TEMP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop(
                ).create_task(
                    progress(d, t, event, c_time, f"{text} \n\nDownloading...")))
        except Exception as e:  # pylint:disable=C0103,W0703
            await rkp.edit(str(e))
        else:
            await rkp.edit(f"{text} \n\nDownloaded successfully !!")
    else:
        return await rkp.edit(f"Error\n`Reply to a file to scan.`")
    await rkp.edit(" `Scanning......`")
    vscan = downloaded_file_name
    if a ==2:
		      return await rkp.edit("`You need to Update Javes to use this command.......`")
    if not vscan:
		     return await rkp.edit("`Unknown command type !help virus_scan for more info`")            
    try:
         vtotal = Virustotal(Vapi)
    except:
          return await rkp.edit("Failed to connect virus total , is api key added? type `!help virus_scan` for more info")
    try:
      vr = vtotal.file_scan(vscan)
    except:
      return await rkp.edit("`Unknown command type !help virus_scan for more info")            
    test = vr['json_resp'] ; link = test['permalink'] ; scan_id = test['scan_id'] ; response_code = test['response_code']
    return await rkp.edit(""                 
                    f"• **Virus Total Response Code:** `{response_code}`\n"                                 
                    f"• **Scan Results:** [ClickHere]({link}) ")
                    
                    
                    
                    
                    

@javes05(outgoing=True, pattern="^!scan2(?: |$)(.*)")
async def _(event):
    reply_message = await event.get_reply_message() 
    if not reply_message or not event.reply_to_msg_id or not reply_message.media or not reply_message.media:
       return await event.edit("```Reply to a media message```")
    chat = "@DrWebBot"
    sender = reply_message.sender
    await event.edit(" `Scanning......`")
    async with bot.conversation(chat) as conv:
          try:        
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=161163358))                   
              await conv.send_message(reply_message)
              song2 = await conv.get_response()
              return await event.edit(f"**{JAVES_NNAME}:**  {song2.message}")
          except:      
              return await event.reply(f"Please unblock @DrWebBot and try again")

@javes.on(rekcah05(pattern=f"scan2(?: |$)(.*)", allow_sudo=True))
async def _(event):
    reply_message = await event.get_reply_message() 
    if not reply_message or not event.reply_to_msg_id or not reply_message.media or not reply_message.media:
       return await event.reply("```Reply to a media message```")
    chat = "@DrWebBot"
    sender = reply_message.sender
    rkp = await event.reply(" `Scanning......`")
    async with bot.conversation(chat) as conv:
          try:        
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=161163358))                   
              await conv.send_message(reply_message)
              song2 = await conv.get_response()
              return await rkp.edit(f"**{JAVES_NNAME}:**  {song2.message}")
          except:      
              return await event.reply(f"Please unblock @DrWebBot and try again")

                                

@javes05(outgoing=True, pattern="^!uscan(?: |$)(.*)")
async def _(event):
       rksong = event.pattern_match.group(1)
       if not rksong:
            return await event.edit("`Give a link to scan.....`")
       await event.edit(" `Scanning url.........`")
       chat = "@DrWebBot"
       async with bot.conversation(chat) as conv: 
          try:        
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=161163358))                   
              await conv.send_message(rksong)
              song2 = await conv.get_response()
              return await event.edit(f"**{JAVES_NNAME}**:  {song2.message}")
          except : 
              return await event.reply("Please unblock @DrWebBot and try again")

                 
@javes.on(rekcah05(pattern=f"uscan(?: |$)(.*)", allow_sudo=True))
async def _(event):
       rksong = event.pattern_match.group(1)
       if not rksong:
            return await event.reply("`Give a link to scan.....`")
       rkp = await event.reply(" `Scanning url.........`")
       chat = "@DrWebBot"
       async with bot.conversation(chat) as conv: 
          try:        
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=161163358))                   
              await conv.send_message(rksong)
              song2 = await conv.get_response()
              return await rkp.edit(f"**{JAVES_NNAME}**:  {song2.message}")
          except : 
              return await event.reply("Please unblock @DrWebBot and try again")

                     



CMD_HELP.update({
    "virus_scan":
    "`!scan <file path>`\
\n**Example:** `!scan reply to a file` \
\n**Usage:** Scan file in https://www.virustotal.com/gui/\
\n\n`!scan2 <reply to a message>`\
\n**Usage:** scan the file\
\n`!uscan <url>`\
\n**Usage:** scan the url\
\n\n**All Commands Support Sudo type !help sudo fore more info**\
"
})
















    
    
    