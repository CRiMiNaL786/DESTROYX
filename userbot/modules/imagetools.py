#    Copyright (C) Midhun KM 2020
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.from shutil import rmtree
import os
from shutil import rmtree

import cv2
import numpy as np
import requests
from PIL import Image, ImageDraw, ImageFont
from telegraph import upload_file
from telethon.tl.types import MessageMediaPhoto

from userbot import CMD_HELP
from userbot.function import convert_to_image, crop_vid, runcmd
from userbot.utils import admin_cmd, sudo_cmd

sedpath = "./keinshin/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)


@borg.on(admin_cmd(pattern=r"cit"))
@borg.on(sudo_cmd(pattern=r"cit", allow_sudo=True))
async def hmm(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    hmmu = await event.edit("Colourzing..")
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    net = cv2.dnn.readNetFromCaffe(
        "./resources/imgcolour/colouregex.prototxt",
        "./resources/imgcolour/colorization_release_v2.caffemodel",
    )
    pts = np.load("./resources/imgcolour/pts_in_hull.npy")
    class8 = net.getLayerId("class8_ab")
    conv8 = net.getLayerId("conv8_313_rh")
    pts = pts.transpose().reshape(2, 313, 1, 1)
    net.getLayer(class8).blobs = [pts.astype("float32")]
    net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]
    image = cv2.imread(img)
    scaled = image.astype("float32") / 255.0
    lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)
    resized = cv2.resize(lab, (224, 224))
    L = cv2.split(resized)[0]
    L -= 50
    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0, :, :, :].transpose((1, 2, 0))
    ab = cv2.resize(ab, (image.shape[1], image.shape[0]))
    L = cv2.split(lab)[0]
    colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
    colorized = np.clip(colorized, 0, 1)
    colorized = (255 * colorized).astype("uint8")
    file_name = "Colour.png"
    ok = sedpath + "/" + file_name
    cv2.imwrite(ok, colorized)
    await borg.send_file(event.chat_id, ok)
    await hmmu.delete()
    for files in (ok, img):
        if files and os.path.exists(files):
            os.remove(files)


@borg.on(admin_cmd(pattern=r"toon"))
@borg.on(sudo_cmd(pattern=r"toon", allow_sudo=True))
async def hmm(event):
    life = Config.DEEP_API_KEY
    if life == None:
        life = "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"
        await event.edit("No Api Key Found, Please Add it. For Now Using Local Key")
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    headers = {"api-key": life}
    hmm = await event.edit("Toooning.....")
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    img_file = {
        "image": open(img, "rb"),
    }
    url = "https://api.deepai.org/api/toonify"
    r = requests.post(url=url, files=img_file, headers=headers).json()
    sedimg = r["output_url"]
    await borg.send_file(event.chat_id, sedimg)
    await hmm.delete()
    if os.path.exists(img):
        os.remove(img)


@borg.on(admin_cmd(pattern=r"nst"))
@borg.on(sudo_cmd(pattern=r"nst", allow_sudo=True))
async def hmm(event):
    life = Config.DEEP_API_KEY
    if life == None:
        life = "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"
        await event.edit("No Api Key Found, Please Add it. For Now Using Local Key")
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    headers = {"api-key": life}
    hmm = await event.edit("Colourzing..")
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    img_file = {
        "image": open(img, "rb"),
    }
    url = "https://api.deepai.org/api/nsfw-detector"
    r = requests.post(url=url, files=img_file, headers=headers).json()
    sedcopy = r["output"]
    hmmyes = sedcopy["detections"]
    game = sedcopy["nsfw_score"]
    final = f"**IMG RESULT** \n**Detections :** `{hmmyes}` \n**NSFW SCORE :** `{game}`"
    await borg.send_message(event.chat_id, final)
    await hmm.delete()
    if os.path.exists(img):
        os.remove(img)


@borg.on(admin_cmd(pattern=r"thug"))
@borg.on(sudo_cmd(pattern=r"thug", allow_sudo=True))
async def iamthug(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    hmm = await event.edit("`Converting To thug Image..`")
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    imagePath = img
    maskPath = "./resources/thuglife/mask.png"
    cascPath = "./resources/thuglife/face_regex.xml"
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
    file_name = "fridaythug.png"
    ok = sedpath + "/" + file_name
    background.save(ok, "PNG")
    await borg.send_file(event.chat_id, ok)
    await hmm.delete()
    for files in (ok, img):
        if files and os.path.exists(files):
            os.remove(files)


@borg.on(admin_cmd(pattern=r"tig"))
@borg.on(sudo_cmd(pattern=r"tig", allow_sudo=True))
async def lolmetrg(event):
    await event.edit("`Triggered This Image`")
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/triggered?avatar={imglink}"
    r = requests.get(lolul)
    open("triggered.gif", "wb").write(r.content)
    lolbruh = "triggered.gif"
    await borg.send_file(
        event.chat_id, lolbruh, caption="You got triggered....", reply_to=sed
    )
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)


@borg.on(admin_cmd(pattern=r"spin ?(.*)"))
@borg.on(sudo_cmd(pattern=r"spin ?(.*)", allow_sudo=True))
async def spinshit(message):
    reply = await message.get_reply_message()
    lmaodict = {"1": 1, "2": 3, "3": 6, "4": 12, "5": 24, "6": 60}
    lolshit = message.pattern_match.group(1)
    keke = f"{lolshit}"
    if not reply:
        await message.edit("`Reply To Media First !`")
        return
    else:
        if lolshit:
            step = lmaodict[keke]
        else:
            step = 1
    pic_loc = await convert_to_image(message, borg)
    if not pic_loc:
        await message.edit("`Reply to a valid media first.`")
        return
    await message.edit("🌀 `Tighten your seatbelts, sh*t is about to get wild ...`")
    spin_dir = 1
    path = "resources/rotate-disc/"
    if os.path.exists(path):
        rmtree(path, ignore_errors=True)
    os.mkdir(path)
    im = Image.open(pic_loc)
    if im.mode != "RGB":
        im = im.convert("RGB")
    # Rotating pic by given angle and saving
    for k, nums in enumerate(range(1, 360, step), start=0):
        y = im.rotate(nums * spin_dir)
        y.save(os.path.join(path, "spinx%s.jpg" % k))
    output_vid = os.path.join(path, "out.mp4")
    # ;__; Maths lol, y = mx + c
    frate = int(((90 / 59) * step) + (1680 / 59))
    # https://stackoverflow.com/questions/20847674/ffmpeg-libx264-height-not-divisible-by-2
    await runcmd(
        f'ffmpeg -framerate {frate} -i {path}spinx%d.jpg -c:v libx264 -preset ultrafast -vf "crop=trunc(iw/2)*2:trunc(ih/2)*2" -pix_fmt yuv420p {output_vid}'
    )
    if os.path.exists(output_vid):
        round_vid = os.path.join(path, "out_round.mp4")
        await crop_vid(output_vid, round_vid)
        await borg.send_file(
            message.chat_id, round_vid, video_note=True, reply_to=reply.id
        )
        await message.delete()
    os.remove(pic_loc)
    rmtree(path, ignore_errors=True)


@borg.on(admin_cmd(pattern=r"jail"))
@borg.on(sudo_cmd(pattern=r"jail", allow_sudo=True))
async def hmm(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    hmmu = await event.edit("hmm... Sending him to jail...🚶")
    await event.get_reply_message()
    img = await convert_to_image(event, borg)
    mon = "./resources/jail/hmm.png"
    foreground = Image.open(mon).convert("RGBA")

    background = Image.open(img).convert("RGB")
    with Image.open(img) as img:
        width, height = img.size
    fg_resized = foreground.resize((width, height))
    background.paste(fg_resized, box=(0, 0), mask=fg_resized)

    background.save("./keinshin/testing.png")

    file_name = "testing.png"
    ok = "./keinshin/" + file_name
    await borg.send_file(event.chat_id, ok)
    await hmmu.delete()
    for files in (ok, img):
        if files and os.path.exists(files):
            os.remove(files)


@borg.on(admin_cmd(pattern=r"greyscale"))
@borg.on(sudo_cmd(pattern=r"greyscale", allow_sudo=True))
async def hmm(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    hmmu = await event.edit("hmm.. Creating a black&White image...")
    await event.get_reply_message()
    img = await convert_to_image(event, borg)
    img1 = cv2.imread(img)

    gray_img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    cv2.imwrite("./keinshin/testing.png", gray_img)
    file_name = "testing.png"
    ok = "./keinshin/" + file_name
    await borg.send_file(event.chat_id, ok)
    await hmmu.delete()
    for files in (ok, img):
        if files and os.path.exists(files):
            os.remove(files)


# Plugin By - XlayerCharon[XCB]
# TG ~>>//@CharonCB21
# @code-rgb
@borg.on(admin_cmd(pattern=r"fgs ?(.*)"))
@borg.on(sudo_cmd(pattern=r"fgs ?(.*)", allow_sudo=True))
async def img(event):
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("No input found!")
        return
    if ";" in text:
        search, result = text.split(";", 1)
    else:
        event.edit("Invalid Input! Check help for more info!")
        return
    photo = Image.open("resources/dummy_image/fgs.jpg")
    drawing = ImageDraw.Draw(photo)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    font1 = ImageFont.truetype("Fonts/ProductSans-BoldItalic.ttf", 20)
    font2 = ImageFont.truetype("Fonts/ProductSans-Light.ttf", 23)
    drawing.text((450, 258), result, fill=blue, font=font1)
    drawing.text((270, 37), search, fill=black, font=font2)
    file_name = "fgs.jpg"
    ok = sedpath + "/" + file_name
    photo.save(ok)
    await event.delete()
    await friday.send_file(event.chat_id, ok)
    if os.path.exists(ok):
        os.remove(ok)


@borg.on(admin_cmd(pattern=r"lg"))
@borg.on(sudo_cmd(pattern=r"lg", allow_sudo=True))
async def lottiepie(event):
    await event.edit("`Prooooooccccesssssssinggggg.....`")
    message = await event.get_reply_message()
    if message.media and message.media.document:
        mime_type = message.media.document.mime_type
        if not "tgsticker" in mime_type:
            await event.edit("Not Supported Yet.")
            return
        await message.download_media("tgs.tgs")
        await runcmd("lottie_convert.py tgs.tgs json.json")
        json = open("json.json", "r")
        jsn = json.read()
        json.close()
        jsn = (
            jsn.replace("[1]", "[2]")
            .replace("[2]", "[3]")
            .replace("[3]", "[4]")
            .replace("[4]", "[5]")
            .replace("[5]", "[6]")
        )
        open("json.json", "w").write(jsn)
        await event.delete()
        await runcmd(f"lottie_convert.py json.json tgs.tgs")
        await borg.send_file(event.chat_id, file="tgs.tgs", force_document=False)
        os.remove("json.json")
        os.remove("tgs.tgs")


@borg.on(admin_cmd(pattern=r"ph ?(.*)"))
@borg.on(sudo_cmd(pattern=r"ph ?(.*)", allow_sudo=True))
async def img(event):
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("No input found!  --__--")
        return
    if ":" in text:
        username, texto = text.split(":", 1)
    else:
        event.edit("Invalid Input! Check help for more info!")
        return
    img = Image.open("./resources/pb/pb.jpg")
    d1 = ImageDraw.Draw(img)

    myFont = ImageFont.truetype("./resources/pb/font.TTF", 100)

    d1.text((300, 700), username, font=myFont, fill=(135, 98, 87))

    d1.text((12, 1000), texto, font=myFont, fill=(203, 202, 202))

    img.save("./keinshin/testpb.jpg")
    file_name = "testpb.jpg"
    ok = "./keinshin/" + file_name
    await borg.send_file(event.chat_id, ok)
    for files in (ok, img):
        if files and os.path.exists(files):
            os.remove(files)


CMD_HELP.update(
    {
        "imagetools": "**imagetools**\
        \n\n**Syntax : **`.cit`\
        \n**Usage :** colourizes the given picture.\
        \n\n**Syntax : **`.nst`\
        \n**Usage :** removes colours from image.\
        \n\n**Syntax : ** `.thug`\
        \n**Usage :** makes a thug life meme image.\
        \n\n**Syntax : ** `.tig`\
        \n**Usage :** Makes a triggered gif of the replied image.\
        \n\n**Syntax : ** `.jail`\
        \n**Usage :** Makes a jail image of the replied image.\
        \n\n**Syntax : ** `.fgs searchtext;fake text`\
        \n**Usage :** Makes a Fake Google Search Image.\
        \n\n**Syntax : ** `.ph username:fake text`\
        \n**Usage :** Makes a Fake PornHub comment with given username and text.\
        \n\n**Syntax : ** `.greyscale`\
        \n**Usage :** Makes a black and white image of the replied image."
    }
)
