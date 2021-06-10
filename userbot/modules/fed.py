import asyncio

from telethon import events

from userbot import bot

borg = bot
from userbot import bot as borg

# CREDITS => @LEGENDX22
# Baki pta nhi agar kisi hor ka hua toh contact kr lena bhaiya pehle @Criminal786


@bot.on(events.NewMessage(pattern=".fed", outgoing=True))
async def myfeds(event):
    GAAND = await event.edit("Wᴇɪᴛ ᴍᴀsᴛᴇʀ ᴄʜᴇᴄᴋɪɴɢ ʏᴏᴜʀ ᴀʟʟ ғᴇᴅs...")
    async with borg.conversation("missrose_bot") as rose:
        await rose.send_message("/start")
        await rose.get_response()
        await rose.send_message("/myfeds")
        pro = await rose.get_response()
        if "Looks like" in pro.text:
            await pro.click(0)
            await asyncio.sleep(1.5)
            pro = await rose.get_response()
            await borg.send_file(
                event.chat_id, pro, caption="Cʜᴇᴄᴋᴇᴅ ʙʏ JAVES 2.0 ฅ^•ﻌ•^ฅ"
            )
        else:
            await GAAND.edit(pro.text + "\n\nCʜᴇᴄᴋᴇᴅ ʙʏ JAVES 2.0 ฅ^•ﻌ•^ฅ")
