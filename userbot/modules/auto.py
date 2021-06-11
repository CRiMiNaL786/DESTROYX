
import os
from datetime import datetime
import asyncio
import time
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
import shutil
import pytz
from telethon.tl import functions
from telethon.errors import FloodWaitError
from userbot.events import javes05
from userbot import CMD_HELP, bot, BIO_MESSAGE, BIO_MSG, JAVES_NAME
from telethon.events import ChatAction
from userbot import bot
javes = bot
try:
  import pyfiglet
except:
  pass
AUTO_PP = os.environ.get("AUTO_PP","https://telegra.ph/file/edc2836f4353c6b01bcb4.jpg")
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)
BIO_MMSG = str(BIO_MESSAGE) if BIO_MESSAGE else str(BIO_MSG)
FONT_FILE_TO_USE = "userbot/javes_main/extra/DejaVuSansMono.ttf"
TZZ = os.environ.get("TIME_ZONE","Asia/Kolkata")
DEL_TIME_OUT = 60
DDEL_TIME_OUT = 60
AUTO_NAME = os.environ.get("AUTO_NAME", None)
AUTO_BIO = os.environ.get("AUTO_BIO", None)
AUTO_PIC = os.environ.get("AUTO_PIC", None)
import random




async def rk():
    while True:    	        
        NT = datetime.now(pytz.timezone(TZZ))
        HM = NT.strftime("%I:%M%p")
        nnmel = f"{HM}"
        #await event.reply(f"**{JAVES_NAME}**: `successfully set last name to {HM} {TZZ}\n Sleeping 60s........`")        
        try:        	
            await bot(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                last_name=nnmel
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DDEL_TIME_OUT)
        

async def rk2():
    while True:        
        DMY = time.strftime("%Y:%m:%d ")
        NT = datetime.now(pytz.timezone(TZZ))
        HM = NT.strftime("%A, %d. %B %Y %I:%M%p")
        bio = f" {BIO_MMSG}| {HM}"
        #await event.reply(f"**{JAVES_NAME}**: `successfully set auto bio with {BIO_MMSG} with {HM} {TZZ}\n Sleeping 60s.......`")
        
        try:
            await bot(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                about=bio
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)
       
        

async def rk3():
    downloaded_file_name = "userbot/original_pic.png"
    downloader = SmartDL(AUTO_PP, downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    photo = "userbot/photo_pfp.png"
    while not downloader.isFinished():
        place_holder = None
    counter = -30
    while True:
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        #file_test = im.rotate(counter, expand=False).save(photo, "PNG")
        NT = datetime.now(pytz.timezone(TZZ))
        current_time = NT.strftime(f"%I:%M %p")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 120)
        drawn_text.text((25, 530), current_time, font=fnt, fill=(280, 280, 280))
        img.save(photo)
        file = await bot.upload_file(photo)  # pylint:disable=E0602
        #await event.reply(f"**{JAVES_NAME}**: `successfully set profile picture \nSleeping 60s.......`")
        await event.client(functions.photos.DeletePhotosRequest(await event.client.get_profile_photos("me", limit=1)))     
        try:
            await bot(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            counter -= 30
            await asyncio.sleep(60)
        except:
            return
       



        

@javes05(outgoing=True, pattern="^!autoname")
async def _(event):
    while True:    	        
        NT = datetime.now(pytz.timezone(TZZ))
        HM = NT.strftime("%I:%M%p")
        nnmel = f"{HM}"
        await event.reply(f"**{JAVES_NAME}**: `successfully set last name to {HM} {TZZ}\n Sleeping 60s........`")
        
        try:
        	
            await bot(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                last_name=nnmel
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DDEL_TIME_OUT)
        


@javes05(outgoing=True, pattern="^!autobio$")
async def _(event):  
    while True:        
        DMY = time.strftime("%Y:%m:%d ")
        NT = datetime.now(pytz.timezone(TZZ))
        HM = NT.strftime("%A, %d. %B %Y %I:%M%p")
        bio = f" {BIO_MMSG}| {HM}"
        await event.reply(f"**{JAVES_NAME}**: `successfully set auto bio with {BIO_MMSG} with {HM} {TZZ}\n Sleeping 60s.......`")
        
        try:
            await bot(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                about=bio
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)
       



@javes05(outgoing=True, pattern="^!autopic$")
async def autopic(event):
    await event.reply(f"**{JAVES_NAME}**: `Auto pic Activated`")
    downloaded_file_name = "userbot/original_pic.png"
    downloader = SmartDL(AUTO_PP, downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    photo = "userbot/photo_pfp.png"
    while not downloader.isFinished():
        place_holder = None
    counter = -30
    while True:
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        #file_test = im.rotate(counter, expand=False).save(photo, "PNG")
        NT = datetime.now(pytz.timezone(TZZ))
        current_time = NT.strftime(f"%I:%M %p")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 120)
        drawn_text.text((25, 530), current_time, font=fnt, fill=(280, 280, 280))
        img.save(photo)
        file = await bot.upload_file(photo)  # pylint:disable=E0602        
        await event.client(functions.photos.DeletePhotosRequest(await event.client.get_profile_photos("me", limit=1)))     
        while True:
          try:
            await bot(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            counter -= 30
            await asyncio.sleep(60)
          except:
            continue
          break


@javes05(outgoing=True, pattern="^!runclock$")
async def _(event):
    if event.fwd_from:
        return
    while True:
        LT = datetime.now(pytz.timezone(TZZ))
        OT = LT.strftime("%I:%M:%S ")
        input = pyfiglet.figlet_format(OT, font = "3x5") 
        final = f"```..{input}```.." 
        await event.edit(final)
        await asyncio.sleep(1)







@javes05(outgoing=True, pattern="^!autopic2$")
async def _(event):
 FONT_FILE_TO_USE = "userbot/javes_main/extra/JollyBold-ZGW3.ttf"
 downloaded_file_name = "userbot/original_pic.png"
 downloader = SmartDL(AUTO_PP, downloaded_file_name, progress_bar=False)
 downloader.start(blocking=False)
 photo = "userbot/photo_pfp.png"
 while not downloader.isFinished():
     place_holder = None
 counter = -30
 while True:
    x=(random.randrange(1,96))
    
    if x==1:

        rk = "Underwater bubbles and raindrops\nare total opposites of each other."

    if x==2:

        rk = "If you buy an eraser you are literally\npaying for your mistakes."
    if x==3:

        rk = "The Person you care for most has the potential to destroy you the most."

    if x==4:

        rk = "If humans colonize the moon\nit will\nprobably attract retirement homes as the weaker gravity will allow the elderly to feel stronger."

    if x==5:

        rk = "Any video with ?wait for it? in the title\n is simply too long."

    if x==6:

        rk = "Your age in years is how many times you?ve \ncircled the Sun\nbut your age in months is how many times the Moon has circled you."

    if x==7:

        rk = "Biting your tongue while eating is a perfec\nt example of how you can still screw up\neven with decades of experience."

    if x==8:

        rk = "Saying that your home is powered by a wirel\ness Nuclear fusion reactor that is 93 Million miles away sounds way cooler than just saying you have solar panels on your roof."

    if x==9:

        rk = "The most crushing feeling is when someone s\nmiles at you on the street and you don?t react fast enough to smile back."

    if x==10:

        rk = "Teeth constantly require maintenance to pre\nvent their decay when alive\nand yet they manage to survive for thousands of years buried as fossils."

    if x==11:

        rk = "A folder is for things that you don't want \nto fold."

    if x==12:

        rk = "Waking up in the morning sometimes feels li\nke resuming a shitty movie you decided to quit watching."

    if x==13:

        rk = "If everything goes smoothly\nyou probably won't remember today."

    if x==14:

        rk = "When you meet new people in real life\nyou \nunlock more characters for your dream world."

    if x==15:

        rk = "Maybe if they renamed sunscreen to ?anti-ca\nncer cream? more people would wear it."

    if x==16:

        rk = "200 years ago\npeople would never have gues\nsed that humans in the future would communicate by silently tapping on glass."

    if x==17:

        rk = "Parents worry about what their sons downloa\nd and worry about what their daughters upload."

    if x==18:

        rk = "It's crazy how you can be the same age as \nsomeone\nbut at a completely different stage in your life."

    if x==19:

        rk = "When you think you wanna die\nyou really \ndon't wanna die\nyou just don't wanna live like this."

    if x==20:

        rk = "Technically\nno one has ever \nbeen in an empty room."

    if x==21:

        rk = "An onion is the bass player of food. \nYou would probably not enjoy it solo\nbut you?d miss it if it wasn?t there."

    if x==22:

        rk = "We run everywhere in videogames \nbecause we're too lazy to walk\nbut In real life we walk everywhere because we're too lazy to run."

    if x==23:

        rk = "Every single decision you ever made \nhas brought you to read this sentence."

    if x==24:

        rk = "The word 'quiet' is often said very loud."

    if x==25:

        rk = "Everybody wants you to work hard\nbut nobody wants to hear \nabout how hard you work."

    if x==26:

        rk = "We brush our teeth with hair on a stick \nand brush our hair with teeth on a stick."

    if x==27:

        rk = "No one remembers your awkward \nmoments but they?re too busy remembering their own."

    if x==28:

        rk = "Dumb people try to say simple ideas \nas complex as possible while smart people try to say complex ideas as simple as possible."

    if x==29:

        rk = "Some people think they're better than you because \nthey grew up richer. \nSome people think they're better than you because\n they grew up poorer."

    if x==30:

        rk = "The biggest irony is that computers & \nmobiles were invented to save out time!"

    if x==31:

        rk = "After honey was first discovered\nthere was likely a period where people \nwere taste testing any available slime from insects."

    if x==32:

        rk = "You know you?re getting old when your \nparents start disappointing you\ninstead of you disappointing them."

    if x==33:

        rk = "Humans are designed to learn through experience yet the \neducation system has made it so we get no experience."

    if x==34:

        rk = "By focusing on blinking\nyou blink slower... Same for breathing."

    if x==35:

        rk = "Drivers in a hurry to beat traffic \nusually cause the accidents which create the traffic they were trying to avoid."

    if x==36:

        rk = "Characters that get \nmarried in fiction were literally made for each other."

    if x==37:

        rk = "Babies are a clean hard drive that can be \nprogrammed with any language."

    if x==38:

        rk = "There could be a \nmiracle drug that cures every disease to man\nthat we'll never know about because it doesn't work on rats."

    if x==39:

        rk = "Rhinos evolved to grow a horn \nfor protection\nbut it's what's making them go extinct."

    if x==40:

        rk = "Maybe we \ndon't find time travelers because we all die in 25-50 years."

    if x==41:

        rk = "Sleep is the trial version of death\nIt even comes with ads based on your activity."

    if x==42:

        rk = "The most unrealistic thing \nabout Spy movies is how clean the air ventilation system is!"

    if x==43:

        rk = "In games we \nplay through easy modes to unlock hard modes. In life we play through hard modes to unlock easy modes."

    if x==44:

        rk = "Silent people seem smarter than \nloud people\nbecause they keep their stupid thoughts to themselves."

    if x==45:

        rk = "If Greenland \nactually turns green\nwe're all screwed."

    if x==46:

        rk = "If someone says clever things in \nyour dream\nit actually shows your own cleverness."

    if x==47:

        rk = "Famous movie quotes \nare credited to the actor and not the actual writer \nwho wrote them."

    if x==48:

        rk = "No one actually teaches you how to \nride a bicycle. They just hype you up until you work it out."

    if x==49:

        rk = "Ask yourself why the the brain \nignores the second the."

    if x==50:

        rk = "You?ve probably forgot about 80% of \nyour entire life and most of the memories you do remember are not very accurate to what actually happened."

    if x==51:

        rk = "It will be a lot harder for \nkids to win against their parents in video games in the future."

    if x==52:

        rk = "Everyone has flaws\nif you don't recognize yours\nyou have a new one."

    if x==53:

        rk = "Raising a child is training your \nreplacement."

    if x==54:

        rk = "'O'pen starts with a Closed circle\nand 'C'lose starts with an open circle."

    if x==55:

        rk = "There's always someone who \nhated you for no reason\nand still does."

    if x==56:

        rk = "After popcorn was discovered\nthere must have been a lot of random seeds \nthat were roasted to see if it would \nhave the same effect."

    if x==57:

        rk = "The more important a good night's sleep is\nthe harder it is to fall asleep."

    if x==58:

        rk = "Blessed are those that can \nproperly describe the type of haircut they want to a new stylist."

    if x==59:

        rk = "Too many people spend money \nthey haven't earned\nto buy things they don't want\nto impress people they don't like!"

    if x==60:

        rk = "Theme park employees must be good at \ntelling the difference between screams of horror and excitement."

    if x==61:

        rk = "6 to 6:30 feels more \nhalf-an-hour than 5:50 to 6:20"

    if x==62:

        rk = "Getting your password right on the last \nlogin attempt before lockout is the closest \nthing to disarming a bomb at the last minute that most \nof us will experience."

    if x==63:

        rk = "Listening to podcasts before bed \nis the adult version of story-time."

    if x==64:

        rk = "If all criminals stopped \nrobbing then the security industry would fall in which they could then easily go back to robbing."

    if x==65:

        rk = "A ton of whales is\nreally only like half a whale."

    if x==66:

        rk = "When you get old\nthe old you is technically the new you\nand your young self is the old you."

    if x==67:

        rk = "You probably won't find many negative \nreviews of parachutes on the Internet."

    if x==68:

        rk = "We show the most love and admiration for people \nwhen they're no longer around to appreciate it."

    if x==69:

        rk = "We've practiced sleeping thousands of times\nyet can't do it very well or be consistent."

    if x==70:

        rk = "Humans are more enthusiastic about \nmoving to another planet with \nhostile environment than preserving earth - the \nplanet they are perfectly shaped for."

    if x==71:

        rk = "The happiest stage of most people's lives is \nwhen their brains aren't fully developed yet."

    if x==72:

        rk = "The most effective alarm clock is \na full bladder."

    if x==73:

        rk = "You probably just synchronized \nblinks with millions of people."

    if x==74:

        rk = "Since we test drugs on animals first\nrat medicine must be years \n ahead of human medicine."

    if x==75:

        rk = "Night before a day off is more \n satisfying than the actual day off."

    if x==76:

        rk = "We put paper in a folder to keep it from folding."

    if x==77:

        rk = "Somewhere\ntwo best \nfriends are meeting for the first time."

    if x==78:

        rk = "Our brain simultaneously hates us\nloves us\ndoesn't care about us\nand micromanages our every move."

    if x==79:

        rk = "Being a male is a matter of birth. \nBeing a man is a matter of age. But being a gentleman is a matter of choice."

    if x==80:

        rk = "Soon the parents will be hiding their social account from their \nkids rather than kids hiding their accounts from the parents."

    if x==81:

        rk = "Wikipedia is what the internet was meant \nto be."

    if x==82:

        rk = "A theme park is the only place that you can hear screams in the \ndistance and not be concerned."

    if x==83:

        rk = "A wireless phone charger offers less freedom \nof movement than a wired one."

    if x==84:

        rk = "If you repeatedly criticize someone for\n liking something you don't\nthey won't stop liking it. They'll stop liking you."

    if x==85:

        rk = "Somewhere there is a grandmother\nwhose grandson really is the most \nhandsome boy in the world."

    if x==86:

        rk = "If someday human teleportation becomes real\npeople will still be late for work."

    if x==87:

        rk = "The first humans who ate crabs must have been \nreally hungry to try and eat an armored sea spider"

    if x==88:

        rk = "Doing something alone is kind of sad\nbut doing it solo is cool af."

    if x==89:

        rk = "Your brain suddenly becomes \nperfect at proofreading after you post something."

    if x==90:

        rk = "There's always that one song in your \nplaylist that you always skip but never remove."

    if x==91:

        rk = "Kids next century will probably hate us for \ntaking all the good usernames."

    if x==92:

        rk = "Bubbles are to fish \nwhat rain is to humans."

    if x==93:

        rk = "The more people you meet\nthe more you realise and appreciate how well your \nparents raised you."

    if x==94:

        rk = "A comma is a short pause\na coma is a long pause."

    if x==95:

        rk = "Someday you will either not \nwake up or not go to sleep."     

    if x==96:

        rk = "Bermuda Triangle might be the exit \nportal of this simulation."
    
    if x==97:
        rk = "If we put solar panels above parking lots, then our cars wouldn't get hot and we would have a lot of clean energy."          
    shutil.copy(downloaded_file_name, photo)
    im = Image.open(photo)
    #file_test = im.rotate(counter, expand=False).save(photo, "PNG")
    NT = datetime.now(pytz.timezone(TZZ))
    current_time = NT.strftime(f" Time: %I:%M%p\n{rk}")
    img = Image.open(photo)
    drawn_text = ImageDraw.Draw(img)
    fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
    drawn_text.text((25, 450), current_time, font=fnt, fill=(280, 280, 280))
    img.save(photo)
    file = await bot.upload_file(photo)  # pylint:disable=E0602
    await event.reply(f"**{JAVES_NAME}**: `successfully set profile picture \nSleeping 60s.......`")
    try:
        await bot(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
            file
        ))
        os.remove(photo)
        counter -= 30
        await asyncio.sleep(60)
    except:
        return
    




CMD_HELP.update({
    "auto":
    "!autoname\
\nUsage: change your last name to a clock  \
\n\n!autobio \
\nUsage: change your bio to a clock , you can set custom bio message by !set var BIO_MESSAGE <message>.\
\n\n!autopic\
\nUsage: add clock in your profile picture, add custm profile img by !set var AUTO_PP <pic link>\
\n\n!autopic2\
\nUsage: same like autopic but with logic words \
\n\n!runclock\
\nUsage: run a clock  ( warning it cost flood wait error)\
\n\n**For stop this restart javes**\
\n\nTip : You can set your country time by !set var TIME_ZONE <timeZone like Asia/Kolkata(indiantime)>\
"
})





