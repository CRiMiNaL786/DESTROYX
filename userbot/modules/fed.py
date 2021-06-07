from userbot import bot as borg
from telethon import events
import asyncio
borg = bot
from userbot import bot as  borg
from userbot import CMD_HELP




#unknown credit




@bot.on(events.NewMessage(pattern=".fed"))
async def myfeds(event):
  GAAND = await event.edit("Wᴇɪᴛ ᴍᴀsᴛᴇʀ ᴄʜᴇᴄᴋɪɴɢ ʏᴏᴜʀ ᴀʟʟ ғᴇᴅs...``")
  async with borg.conversation("missrose_bot") as rose:
    await rose.send_message("/start")
    await rose.get_response()
    await rose.send_message("/myfeds")
    pro = await rose.get_response()
    if "Looks like" in pro.text:
      await pro.click(0)
      await asyncio.sleep(1.5)
      pro = await rose.get_response()
      await borg.send_file(event.chat_id, pro, caption='Cʜᴇᴄᴋᴇᴅ ʙʏ JAVES 2.0 ฅ^•ﻌ•^ฅ')
    else:
      await GAAND.edit(pro.text + "\n\nCʜᴇᴄᴋᴇᴅ ʙʏ JAVES 2.0 ฅ^•ﻌ•^ฅ")
