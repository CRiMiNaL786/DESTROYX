from userbot import bot
from userbot.utils import admin_cmd

@bot.on(admin_cmd(pattern=r"deployme"))
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("[Click Here to deploy My Bot](https://heroku.com/deploy?template=https://github.com/Javes786/javes-2.0/blob/main)")
