from telethon import events
import subprocess, os , asyncio, PIL, cv2, shutil
from userbot.utils import admin_cmd
from userbot import CMD_HELP
import pygments, os, asyncio
from pygments.lexers import Python3Lexer
from pygments.formatters import ImageFormatter
from userbot.utils import admin_cmd
from userbot import bot
from userbot import bot as borg
import numpy as np
from PIL import Image, ImageDraw
@bot.on(admin_cmd(pattern="icircle", outgoing=True))
# By @shivam_patel
# Enhanced @danish_00
#dont kang
async def shiv(event):
    
    path = "shivamencircles"
    licence = event.text
    liscence=licence[8:]
    await event.delete()
    reply = await event.get_reply_message()
    
    download = await borg.download_media(reply.media, path)
    miraculous=cv2.VideoCapture(download)
    ladybug,catnoar = miraculous.read()
    cv2.imwrite("shivamcircular.png", catnoar)
    #image = PIL.Image.open(download)
    img=Image.open("shivamcircular.png").convert("RGB")
    npImage=np.array(img)
    h,w=img.size
    alpha = Image.new('L', img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0,0,h,w],0,360,fill=255)
    npAlpha=np.array(alpha)

    # Add alpha layer to RGB
    npImage=np.dstack((npImage,npAlpha))

    # Save with alpha
    Image.fromarray(npImage).save('sirsle.png')
    #await event.edit(f"Dimensions Of Image are {shi} by {vam}")
    #img.save("sh1vam.png", format="PNG", optimize=True)
    await event.client.send_file(event.chat_id, "sirsle.png", force_document=True, reply_to=event.reply_to_msg_id)
    await event.client.send_file(event.chat_id, "sirsle.png", force_document=False, reply_to=event.reply_to_msg_id)
    os.remove(download)
    os.remove("sirsle.png")
    os.remove("shivamcircular.png")



path = "./dcobra/"
if not os.path.isdir(path):
    os.makedirs(path)

@bot.on(admin_cmd(pattern="scircle", outgoing=True))
async def shiv(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any media.")
        return
    licence = event.text
    liscence=licence[8:]
    await event.edit("```Processing...```")
    reply = await event.get_reply_message()
    download = await bot.download_media(reply.media, path)
    danish = cv2.VideoCapture(download) 
    ret, frame = danish.read()
    cv2.imwrite("danish.jpg", frame)
    img=Image.open("danish.jpg").convert("RGB")
    npImage=np.array(img)
    h,w=img.size
    alpha = Image.new('L', img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0,0,h,w],0,360,fill=255)
    npAlpha=np.array(alpha)
    npImage=np.dstack((npImage,npAlpha))
    Image.fromarray(npImage).save('shivam.webp')
    await event.client.send_file(event.chat_id, "shivam.webp", force_document=False, reply_to=event.reply_to_msg_id)
    shutil.rmtree(path)
    os.remove("shivam.webp")
    os.remove("danish.jpg")










    
