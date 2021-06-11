
import os
from telethon.errors import ImageProcessFailedError, PhotoCropSizeSmallError
from telethon.errors.rpcerrorlist import (PhotoExtInvalidError,UsernameOccupiedError)
from telethon.tl.functions.account import (UpdateProfileRequest,UpdateUsernameRequest)
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from telethon.tl.functions.photos import (DeletePhotosRequest,GetUserPhotosRequest,UploadProfilePhotoRequest)
from telethon.tl.types import InputPhoto, MessageMediaPhoto, User, Chat, Channel
from userbot import bot, CMD_HELP
from userbot.events import javes05


INVALID_MEDIA = "```The extension of the media entity is invalid.```"
PP_CHANGED = "```Profile picture changed successfully.```"
PP_TOO_SMOL = "```This image is too small, use a bigger image.```"
PP_ERROR = "```Failure occured while processing image.```"
BIO_SUCCESS = "```Successfully edited Bio.```"
NAME_OK = "```Your name was succesfully changed.```"
USERNAME_SUCCESS = "```Your username was succesfully changed.```"
USERNAME_TAKEN = "```This username is already taken.```"



@javes05(outgoing=True, pattern="^!reserved$")
async def mine(event):   
    result = await bot(GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"{channel_obj.title}\n@{channel_obj.username}\n\n"
    await event.edit(output_str)


@javes05(outgoing=True, pattern="^!name")
async def update_name(name):    
    newname = name.text[6:]
    if " " not in newname:
        firstname = newname
        lastname = ""
    else:
        namesplit = newname.split(" ", 1)
        firstname = namesplit[0]
        lastname = namesplit[1]
    await name.client(
        UpdateProfileRequest(first_name=firstname, last_name=lastname))
    await name.edit(NAME_OK)


@javes05(outgoing=True, pattern="^!setpfp$")
async def set_profilepic(propic):
    await propic.edit("`Processing...`") 
    replymsg = await propic.get_reply_message()
    photo = None
    #Prevent Channel Bug to control Change Profile
    if propic.is_channel and not propic.is_group:
        await propic.edit("`Setpfp Commad isn't permitted on channels`")
        return
    if replymsg.media:
        if isinstance(replymsg.media, MessageMediaPhoto):
            photo = await propic.client.download_media(message=replymsg.photo)
        elif "image" in replymsg.media.document.mime_type.split('/'):
            photo = await propic.client.download_file(replymsg.media.document)
        else:
            await propic.edit(INVALID_MEDIA)
    if photo:
        try:
            await propic.client(
                UploadProfilePhotoRequest(await
                                          propic.client.upload_file(photo)))
            os.remove(photo)
            await propic.edit(PP_CHANGED)
        except PhotoCropSizeSmallError:
            await propic.edit(PP_TOO_SMOL)
        except ImageProcessFailedError:
            await propic.edit(PP_ERROR)
        except PhotoExtInvalidError:
            await propic.edit(INVALID_MEDIA)


@javes05(outgoing=True, pattern="^!setbio (.*)")
async def set_biograph(setbio):    
    await setbio.edit("`Processing...`")
    newbio = setbio.pattern_match.group(1)  
    if setbio.is_channel and not setbio.is_group:
        await setbio.edit("`setbio Commad isn't permitted on channels`")
        return
    await setbio.client(UpdateProfileRequest(about=newbio))
    await setbio.edit(BIO_SUCCESS)


@javes05(outgoing=True, pattern="^!username (.*)")
async def update_username(username):
    """ For .username command, set a new username in Telegram. """
    await username.edit("`Processing...`")
    newusername = username.pattern_match.group(1) 
    if username.is_channel and not username.is_group:
        await username.edit("`username Commad isn't permitted on channels`")
        return
    try:
        await username.client(UpdateUsernameRequest(newusername))
        await username.edit(USERNAME_SUCCESS)
    except UsernameOccupiedError:
        await username.edit(USERNAME_TAKEN)


@javes05(outgoing=True, pattern="^!count$")
async def count(event):    
    u = 0
    g = 0
    c = 0
    bc = 0
    b = 0
    result = ""
    await event.edit("`Processing...`")
    dialogs = await bot.get_dialogs(limit=None, ignore_migrated=True)
    for d in dialogs:
        currrent_entity = d.entity
        if isinstance(currrent_entity, User):
            if currrent_entity.bot:
                b += 1
            else:
                u += 1
        elif isinstance(currrent_entity, Chat):
            g += 1
        elif isinstance(currrent_entity, Channel):
            if currrent_entity.broadcast:
                bc += 1
            else:
                c += 1
        else:
            print(d)
    result += f"`Users:`\t**{u}**\n"
    result += f"`Groups:`\t**{g}**\n"
    result += f"`Super Groups:`\t**{c}**\n"
    result += f"`Channels:`\t**{bc}**\n"
    result += f"`Bots:`\t**{b}**"
    await event.edit(result)


@javes05(outgoing=True, pattern=r"^!delpfp")
async def remove_profilepic(delpfp):
    """ For .delpfp command, delete your current profile picture in Telegram. """
    await delpfp.edit("`Processing...`")
    group = delpfp.text[8:]    
    if delpfp.is_channel and not delpfp.is_group:
        await delpfp.edit("`delpfp Commad isn't permitted on channels`")
        return
    if group == 'all':
        lim = 0
    elif group.isdigit():
        lim = int(group)
    else:
        lim = 1

    pfplist = await delpfp.client(
        GetUserPhotosRequest(user_id=delpfp.from_id,
                             offset=0,
                             max_id=0,
                             limit=lim))
    input_photos = []
    for sep in pfplist.photos:
        input_photos.append(
            InputPhoto(id=sep.id,
                       access_hash=sep.access_hash,
                       file_reference=sep.file_reference))
    await delpfp.client(DeletePhotosRequest(id=input_photos))
    await delpfp.edit(
        f"`Successfully deleted {len(input_photos)} profile picture(s).`")


CMD_HELP.update({
    "me":
    "`!username <new_username>`\
\n**Usage:** Changes your Telegram username.\
\n\n`!name <firstname> or !name <firstname> <lastname>`\
\n**Usage:** Changes your Telegram name.(First and last name will get split by the first space)\
\n\n`!setpfp`\
\n**Usage:** Reply with .setpfp to an image to change your Telegram profie picture.\
\n\n`!setbio <new_bio>`\
\n**Usage:** Changes your Telegram bio.\
\n\n`!delpfp <number>/<all>`\
\n**Usage:** Deletes your Telegram profile picture(s).\
\n\n`!reserved`\
\n**Usage:** Shows usernames reserved by you.\
\n\n`!count`\
\n**Usage:** Counts your groups, chats, bots etc..."
})
