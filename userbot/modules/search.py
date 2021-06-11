
#telegram javes05




from telethon import *
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.events import javes05, rekcah05
from userbot import CMD_HELP, ALIVE_NAME, PM_MESSAGE, JAVES_NAME, JAVES_MSG, ORI_MSG, bot, TEMP_DOWNLOAD_DIRECTORY, BOTLOG, BOTLOG_CHATID
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)
import subprocess, io, asyncio, time, glob, os, datetime, re, json, shutil, bs4, requests, json, io
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
javes = bot
try:
  import asyncurban
except:
   pass
from bs4 import BeautifulSoup
from html import unescape
from re import findall
from random import choice
from difflib import get_close_matches
from urllib.parse import quote_plus
from urllib.error import HTTPError
from wikipedia import summary
from wikipedia.exceptions import DisambiguationError, PageError
from urbandict import define
from requests import get
from search_engine_parser import GoogleSearch
try:
  from googleapiclient.discovery import build
  from googleapiclient.errors import HttpError
  from googletrans import LANGUAGES, Translator
except:
   pass
from gtts import gTTS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from emoji import get_emoji_regexp
from asyncio import sleep
from userbot.events import register
from telethon.tl.types import DocumentAttributeAudio
from userbot.javes_main.commands import progress
from userbot.javes_main.extra.google_images_download import googleimagesdownload
from datetime import datetime
from PIL import Image
import urllib
from telethon.tl.types import MessageMediaPhoto
from urllib.request import urlopen
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.tl.types import DocumentAttributeVideo
try:
   from userbot.javes_main.commands import meaning
except:
   pass

opener = urllib.request.build_opener() ; useragent = 'Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.70 Mobile Safari/537.36' ; opener.addheaders = [('User-agent', useragent)]

async def devices_specifimions(request):
    textx = await request.get_reply_message()
    brand = request.pattern_match.group(1).lower()
    device = request.pattern_match.group(2).lower()
    if brand and device:
        pass
    elif textx:
        brand = textx.text.split(' ')[0]
        device = ' '.join(textx.text.split(' ')[1:])
    else:
        await request.reply("`**Usage:** !specs <brand> <device>`")
        return
    all_brands = BeautifulSoup(
        get('https://www.devicespecifications.com/en/brand-more').content,
        'lxml').find('div', {
            'class': 'brand-listing-container-news'
        }).findAll('a')
    brand_page_url = None
    try:
        brand_page_url = [
            i['href'] for i in all_brands if brand == i.text.strip().lower()
        ][0]
    except IndexError:
        await rkp.edit(f'`{brand} is unknown brand!`')
    devices = BeautifulSoup(get(brand_page_url).content, 'lxml') \
        .findAll('div', {'class': 'model-listing-container-80'})
    device_page_url = None
    try:
        device_page_url = [
            i.a['href']
            for i in BeautifulSoup(str(devices), 'lxml').findAll('h3')
            if device in i.text.strip().lower()
        ]
    except IndexError:
        await request.reply(f"`can't find {device}!`")
    if len(device_page_url) > 2:
        device_page_url = device_page_url[:2]
    reply = ''
    for url in device_page_url:
        info = BeautifulSoup(get(url).content, 'lxml')
        reply = '\n' + info.title.text.split('-')[0].strip() + '\n'
        info = info.find('div', {'id': 'model-brief-specifimions'})
        specifimions = re.findall(r'<b>.*?<br/>', str(info))
        for item in specifimions:
            title = re.findall(r'<b>(.*?)</b>', item)[0].strip()
            data = re.findall(r'</b>: (.*?)<br/>', item)[0] \
                .replace('<b>', '').replace('</b>', '').strip()
            reply += f'**{title}**: {data}\n'
    await request.reply(reply)
 
async def ParseSauce(googleurl):   
    source = opener.open(googleurl).read()
    soup = BeautifulSoup(source, 'html.parser')
    results = {'similar_images': '', 'best_guess': ''}
    try:
        for similar_image in soup.findAll('input', {'class': 'gLFyf'}):
            url = 'https://www.google.com/search?tbm=isch&q=' + \
                urllib.parse.quote_plus(similar_image.get('value'))
            results['similar_images'] = url
    except BaseException:
        pass
    for best_guess in soup.findAll('div', attrs={'class': 'r5a77d'}):
        results['best_guess'] = best_guess.get_text()
    return results

async def scam(results, lim):
    single = opener.open(results['similar_images']).read()
    decoded = single.decode('utf-8')
    imglinks = []
    counter = 0
    pattern = r'^,\[\"(.*[!png|!jpg|!jpeg])\",[0-9]+,[0-9]+\]$'
    oboi = re.findall(pattern, decoded, re.I | re.M)
    for imglink in oboi:
        counter += 1
        if not counter >= int(lim):
            imglinks.append(imglink)
        else:
            break
    return imglinks


  
async def chrome(chrome_options=None):
    if chrome_options is None:
        chrome_options = await options()
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.mkdir(TEMP_DOWNLOAD_DIRECTORY)
    prefs = {'download.default_directory': TEMP_DOWNLOAD_DIRECTORY}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER,
                              options=chrome_options)
    return driver
    



GITHUB = 'https://github.com'
DEVICES_DATA = 'https://raw.githubusercontent.com/androidtrackers/' \
               'certified-android-devices/master/devices.json'

@javes.on(rekcah05(pattern=f"app (.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!app (.*)")
async def apk(e):
    sender = await e.get_sender() ; me = await e.client.get_me()
    if not sender.id == me.id:
        rkp = await e.reply("`processing...`")
    else:
    	rkp = await e.edit("`processing...`")
    try:
        app_name = e.pattern_match.group(1)
        remove_space = app_name.split(' ')
        final_name = '+'.join(remove_space)
        page = requests.get("https://play.google.com/store/search?q="+final_name+"&c=apps")
        lnk = str(page.status_code)
        soup = bs4.BeautifulSoup(page.content,'lxml', from_encoding='utf-8')
        results = soup.findAll("div","ZmHEEd")
        app_name = results[0].findNext('div', 'Vpfmgd').findNext('div', 'WsMG1c nnK0zc').text
        app_dev = results[0].findNext('div', 'Vpfmgd').findNext('div', 'KoLSrc').text
        app_dev_link = "https://play.google.com"+results[0].findNext('div', 'Vpfmgd').findNext('a', 'mnKHRc')['href']
        app_rating = results[0].findNext('div', 'Vpfmgd').findNext('div', 'pf5lIe').find('div')['aria-label']
        app_link = "https://play.google.com"+results[0].findNext('div', 'Vpfmgd').findNext('div', 'vU6FJ p63iDd').a['href']
        app_icon = results[0].findNext('div', 'Vpfmgd').findNext('div', 'uzcko').img['data-src']
        app_details = "<a href='"+app_icon+"'📲&#8203;</a>"
        app_details += " <b>"+app_name+"</b>"
        app_details += "\n\n<code>Developer :</code> <a href='"+app_dev_link+"'>"+app_dev+"</a>"
        app_details += "\n<code>Rating :</code> "+app_rating.replace("Rated ", "⭐ ").replace(" out of ", "/").replace(" stars", "", 1).replace(" stars", "⭐ ").replace("five", "5")
        app_details += "\n<code>Features :</code> <a href='"+app_link+"'>View in Play Store</a>"      
        await rkp.edit(app_details, link_preview = True, parse_mode = 'HTML')
    except IndexError:
        await rkp.edit("No result found in search. Please enter **Valid app name**")
    except Exception as err:
        await rkp.edit("Exception Occured:- "+str(err))


@javes.on(rekcah05(pattern=f"ggl (.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!ggl (.*)")
async def let_me_google_that_for_you(lmgtfy_q):
    sender = await lmgtfy_q.get_sender() ; me = await lmgtfy_q.client.get_me()
    if not sender.id == me.id:
        rkp = await lmgtfy_q.reply("`processing...`")
    else:
    	rkp = await lmgtfy_q.edit("`processing...`")
    textx = await lmgtfy_q.get_reply_message()
    qry = lmgtfy_q.pattern_match.group(1)
    if qry:
        query = str(qry)
    elif textx:
        query = textx
        query = query.message
    query_encoded = query.replace(" ", "+")
    lfy_url = f"http://lmgtfy.com/?s=g&iie=1&q={query_encoded}"
    payload = {'format': 'json', 'url': lfy_url}
    r = requests.get('http://is.gd/create.php', params=payload)
    await rkp.edit(f"Tap this blue, help yourself.\
    \n[{query}]({r.json()['shorturl']})")


@javes05(outgoing=True, pattern="^\!currency (.*)")
@javes.on(rekcah05(pattern=f"currency (.*)", allow_sudo=True))
async def moni(event):
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
    else:
    	rkp = await event.edit("`processing...`")
    input_str = event.pattern_match.group(1)
    input_sgra = input_str.split(" ")
    if len(input_sgra) == 3:
        try:
            number = float(input_sgra[0])
            currency_from = input_sgra[1].upper()
            currency_to = input_sgra[2].upper()
            request_url = "https://api.exchangeratesapi.io/latest?base={}".format(
                currency_from)
            current_response = get(request_url).json()
            if currency_to in current_response["rates"]:
                current_rate = float(current_response["rates"][currency_to])
                rebmun = round(number * current_rate, 2)
                await rkp.edit("{} {} = {} {}".format(
                    number, currency_from, rebmun, currency_to))
            else:
                await rkp.edit(
                    "`unknown currency, which I can't convert right now.`"
                )
        except Exception as e:
            await rkp.edit(str(e))
    else:
        await rkp.edit("`Use currency <amount> <from> <to>`")
        return


@javes05(outgoing=True, pattern="^!img (.*)")
@javes.on(rekcah05(pattern=f"img (.*)", allow_sudo=True))
async def img_sampler(event):
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
    else:
    	rkp = await event.edit("`processing...`")   
    query = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif query:
        query = reply.message
    else:
    	await rkp.edit(f"**I  need Something to Search **")
    	return      
    lim = findall(r"max\d+", query)
    try:
        lim = lim[0]
        lim = lim.replace("max", "")
        query = query.replace("max" + lim[0], "")
    except IndexError:
        lim = 3
    response = googleimagesdownload()
    arguments = {
        "keywords": query,
        "limit": lim,
        "format": "jpg",
        "no_directory": "no_directory"
    }
    paths = response.download(arguments)
    lst = paths[0][query]
    await event.client.send_file(await event.client.get_input_entity(event.chat_id), lst, reply_to=event.message.reply_to_msg_id)
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    return await rkp.delete()


@javes.on(rekcah05(pattern=f"movie (.*)", allow_sudo=True))
@register(outgoing=True, pattern="^!movie (.*)")
async def imdb(e):
    sender = await e.get_sender() ; me = await e.client.get_me()
    if not sender.id == me.id:
        rkp = await e.reply("`processing...`")
    else:
    	rkp = await e.edit("`processing...`")   
    try:
        movie_name = e.pattern_match.group(1)
        remove_space = movie_name.split(' ')
        final_name = '+'.join(remove_space)
        page = get("https://www.imdb.com/find?ref_=nv_sr_fn&q=" + final_name +
                   "&s=all")
        soup = BeautifulSoup(page.content, 'lxml')
        odds = soup.findAll("tr", "odd")
        mov_title = odds[0].findNext('td').findNext('td').text
        mov_link = "http://www.imdb.com/" + \
            odds[0].findNext('td').findNext('td').a['href']
        page1 = get(mov_link)
        soup = BeautifulSoup(page1.content, 'lxml')
        if soup.find('div', 'poster'):
            poster = soup.find('div', 'poster').img['src']
        else:
            poster = ''
        if soup.find('div', 'title_wrapper'):
            pg = soup.find('div', 'title_wrapper').findNext('div').text
            mov_details = re.sub(r'\s+', ' ', pg)
        else:
            mov_details = ''
        credits = soup.findAll('div', 'credit_summary_item')
        if len(credits) == 1:
            director = credits[0].a.text
            writer = 'Not available'
            stars = 'Not available'
        elif len(credits) > 2:
            director = credits[0].a.text
            writer = credits[1].a.text
            actors = []
            for x in credits[2].findAll('a'):
                actors.append(x.text)
            actors.pop()
            stars = actors[0] + ',' + actors[1] + ',' + actors[2]
        else:
            director = credits[0].a.text
            writer = 'Not available'
            actors = []
            for x in credits[1].findAll('a'):
                actors.append(x.text)
            actors.pop()
            stars = actors[0] + ',' + actors[1] + ',' + actors[2]
        if soup.find('div', "inline canwrap"):
            story_line = soup.find('div',
                                   "inline canwrap").findAll('p')[0].text
        else:
            story_line = 'Not available'
        info = soup.findAll('div', "txt-block")
        if info:
            mov_country = []
            mov_language = []
            for node in info:
                a = node.findAll('a')
                for i in a:
                    if "country_of_origin" in i['href']:
                        mov_country.append(i.text)
                    elif "primary_language" in i['href']:
                        mov_language.append(i.text)
        if soup.findAll('div', "ratingValue"):
            for r in soup.findAll('div', "ratingValue"):
                mov_rating = r.strong['title']
        else:
            mov_rating = 'Not available'
        await rkp.edit('<a href=' + poster + '>&#8203;</a>'
                     '<b>Title : </b><code>' + mov_title + '</code>\n<code>' +
                     mov_details + '</code>\n<b>Rating : </b><code>' +
                     mov_rating + '</code>\n<b>Country : </b><code>' +
                     mov_country[0] + '</code>\n<b>Language : </b><code>' +
                     mov_language[0] + '</code>\n<b>Director : </b><code>' +
                     director + '</code>\n<b>Writer : </b><code>' + writer +
                     '</code>\n<b>Stars : </b><code>' + stars +
                     '</code>\n<b>IMDB Url : </b>' + mov_link +
                     '\n<b>Story Line : </b>' + story_line,
                     link_preview=True,
                     parse_mode='HTML')
    except IndexError:
        await rkp.edit(" **unknown movie name** ")


@javes.on(rekcah05(pattern=f"google (.*)", allow_sudo=True))
@register(outgoing=True, pattern=r"^!google (.*)")
async def gsearch(q_event):
    sender = await q_event.get_sender() ; me = await q_event.client.get_me()
    if not sender.id == me.id:
        rkp = await q_event.reply("`processing...`")
    else:
    	rkp = await q_event.edit("`processing...`")   
    match = q_event.pattern_match.group(1)
    page = findall(r"page=\d+", match)
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    search_args = (str(match), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(10):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"[{title}]({link})\n`{desc}`\n\n"
        except IndexError:
            break
    await rkp.edit("**Search Query:**\n`" + match + "`\n\n**Results:**\n" +
                       msg,
                       link_preview=False)

@javes.on(rekcah05(pattern=f"wiki (.*)", allow_sudo=True))
@javes05(outgoing=True, pattern=r"^\!wiki (.*)")
async def wiki(wiki_q):
    lazy = wiki_q ; sender = await lazy.get_sender() ; me = await lazy.client.get_me()
    if not sender.id == me.id:
        rkp = await lazy.reply("`processing...`")
    else:
    	rkp = await lazy.edit("`processing...`")   
    match = wiki_q.pattern_match.group(1)
    try:
        summary(match)
    except DisambiguationError as error:
        await rkp.edit(f"Disambiguated page found.\n\n{error}")
        return
    except PageError as pageerror:
        await rkp.edit(f"Page not found.\n\n{pageerror}")
        return
    result = summary(match)
    if len(result) >= 4096:
        file = open("output.txt", "w+")
        file.write(result)
        file.close()
        await wiki_q.client.send_file(
            wiki_q.chat_id,
            "output.txt",
            reply_to=wiki_q.id,
            caption="`Output too large, sending as file`",
        )
        if os.path.exists("output.txt"):
            os.remove("output.txt")
        return
    return await rkp.edit("**Search:**\n`" + match + "`\n\n**Result:**\n" + result)
    

@javes.on(rekcah05(pattern=f"ud (.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^\!ud (.*)")
async def urban_dict(ud_e):
    lazy = ud_e ; sender = await lazy.get_sender() ; me = await lazy.client.get_me()
    if not sender.id == me.id:
        rkp = await lazy.reply("`processing...`")
    else:
    	rkp = await lazy.edit("`processing...`")       
    query = ud_e.pattern_match.group(1)
    urban_dict_helper = asyncurban.UrbanDictionary()
    try:
        urban_def = await urban_dict_helper.get_word(query)
    except asyncurban.WordNotFoundError:
        await rkp.edit(f"Sorry, couldn't find any results for: {query}")
        return
    deflen = sum(len(i) for i in urban_def.definition)
    exalen = sum(len(i) for i in urban_def.example)
    meanlen = deflen + exalen
    if int(meanlen) >= 0:
        if int(meanlen) >= 4096:
            await rkp.edit("`Output too large, sending as file.`")
            file = open("output.txt", "w+")
            file.write("Text: " + query + "\n\nMeaning: " +
                       urban_def.definition + "\n\n" + "Example: \n" +
                       urban_def.example)
            file.close()
            await ud_e.client.send_file(
                ud_e.chat_id,
                "output.txt",
                caption="`Output was too large, sent it as a file.`")
            if os.path.exists("output.txt"):
                os.remove("output.txt")
            await ud_e.delete()
            return
        return await rkp.edit("Text: **" + query + "**\n\nMeaning: **" +
                        urban_def.definition + "**\n\n" + "Example: \n__" +
                        urban_def.example + "__")        
    else:
        return await rkp.edit("No result found for **" + query + "**")
    
@javes05(outgoing=True, pattern="^!magisk$")
@javes.on(rekcah05(pattern=f"magisk$", allow_sudo=True))
async def magisk(request):
    lazy = request ; sender = await lazy.get_sender() ; me = await lazy.client.get_me()
    if not sender.id == me.id:
        rkp = await lazy.reply("`processing...`")
    else:
    	rkp = await lazy.edit("`processing...`")       
    magisk_dict = {
        "Stable":
        "https://raw.githubusercontent.com/topjohnwu/magisk_files/master/stable.json",
        "Beta":
        "https://raw.githubusercontent.com/topjohnwu/magisk_files/master/beta.json",
        "Canary (Release)":
        "https://raw.githubusercontent.com/topjohnwu/magisk_files/canary/release.json",
        "Canary (Debug)":
        "https://raw.githubusercontent.com/topjohnwu/magisk_files/canary/debug.json"
    }
    releases = 'Latest Magisk Releases:\n'
    for name, release_url in magisk_dict.items():
        data = get(release_url).json()
        releases += f'{name}: [ZIP v{data["magisk"]["version"]}]({data["magisk"]["link"]}) | ' \
                    f'[APK v{data["app"]["version"]}]({data["app"]["link"]}) | ' \
                    f'[Uninstaller]({data["uninstaller"]["link"]})\n'
    await rkp.edit(releases)


@javes05(outgoing=True, pattern=r"^!specs(?: |)([\S]*)(?: |)([\s\S]*)")
@javes.on(rekcah05(pattern=f"specs(?: |)([\S]*)(?: |)([\s\S]*)", allow_sudo=True))
async def devices_specifimions(request):
    lazy = request ; sender = await lazy.get_sender() ; me = await lazy.client.get_me()
    if not sender.id == me.id:
        rkp = await lazy.reply("`processing...`")
    else:
    	rkp = await lazy.edit("`processing...`")       
    textx = await request.get_reply_message()
    brand = request.pattern_match.group(1).lower()
    device = request.pattern_match.group(2).lower()
    if brand and device:
        pass
    elif textx:
        brand = textx.text.split(' ')[0]
        device = ' '.join(textx.text.split(' ')[1:])
    else:
        await rkp.edit("`Usage: specs <brand> <device>`")
        return
    all_brands = BeautifulSoup(
        get('https://www.devicespecifications.com/en/brand-more').content,
        'lxml').find('div', {
            'class': 'brand-listing-container-news'
        }).findAll('a')
    brand_page_url = None
    try:
        brand_page_url = [
            i['href'] for i in all_brands if brand == i.text.strip().lower()
        ][0]
    except IndexError:
        await rkp.edit(f'`{brand} is unknown brand!`')
    devices = BeautifulSoup(get(brand_page_url).content, 'lxml') \
        .findAll('div', {'class': 'model-listing-container-80'})
    device_page_url = None
    try:
        device_page_url = [
            i.a['href']
            for i in BeautifulSoup(str(devices), 'lxml').findAll('h3')
            if device in i.text.strip().lower()
        ]
    except IndexError:
        await rkp.edit(f"`can't find {device}!`")
    if len(device_page_url) > 2:
        device_page_url = device_page_url[:2]
    reply = ''
    for url in device_page_url:
        info = BeautifulSoup(get(url).content, 'lxml')
        reply = '\n' + info.title.text.split('-')[0].strip() + '\n'
        info = info.find('div', {'id': 'model-brief-specifications'})
        specifications = re.findall(r'<b>.*?<br/>', str(info))
        for item in specifications:
            title = re.findall(r'<b>(.*?)</b>', item)[0].strip()
            data = re.findall(r'</b>: (.*?)<br/>', item)[0] \
                .replace('<b>', '').replace('</b>', '').strip()
            reply += f'**{title}**: {data}\n'
    await rkp.edit(reply)





@javes.on(rekcah05(pattern=f"song2(?: |$)(.*)", allow_sudo=True))
async def _(event):
    rksong = event.pattern_match.group(1)  
    rkkk= await event.reply(f"`{JAVES_NNAME}: ` **Finding {rksong} in world wide please wait........**")
    chat = "@FindMusicPleaseBot"
    async with event.client.conversation(chat) as conv:             	
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=442186886))              
              await conv.send_message("/start")
              response = await conv.get_response()     
              if not response.text.startswith("Hi,"):      
                         await event.reply(f"`{JAVES_NNAME}`: **Sorry, look like my frined is sleeping.... please try later \nOr use alternative way !song <song name> **")
              else:
                         await conv.send_message(rksong)
                         song2 = await conv.get_response()
                         if song2.text.startswith("Sorry,"):
                             await rkkk.edit(f"`{JAVES_NNAME}`: `Sorry,failed to find \nTry alternative way !song <songname>`")
                         else: 
                             await event.client.send_message(event.chat_id, song2)
                             await conv.get_response()
                             song3 = await conv.get_response()
                             await event.client.send_file(event.chat_id, song3)
 

@javes.on(rekcah05(pattern=f"mean(?: |$)(.*)", allow_sudo=True))
@javes05(outgoing=True, pattern="^!mean(?: |$)(.*)")
async def dic(event):
  lazy = event ; sender = await lazy.get_sender() ; me = await lazy.client.get_me()
  if not sender.id == me.id:
        rkp = await lazy.reply("`processing...`")
  else:
    	rkp = await lazy.edit("`processing...`")       
  word = event.pattern_match.group(1)
  if not word:
      word = await event.get_reply_message()
      word = word.text
  if not word:
  	return await rkp.edit("`no text given`")
  output = meaning(word) 
  if type(output) == list: 
	  for item in output:   
		    return await rkp.edit(f"**Word**: `{word}` \n\n**Meaning**: `{item}`")
  else: 
      await rkp.edit("`Failed to find`")
      return    

@javes05(outgoing=True, pattern=r"^\!reverse(?: |$)(\d*)")
@javes.on(rekcah05(pattern=f"reverse(?: |$)(\d*)", allow_sudo=True))
async def okgoogle(img):
    lazy = img ; sender = await lazy.get_sender() ; me = await lazy.client.get_me()
    if not sender.id == me.id:
        rkp = await lazy.reply("`processing...`")
    else:
    	rkp = await lazy.edit("`processing...`")       
    if os.path.isfile("okgoogle.png"):
        os.remove("okgoogle.png")
    message = await img.get_reply_message()
    if message and message.media:
        photo = io.BytesIO()
        await img.client.download_media(message, photo)
    else:
        await rkp.edit("Error\n`Usage reverse <reply to a photo or sticker`")
        return
    if photo:        
        try:
            image = Image.open(photo)
        except OSError:
            await rkp.edit('`Error Unsupported media.`')
            return
        name = "okgoogle.png"
        image.save(name, "PNG")
        image.close()
        searchUrl = 'https://www.google.com/searchbyimage/upload'
        multipart = {
            'encoded_image': (name, open(name, 'rb')),
            'image_content': ''
        }
        response = requests.post(searchUrl,
                                 files=multipart,
                                 allow_redirects=False)
        fetchUrl = response.headers['Location']
        if response != 400:
            await rkp.edit("`Image successfully uploaded to Google. `")
        else:
            await rkp.edit("`Error with google response`")
            return
        os.remove(name)
        match = await ParseSauce(fetchUrl +
                                 "&preferences?hl=en&fg=1#languages")
        guess = match['best_guess']
        imgspage = match['similar_images']
        if guess and imgspage:
            await rkp.edit(f"[{guess}]({fetchUrl})\n\n`Looking for images...`")
        else:
            await rkp.edit("`Couldn't find anything .`")
            return
        if img.pattern_match.group(1):
            lim = img.pattern_match.group(1)
        else:
            lim = 3
        images = await scam(match, lim)
        yeet = []
        for i in images:
            k = requests.get(i)
            yeet.append(k.content)
        try:
            await img.client.send_file(entity=await
                                       img.client.get_input_entity(img.chat_id
                                                                   ),
                                       file=yeet,
                                       reply_to=img)
        except TypeError:
            pass
        await rkp.edit(
            f"[{guess}]({fetchUrl})\n\n[View imilar images]({imgspage})")





CMD_HELP.update({
    "search":
    "`!song < song name>`\
\n**Usage:** Find & send given song  \
\n\n`!song2 < song name>` \
\n**Usage:** find & send song from world wide .\
\n\n`!vsong < song name>` \
\n**Usage:** Send video song.\
\n\n`!movie < movie name>` \
\n**Usage:** Shows movie info .\
\n\n`!mean <word>` \
\n**Usage:** Give meaning of text.\
\n\n`!ud < word>` \
\n**Usage:** Does a search on Urban Dictionary.\
\n\n`!wiki <word>` \
\n**Usage:** Does a search on Wikipedia..\
\n\n`!google < ward>` \
\n**Usage:** Does a search on Google.\
\n\n`!img < ward> / !img <ward> max10` \
\n**Usage:** Does an image search on Google and shows .\
\n\n`!reverse < reply to a photo/sticker> ` \
\n**Usage:**Revers-search given img on Google and send similar images!!\
\n\n`!currency <amount> <from> <to> ` \
\n**Usage:** Converts various currencies  like` !currency 1 usd inr`.\
\n\n`!app <name>` \
\n**Usage:** Shows app info .\
\n\n`!magisk` \
\n**Usage:** Shows latest magisk .\
\n\n`!specs <brand> <device>` \
\n**Usage:** Shows device specs.\
\n\n`!ggl <word>` \
\n**Usage:** Shows How to search google.\
\n\n**All commands support Sudo , type !help sudo for more info**\
"
})








           
    
    
    