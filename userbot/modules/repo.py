from userbot import bot
from userbot.utils import admin_cmd

@bot.on(admin_cmd(pattern=r"myrepo"))
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("[Click here](https://github.com/Sh1vam/javes-2.0) to open this Upgraded bot.")
