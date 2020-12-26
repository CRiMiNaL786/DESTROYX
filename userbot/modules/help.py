from userbot.events import javes05, rekcah05
from userbot import bot as javes, CMD_HELP
import os

IN = os.environ.get("INLINE_MODE", None)


if not IN:
 @javes05(outgoing=True, pattern="^!help(?: |$)(.*)")
 async def help(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("`Unknown module type !help to see all modules`")
    else:
        await event.edit(" Support Group for help & report bugs @javes05 ")
        string = (f"`Use !help <module_name>`\n\n**Currently Loaded [{len(CMD_HELP)}] Modules **\n")
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\n"
        await event.reply(string)
 
