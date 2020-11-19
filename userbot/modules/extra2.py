#Telegram @javes05

from telethon import events
import os
from userbot import client
javes = client
from userbot import JAVES_NAME, JAVES_MSG
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)
EP = os.environ.get("EP", None)
DP = os.environ.get("EG", None)
EG = os.environ.get("EG", None)
DG = os.environ.get("DG", None)
LG = os.environ.get("LG", None)
from userbot import CMD_HELP










@client.on(events.MessageDeleted)
async def handler(event):
  if event.is_private: 
   if DP: 
       await client.send_message(event.chat_id, f'User  Deleted His message just now !! \n **Event Details ** \n {event}')                 
  if not event.is_private: 
    if DG : 
       await client.send_message(event.chat_id, f'User  Deleted His message just now !! \n **Event Details ** \n {event}')
       


       
@client.on(events.MessageEdited)
async def handler(event):
  if event.is_private: 
   if EP : 
       me = await event.client.get_me()
       date = event.date
       id = event.from_id
       hide = event.edit_hide
       mentioned = event.mentioned
       silent = event.silent
       scheduled = event.from_scheduled
       editdate = event.edit_date
       editprot = event.media_unread       
       if event.from_id == me.id:
           return       
       return await event.reply(
                     f"`{JAVES_NNAME}:` **User  Edited His message !!** \n"                      
                     f"**date**: `{date}`\n"                   
                     f"**Edited date **  : `{editdate}`\n"
                     f"**Silent message **  : `{silent}`\n"
                     f"**scheduled message **  : `{scheduled}`\n"
                     f"**mentioned**  : `{mentioned}`\n"
                     f"**userid**  : `{id}`\n")   
  if not event.is_private: 
    if EG : 
       me = await event.client.get_me()
       date = event.date
       id = event.from_id
       hide = event.edit_hide
       mentioned = event.mentioned
       silent = event.silent
       scheduled = event.from_scheduled
       editdate = event.edit_date
       editprot = event.media_unread       
       if event.from_id == me.id:
           return       
       return await event.reply(
                     f"`{JAVES_NNAME}:` **User  Edited His message !!** \n"                      
                     f"**date**: `{date}`\n"                   
                     f"**Edited date **  : `{editdate}`\n"
                     f"**Silent message **  : `{silent}`\n"
                     f"**scheduled message **  : `{scheduled}`\n"
                     f"**mentioned**  : `{mentioned}`\n"
                     f"**userid**  : `{id}`\n")   
       




@client.on(events.ChatAction)
async def handler(rkG):
    if rkG.user_left:
    	if LG:   
           guser = await rkG.get_user() ; chat = await rkG.get_chat() ; admin = chat.admin_rights
           creator = chat.creator   
           if admin or creator:
                await client.edit_permissions(rkG.chat_id, guser.id, view_messages=False)  
                return await rkG.reply(
                     f"`{JAVES_NNAME}:` ** User left the group and permanently banned!!** \n"                      
                     f"`Victim Id`: **[{guser.id}](tg://user?id={guser.id})**")  


    
       
CMD_HELP.update({
    "extra":
    "!set var EP True\
\n**Usage:**  If any user edited any message  in your pm bot will shoutout\
\n\n!del var EP \
\n**Usage:**  Off EP\
\n\n!set var EG True\
\n**Usage:**  If any user edited message in groups bot will shouout \
\n\n!delvar EG\
\n**Usage:**  off EG \
\n\n!set var DG True\
\n**Usage:**  If any user deleted his message in group bot will shouout \
\n\n!del var DG \
\n**Usage:**  Off DG \
\n\n!set var LG True\
\n**Usage:**  If any one leave your group javes auto ban him permanently \
\n\n!del var LG \
\n**Usage:**  Off LG \
\n\nAll commands Support if you active full sudo  ( type !help sudo for more info)\
"
})
   
       
       