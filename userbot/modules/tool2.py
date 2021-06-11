from telethon import events, types
import os, asyncio, zipfile, time, json, requests, aiohttp, pytz, math, io
from PIL import Image
from pySmartDL import SmartDL
from datetime import datetime, date
from telegraph import Telegraph, upload_file, exceptions
from userbot import (TEMP_DOWNLOAD_DIRECTORY, BOTLOG_CHATID, CMD_HELP, bot, client)
from userbot.events import javes05, rekcah05
try:
  import pyfiglet
except:
   pass
from io import BytesIO
from asyncio import sleep
from telethon.tl import functions, types
from telethon.errors import PhotoInvalidDimensionsError
from telethon.tl.functions.messages import SendMediaRequest
from userbot.events import humanbytes, progress, time_formatter
javes = client
thumb_image_path = TEMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"
extracted = TEMP_DOWNLOAD_DIRECTORY + "extracted/"
if not os.path.isdir(extracted):
    os.makedirs(extracted)
ZIP_DOWNLOAD_DIRECTORY = TEMP_DOWNLOAD_DIRECTORY
import time as t
x = math.inf
counter = 0
start=t.time()
telegraph = Telegraph()
javes = bot
today = date.today()
r = telegraph.create_account(short_name="telegraph")
auth_url = r["auth_url"]

SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_KEY", None)

def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
            os.remove(os.path.join(root, file))

def get_lst_of_files(input_directory, output_lst):
    filesinfolder = os.listdir(input_directory)
    for file_name in filesinfolder:
        current_file_name = os.path.join(input_directory, file_name)
        if os.path.isdir(current_file_name):
            return get_lst_of_files(current_file_name, output_lst)
        output_lst.append(current_file_name)
    return output_lst

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
            os.remove(os.path.join(root, file))




@javes.on(rekcah05(pattern=f"telegraph (media|text)$", allow_sudo=True))
@javes05(outgoing=True, pattern="^!telegraph (media|text)$")
async def telegraphs(graph):    
  try:
    sender = await graph.get_sender() ; me = await graph.client.get_me()
    if not sender.id == me.id:
        rkp = await graph.reply("`processing`")
    else:
    	rkp = await graph.edit("`processing`")
    if graph.text[0].isalpha() or graph.text[0] in ("/", "#", "@") or graph.fwd_from:
        return 
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if graph.reply_to_msg_id:
        start = datetime.now()
        r_message = await graph.get_reply_message()
        input_str = graph.pattern_match.group(1)        
        if input_str == "media":
            downloaded_file_name = await bot.download_media( r_message, TEMP_DOWNLOAD_DIRECTORY )
            end = datetime.now()
            ms = (end - start).seconds
            await rkp.edit("Downloaded to {} in {} seconds.".format(downloaded_file_name, ms))
            if downloaded_file_name.endswith((".webp")):
                resize_image(downloaded_file_name)
            try:
                start = datetime.now()
                media_urls = upload_file(downloaded_file_name)
            except exceptions.TelegraphException as exc:
                await rkp.edit("ERROR: " + str(exc))
                os.remove(downloaded_file_name)
            else:
                end = datetime.now()
                ms_two = (end - start).seconds
                os.remove(downloaded_file_name)
                await rkp.edit("Uploaded to https://telegra.ph{} in {} seconds.".format(media_urls[0], (ms + ms_two)), link_preview=True)
        elif input_str == "text":
            user_object = await bot.get_entity(r_message.from_id)
            title_of_page = user_object.first_name # + " " + user_object.last_name            
            page_content = r_message.message
            if r_message.media:
                if page_content != "":
                    title_of_page = page_content
                downloaded_file_name = await bot.download_media( r_message, TEMP_DOWNLOAD_DIRECTORY )
                m_list = None
                with open(downloaded_file_name, "rb") as fd:
                    m_list = fd.readlines()
                for m in m_list:
                    page_content += m.decode("UTF-8") + "\n"
                os.remove(downloaded_file_name)
            page_content = page_content.replace("\n", "<br>")
            response = telegraph.create_page( title_of_page, html_content=page_content )
            end = datetime.now()
            ms = (end - start).seconds
            await rkp.edit("Pasted to https://telegra.ph/{} in {} seconds.".format(response["path"], ms), link_preview=True)
    else:
        await rkp.edit("Reply to a message to get a permanent telegra.ph link.")
  except:
  	await rkp.edit("Error.")


@javes.on(rekcah05(pattern=f"figlet(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^\!figlet(?: |$)(.*)")
async def figlet(e):
    sender = await e.get_sender() ; me = await e.client.get_me()
    if not sender.id == me.id:
        rkp = await e.reply("`processing`")
    else:
    	rkp = await e.edit("`processing`")
    if e.fwd_from:
        return
    CMD_FIG = {"slant": "slant", "3D": "3-d", "5line": "5lineoblique", "alpha": "alphabet", "banner": "banner3-D", "doh": "doh", "iso": "isometric1", "letter": "letters", "allig": "alligator", "dotm": "dotmatrix", "bubble": "bubble", "bulb": "bulbhead", "digi": "digital"}
    input_str = e.pattern_match.group(1)
    if "." in input_str:
        text, cmd = input_str.split(".", maxsplit=1)
    elif input_str is not None:
        cmd = None
        text = input_str
    else:
        await rkp.edit("`Please add some text to figlet`")
        return
    if cmd is not None:
        try:
            font = CMD_FIG[cmd]
        except KeyError:
            await rkp.edit("`Invalid selected font.`")
            return
        result = pyfiglet.figlet_format(text, font=font)
    else:
        result = pyfiglet.figlet_format(text)
    await e.respond("‌‌‎`{}`".format(result))
    await e.delete()
 
@javes.on(rekcah05(pattern=f"docpic(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^\!docpic(?: |$)(.*)")
async def on_file_to_photo(pics):
    sender = await pics.get_sender() ; me = await pics.client.get_me()
    if not sender.id == me.id:
        rkp = await pics.reply("`processing`")
    else:
    	rkp = await pics.edit("`processing`")
    await rkp.edit("Converting Document image to Full Size Image\nPlease wait...")
    await sleep(2.5)
    await pics.delete()
    target = await pics.get_reply_message()
    try:
        image = target.media.document
    except AttributeError:
        return
    if not image.mime_type.startswith('image/'):
        return  
    if image.mime_type == 'image/webp':
        return  
    if image.size > 10 * 2560 * 1440:
        return  

    file = await pics.client.download_media(target, file=BytesIO())
    file.seek(0)
    img = await pics.client.upload_file(file)
    img.name = 'image.png'
    try:
        await pics.client(SendMediaRequest( peer=await pics.get_input_chat(), media=types.InputMediaUploadedPhoto(img), message=target.message, entities=target.entities, reply_to_msg_id=target.id ))
    except PhotoInvalidDimensionsError:
        return await pics.reply("Error")

@javes.on(rekcah05(pattern=f"ifsc(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!ifsc(.*)")
async def _(event):
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing`")
    else:
    	rkp = await event.edit("`processing`")
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    url = "https://ifsc.razorpay.com/{}".format(input_str)
    r = requests.get(url)
    if r.status_code == 200:
        b = r.json()
        a = json.dumps(b, sort_keys=True, indent=4)        
        await rkp.edit(str(a))
    else:
        await rkp.edit("`{}`: {}\nhttps://ifsc.razorpay.com".format(input_str, r.text))

@javes.on(rekcah05(pattern=f"zip$", allow_sudo=True))
@javes05(outgoing=True, pattern="^!zip$")
async def _(event):
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing`")
    else:
    	rkp = await event.edit("`processing`")
    if event.fwd_from:
        return
    if not event.is_reply:
        await rkp.edit("Reply to a file to compress it.")
        return
    mone = await rkp.edit("Processing ...")
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        try:
            c_time = t.time()
            downloaded_file_name = await bot.download_media(
                reply_message,
                TEMP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "trying to download")
                )
            )
            directory_name = downloaded_file_name
            await rkp.edit(downloaded_file_name)
        except Exception as e:  # pylint:disable=C0103,W0703
            await rkp.edit(str(e))
    zipfile.ZipFile(directory_name + '.zip', 'w', zipfile.ZIP_DEFLATED).write(directory_name)
    await bot.send_file(
        event.chat_id,
        directory_name + ".zip",
        caption="Zipped ",
        force_document=True,
        allow_cache=False,
        reply_to=event.message.id,
    )
    await rkp.edit("DONE!!!")
    await asyncio.sleep(7)
    await event.delete()



@javes.on(rekcah05(pattern=f"unzip$", allow_sudo=True))
@javes05(outgoing=True, pattern="^!unzip$")
async def _(event):
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing`")
    else:
    	rkp = await event.edit("`processing`")
    if event.fwd_from:
        return
    mone = await rkp.edit("Processing ...")
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        start = datetime.now()
        reply_message = await event.get_reply_message()
        try:
            c_time = t.time()
            downloaded_file_name = await bot.download_media(
                reply_message,
                TEMP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "trying to download")
                )
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await rkp.edit(str(e))
        else:
            end = datetime.now()
            ms = (end - start).seconds
            await rkp.edit("Stored the zip to `{}` in {} seconds.".format(downloaded_file_name, ms))

        with zipfile.ZipFile(downloaded_file_name, 'r') as zip_ref:
            zip_ref.extractall(extracted)
        filename = sorted(get_lst_of_files(extracted, []))
        #filename = filename + "/"
        await rkp.edit("Unzipping now")
        # r=root, d=directories, f = files
        for single_file in filename:
            if os.path.exists(single_file):
                # https://stackoverflow.com/a/678242/4723940
                caption_rts = os.path.basename(single_file)
                force_document = True
                supports_streaming = False
                document_attributes = []
                if single_file.endswith((".mp4", ".mp3", ".flac", ".webm")):
                    metadata = extractMetadata(createParser(single_file))
                    duration = 0
                    width = 0
                    height = 0
                    if metadata.has("duration"):
                        duration = metadata.get('duration').seconds
                    if os.path.exists(thumb_image_path):
                        metadata = extractMetadata(createParser(thumb_image_path))
                        if metadata.has("width"):
                            width = metadata.get("width")
                        if metadata.has("height"):
                            height = metadata.get("height")
                    document_attributes = [
                        DocumentAttributeVideo(
                            duration=duration,
                            w=width,
                            h=height,
                            round_message=False,
                            supports_streaming=True
                        )
                    ]
                try:
                    await bot.send_file(
                        event.chat_id,
                        single_file,
                        caption=f"UnZipped `{caption_rts}`",
                        force_document=force_document,
                        supports_streaming=supports_streaming,
                        allow_cache=False,
                        reply_to=event.message.id,
                        attributes=document_attributes,
                        # progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                        #     progress(d, t, event, c_time, "trying to upload")
                        # )
                    )
                except Exception as e:
                    await bot.send_message(
                        event.chat_id,
                        "{} caused `{}`".format(caption_rts, str(e)),
                        reply_to=event.message.id
                    )
                    # some media were having some issues
                    continue
                os.remove(single_file)
        os.remove(downloaded_file_name)





@javes.on(rekcah05(pattern=f"dns (.*)", allow_sudo=True))
@javes05(outgoing=True, pattern=r"^!dns (.*)")
async def _(event):
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing`")
    else:
    	rkp = await event.edit("`processing`")
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/dns/{}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await rkp.edit("DNS records of {} are \n{}".format(input_str, response_api))
    else:
        return await rkp.edit("i can't seem to find {} on the internet".format(input_str))


@javes.on(rekcah05(pattern=f"urlshort (.*)", allow_sudo=True))
@javes05(outgoing=True, pattern=r"^!urlshort (.*)")
async def _(event):
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing`")
    else:
    	rkp = await event.edit("`processing`")
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        return await rkp.edit("Generated {} for {}.".format(response_api, input_str))
    else:
        return await rkp.edit("something is wrong. please try again later.")

@javes.on(rekcah05(pattern=f"urldirect (.*)", allow_sudo=True))
@javes05(outgoing=True, pattern=r"^!urldirect (.*)")
async def _(event):
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing`")
    else:
    	rkp = await event.edit("`processing`")
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if not input_str.startswith("http"):
        input_str = "http://" + input_str
    r = requests.get(input_str, allow_redirects=False)
    if str(r.status_code).startswith('3'):
        return await rkp.edit("Input URL: {}\nReDirected URL: {}".format(input_str, r.headers["Location"]))
    else:
        return await rkp.edit("Input URL {} returned status_code {}".format(input_str, r.status_code))


@javes.on(rekcah05(pattern=f"git (.*)", allow_sudo=True))
@javes05(pattern=r"!git (.*)", outgoing=True)
async def github(event):
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing`")
    else:
    	rkp = await event.edit("`processing`")
    URL = f"https://api.github.com/users/{event.pattern_match.group(1)}"
    chat = await event.get_chat()
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                await event.reply("`" + event.pattern_match.group(1) +
                                  " not found`")
                return
            result = await request.json()
            url = result.get("html_url", None)
            name = result.get("name", None)
            company = result.get("company", None)
            bio = result.get("bio", None)
            created_at = result.get("created_at", "Not Found")
            REPLY = f"GitHub Info for `{event.pattern_match.group(1)}`\
            \nUsername: `{name}`\
            \nBio: `{bio}`\
            \nURL: {url}\
            \nCompany: `{company}`\
            \nCreated at: `{created_at}`"
            if not result.get("repos_url", None):
                await rkp.edit(REPLY)
                return
            async with session.get(result.get("repos_url", None)) as request:
                result = request.json
                if request.status == 404:
                    await rkp.edit(REPLY)
                    return
                result = await request.json()
                REPLY += "\nRepos:\n"
                for nr in range(len(result)):
                    REPLY += f"[{result[nr].get('name', None)}]({result[nr].get('html_url', None)})\n"
                return await rkp.edit(REPLY)


@javes.on(rekcah05(pattern=f"create (b|g|c)(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!create (b|g|c)(?: |$)(.*)")
async def telegraphs(grop):    
    sender = await grop.get_sender() ; me = await grop.client.get_me()
    if not sender.id == me.id:
        rkp = await grop.reply("`processing`")
    else:
    	rkp = await grop.edit("`processing`")
    if not grop.text[0].isalpha() and grop.text[0] not in ("/", "#", "@"):
        if grop.fwd_from:
            return
        type_of_group = grop.pattern_match.group(1)
        group_name = grop.pattern_match.group(2)
        if type_of_group == "b":
            try:
                result = await grop.client(functions.messages.CreateChatRequest(  # pylint:disable=E0602
                    users=["@MissRose_bot"],                    
                    title=group_name
                ))
                created_chat_id = result.chats[0].id
                await grop.client(functions.messages.DeleteChatUserRequest(
                    chat_id=created_chat_id,
                    user_id="@MissRose_bot"
                ))
                result = await grop.client(functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                ))
                await rkp.edit("Your `{}` Group Created Successfully. Click [{}]({}) to join".format(group_name, group_name, result.link))
            except Exception as e:  
                await rkp.edit(str(e))
        elif type_of_group == "g" or type_of_group == "c":
            try:
                r = await grop.client(functions.channels.CreateChannelRequest(  # pylint:disable=E0602
                    title=group_name,
                    about="Welcome ",
                    megagroup=False if type_of_group == "c" else True
                ))
                created_chat_id = r.chats[0].id
                result = await grop.client(functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                ))
                return await rkp.edit("Your `{}` Group/Channel Created Successfully. Click [{}]({}) to join".format(group_name, group_name, result.link))
            except Exception as e:  
                return await rkp.edit(str(e))

@javes.on(rekcah05(pattern=f"poll(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!poll(.*)")
async def _(event):
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing`")
    else:
    	rkp = await event.edit("`processing`")
    reply_message = await event.get_reply_message()
    if not reply_message:
    	return await rkp.edit("Please reply to a poll")
    if reply_message.media is None:
        return await rkp.edit("Please reply to a poll")
    elif reply_message.media.poll is None:
        return await rkp.edit("Please reply to a poll")
    else:
        media = reply_message.media
        poll = media.poll
        closed_status = poll.closed
        answers = poll.answers
        question = poll.question
        edit_caption = """Poll is Closed: {}
Question: {}
Answers: \n""".format(closed_status, question)
        if closed_status:
            results = media.results
            i = 0
            for result in results.results:
                edit_caption += "{}> {}    {}\n".format(result.option, answers[i].text, result.voters)
                i += 1
            edit_caption += "Total Voters: {}".format(results.total_voters)
        else:
            for answer in answers:
                edit_caption += "{}> {}\n".format(answer.option, answer.text)
        return await rkp.edit(edit_caption)


@javes.on(rekcah05(pattern=f"goss(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!goss(.*)")
async def _(event):
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing`")
    else:
    	rkp = await event.edit("`processing`")
    if SCREEN_SHOT_LAYER_ACCESS_KEY is None:
        await rkp.edit("Add var SCREEN_SHOT_KEY , API key from https://screenshotlayer.com/product !")
        return
    await rkp.edit("Processing ...")
    sample_url = "https://api.screenshotlayer.com/api/capture?access_key={}&url={}&fullpage={}&viewport={}&format={}&force={}"
    input_str = event.pattern_match.group(1)
    response_api = requests.get(sample_url.format(
        SCREEN_SHOT_LAYER_ACCESS_KEY,
        input_str,
        "1",
        "2560x1440",
        "PNG",
        "1"
    ))    
    contentType = response_api.headers['content-type']
    if "image" in contentType:
        with io.BytesIO(response_api.content) as screenshot_image:
            screenshot_image.name = "screencapture.png"
            try:
                await borg.send_file(
                    event.chat_id,
                    screenshot_image,
                    caption=input_str,
                    force_document=True,
                    reply_to=event.message.reply_to_msg_id
                )
                await rkp.delete()
            except Exception as e:
                await rkp.edit(str(e))
    else:
        await rkp.edit(response_api.text)




CMD_HELP.update({
    "tools2":
"`!telegraph media / text <reply to a media / message >`\
\n**Usage:**  Upload text & media on Telegraph\
\n\n`!figlet `<text.style>\
\n**Usage:**  Enhance ur text Styles (`slant`, `3D`, `5line`, `alpha`, `banner`, `doh`, `iso`, `letter`, `allig`, `dotm`, `bubble`, `bulb`, `digi`)\
\n\n`!docpic `<reply to a img>\
\n**Usage:**  Convert any Document Image to Full Size Image.\
\n\n`!ifsc` <code>\
\n**Usage:**  Find bank details through ifsc code.\
\n\n`!zip `<Reply to a media>\
\n**Usage:**  make files to zip..\
\n\n`!unzip` <reply to a media>\
\n**Usage:**  upload zip list.!!\
\n\n`!dns `<link>\
\n**Usage:**  give dns records .\
\n\n`!urlshort` <link>\
\n**Usage:**  shorten url.\
\n\n`!urldirect` <link>\
\n**Usage:** get direct url from  shorten url.\
\n\n`!git` <account name>\
\n**Usage:** get github account information.\
\n\n`!create g` <name>\
\n**Usage:** Create a Private super Group .\
\n\n`!create b` < name>\
\n**Usage:** Create a Group with Bot.\
\n\n`!create c` <name>\
\n**Usage:** Create a Channel..\
\n\n`!poll` <reply to a poll>\
\n**Usage:** Get poll details..\
\n\n`!goss` <link>\
\n**Usage:** Takes a screenshot of a website and sends the screenshot.\
\n\n**All commands support sudo , type !help sudo for more info**\
"
})














