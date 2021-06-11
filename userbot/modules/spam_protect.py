#Telegram @javes05



import spamwatch, os, asyncio
from telethon import events
from userbot import client as javes, JAVES_NAME, JAVES_MSG
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)
swapi = os.environ.get("SPAMWATCH_API_KEY", None)
SPAM_PROTECT = os.environ.get("SPAM_PROTECT", None)
SPAMWATCH_SHOUT = os.environ.get("SPAMWATCH_SHOUT", None)
W_CHAT = set(int(x) for x in os.environ.get("WHITE_CHATS", "").split())


if SPAM_PROTECT:
 @javes.on(events.ChatAction)
 async def handler(rkG): 
   if rkG.user_joined or rkG.user_added and not rkG.chat_id in W_CHAT and SPAM_PROTECT and swapi and not event.is_private:
       chat = await rkG.get_chat()
       admin = chat.admin_rights
       creator = chat.creator   
       if admin or creator:
           return
       sw = spamwatch.Client(swapi)
       guser = await rkG.get_user()      
       try:
           sswatch = sw.get_ban(guser.id) 
       except: 
           return                   
       if sswatch:                                                                                                
                 try:
                    await javes.edit_permissions(rkG.chat_id, guser.id, view_messages=False)    
                    action = "`ban`" ; return await rkG.reply(f"`{JAVES_NNAME}:` ** This user is detected as spam by SpamWatch!!** \n"                      
            f"**Reason **  : `{sswatch.reason}`\n"
            f"**Victim Id**: [{guser.id}](tg://user?id={guser.id})\n"                   
            f"**Action **  : {action}")                            
                 except:                          
                    return 
                #else:
                	#if SPAMWATCH_SHOUT:
                	    #action = "`Reported to `@admins" ; return await rkG.reply(f"`{JAVES_NNAME}:` ** This user is detected as spam by SpamWatch!!** \n"                      
            #f"**Reason **  : `{sswatch.reason}`\n"
            #f"**Victim Id**: [{guser.id}](tg://user?id={guser.id})\n"                   
            #f"**Action **  : {action}")   
                	    
    	
