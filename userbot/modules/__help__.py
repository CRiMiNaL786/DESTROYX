import asyncio

import requests
from telethon import functions
#from userbot.helpers import yaml_format
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, CMD_HELP, CMD_LIST
from userbot import bot as borg
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Noob"

HELPTYPE=False


@borg.on(admin_cmd(outgoing=True, pattern="hlp ?(.*)"))
async def cmd_list(event):
    global HELPTYPE
    reply_to_id = None
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    input_str = event.pattern_match.group(1)
    if input_str == "text":
        string = (
            "Total {count} commands found in {plugincount} plugins of userbot\n\n"
        )
        catcount = 0
        plugincount = 0
        for i in sorted(CMD_LIST):
            plugincount += 1
            string += f"{plugincount}) Commands found in Plugin " + i + " are \n"
            for iter_list in CMD_LIST[i]:
                string += "    " + str(iter_list)
                string += "\n"
                catcount += 1
            string += "\n"
        if len(string) > 4095:
            data = string.format(count=catcount, plugincount=plugincount)
            key = (
                requests.post(
                    "https://nekobin.com/api/documents", json={"content": data}
                )
                .json()
                .get("result")
                .get("key")
            )
            url = f"https://nekobin.com/{key}"
            reply_text = f"**All commands of the userbot can be seen [here]({url})**"
            await event.edit(reply_text)
            return
        await event.edit(string.format(count=catcount, plugincount=plugincount))
        return
    if input_str:
        if input_str in CMD_LIST:
            string = "<b>{count} Commands found in plugin {input_str}:</b>\n\n"
            catcount = 0
            for i in CMD_LIST[input_str]:
                string += f"  •  <code>{i}</code>"
                string += "\n"
                catcount += 1
            await event.edit(
                string.format(count=catcount, input_str=input_str), parse_mode="HTML"
            )
        else:
            await event.edit(input_str + " is not a valid plugin!")
            await asyncio.sleep(3)
            await event.delete()
    else:
        if HELPTYPE is True:
            help_string = f"Userbot Helper.. Provided by {DEFAULTUSER}\
                          \nUserbot Helper to reveal all the plugin names"
                          
            tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
            results = await bot.inline_query(  # pylint:disable=E0602
                tgbotusername, help_string
            )
            await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
            await event.delete()
        else:
            string = "<b>Please specify which plugin do you want help for !!\
                \nNumber of plugins : </b><code>{count}</code>\
                \n<b>Usage:</b> <code>.hlp</code> plugin name\n\n"
            catcount = 0
            for i in sorted(CMD_LIST):
                string += "• " + f"<code>{str(i)}</code>"
                string += "   "
                catcount += 1
            await event.edit(string.format(count=catcount), parse_mode="HTML")




@borg.on(admin_cmd(outgoing=True, pattern="chk ?(.*)"))

async def info(event):
    """ For .info command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            event = await event.edit("Please specify a valid plugin name.")
            await asyncio.sleep(4)
            await event.delete()
    else:
        string = "<b>Please specify which plugin do you want help for !!\
            \nNumber of plugins : </b><code>{count}</code>\
            \n<b>Usage : </b><code>.chk</code> <plugin name>\n\n"
        catcount = 0
        for i in sorted(CMD_HELP):
            string += "• " + f"<code>{str(i)}</code>"
            string += "   "
            catcount += 1
       
            await event.edit(string.format(count=catcount), parse_mode="HTML")


'''@borg.on(admin_cmd(pattern="dc$"))
async def _(event):
    result = await bot(functions.help.GetNearestDcRequest())
    result = (
        yaml_format(result)
        + "\n\n**List Of Telegram Data Centres:**\
                \nDC1 : Miami FL, USA\
                \nDC2 : Amsterdam, NL\
                \nDC3 : Miami FL, USA\
                \nDC4 : Amsterdam, NL\
                \nDC5 : Singapore, SG\
                "
    )
    await event.edit(result)
'''

