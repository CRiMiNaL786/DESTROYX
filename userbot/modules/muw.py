from userbot.utils import admin_cmd
from userbot import bot as borg
@borg.on(admin_cmd(pattern=r"wis ?(.*)"))
async def wis(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        r_msg = await event.get_reply_message()
        try:
            new_update = await borg.get_entity(int("{}".format(str(r_msg.from_id))[17:-1]))
        except :
            new_update = await borg.get_entity("{}".format(str(r_msg.from_id))[17:-1])
        else:
            new_update = await borg.get_entity('me')
        await event.edit(new_update.stringify())
@borg.on(admin_cmd(pattern=r"uis ?(.*)"))
async def ues(event):
    giveVar = event.text
    a = giveVar[5:]
    try:
        new_update = await borg.get_entity(int(a))
    except ValueError:
        new_update = await borg.get_entity('me')
    await event.edit(new_update.stringify())
@borg.on(admin_cmd(pattern=r"mes ?(.*)"))
async def mes(event):
    new_update = await borg.get_entity('me')
    await event.edit(new_update.stringify())
