from datetime import datetime
from random import randint
from asyncio import sleep
from os import execl
import sys
import os
from userbot import bot as javes
from userbot.events import admin_cmd, command
import io
import heroku3
from userbot import CMD_HELP, ALIVE_NAME, PM_MESSAGE, JAVES_NAME, JAVES_MSG, ORI_MSG
import asyncio
from asyncio import create_subprocess_shell as asyncSubprocess
from asyncio.subprocess import PIPE as asyncPIPE
from userbot import CMD_HELP, LOGS, HEROKU_APPNAME, HEROKU_APIKEY
import sys
import json
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot, UPSTREAM_REPO_URL
from speedtest import Speedtest
from telethon import functions
from os import remove, execle, path, makedirs, getenv, environ
from shutil import rmtree
import asyncio
import json
from asyncio import sleep
from telethon.errors import rpcbaseerrors
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
import os
import subprocess
import time
import math
from pySmartDL import SmartDL
import asyncio
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.tl.types import DocumentAttributeVideo
from userbot import LOGS, CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
import sys
try:
   from git import Repo
   from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
except:
	pass
from userbot import CMD_HELP, bot, HEROKU_APIKEY, HEROKU_APPNAME, UPSTREAM_REPO_URL
from userbot import CMD_HELP, LOGS, HEROKU_APP_NAME, HEROKU_API_KEY
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which
from os import remove
from telethon import version
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import javes05
import heroku3
import asyncio
import os
import requests
import math
from userbot.javes_main.commands import progress, humanbytes, time_formatter
from userbot import CMD_HELP
HEROKU_APP_NAME = os.environ.get("HEROKU_APPNAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_APIKEY", None)
HEROKU_APPNAME = os.environ.get("HEROKU_APPNAME", None)
HEROKU_APIKEY = os.environ.get("HEROKU_APIKEY", None)
from userbot.events import javes05
from userbot.prettyjson import prettyjson
from userbot import CMD_HELP, ALIVE_NAME, PM_MESSAGE, JAVES_NAME, JAVES_MSG, ORI_MSG, ALIVE_S_MESSAGE, ALIVE_E_MESSAGE, ALIVE_S_MSG, ALIVE_E_MSG
Heroku = heroku3.from_key(HEROKU_API_KEY)
GIT_REPO_NAME = "javes-2.0"
heroku_api = "https://api.heroku.com"
UPSTREAM_REPO_URL="https://github.com/Sh1vam/javes-2.0"

# ================= CONSTANT =================
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)
ALIVE_S_MMSG = str(ALIVE_S_MESSAGE) if ALIVE_S_MESSAGE else str(ALIVE_S_MSG)
ALIVE_E_MMSG = str(ALIVE_E_MESSAGE) if ALIVE_E_MESSAGE else str(ALIVE_E_MSG)
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

Heroku = heroku3.from_key(HEROKU_API_KEY)


async def subprocess_run(cmd, heroku):
    subproc = await asyncSubprocess(cmd, stdout=asyncPIPE, stderr=asyncPIPE)
    stdout, stderr = await subproc.communicate()
    exitCode = subproc.returncode
    if exitCode != 0:
        await heroku.edit(
            '**An error was detected while running subprocess**\n'
            f'```exitCode: {exitCode}\n'
            f'stdout: {stdout.decode().strip()}\n'
            f'stderr: {stderr.decode().strip()}```')
        return exitCode
    return stdout.decode().strip(), stderr.decode().strip(), exitCode







@javes05(outgoing=True, pattern="^\!sysd$")
async def sysdetails(sysd):
    """ For .sysd command, get system info using neofetch. """
    try:
        neo = "neofetch --stdout"
        fetch = await asyncrunapp(
            neo,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )

        stdout, stderr = await fetch.communicate()
        result = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())

        await sysd.edit("`" + result + "`")
    except FileNotFoundError:
        await sysd.edit("`Install neofetch first !!`")





@javes05(outgoing=True, pattern="^\!pip(?: |$)(.*)")
async def pipcheck(pip):
    """ For .pip command, do a pip search. """
    pipmodule = pip.pattern_match.group(1)
    if pipmodule:
        await pip.edit("`Searching . . .`")
        invokepip = f"pip3 search {pipmodule}"
        pipc = await asyncrunapp(
            invokepip,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )

        stdout, stderr = await pipc.communicate()
        pipout = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())

        if pipout:
            if len(pipout) > 4096:
                await pip.edit("`Output too large, sending as file`")
                file = open("output.txt", "w+")
                file.write(pipout)
                file.close()
                await pip.client.send_file(
                    pip.chat_id,
                    "output.txt",
                    reply_to=pip.id,
                )
                remove("output.txt")
                return
            await pip.edit("**Query: **\n`"
                           f"{invokepip}"
                           "`\n**Result: **\n`"
                           f"{pipout}"
                           "`")
        else:
            await pip.edit("**Query: **\n`"
                           f"{invokepip}"
                           "`\n**Result: **\n`No Result Returned/False`")
    else:
        await pip.edit("`Use .help pip to see an example`")








requirements_path = path.join(
    path.dirname(path.dirname(path.dirname(__file__))), 'requirements.txt')


async def gen_chlog(repo, diff):
    ch_log = ''
    d_form = "%d/%m/%y"
    for c in repo.iter_commits(diff):
        ch_log += f'•[{c.committed_datetime.strftime(d_form)}]: {c.summary} <{c.author}>\n'
    return ch_log


async def update_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            ' '.join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


@javes05(outgoing=True, pattern="^\!update(?: |$)(.*)")
async def upstream(ups):
    "For .update command, check if the bot is up to date, update if specified"
    await ups.edit("`Checking for updates, please wait....`")
    conf = ups.pattern_match.group(1)
    off_repo = UPSTREAM_REPO_URL
    force_update = False

    try:
        txt = "`Oops.. Updater cannot continue "
        txt += "please add heroku apikey, name`\n\n**LOGTRACE:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        await ups.edit(f'{txt}\n`directory {error} is not found`')
        repo.__del__()
        return
    except GitCommandError as error:
        await ups.edit(f'{txt}\n`Early failure! {error}`')
        repo.__del__()
        return
    except InvalidGitRepositoryError as error:
        if conf != "now":
            await ups.edit(
                f"`Unfortunately, the directory {error} does not seem to be a git repository.\
            \nBut we can fix that by force updating the userbot using .update now.`"
            )
            return
        repo = Repo.init()
        origin = repo.create_remote('upstream', off_repo)
        origin.fetch()
        force_update = True
        repo.create_head('main', origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)

    ac_br = repo.active_branch.name
    if ac_br != 'main':
        await ups.edit(
            f'**[UPDATER]:**` Looks like you are using your own custom branch ({ac_br}). '
            'in that case, Updater is unable to identify '
            'which branch is to be merged. '
            'please checkout to any official branch`')
        repo.__del__()
        return

    try:
        repo.create_remote('upstream', off_repo)
    except BaseException:
        pass

    ups_rem = repo.remote('upstream')
    ups_rem.fetch(ac_br)

    changelog = await gen_chlog(repo, f'HEAD..upstream/{ac_br}')

    if not changelog and not force_update:
        await ups.edit(
            f'\n`{JAVES_NNAME} is`  **up-to-date**  \n')
        repo.__del__()
        return

    if conf != "now" and not force_update:
        changelog_str = f'**New UPDATE available for {JAVES_NNAME}\n\nCHANGELOG:**\n`{changelog}`'
        if len(changelog_str) > 4096:
            await ups.edit("`Changelog is too big, view the file to see it.`")
            file = open("output.txt", "w+")
            file.write(changelog_str)
            file.close()
            await ups.client.send_file(
                ups.chat_id,
                "output.txt",
                reply_to=ups.id,
            )
            remove("output.txt")
        else:
            await ups.edit(changelog_str)
        await ups.respond('`do \"!update now\" to update`')
        return

    if force_update:
        await ups.edit(
            '`Force-Syncing to latest stable userbot code, please wait...`')
    else:
        await ups.edit('`Finiding your heroku app.....`')
    # We're in a Heroku Dyno, handle it's memez.
    if HEROKU_APIKEY is not None:
        import heroku3
        heroku = heroku3.from_key(HEROKU_APIKEY)
        heroku_app = None
        heroku_applications = heroku.apps()
        if not HEROKU_APPNAME:
            await ups.edit(
                '`Please set up the HEROKU_APPNAME variable to be able to update userbot.`'
            )
            repo.__del__()
            return
        for app in heroku_applications:
            if app.name == HEROKU_APPNAME:
                heroku_app = app
                break
        if heroku_app is None:
            await ups.edit(
                f'{txt}\n`Invalid Heroku credentials for updating userbot dyno.`'
            )
            repo.__del__()
            return
        await ups.edit(f'`[Updater]\
                        {JAVES_NNAME} •dyno build in progress, please wait for it to complete.\n•It may take 10 minutes `'
                       )
        ups_rem.fetch(ac_br)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", "https://api:" + HEROKU_APIKEY + "@")
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)
        try:
            remote.push(refspec="HEAD:refs/heads/main", force=True)
        except GitCommandError as error:
            await ups.edit(f'{txt}\n`Here is the error log:\n{error}`')
            repo.__del__()
            return
        await ups.edit('Successfully Updated!\n'
                       'Restarting.......')
    else:
        # Classic Updater, pretty straightforward.
        try:
            ups_rem.pull(ac_br)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        reqs_upgrade = await update_requirements()
        await ups.edit('`Successfully Updated!\n'
                       'restarting......`')
        # Spin a new instance of bot
        args = [sys.executable, "-m", "userbot"]
        execle(sys.executable, *args, environ)
        return



@javes05(outgoing=True, pattern="^\!speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Running speed test . . .`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("`"
                   "Started at "
                   f"{result['timestamp']} \n\n"
                   "Download "
                   f"{speed_convert(result['download'])} \n"
                   "Upload "
                   f"{speed_convert(result['upload'])} \n"
                   "Ping "
                   f"{result['ping']} \n"
                   "ISP "
                   f"{result['client']['isp']}"
                   "`")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@javes05(outgoing=True, pattern="^\!dc$")
async def neardc(event):
    """ For .dc command, get the nearest datacenter information. """
    result = await event.client(functions.help.GetNearestDcRequest())
    await event.edit(f"Country : `{result.country}`\n"
                     f"Nearest Datacenter : `{result.nearest_dc}`\n"
                     f"This Datacenter : `{result.this_dc}`")


@javes05(outgoing=True, pattern="^\!ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`Pong!`")
    end = datetime.now()
    duration = (end - start).microseconds / 10000
    await pong.edit("`Pong!\n%sms`" % (duration))






    

from telethon.events import *








@javes05(outgoing=True, pattern="^\!random")
async def randomise(items):
    """ For .random command, get a random item from the list of items. """
    itemo = (items.text[8:]).split()
    if len(itemo) < 2:
        await items.edit(
            "`2 or more items are required! `"
        )
        return
    index = randint(1, len(itemo) - 1)
    await items.edit("**Query: **\n`" + items.text[8:] + "`\n**Output: **\n`" +
                     itemo[index] + "`")


@javes05(outgoing=True, pattern="^\!sleep( [0-9]+)?$")
async def sleepybot(time):
    """ For .sleep command, let the userbot snooze for a few second. """
    message = time.text
    if " " not in time.pattern_match.group(1):
        await time.reply("Syntax: `.sleep [seconds]`")
    else:
        counter = int(time.pattern_match.group(1))
        await time.edit("`sleeping....`")
        await sleep(2)
        if BOTLOG:
            await time.client.send_message(
                BOTLOG_CHATID,
                "You put the bot to sleep for " + str(counter) + " seconds",
            )
        await sleep(counter)
        await time.edit("`OK, I'm awake now.`")









@javes05(outgoing=True, pattern="^\!repeat (.*)")
async def repeat(rep):
    cnt, txt = rep.pattern_match.group(1).split(' ', 1)
    replyCount = int(cnt)
    toBeRepeated = txt

    replyText = toBeRepeated + "\n"

    for i in range(0, replyCount - 1):
        replyText += toBeRepeated + "\n"

    await rep.edit(replyText)


@javes05(outgoing=True, pattern="^\!repo$")
async def repo_is_here(wannasee):
    await wannasee.edit(
        f"Click [here](https://telegra.ph/HOW-MAKE-JAVESTELEGRAM-USER-BOT-07-05) For make your own javes \n Repo : click [here](https://github.com/Sh1vam/javes-2.0)")

@javes05(outgoing=True, pattern="^\!raw$")
async def raw(event):
    the_real_message = None
    reply_to_id = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.stringify()
        reply_to_id = event.reply_to_msg_id
    else:
        the_real_message = event.stringify()
        reply_to_id = event.message.id
    with io.BytesIO(str.encode(the_real_message)) as out_file:
        out_file.name = "raw_message_data.txt"
        await event.edit(
            f"`{JAVES_NNAME}:  `i have sent decoded message data in my chat!")
        await event.client.send_file(
            BOTLOG_CHATID,
            out_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            caption="`Here's the decoded message data !!`")




@javes.on(admin_cmd(pattern=f"sysd$", allow_sudo=True))
async def sysdetails(sysd):
    """ For .sysd command, get system info using neofetch. """
    try:
        neo = "neofetch --stdout"
        fetch = await asyncrunapp(
            neo,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )

        stdout, stderr = await fetch.communicate()
        result = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())

        await sysd.reply("`" + result + "`")
    except FileNotFoundError:
        await sysd.reply("`Install neofetch first !!`")

@javes.on(admin_cmd(pattern=f"pip(?: |$)(.*)", allow_sudo=True))
async def pipcheck(pip):
    """ For .pip command, do a pip search. """
    pipmodule = pip.pattern_match.group(1)
    if pipmodule:
        await pip.reply("`Searching . . .`")
        invokepip = f"pip3 search {pipmodule}"
        pipc = await asyncrunapp(
            invokepip,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )

        stdout, stderr = await pipc.communicate()
        pipout = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())

        if pipout:
            if len(pipout) > 4096:
                await pip.reply("`Output too large, sending as file`")
                file = open("output.txt", "w+")
                file.write(pipout)
                file.close()
                await pip.client.send_file(
                    pip.chat_id,
                    "output.txt",
                    reply_to=pip.id,
                )
                remove("output.txt")
                return
            await pip.reply("**Query: **\n`"
                           f"{invokepip}"
                           "`\n**Result: **\n`"
                           f"{pipout}"
                           "`")
        else:
            await pip.reply("**Query: **\n`"
                           f"{invokepip}"
                           "`\n**Result: **\n`No Result Returned/False`")
    else:
        await pip.reply("`Use .help pip to see an example`")

@javes.on(admin_cmd(pattern=f"sleep( [0-9]+)?$", allow_sudo=True))
async def sleepybot(time):
    """ For .sleep command, let the userbot snooze for a few second. """
    message = time.text
    if " " not in time.pattern_match.group(1):
        await time.reply("Syntax: `.sleep [seconds]`")
    else:
        counter = int(time.pattern_match.group(1))
        await time.reply("`sleeping....`")
        await sleep(2)
        if BOTLOG:
            await time.client.send_message(
                BOTLOG_CHATID,
                "You put the bot to sleep for " + str(counter) + " seconds",
            )
        await sleep(counter)
        await time.reply("`OK, I'm awake now.`")


@javes.on(admin_cmd(pattern=f"repeat (.*)", allow_sudo=True))
async def repeat(rep):
    cnt, txt = rep.pattern_match.group(1).split(' ', 1)
    replyCount = int(cnt)
    toBeRepeated = txt

    replyText = toBeRepeated + "\n"

    for i in range(0, replyCount - 1):
        replyText += toBeRepeated + "\n"

    await rep.reply(replyText)

@javes.on(admin_cmd(pattern=f"repo$", allow_sudo=True))
async def repo_is_here(wannasee):
    """ For .repo command, just returns the repo URL. """
    await wannasee.reply(
        f"This bot just re-edit PaperplaneExtended  and added more features from unibot's plugin\n Click [here](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Frekcah-pavi%2Fjaves&template=https%3A%2F%2Fgithub.com%2Frekcah-pavi%2Fjaves) to open my javes\n =>Join channel for more information @javes05")


@javes.on(admin_cmd(pattern=f"raw$", allow_sudo=True))
async def repo_is_here(wannasee):
    """ For .repo command, just returns the repo URL. """
    await wannasee.reply(
        f"`Privacy Error\nSorry this command not permitted`")





    


@javes.on(admin_cmd(pattern=f"random", allow_sudo=True))
async def randomise(items):
    """ For .random command, get a random item from the list of items. """
    itemo = (items.text[8:]).split()
    if len(itemo) < 2:
        await items.reply(
            "`2 or more items are required! `"
        )
        return
    index = randint(1, len(itemo) - 1)
    await items.reply("**Query: **\n`" + items.text[8:] + "`\n**Output: **\n`" +
                     itemo[index] + "`")
                     
@javes.on(admin_cmd(pattern=f"uploadas(stream|vn|all) (.*)", allow_sudo=True))
async def uploadas(uas_event):
    """ For .uploadas command, allows you to specify some arguments for upload. """
    await uas_event.reply("Processing ...")
    type_of_upload = uas_event.pattern_match.group(1)
    supports_streaming = False
    round_message = False
    spam_big_messages = False
    if type_of_upload == "stream":
        supports_streaming = True
    if type_of_upload == "vn":
        round_message = True
    if type_of_upload == "all":
        spam_big_messages = True
    input_str = uas_event.pattern_match.group(2)
    thumb = None
    file_name = None
    if "|" in input_str:
        file_name, thumb = input_str.split("|")
        file_name = file_name.strip()
        thumb = thumb.strip()
    else:
        file_name = input_str
        thumb_path = "a_random_f_file_name" + ".jpg"
        thumb = get_video_thumb(file_name, output=thumb_path)
    if os.path.exists(file_name):
        metadata = extractMetadata(createParser(file_name))
        duration = 0
        width = 0
        height = 0
        if metadata.has("duration"):
            duration = metadata.get("duration").seconds
        if metadata.has("width"):
            width = metadata.get("width")
        if metadata.has("height"):
            height = metadata.get("height")
        try:
            if supports_streaming:
                c_time = time.time()
                await uas_event.client.send_file(
                    uas_event.chat_id,
                    file_name,
                    thumb=thumb,
                    caption=input_str,
                    force_document=False,
                    allow_cache=False,
                    reply_to=uas_event.message.id,
                    attributes=[
                        DocumentAttributeVideo(
                            duration=duration,
                            w=width,
                            h=height,
                            round_message=False,
                            supports_streaming=True,
                        )
                    ],
                    progress_callback=lambda d, t: asyncio.get_event_loop(
                    ).create_task(
                        progress(d, t, uas_event, c_time, "Uploading...",
                                 file_name)))
            elif round_message:
                c_time = time.time()
                await uas_event.client.send_file(
                    uas_event.chat_id,
                    file_name,
                    thumb=thumb,
                    allow_cache=False,
                    reply_to=uas_event.message.id,
                    video_note=True,
                    attributes=[
                        DocumentAttributeVideo(
                            duration=0,
                            w=1,
                            h=1,
                            round_message=True,
                            supports_streaming=True,
                        )
                    ],
                    progress_callback=lambda d, t: asyncio.get_event_loop(
                    ).create_task(
                        progress(d, t, uas_event, c_time, "Uploading...",
                                 file_name)))
            elif spam_big_messages:
                await uas_event.reply("TBD: Not (yet) Implemented")
                return
            os.remove(thumb)
            await uas_event.reply("Uploaded successfully !!")
        except FileNotFoundError as err:
            await uas_event.reply(str(err))
    else:
        await uas_event.reply("404: File Not Found")



    

@javes.on(admin_cmd(pattern=f"upload (.*)", allow_sudo=True))
async def upload(u_event):
    """ For .upload command, allows you to upload a file from the userbot's server """
    await u_event.reply("Processing ...")
    input_str = u_event.pattern_match.group(1)
    if input_str in ("userbot.session", "config.env"):
        await u_event.reply("`That's a dangerous operation! Not Permitted!`")
        return
    if os.path.exists(input_str):
        c_time = time.time()
        await u_event.client.send_file(
            u_event.chat_id,
            input_str,
            force_document=True,
            allow_cache=False,
            reply_to=u_event.message.id,
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, u_event, c_time, "Uploading...", input_str)))
        await u_event.reply("Uploaded successfully !!")
    else:
        await u_event.reply("404: File Not Found")


def get_video_thumb(file, output=None, width=90):
    """ Get video thumbnail """
    metadata = extractMetadata(createParser(file))
    popen = subprocess.Popen(
        [
            "ffmpeg",
            "-i",
            file,
            "-ss",
            str(
                int((0, metadata.get("duration").seconds
                     )[metadata.has("duration")] / 2)),
            "-filter:v",
            "scale={}:-1".format(width),
            "-vframes",
            "1",
            output,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    if not popen.returncode and os.path.lexists(file):
        return output
    return None


def extract_w_h(file):
    """ Get width and height of media """
    command_to_run = [
        "ffprobe",
        "-v",
        "quiet",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        file,
    ]
    # https://stackoverflow.com/a/11236144/4723940
    try:
        t_response = subprocess.check_output(command_to_run,
                                             stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as exc:
        LOGS.warning(exc)
    else:
        x_reponse = t_response.decode("UTF-8")
        response_json = json.loads(x_reponse)
        width = int(response_json["streams"][0]["width"])
        height = int(response_json["streams"][0]["height"])
        return width, height



@javes.on(admin_cmd(pattern=f"uploadir (.*)", allow_sudo=True))
async def uploadir(udir_event):
    """ For .uploadir command, allows you to upload everything from a folder in the server"""
    input_str = udir_event.pattern_match.group(1)
    if os.path.exists(input_str):
        await udir_event.reply("Processing ...")
        lst_of_files = []
        for r, d, f in os.walk(input_str):
            for file in f:
                lst_of_files.append(os.path.join(r, file))
            for file in d:
                lst_of_files.append(os.path.join(r, file))
        LOGS.info(lst_of_files)
        uploaded = 0
        await udir_event.reply(
            "Found {} files. Uploading will start soon. Please wait!".format(
                len(lst_of_files)))
        for single_file in lst_of_files:
            if os.path.exists(single_file):
                # https://stackoverflow.com/a/678242/4723940
                caption_rts = os.path.basename(single_file)
                c_time = time.time()
                if not caption_rts.lower().endswith(".mp4"):
                    await udir_event.client.send_file(
                        udir_event.chat_id,
                        single_file,
                        caption=caption_rts,
                        force_document=False,
                        allow_cache=False,
                        reply_to=udir_event.message.id,
                        progress_callback=lambda d, t: asyncio.get_event_loop(
                        ).create_task(
                            progress(d, t, udir_event, c_time, "Uploading...",
                                     single_file)))
                else:
                    thumb_image = os.path.join(input_str, "thumb.jpg")
                    c_time = time.time()
                    metadata = extractMetadata(createParser(single_file))
                    duration = 0
                    width = 0
                    height = 0
                    if metadata.has("duration"):
                        duration = metadata.get("duration").seconds
                    if metadata.has("width"):
                        width = metadata.get("width")
                    if metadata.has("height"):
                        height = metadata.get("height")
                    await udir_event.client.send_file(
                        udir_event.chat_id,
                        single_file,
                        caption=caption_rts,
                        thumb=thumb_image,
                        force_document=False,
                        allow_cache=False,
                        reply_to=udir_event.message.id,
                        attributes=[
                            DocumentAttributeVideo(
                                duration=duration,
                                w=width,
                                h=height,
                                round_message=False,
                                supports_streaming=True,
                            )
                        ],
                        progress_callback=lambda d, t: asyncio.get_event_loop(
                        ).create_task(
                            progress(d, t, udir_event, c_time, "Uploading...",
                                     single_file)))
                os.remove(single_file)
                uploaded = uploaded + 1
        await udir_event.reply(
            "Uploaded {} files successfully !!".format(uploaded))
    else:
        await udir_event.reply("404: Directory Not Found")





@javes.on(admin_cmd(pattern=f"download(?: |$)(.*)", allow_sudo=True))
async def download(target_file):
    """ For .download command, download files to the userbot's server. """
    await target_file.reply("Processing ...")
    input_str = target_file.pattern_match.group(1)
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if "|" in input_str:
        url, file_name = input_str.split("|")
        url = url.strip()
        # https://stackoverflow.com/a/761825/4723940
        file_name = file_name.strip()
        head, tail = os.path.split(file_name)
        if head:
            if not os.path.isdir(os.path.join(TEMP_DOWNLOAD_DIRECTORY, head)):
                os.makedirs(os.path.join(TEMP_DOWNLOAD_DIRECTORY, head))
                file_name = os.path.join(head, tail)
        downloaded_file_name = TEMP_DOWNLOAD_DIRECTORY + "" + file_name
        downloader = SmartDL(url, downloaded_file_name, progress_bar=False)
        downloader.start(blocking=False)
        c_time = time.time()
        display_message = None
        while not downloader.isFinished():
            status = downloader.get_status().capitalize()
            total_length = downloader.filesize if downloader.filesize else None
            downloaded = downloader.get_dl_size()
            now = time.time()
            diff = now - c_time
            percentage = downloader.get_progress() * 100
            speed = downloader.get_speed()
            elapsed_time = round(diff) * 1000
            progress_str = "[{0}{1}] {2}%".format(
                ''.join(["?" for i in range(math.floor(percentage / 10))]),
                ''.join(["?"
                         for i in range(10 - math.floor(percentage / 10))]),
                round(percentage, 2))
            estimated_total_time = downloader.get_eta(human=True)
            try:
                current_message = f"{status}..\
                \nURL: {url}\
                \nFile Name: {file_name}\
                \n{progress_str}\
                \n{humanbytes(downloaded)} of {humanbytes(total_length)}\
                \nETA: {estimated_total_time}"

                if round(diff %
                         10.00) == 0 and current_message != display_message:
                    await target_file.reply(current_message)
                    display_message = current_message
            except Exception as e:
                LOGS.info(str(e))
        if downloader.isSuccessful():
            await target_file.reply("Downloaded to `{}` successfully !!".format(
                downloaded_file_name))
        else:
            await target_file.reply("Incorrect URL\n{}".format(url))
    elif target_file.reply_to_msg_id:
        try:
            c_time = time.time()
            downloaded_file_name = await target_file.client.download_media(
                await target_file.get_reply_message(),
                TEMP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop(
                ).create_task(
                    progress(d, t, target_file, c_time, "Downloading...")))
        except Exception as e:  # pylint:disable=C0103,W0703
            await target_file.reply(str(e))
        else:
            await target_file.reply("Downloaded to `{}` successfully !!".format(
                downloaded_file_name))
    else:
        await target_file.reply(
            "Reply to a message to download to my local server.")

@javes.on(admin_cmd(pattern=f"ping$", allow_sudo=True))
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    #await pong.reply("`Pong!`")
    end = datetime.now()
    duration = (end - start).microseconds / 10000
    await pong.reply("`Pong!\n%sms`" % (duration))


@javes.on(admin_cmd(pattern=f"speed$", allow_sudo=True))
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.reply("`Running speed test . . .`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.reply("`"
                   "Started at "
                   f"{result['timestamp']} \n\n"
                   "Download "
                   f"{speed_convert(result['download'])} \n"
                   "Upload "
                   f"{speed_convert(result['upload'])} \n"
                   "Ping "
                   f"{result['ping']} \n"
                   "ISP "
                   f"{result['client']['isp']}"
                   "`")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"



@javes.on(admin_cmd(pattern=f"update(?: |$)(.*)", allow_sudo=True))
async def upstream(ups):
    "For .update command, check if the bot is up to date, update if specified"
    await ups.reply("`Checking for updates, please wait....`")
    conf = ups.pattern_match.group(1)
    off_repo = UPSTREAM_REPO_URL
    force_update = False

    try:
        txt = "`Oops.. Updater cannot continue "
        txt += "please add heroku apikey, name`\n\n**LOGTRACE:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        await ups.reply(f'{txt}\n`directory {error} is not found`')
        repo.__del__()
        return
    except GitCommandError as error:
        await ups.reply(f'{txt}\n`Early failure! {error}`')
        repo.__del__()
        return
    except InvalidGitRepositoryError as error:
        if conf != "now":
            await ups.reply(
                f"`Unfortunately, the directory {error} does not seem to be a git repository.\
            \nBut we can fix that by force updating the userbot using .update now.`"
            )
            return
        repo = Repo.init()
        origin = repo.create_remote('upstream', off_repo)
        origin.fetch()
        force_update = True
        repo.create_head('main', origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)

    ac_br = repo.active_branch.name
    if ac_br != 'main':
        await ups.reply(
            f'**[UPDATER]:**` Looks like you are using your own custom branch ({ac_br}). '
            'in that case, Updater is unable to identify '
            'which branch is to be merged. '
            'please checkout to any official branch`')
        repo.__del__()
        return

    try:
        repo.create_remote('upstream', off_repo)
    except BaseException:
        pass

    ups_rem = repo.remote('upstream')
    ups_rem.fetch(ac_br)

    changelog = await gen_chlog(repo, f'HEAD..upstream/{ac_br}')

    if not changelog and not force_update:
        await ups.reply(
            f'\n`{JAVES_NNAME} is`  **up-to-date**  \n')
        repo.__del__()
        return

    if conf != "now" and not force_update:
        changelog_str = f'**New UPDATE available for {JAVES_NNAME}\n\nCHANGELOG:**\n`{changelog}`'
        if len(changelog_str) > 4096:
            await ups.reply("`Changelog is too big, view the file to see it.`")
            file = open("output.txt", "w+")
            file.write(changelog_str)
            file.close()
            await ups.client.send_file(
                ups.chat_id,
                "output.txt",
                reply_to=ups.id,
            )
            remove("output.txt")
        else:
            await ups.reply(changelog_str)
        await ups.respond('`do \"!update now\" to update`')
        return

    if force_update:
        await ups.reply(
            '`Force-Syncing to latest stable userbot code, please wait...`')
    else:
        await ups.reply('`Finiding your heroku app.....`')
    # We're in a Heroku Dyno, handle it's memez.
    if HEROKU_APIKEY is not None:
        import heroku3
        heroku = heroku3.from_key(HEROKU_APIKEY)
        heroku_app = None
        heroku_applications = heroku.apps()
        if not HEROKU_APPNAME:
            await ups.reply(
                '`Please set up the HEROKU_APPNAME variable to be able to update userbot.`'
            )
            repo.__del__()
            return
        for app in heroku_applications:
            if app.name == HEROKU_APPNAME:
                heroku_app = app
                break
        if heroku_app is None:
            await ups.reply(
                f'{txt}\n`Invalid Heroku credentials for updating userbot dyno.`'
            )
            repo.__del__()
            return
        await ups.reply(f'`[Updater]\
                        {JAVES_NNAME} dyno build in progress, please wait for it to complete.\nIt may take 7 minutes `'
                       )
        ups_rem.fetch(ac_br)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", "https://api:" + HEROKU_APIKEY + "@")
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)
        try:
            remote.push(refspec="HEAD:refs/heads/main", force=True)
        except GitCommandError as error:
            await ups.reply(f'{txt}\n`Here is the error log:\n{error}`')
            repo.__del__()
            return
        await ups.reply('Successfully Updated!\n'
                       'Restarting.......')
    else:
        # Classic Updater, pretty straightforward.
        try:
            ups_rem.pull(ac_br)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        reqs_upgrade = await update_requirements()
        await ups.reply('`Successfully Updated!\n'
                       'restarting......`')
        # Spin a new instance of bot
        args = [sys.executable, "-m", "userbot"]
        execle(sys.executable, *args, environ)
        return


