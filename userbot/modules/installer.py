from userbot import client, CMD_HELP, CMD_LIST
from telethon import events
from userbot.events import javes05, rekcah05, zzaacckkyy, remove_plugin, load_module
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from userbot.utils import command, remove_plugin, load_module
from pathlib import Path
from userbot import LOAD_PLUG
from datetime import datetime
DELETE_TIMEOUT = 5
import sys, asyncio, traceback, os, importlib
import userbot.utils
from userbot import CMD_HELP, ALIVE_NAME, PM_MESSAGE, JAVES_NAME, JAVES_MSG, ORI_MSG
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)



@zzaacckkyy(pattern="^!install", outgoing=True)
async def install(event):
    a = "__Installing.__"
    b = 1
    await event.edit(a)
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(  # pylint:disable=E0602
                await event.get_reply_message(),
                "/root/userbot/userbot/modules/"  # pylint:disable=E0602
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                if shortname in CMD_LIST:
                    string = "**Commands found in** `{}`\n".format((os.path.basename(downloaded_file_name)))
                    for i in CMD_LIST[shortname]:
                        string += "  •  `" + i 
                        string += "`\n"
                        if b == 1:
                            a = "__Installing..__"
                            b = 2
                        else:
                            a = "__Installing...__"
                            b = 1
                        await event.edit(a)
                    return await event.edit(f"**Installed module**\n`{shortname}`\n\n{string}")
                return await event.edit(f"Installed module `{os.path.basename(downloaded_file_name)}`")
            else:
                os.remove(downloaded_file_name)
                return await event.edit(f"**Failed to Install** \n`Error`\nModule already installed or unknown formet")
        except Exception as e: 
            await event.edit(f"**Failed to Install** \n`Error`\n{str(e)}")
            return os.remove(downloaded_file_name)
    

@zzaacckkyy(pattern="^!load (?P<shortname>\w+)$", outgoing=True)
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except:
            pass
        load_module(shortname)
        await event.edit(f"Successfully loaded {shortname}")
    except Exception as e:
        await event.edit(f"Could not load {shortname} because of the following error.\n{str(e)}")


@zzaacckkyy(pattern="^!send (?P<shortname>\w+)$", outgoing=True)
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    input_str = event.pattern_match["shortname"]
    the_plugin_file = "./userbot/modules/{}.py".format(input_str)
    start = datetime.now()
    await event.client.send_file(  # pylint:disable=E0602
        event.chat_id,
        the_plugin_file,
        force_document=True,
        allow_cache=False,
        reply_to=message_id
    )
    end = datetime.now()
    time_taken_in_ms = (end - start).seconds
    await event.edit("Uploaded {} in {} seconds".format(input_str, time_taken_in_ms))
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


@zzaacckkyy(pattern="^!unload (?P<shortname>\w+)$", outgoing=True)
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await event.edit(f"Unloaded {shortname} successfully")
    except Exception as e:
        await event.edit("Successfully unload {shortname}\n{}".format(shortname, str(e)))





@javes05(outgoing=True, pattern="^!installall (.*)")
async def install(event):
    try:
      chat = event.pattern_match.group(1) ; text = f"**Installing plugins from {chat}..\n\n**" ; cui = await client.get_messages(chat, limit = 75, filter=InputMessagesFilterDocument)  ; total = int(cui.total) ; total_doxx = range(0, total)
    except:
    	return await event.edit("Error\nUsage: `!installall <channel/group username>`")
    for ixo in total_doxx:
        await event.edit(text) ; mxo = cui[ixo].id ; downloaded_file_name = await event.client.download_media(await client.get_messages(chat, ids=mxo), "userbot/modules/")
        if "(" not in downloaded_file_name:
            path1 = Path(downloaded_file_name) ; shortname = path1.stem
            if (os.path.basename(downloaded_file_name)).endswith('.py'):
               try:
                 load_module(shortname.replace(".py", "")) ; text += f"**• Installed** {(os.path.basename(downloaded_file_name))}\n"
               except:
               	text += f"**× Failed to install** {(os.path.basename(downloaded_file_name))}\n" ; os.remove (downloaded_file_name) ; pass
            else: 
                  text += f"** Skiped** {(os.path.basename(downloaded_file_name))}\n" ; os.remove (downloaded_file_name)
        else:
            text += f"** Skiped** {(os.path.basename(downloaded_file_name))}\n" ; os.remove (downloaded_file_name)
    return await event.edit(f"{text}\n\n**Install completed**")
        
        
        
CMD_HELP.update({
    "install":
    "`!install <reply to a plugin>`\
\n**Usage:** Install the plugin\
\n\n`!installall <channel/group username>`\
\n**Usage:**Install all plugins from the channel or group\
"
})



