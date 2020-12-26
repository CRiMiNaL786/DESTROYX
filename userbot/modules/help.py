from userbot.events import javes05, rekcah05
from userbot import bot as javes, CMD_HELP
import os

IN = os.environ.get("INLINE_MODE", None)


if not IN:
 @javes05(outgoing=True, pattern="^!help(?: |$)(.*)")
 async def help(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("`Unknown module type !help to see all modules`")
    else:
        await event.edit(" For Support, Report bugs & help @Javes2suPPort ")
        string = (f"`Use !help <module_name>`\n\n**Currently Loaded [{len(CMD_HELP)}] Modules **\n")
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\n"
        await event.reply(string)
 




@javes.on(rekcah05(pattern=f"help(?: |$)(.*)", allow_sudo=True))
async def help(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.reply(str(CMD_HELP[args]))
        else:
            await event.reply("`Unknown module type !help to see all modules`")
    else:
        await event.reply(" For Support, Report bugs & help @Javes2SuPPort ")
        string = (f"`Use .help <module_name>`\n\n**Currently Loaded [{len(CMD_HELP)}] Modules **\n")
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\n"
        await event.reply(string)





        







CMD_HELP.update({
    "locks":
    "!lock <all (or) type(s)> or !unlock <all (or) type(s)>\
\nUsage: Allows you to lock/unlock some common message types in the chat.\
[NOTE: Requires proper admin rights in the chat !!]\
\n\nAvailable message types to lock/unlock are: \
\n`all, msg, media, sticker, gif, game, inline, poll, invite, pin, info`"
})


CMD_HELP.update({
    "chat":
    "!chatid\
\nUsage: Fetches the current chat's ID\
\n\n!userid\
\nUsage: Fetches the ID of the user in reply, if its a forwarded message, finds the ID for the source.\
\n\n!chatinfo\
\nUsage: Fetches the group's info\
\n\n!log\
\nUsage: Forwards the message you've replied to in your bot logs group.\
\n\n!invite\
\nUsage: !invite <username> invite the user to the group.\
\n\n!kickme\
\nUsage: Leave from a targeted group.\
\n\n!link <username/userid> : <optional text> (or) reply to someone's message with !link <optional text>\
\nUsage: Generate a permanent link to the user's profile with optional custom text."
})

CMD_HELP.update({
    "filter":
    "!checkfilter\
    \nUsage: Lists all active userbot filters in a chat.\
    \n\n!savefilter reply to a message with !savefilter <keyword>\
    \nUsage: Saves the replied message as a reply to the 'keyword'.\
    \nThe bot will reply to the message whenever 'keyword' is mentioned.\
    \nWorks with everything from files to stickers.\
    \n\n!clearfilter <filter>\
    \nUsage: Stops the specified filter. \
    \n\n!clearallfilter \
    \nUsage: Stops all filters.\
    \n\n!savefilter2 ,  !checkfilter2,  clearfilter2\
    \nUsage: same like filter "
})


CMD_HELP.update({
    "stickers":
    "!kang\
\nUsage: Reply !kang to a sticker or an image to kang it to your userbot pack.\
\n\n!kang [emoji('s)]\
\nUsage: Works just like !kang but uses the emoji('s) you picked.\
\n\n!kang [number]\
\nUsage: Kang's the sticker/image to the specified pack \
\n\n!kang [emoji('s)] [number]\
\nUsage: Kang's the sticker/image to the specified pack and uses the emoji('s) you picked.\
\n\n!stickerinfo\
\nUsage: Gets info about the sticker pack.\
\n\n!ss\
\nUsage: convert user text to sticker like a sticker screenshot\
\n\n!ss2\
\nUsage: Convert picture to sticker\
\n\n!text\
\nUsage: text to sticker\
\n\n!text2\
\nUsage: same like !text but can use custom fonts like !text font | message ex -  !text2 font | lol \
\n\n!fry\
\nUsage: make given image funny\
"
})


CMD_HELP.update({
    "beta":
    "!mail\
\nUsage: Create a fake  main and list it \
\n\n!ushort \
\nUsage: shorten the url.\
\n\n!song2\
\nUsage: find the target song \
\n\n!lyrics2 [emoji('s)] [number]\
\nUsage: get lyrics of song\
\n\n!mask\
\nUsage: make mask for tagged photo/sticker\
"
})






CMD_HELP.update({
    "blacklist":
    "!checkblacklist\
    \nUsage: Lists all active userbot blacklists in a chat.\
    \n\n!saveblacklist <keyword> <reply text> or reply to a message with !saveblacklist <keyword>\
    \nUsage: Delete then non admins blacklisted wards.\
    \n\n!clearblacklist <ward>\
    \nUsage: Stops the specified blacklist ward."
})


CMD_HELP.update({
    "sudo":
    "if you active sudo , sudo users can controll your javes like you controll groupmanaging bots\
    \nyou can active sudo by !set var SUDO_USERS <your sudo user's id>\
    \n\nyou can active multiple sudo users by space between each ids\
    \ncheck sudo by .sudo in sudo user's account\
    \n video example :- https://t.me/javes05/116 \
    \n(!) command for bot owner , (.) command for sudo users like !ban for owner , .ban for sudo users\
    \n\n normal sudo disabled for some comands due to privacy , if you want full sudo access you can set FULL_SUDO as True in herolu var\
"
})




