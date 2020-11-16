"""Rename Telegram Files
Syntax:
.rename file.name
.rnupload file.name
.rnstreamupload file.name
By @Ck_ATR"""
from userbot import bot as javes
import aiohttp
import asyncio
from datetime import datetime
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
import json
import os
import requests
import subprocess
from telethon import events
from telethon.tl.types import DocumentAttributeVideo
from telethon.errors import MessageNotModifiedError
import time
from userbot.utils import progress, humanbytes, time_formatter, admin_cmd
import io
import math
import os
from pySmartDL import SmartDL
from userbot.javes_main.heroku_var import *
config=Config

thumb_image_path = Config.TEMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpeg"


@javes.on(admin_cmd("pti (.*)"))
async def _(event):
    if event.fwd_from:
        return
    thumb = None
    if os.path.exists(thumb_image_path):
        thumb = thumb_image_path
    await event.edit("Rename & Upload in process 🙄🙇‍♂️🙇‍♂️🙇‍♀️ It might take some time if file size is big")
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(Config.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TEMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        start = datetime.now()
        file_name = input_str + ".ico"
        reply_message = await event.get_reply_message()
        to_download_directory = Config.TEMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await javes.download_media(
            reply_message,
            downloaded_file_name
        )
        end = datetime.now()
        ms_one = (end - start).seconds
        if os.path.exists(downloaded_file_name):
            c_time = time.time()
            await javes.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=False,
                supports_streaming=False,
                allow_cache=False,
                reply_to=event.message.id,
                thumb=thumb,
                
            )
            end_two = datetime.now()
            os.remove(downloaded_file_name)
            ms_two = (end_two - end).seconds
            await event.edit("Downloaded in {} seconds. Uploaded in {} seconds.".format(ms_one, ms_two))
        else:
            await event.edit("File Not Found {}".format(input_str))
    else:
        await event.edit("Syntax // .pti<name>  as reply to a photo")
        
@javes.on(admin_cmd("pts (.*)"))
async def _(event):
    if event.fwd_from:
        return
    thumb = None
    if os.path.exists(thumb_image_path):
        thumb = thumb_image_path
    await event.edit("Rename & Upload in process 🙄🙇‍♂️🙇‍♂️🙇‍♀️ It might take some time if file size is big")
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(Config.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TEMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        start = datetime.now()
        file_name = input_str + ".webp"
        reply_message = await event.get_reply_message()
        to_download_directory = Config.TEMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await javes.download_media(
            reply_message,
            downloaded_file_name
        )
        end = datetime.now()
        ms_one = (end - start).seconds
        if os.path.exists(downloaded_file_name):
            c_time = time.time()
            await javes.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=False,
                supports_streaming=False,
                allow_cache=False,
                reply_to=event.message.id,
                thumb=thumb,
                
            )
            end_two = datetime.now()
            os.remove(downloaded_file_name)
            ms_two = (end_two - end).seconds
            await event.edit("Downloaded in {} seconds. Uploaded in {} seconds.".format(ms_one, ms_two))
        else:
            await event.edit("File Not Found {}".format(input_str))
    else:
        await event.edit("Syntax // .pts<name> as reply to a Telegram media")
        
@javes.on(admin_cmd("vtg (.*)"))
async def _(event):
    if event.fwd_from:
        return
    thumb = None
    if os.path.exists(thumb_image_path):
        thumb = thumb_image_path
    await event.edit("Rename & Upload in process 🙄🙇‍♂️🙇‍♂️🙇‍♀️ It might take some time if file size is big")
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(Config.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TEMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        start = datetime.now()
        file_name = input_str + ".gif"
        reply_message = await event.get_reply_message()
        to_download_directory = Config.TEMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await javes.download_media(
            reply_message,
            downloaded_file_name
        )
        end = datetime.now()
        ms_one = (end - start).seconds
        if os.path.exists(downloaded_file_name):
            c_time = time.time()
            await javes.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=False,
                supports_streaming=False,
                allow_cache=False,
                reply_to=event.message.id,
                thumb=thumb,
                
            )
            end_two = datetime.now()
            os.remove(downloaded_file_name)
            ms_two = (end_two - end).seconds
            await event.edit("Downloaded in {} seconds. Uploaded in {} seconds.".format(ms_one, ms_two))
        else:
            await event.edit("File Not Found {}".format(input_str))
    else:
        await event.edit("Syntax // .vtg<name> as reply to a Telegram video")
