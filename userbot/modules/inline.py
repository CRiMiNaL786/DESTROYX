
#telegram channel @javes05
#from https://t.me/pldhsys



from telethon.tl.custom import Button 
from telethon import events
from telethon import sync
import io, os
from userbot import CMD_HELP,  client
from userbot.events import javes05

try:
  from userbot import tebot
except:
   tebot = None
   pass




 






IN = os.environ.get("INLINE_MODE", None)
BT = os.environ.get("BOT_TOKEN", None)

if IN:
  @javes05(outgoing=True, pattern="^!help(?: |$|\n)([\s\S]*)")
  async def ban(event):
    if not BT:
       return await event.edit (" Error Add bot token as BOT_TOKEN in heroku var or set inline mode off ")
    mbt = await tebot.get_me()
    try:
       results = await event.client.inline_query(mbt.username, "helpme" )
    except:
       return await  event.edit (" Error go @BotFather and enable inline mode to your bot for use this mode")
    return await results[0].click( event.chat_id, reply_to=event.reply_to_msg_id, hide_via=False )
   

if tebot:
 @tebot.on(events.CallbackQuery)
 async def handler(event):
  try:
    me = await client.get_me()
    if not event.query.user_id == me.id:
        return await event.answer("Sorry, You dont have permission to  Access me!", alert=True)
    et = event.data.decode("UTF-8")
    if et == "back":
        sad = sad2 = sad3 = sad4 = None
        lol = 0
        tbu = [[ Button.inline('❌ Close menu', b'close'), ]] 
        for i in CMD_HELP:
            if lol == 0:
               sad = str(i)
               lol = 1
            elif lol == 1:
                sad2 = str(i)
                lol = 2
            elif lol == 2:
                sad3 = str(i)
                lol = 3
            elif lol == 3:
                sad4 = str(i)
                lol = 0
            if sad and sad2 and sad3 and sad4:
               tbu += [[ Button.inline(f"{sad}" , f"{sad}"), Button.inline(f"{sad2}"  , f"{sad2}"), Button.inline(f"{sad3}" , f"{sad3}"), Button.inline(f"{sad4}" , f"{sad4}")]]   
               sad = sad2 = sad3 = sad4 = None 
        if sad:
	        tbu += [[ Button.inline(f"{sad}"  , f"{sad}")]]   
        if sad2:
	        tbu += [[ Button.inline(f"{sad2}"  , f"{sad2}")]]   
        if sad3:
           tbu += [[ Button.inline(f"{sad3}"  , f"{sad3}")]]   
        return await event.edit ("Support Channel For Report bugs & help @javes05", buttons=tbu, link_preview=False)   
    if et == "close":
        return await event.edit (" Help Menu Closed")   
    if et in CMD_HELP: 
          fci = [[Button.inline('Go back', 'back')]]            
          await event.edit(str(CMD_HELP[et]), buttons=fci)
    else:
    	await event.answer("error", alert=True)
  except Exception as e:     
    	return await event.edit(str(e))
        
        
if tebot:
 @tebot.on(events.InlineQuery)  
 async def inline_handler(event):
  me = await client.get_me()  
  builder = event.builder
  query = event.text
  split = query.split(' ', 1) 
  if not event.query.user_id == me.id:      
      return
  if query.startswith("helpme"):
      sad = sad2 = sad3 = sad4 = None
      lol = 0
      tbu = [[ Button.inline('❌ Close menu', b'close'), ]] 
      for i in CMD_HELP:
            if lol == 0:
               sad = str(i)
               lol = 1
            elif lol == 1:
                sad2 = str(i)
                lol = 2
            elif lol == 2:
                sad3 = str(i)
                lol = 3
            elif lol == 3:
                sad4 = str(i)
                lol = 0
            if sad and sad2 and sad3 and sad4:
               tbu += [[ Button.inline(f"{sad}" , f"{sad}"), Button.inline(f"{sad2}"  , f"{sad2}"), Button.inline(f"{sad3}" , f"{sad3}"), Button.inline(f"{sad4}" , f"{sad4}")]]   
               sad = sad2 = sad3 = sad4 = None 
      if sad:
	        tbu += [[ Button.inline(f"{sad}"  , f"{sad}")]]   
      if sad2:
	        tbu += [[ Button.inline(f"{sad2}"  , f"{sad2}")]]   
      if sad3:
	       tbu += [[ Button.inline(f"{sad3}"  , f"{sad3}")]]   
      result = builder.article("Help menu", text = "Support Channel For Report bugs & help @javes05", buttons=tbu, link_preview=False)      
      return await event.answer([result])
  return




