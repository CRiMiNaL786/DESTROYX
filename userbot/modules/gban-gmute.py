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

@client.on(ChatAction)
async def handler(rkG): 
   if rkG.user_joined or rkG.user_added:      
       try:       	
         from userbot.modules.sql_helper.gmute_sql import is_gmuted
         guser = await rkG.get_user()      
         gmuted = is_gmuted(guser.id)             
       except:      
          return
       if gmuted:
        for i in gmuted:
            if i.sender == str(guser.id):                                                                         
                chat = await rkG.get_chat()
                admin = chat.admin_rights
                creator = chat.creator   
                if admin or creator:
                 try:
                    await client.edit_permissions(rkG.chat_id, guser.id, view_messages=False)                              
                    await rkG.reply(
                     f"`{JAVES_NNAME}:` ** Gbanned User Joined!!** \n"                      
                     f"**Victim Id**: [{guser.id}](tg://user?id={guser.id})\n"                   
                     f"**Action **  : `Banned`")                                                
                 except:                          
                    return 
if client2:
 @client2.on(ChatAction)
 async def handler(rkG): 
   if rkG.user_joined or rkG.user_added:      
       try:       	
         from userbot.modules.sql_helper.gmute_sql import is_gmuted
         guser = await rkG.get_user()      
         gmuted = is_gmuted(guser.id)             
       except:      
          return
       if gmuted:
        for i in gmuted:
            if i.sender == str(guser.id):                                                                         
                chat = await rkG.get_chat()
                admin = chat.admin_rights
                creator = chat.creator   
                if admin or creator:
                 try:
                    await client.edit_permissions(rkG.chat_id, guser.id, view_messages=False)                              
                    await rkG.reply(
                     f"`{JAVES_NNAME}:` ** Gbanned User Joined!!** \n"                      
                     f"**Victim Id**: [{guser.id}](tg://user?id={guser.id})\n"                   
                     f"**Action **  : `Banned`")                                                
                 except:                          
                    return
                    
if client3:
 @client3.on(ChatAction)
 async def handler(rkG): 
   if rkG.user_joined or rkG.user_added:      
       try:       	
         from userbot.modules.sql_helper.gmute_sql import is_gmuted
         guser = await rkG.get_user()      
         gmuted = is_gmuted(guser.id)             
       except:      
          return
       if gmuted:
        for i in gmuted:
            if i.sender == str(guser.id):                                                                         
                chat = await rkG.get_chat()
                admin = chat.admin_rights
                creator = chat.creator   
                if admin or creator:
                 try:
                    await client.edit_permissions(rkG.chat_id, guser.id, view_messages=False)                              
                    await rkG.reply(
                     f"`{JAVES_NNAME}:` ** Gbanned User Joined!!** \n"                      
                     f"**Victim Id**: [{guser.id}](tg://user?id={guser.id})\n"                   
                     f"**Action **  : `Banned`")                                                
                 except:                          
                    return 
    	        

@javes05(incoming=True, disable_errors=True)
async def muter(rkG):
    try:        
        from userbot.modules.sql_helper.gmute_sql import is_gmuted
        from userbot.modules.sql_helper.globelmute_sql import is_globelmuted
    except:
        return    
    gmuted = is_gmuted(rkG.sender_id)
    gmuted2 = is_globelmuted(rkG.sender_id)
    if gmuted2:
        for i in gmuted2:
            if i.sender == str(rkG.sender_id):
                if rkG.is_private:                           
                    return await rkG.delete()                           
                chat = await rkG.get_chat()
                admin = chat.admin_rights
                creator = chat.creator   
                if admin or creator:
                 try:
                    return await rkG.delete()                                    
                 except:                          
                    return 
    if gmuted:
        for i in gmuted:
            if i.sender == str(rkG.sender_id):
                if rkG.is_private:                           
                    await rkG.client(BlockRequest(rkG.sender_id))
                    return await rkG.reply(
                     f"`{JAVES_NNAME}:` ** Gbanned User Found!!** \n"        
                     f"**Victim Id**: [{rkG.sender_id}](tg://user?id={rkG.sender_id})\n"                                
                     f"**Action **  : `Blocked`")                                                    
                chat = await rkG.get_chat()
                admin = chat.admin_rights
                creator = chat.creator   
                if admin or creator:
                 try:
                    await client.edit_permissions(rkG.chat_id, guser.id, view_messages=False)                              
                    await rkG.reply(
                     f"`{JAVES_NNAME}:` ** Gbanned User Joined!!** \n"                      
                     f"**Victim Id**: [{guser.id}](tg://user?id={guser.id})\n"                   
                     f"**Action **  : `Banned`")                                                
                 except:                          
                    return 











@javes.on(rekcah05(pattern=f"gmute(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!gmute(?: |$)(.*)")
async def gspider(rk): 
   lazy = rk ; sender = await lazy.get_sender() ; me = await lazy.client.get_me()
   if not sender.id == me.id:
        rkp = await lazy.reply("`processing...`")
   else:
    	rkp = await lazy.edit("`processing...`")   
   me = await rk.client.get_me() ; await rkp.edit(f"`Gmuting....`") ; my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id) ; my_username = f"@{me.username}" if me.username else my_mention ; chat = await rk.get_chat() ; a = b = 0
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
        if user.id == 710844948:     
    	             return await rkp.edit(f"`{JAVES_NNAME}:`**Error! cant globelmute this user.**")
        try:
          from userbot.modules.sql_helper.globelmute_sql import globelmute          
        except:
   	     pass        
   else:
       return await rkp.edit(f"`{JAVES_NNAME}:` **Reply to a user !! **")        
   try:
     if globelmute(user.id) is False:
            return await rkp.edit(f"`{JAVES_NNAME}:`**Error! User probably already globelmuted.**")
   except:
    	pass
   return await rkp.edit(f"`Globelly taped`") 
 
@javes.on(rekcah05(pattern=f"ungmute(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!ungmute(?: |$)(.*)")
async def gspider(rk):    
   lazy = rk ; sender = await lazy.get_sender() ; me = await lazy.client.get_me()
   if not sender.id == me.id:
        rkp = await lazy.reply("`processing...`")
   else:
    	rkp = await lazy.edit("`processing...`")   
   me = await rk.client.get_me() ; await rkp.edit(f"`ungmuting`") ; my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id) ; my_username = f"@{me.username}" if me.username else my_mention ; chat = await rk.get_chat() ; a = b = 0   
   try:
     from userbot.modules.sql_helper.globelmute_sql import unglobelmute
   except:
   	return
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
   if not user:       
       return await rkp.edit(f"`{JAVES_NNAME}:` **Reply to a user !! **")        
   try:
     if unglobelmute(user.id) is False:
            return await rkp.edit(f"`{JAVES_NNAME}:`**Error! User probably already ungmuted.**")
   except:
    	pass
   return await rkp.edit(f"`Ungmuted`") 
        

@javes.on(rekcah05(pattern=f"gban(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!gban(?: |$)(.*)")
async def gspider(rk): 
   lazy = rk ; sender = await lazy.get_sender() ; me = await lazy.client.get_me()
   if not sender.id == me.id:
        rkp = await lazy.reply("`processing...`")
   else:
    	rkp = await lazy.edit("`processing...`")      
   me = await rk.client.get_me() ; await rkp.edit(f"`{JAVES_NNAME}:` **Requesting  to gban user!**") ; my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id) ; my_username = f"@{me.username}" if me.username else my_mention ; chat = await rk.get_chat() ; a = b = 0
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
        if user.id == 710844948:     
    	             return await rkp.edit(f"`{JAVES_NNAME}:`**Error! cant gban this user.**")
        try:
          from userbot.modules.sql_helper.gmute_sql import gmute            
        except:
   	     pass
        try:
          await rk.client(BlockRequest(user))
          block = 'True'
        except:      
           pass
        testrk = [d.entity.id for d in await rk.client.get_dialogs() if (d.is_group or d.is_channel) ]                          
        for i in testrk:
            try:
                 await rk.client.edit_permissions(i, user, view_messages=False)          
                 a += 1
                 await rkp.edit(f"`{JAVES_NNAME}:` **Requesting  to gban user!\nGbanned {a} chats.....**")
            except:
                 b += 1                     
   else:
       await rkp.edit(f"`{JAVES_NNAME}:` **Reply to a user !! **")        
   try:
     if gmute(user.id) is False:
            return await rkp.edit(f"`{JAVES_NNAME}:`**Error! User probably already gbanned.**")
   except:
    	pass
   return await rkp.edit(f"`{JAVES_NNAME}:` **Gbanned [{user.first_name}](tg://user?id={user.id}) in {a} chat(s) , Blocked user and added to Gban watch **") 
        



@javes.on(rekcah05(pattern=f"ungban(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!ungban(?: |$)(.*)")
async def gspider(rk):
   lazy = rk ; sender = await lazy.get_sender() ; me = await lazy.client.get_me()
   if not sender.id == me.id:
        rkp = await lazy.reply("`processing...`")
   else:
    	rkp = await lazy.edit("`processing...`")   
   me = await rk.client.get_me() ; await rkp.edit(f"`{JAVES_NNAME}:` **Requesting  to ungban user!**") ; my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id) ; my_username = f"@{me.username}" if me.username else my_mention ; chat = await rk.get_chat() ; a = b = 0
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
        if user.id == 710844948:     
    	             return await rkp.edit(f"`{JAVES_NNAME}:`**Error! cant ungban this user.**")
        try:
          from userbot.modules.sql_helper.gmute_sql import ungmute
        except:
   	     pass
        try:
          await rk.client(UnblockRequest(user))
          block = 'True'
        except:      
           pass
        testrk = [d.entity.id for d in await rk.client.get_dialogs() if (d.is_group or d.is_channel) ]                          
        for i in testrk:
            try:
                 await rk.client.edit_permissions(i, user, send_messages=True)          
                 a += 1
                 await rkp.edit(f"`{JAVES_NNAME}:` **Requesting  to ungban user!\nunGbanned {a} chats.....**")
            except:
                 b += 1                     
   else:
       await rkp.edit(f"`{JAVES_NNAME}:` **Reply to a user !! **")        
   try:
     if ungmute(user.id) is False:
            return await rkp.edit(f"`{JAVES_NNAME}:`**Error! User probably already ungbanned.**")
   except:
    	pass
   return await rkp.edit(f"`{JAVES_NNAME}:` **UnGbanned [{user.first_name}](tg://user?id={user.id}) in {a} chat(s) , UnBlocked and removed user from Gban watch **") 
        


CMD_HELP.update({
    "gban-gmute":
    "!gban <username> / <userid> / <reply to a user>\
\n**Usage**: Globel ban the person in all groups, channels , block in pm , add gban watch (use with solution) \
\n\n!ungban <username> / <userid> / <reply to a user>\
\n**Usage**: unban user from all groups, channels , remove user from gban watch.\
\n\n!gmute <username> / <userid> / <reply to a user>\
\n**Usage**: Globel mute the user  \
\n\n!ungmute <username> / <userid> / <reply to a user>\
\n**Usage**: Remove user from gmute list \
\n\n**All commands support sudo**\
"
})

