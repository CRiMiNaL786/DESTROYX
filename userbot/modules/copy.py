"""Syntax: .copy as reply to a message to copy"""
from userbot import bot as borg
from userbot.util import admin_cmd


@borg.on(admin_cmd(pattern="copy"))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.text
        event.reply_to_msg_id
        the_real_message = the_real_message.replace("*", "*")
        the_real_message = the_real_message.replace("_", "_")
        await event.edit(the_real_message)
    else:
        await event.edit(
            "Reply to a message with `.copy` to copy it works on emojis and text"
        )
