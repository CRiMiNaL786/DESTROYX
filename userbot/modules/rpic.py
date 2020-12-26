from PIL import Image
import sys
import os
from userbot.utils import admin_cmd
from userbot import bot 
from userbot import bot as borg
if not os.path.isdir("./rpic/"):
    os.makedirs("./rpic/")


@bot.on(admin_cmd(pattern=r"rpic"))
async def scan(event):
    path = "rpic"
     
    kk = await event.delete()

    reply = await event.get_reply_message()
    
    lol = await borg.download_media(reply.media, path)
    linc = event.text
    link=linc[6:]
    pic=linc[30:]
    import cv2
 
    
    os.system(f'wget {link}')

    imagePath = lol
    
    maskPath = f"{pic}"
    
    cascPath = "haarcascade_frontalface_default.xml"
   
    faceCascade = cv2.CascadeClassifier(cascPath)
   
    image = cv2.imread(imagePath)
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    faces = faceCascade.detectMultiScale(gray, 1.15)
   
    background = Image.open(imagePath)
   
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
   
    file_name = "rpic.png"
   
    hehe = path + "/" + file_name
   
    background.save(hehe, "PNG")
   
    await borg.send_file(event.chat_id, hehe)
   

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
@bot.on(admin_cmd(pattern=r"crpic"))
async def scan(event):
    path = "rpic"
     
    kk = await event.delete()

    reply = await event.get_reply_message()
    
    lol = await borg.download_media(reply.media, path)
    linc = event.text
    link=linc[7:]
    pic=linc[31:]
    import cv2
 
    
    os.system(f'wget {link}')

    imagePath = lol
    
    maskPath = f"{pic}"
    
    cascPath = "haarcascade_frontalcatface.xml"
   
    faceCascade = cv2.CascadeClassifier(cascPath)
   
    image = cv2.imread(imagePath)
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    faces = faceCascade.detectMultiScale(gray, 1.15)
   
    background = Image.open(imagePath)
   
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
   
    file_name = "rpic.png"
   
    hehe = path + "/" + file_name
   
    background.save(hehe, "PNG")
   
    await borg.send_file(event.chat_id, hehe)
   

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
