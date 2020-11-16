import logging
import os
from datetime import datetime
from userbot.javes_main.heroku_var import *
import requests
from requests import exceptions, get
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot as javes
from userbot import CMD_HELP
import userbot
from userbot import *
#from userbot.uniborgConfig import Config
from userbot.utils import admin_cmd

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)


def progress(current, total):
    logging.info(
        "Downloaded {} of {}\nCompleted {}".format(
            current, total, (current / total) * 100
        )
    )


DOGBIN_URL = "https://del.dog/"
try:
	BOTLOG_CHATID = config.PRIVATE_GROUP_ID
except :
	BOTLOG_CHATID = None
else :
	BOTLOG_CHATID = BOTLOG_CHATID
BOTLOG = True


@javes.on(admin_cmd(pattern="paste ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    if not os.path.isdir(Config.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TEMP_DOWNLOAD_DIRECTORY)
    input_str = event.pattern_match.group(1)
    message = "SYNTAX: `.paste <long text to include>`"
    if input_str:
        message = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            downloaded_file_name = await borg.download_media(
                previous_message,
                Config.TEMP_DOWNLOAD_DIRECTORY,
                progress_callback=progress,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                message += m.decode("UTF-8") + "\r\n"
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    else:
        message = "SYNTAX: `.paste <long text to include>`"
    url = "https://del.dog/documents"
    r = requests.post(url, data=message.encode("UTF-8")).json()
    url = f"https://del.dog/{r['key']}"
    end = datetime.now()
    ms = (end - start).seconds
    if r["isUrl"]:
        nurl = f"https://del.dog/v/{r['key']}"
        await event.edit(
            "Pasted to dogbin : [dog]({}) in {} seconds. GoTo Original URL: [link]({})".format(
                url, ms, nurl
            )
        )
    else:
        await event.edit("Pasted to dogbin : [dog]({}) in {} seconds".format(url, ms))


@javes.on(admin_cmd(pattern="neko ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    datetime.now()
    if not os.path.isdir(Config.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TEMP_DOWNLOAD_DIRECTORY)
    input_str = event.pattern_match.group(1)
    message = "SYNTAX: `.neko <long text to include>`"
    if input_str:
        message = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            downloaded_file_name = await borg.download_media(
                previous_message,
                Config.TEMP_DOWNLOAD_DIRECTORY,
                progress_callback=progress,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                # message += m.decode("UTF-8") + "\r\n"
                message += m.decode("UTF-8")
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    else:
        message = "SYNTAX: `.neko <long text to include>`"
    py_file = ""
    if downloaded_file_name.endswith(".py"):
        py_file += ".py"
        data = message
        key = (
            requests.post("https://nekobin.com/api/documents", json={"content": data})
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}{py_file}"
        reply_text = f"Pasted to Nekobin : [neko]({url})"
        await event.edit(reply_text)
    else:
        data = message
        key = (
            requests.post("https://nekobin.com/api/documents", json={"content": data})
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        reply_text = f"Pasted to Nekobin : [neko]({url})"
        await event.edit(reply_text)
