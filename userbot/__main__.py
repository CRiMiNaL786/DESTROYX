import glob
import logging
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient

from userbot import CMD_HNDLR, bot
from userbot.Config import Var
from userbot.uniborgConfig import Config
from userbot.utils import load_assistant, load_module, start_assistant

TELE = Var.PRIVATE_GROUP_ID
BOTNAME = Var.TG_BOT_USER_NAME_BF_HER
LOAD_MYBOT = Var.LOAD_MYBOT
sed = logging.getLogger(Javes")


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


async def startup_log_all_done():
    try:
        await bot.send_message(
            TELE,
            f"**Black Lightning has been deployed.\nSend** `{CMD_HNDLR}alive` **to see if the bot is working.\n\nAdd** @{BOTNAME} **to this group and make it admin for enabling all the features of userbot**",
        )
    except BaseException:
        print("Either PRIVATE_GROUP_ID is wrong or you have left the group.")


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished, no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

path = "userbot/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

print("Javes 2.0 has been deployed! ")

print("Setting up Javes 2.0")
path = "userbot/modules/assistant/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_assistant(shortname.replace(".py", ""))

if Config.ENABLE_ASSISTANTBOT == "ENABLE":
    path = "userbot/modules/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_assistant(shortname.replace(".py", ""))
    sed.info("Javes 2.0  Bot Have Been Installed Successfully !")
else:
    sed.info("Javes 2.0 Has Been Installed Sucessfully !")
    sed.info("You Can Visit @javes_support For Any Support Or Doubts")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
