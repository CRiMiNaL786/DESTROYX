from userbot.events import javes05
from userbot import bot, BOTLOG_CHATID, JAVES_NAME, JAVES_MSG, CMD_HELP
import asyncio
from telethon import events
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import (PeerChat, PeerChannel,ChannelParticipantsAdmins, ChatAdminRights,ChatBannedRights, MessageEntityMentionName,MessageMediaPhoto, ChannelParticipantsBots)
from telethon.tl.types import Channel
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from userbot.events import rekcah05
client = javes = bot 
from telethon.tl.functions.messages import GetCommonChatsRequest
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)
from telethon.events import ChatAction
from userbot.events import rekcah05
client = javes = bot
from userbot.events import javes05
from userbot import bot, BOTLOG_CHATID
import asyncio
from telethon import events
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import (PeerChat, PeerChannel,ChannelParticipantsAdmins, ChatAdminRights,ChatBannedRights, MessageEntityMentionName,MessageMediaPhoto, ChannelParticipantsBots)
from telethon.tl.types import Channel
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG
async def get_user_from_event(event):  
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit(f"`{JAVES_NNAME}`: ** Pass the user's username, id or reply!**")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("Failed \n **Error**\n", str(err))           
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj

try:
   from userbot import client2, client3
except:
   client2 = client3 = None
   pass
@javes.on(rekcah05(pattern=f"gkick(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!gkick(?: |$)(.*)")
async def gspide(rk): 
   lazy = rk ; sender = await lazy.get_sender() ; me = await lazy.client.get_me()
   if not sender.id == me.id:
        rkp = await lazy.reply("`processing...`")
   else:
    	rkp = await lazy.edit("`processing...`")      
   me = await rk.client.get_me() ; await rkp.edit(f"`{JAVES_NNAME}:` **Requesting  to gkick user!**") ; my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id) ; my_username = f"@{me.username}" if me.username else my_mention ; chat = await rk.get_chat() ; a = b = 0
   if rk.is_private:       
   	user = rk.chat ; reason = rk.pattern_match.group(1) ; chat_title = 'PM'  
   else:
   	chat_title = rk.chat.title  
   try:       
    user, reason = await get_user_from_event(rk)  
   except:
      pass
   try:
     if not reason:
       reason = 'Private'
   except:
   	return await rkp.edit(f"`{JAVES_NNAME}:`**Error! Unknown user.**")
   if user:      
        if user.id == 929138153:     
    	             return await rkp.edit(f"`{JAVES_NNAME}:`**HEY THAT'S MY DEV**")
        try:
          await rk.client(BlockRequest(user))
          await rk.client(UnblockRequest(user))
          block = 'True'
        except:      
           pass
        testrk = [d.entity.id for d in await rk.client.get_dialogs() if (d.is_group or d.is_channel) ]                          
        for i in testrk:
            try:
                 await rk.client.edit_permissions(i, user, view_messages=False)
                 await rk.client.edit_permissions(i, user, send_messages=True)
                 a += 1
                 await rkp.edit(f"`{JAVES_NNAME}:` **Requesting  to gkicking user!\nGkicked {a} chats.....**")
                 
            except:
                 b += 1                     
   else:
       await rkp.edit(f"`{JAVES_NNAME}:` **Reply to a user !! **")        

   return await rkp.edit(f"`{JAVES_NNAME}:` **GKicked [{user.first_name}](tg://user?id={user.id}) in {a} chat(s) **") 
#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG#MADE BY SH1VAM DONOT KANG


CMD_HELP.update({
    "gkick":
    "!gkick/.gkick <username> / <userid> / <reply to a user>\
\n\nUsage:Globally kicks the person in comman groups \
\n\nCommand Also Work On Sudo\
"
}
)
