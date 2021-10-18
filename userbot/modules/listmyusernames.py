# For @UniBorg
# (c) Shrimadhav U K
# PoRTeD FRoM ULTRA X 

from telethon import events, functions, types
from userbot.util import admin_cmd
from userbot import CMD_HELP
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from userbot import bot as borg

@borg.on(admin_cmd("listmyusernames"))
async def mine(event):
    result = await bot(GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"{channel_obj.title}\n@{channel_obj.username}\n\n"
    await event.edit(output_str)



CMD_HELP.update({"LisT My Usernames": ".listmyusernames gives you a list of your channels and groups"})
