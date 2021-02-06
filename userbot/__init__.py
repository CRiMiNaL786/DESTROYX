import os
from sys import version_info
import logging
from logging import basicConfig, getLogger, INFO, DEBUG, WARNING
from distutils.util import strtobool as sb
from pySmartDL import SmartDL
from dotenv import load_dotenv
from requests import get
from telethon import TelegramClient
from telethon.sessions import StringSession
from var import Var
load_dotenv("config.env")
from userbot.javes_main.heroku_var import config

sed = logging.getLogger("WARNING")
sedprint = logging.getLogger("WARNING")

CONSOLE_LOGGER_VERBOSE = config.CONSOLE_LOGGER_VERBOSE
basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=INFO)
if Var.STRING_SESSION:
    session_name = str(Var.STRING_SESSION)
    bot = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
else:
    session_name = "startup"
    bot = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
    
LOGS = getLogger(__name__)
ENV = config.ENV
API_KEY = config.API_KEY
API_HASH = config.API_HASH
STRING_SESSION = config.STRING_SESSION
BOTLOG_CHATID = config.BOTLOG_CHATID
BOTLOG = config.BOTLOG
LOGSPAMMER = config.LOGSPAMMER
GENIUS = config.GENIUS
GENIUS_API_TOKEN = config.GENIUS_API_TOKEN
CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)
PM_AUTO_BAN = config.PM_AUTO_BAN
HEROKU_APPNAME = config.HEROKU_APPNAME
HEROKU_APP_NAME = config.HEROKU_APP_NAME
HEROKU_APIKEY = config.HEROKU_APIKEY
HEROKU_API_KEY = config.HEROKU_API_KEY
UPSTREAM_REPO_URL = config.UPSTREAM_REPO_URL
TELEGRAPH_SHORT_NAME = config.TELEGRAPH_SHORT_NAME
CONSOLE_LOGGER_VERBOSE = config.CONSOLE_LOGGER_VERBOSE
DB_URI = config.DB_URI
OCR_SPACE_API_KEY = config.OCR_SPACE_API_KEY
REM_BG_API_KEY = config.REM_BG_API_KEY
CHROME_DRIVER = config.CHROME_DRIVER
GOOGLE_CHROME_BIN = config.GOOGLE_CHROME_BIN
OPEN_WEATHER_MAP_APPID = config.OPEN_WEATHER_MAP_APPID
WEATHER_DEFCITY = config.WEATHER_DEFCITY
LYDIA_API_KEY = config.LYDIA_API_KEY
PM_MESSAGE = config.PM_MESSAGE
JAVES_NAME = config.JAVES_NAME
ANTI_SPAMBOT = config.ANTI_SPAMBOT
ANTI_SPAMBOT_SHOUT = config.ANTI_SPAMBOT_SHOUT
YOUTUBE_API_KEY = config.YOUTUBE_API_KEY
ALIVE_NAME = config.ALIVE_NAME
BLOCK_MESSAGE = config.BLOCK_MESSAGE
AFK_MESSAGE = config.AFK_MESSAGE
ALIVE_S_MESSAGE = config.ALIVE_S_MESSAGE
BIO_MESSAGE = config.BIO_MESSAGE
ALIVE_E_MESSAGE = config.ALIVE_E_MESSAGE
COUNTRY = config.COUNTRY
TZ_NUMBER = config.TZ_NUMBER
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
YOUR_SHORT_NAME = os.environ.get("YOUR_SHORT_NAME", None)
CLEAN_WELCOME = config.CLEAN_WELCOME
BIO_PREFIX = config.BIO_PREFIX
DEFAULT_BIO = config.DEFAULT_BIO
G_DRIVE_CLIENT_ID = config.G_DRIVE_CLIENT_ID
G_DRIVE_CLIENT_SECRET = config.G_DRIVE_CLIENT_SECRET
G_DRIVE_AUTH_TOKEN_DATA = config.G_DRIVE_AUTH_TOKEN_DATA
GDRIVE_FOLDER_ID = config.GDRIVE_FOLDER_ID
TEMP_DOWNLOAD_DIRECTORY = config.TEMP_DOWNLOAD_DIRECTORY

ENV = os.environ.get("ENV", False)
""" PPE initialization. """

if bool(ENV):
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    if CONSOLE_LOGGER_VERBOSE:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=DEBUG,
        )
    else:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=INFO
        )
    LOGS = getLogger(__name__)

    # Check if the config was edited by using the already used variable.
    # Basically, its the 'virginity check' for the config file ;)
    CONFIG_CHECK = os.environ.get(
        "___________PLOX_______REMOVE_____THIS_____LINE__________", None
    )

    if CONFIG_CHECK:
        LOGS.info(
            "Please remove the line mentioned in the first hashtag from the config.env file"
        )
        quit(1)

    # Logging channel/group configuration.
    BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID", None)
    try:
        BOTLOG_CHATID = int(BOTLOG_CHATID)
    except:
        pass

    # Userbot logging feature switch.
    BOTLOG = sb(os.environ.get("BOTLOG", "True"))
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "True"))

    # Bleep Blop, this is a bot ;)
    PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "True"))

    # Console verbose logging
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    # SQL Database URI
    DB_URI = os.environ.get("DATABASE_URL", None)

    # OCR API key
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

    # remove.bg API key
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

    # Chrome Driver and Headless Google Chrome Binaries
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)

    # OpenWeatherMap API Key
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)

    # Anti Spambot Config
    ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))

    ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

    # FedBan Premium Module
    F_BAN_LOGGER_GROUP = os.environ.get("F_BAN_LOGGER_GROUP", None)

    # Autopic
    AUTOPIC_FONT_COLOUR = os.environ.get("AUTOPIC_FONT_COLOUR", None)
    AUTOPIC_FONT = os.environ.get("AUTOPIC_FONT", None)
    AUTOPIC_COMMENT = os.environ.get("AUTOPIC_COMMENT", None)

    # Cbutton
    PRIVATE_CHANNEL_BOT_API_ID = os.environ.get("PRIVATE_CHANNEL_BOT_API_ID", None)

    # SUDOUSERS
    SUDO_USERS = os.environ.get("SUDO_USERS", None)

    # CommandHandler
    CMD_HNDLR = os.environ.get("CMD_HNDLR", r"\.")
    SUDO_HNDLR = os.environ.get("SUDO_HNDLR", r"\!")

    # Heroku Credentials for updater.
    HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

    # Youtube API key
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

    # Default .alive name
    ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
    AUTONAME = os.environ.get("AUTONAME", None)
    # Custom pm permi
    CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)
    # Time & Date - Country and Time Zone
    COUNTRY = str(os.environ.get("COUNTRY", "India"))
    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
    FBAN_REASON = os.environ.get("FBAN_REASON", None)
    FBAN_USER = os.environ.get("FBAN_USER", None)

    # Clean Welcome
    CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
    # for Logging
    BOTLOG = sb(os.environ.get("BOTLOG", "False"))
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))
    # Custom Module
    CUSTOM_STICKER_PACK_NAME = os.environ.get("CUSTOM_STICKER_PACK_NAME", None)
    CUSTOM_ANIMATED_PACK_NAME = os.environ.get("CUSTOM_ANIMATED_PACK_NAME", None)

    # Pm Permit Img
    PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)

    # Gban
    USER_IS = os.environ.get("USER_IS", None)

    # For Bot Purposes
    OWNER_ID = os.environ.get("OWNER_ID", None)

    # Last.fm Module
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)

    LASTFM_API = os.environ.get("LASTFM_API", None)
    LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
    LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
    LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
    LASTFM_PASS = pylast.md5(LASTFM_PASSWORD_PLAIN)
    if not LASTFM_USERNAME == "None":
        lastfm = pylast.LastFMNetwork(
            api_key=LASTFM_API,
            api_secret=LASTFM_SECRET,
            username=LASTFM_USERNAME,
            password_hash=LASTFM_PASS,
        )
    else:
        lastfm = None

    # Google Drive Module
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./downloads")
else:
    # Put your ppe vars here if you are using local hosting
    PLACEHOLDER = None




    
from userbot import ALIVE_NAME
from userbot import DEFAULTUSER
JAVES_MSG = (f"Javes ")
ORI_MSG = (f"Hello Sir, I can't allow you to {ALIVE_NAME}'s PM without his permissions please be patient, Thankyou ")
BLOCK_MSG = (f"I am not going to allow you to spam {DEFAULTUSER}'s PM, You have been blocked ")
JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)
AFK_MSG = (f"Hello Sir, {DEFAULTUSER} is offline Just leave Your message, Thankyou!")
BIO_MSG = (f"")
ALIVE_S_MSG = (f"I am Alone Survivor!")
ALIVE_E_MSG = (f"Javes 2.0 Reloaded Extra Extremely🖕🏻 ")

if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {"https://raw.githubusercontent.com/yshalsager/megadown/master/megadown":"bin/megadown","https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":"bin/cmrudl"}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

S2 = os.environ.get("S2", None)
S3 = os.environ.get("S3", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

client2 = client3 = tebot = None
if STRING_SESSION:
    client = TelegramClient(StringSession(STRING_SESSION),API_KEY,API_HASH,connection_retries=None,auto_reconnect=False,lang_code='en')
else:
     quit(1)
if S2:
    client2 = TelegramClient(StringSession(S2),API_KEY,API_HASH,connection_retries=None,auto_reconnect=False,lang_code='en')
if S3:
    client3 = TelegramClient(StringSession(S3),API_KEY,API_HASH,connection_retries=None,auto_reconnect=False,lang_code='en')
if BOT_TOKEN:    
    tebot = TelegramClient("bot", API_KEY, API_HASH).start(bot_token=BOT_TOKEN)

borg = bot = javes = client
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
CMD_LIST = {}
LOAD_PLUG = {}
ISAFK = None
AFKREASON = None
INT_PLUG = ""

