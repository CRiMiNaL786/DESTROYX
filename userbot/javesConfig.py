import os

ENV = bool(os.environ.get("ENV", False))


class javesConfig(object):
    APP_ID = int(os.environ.get("APP_ID", 6))
    # 6 is a placeholder
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", None)
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", None)
    LOGGER = True
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    # Here for later purposes
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "1021716237").split())
    BOT_HANDLER = os.environ.get("BOT_HANDLER", "^/")
    WHITELIST_USERS = set(
        int(x) for x in os.environ.get("WHITELIST_USERS", "1021716237").split()
    )
    BLACKLIST_USERS = set(int(x) for x in os.environ.get("BLACKLIST_USERS", "").split())
    DEVLOPERS = set(int(x) for x in os.environ.get("DEVLOPERS", "1311769691").split())
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1311769691").split())
    SUPPORT_USERS = set(int(x) for x in os.environ.get("SUPPORT_USERS", "").split())
    # custom vars
    CUSTOM_ALIVE = os.environ.get("CUSTOM_ALIVE", None)
    CUSTOM_ALIVE_EMOJI = os.environ.get("CUSTOM_ALIVE_EMOJI", None)
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    SUDO_HNDLR = os.environ.get("SUDO_HNDLR", "\.")
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", None)
    ALIVE_MSG = os.environ.get("ALIVE_MSG", None)
    LYDIA_API = os.environ.get("LYDIA_API", None)
    NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", True))
    SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", "\.")
    PMBOT_START_MSSG = os.environ.get("PMBOT_START_MSSG", None)
    LESS_SPAMMY = os.environ.get("LESS_SPAMMY", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
    TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
    NO_SONGS = bool(os.environ.get("NO_SONGS", False))
    ENABLE_ASSISTANTBOT = os.environ.get("ENABLE_ASSISTANTBOT", "ENABLE")
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
    MAX_FLOOD_IN_P_M_s = os.environ.get("MAX_FLOOD_IN_P_M_s", "3")
    PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", None))
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    MAX_MESSAGE_SIZE_LIMIT = 4095
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    CMD_HNDLR = os.environ.get("CMD_HNDLR", "\!")
    TAG_FEATURE = os.environ.get("TAG_FEATURE", "DISABLE")
    MAX_SPAM = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 5))
    SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME", None)
    NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD = int(
        os.environ.get("NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD", 10)
    )
    NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD = int(
        os.environ.get("NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD", 7)
    )
    EMOJI_TO_DISPLAY_IN_HELP = os.environ.get("EMOJI_TO_DISPLAY_IN_HELP", "〄𝕭〄")
    SPOTIFY_PASS = os.environ.get("SPOTIFY_PASS", None)
    G_BAN_LOGGER_GROUP = int(os.environ.get("G_BAN_LOGGER_GROUP", -1001291663564))
    SPOTIFY_BIO_PREFIX = os.environ.get("SPOTIFY_BIO_PREFIX", None)
    ASSISTANT_LOG = int(os.environ.get("ASSISTANT_LOG", False))
    UPSTREAM_REPO = os.environ.get(
        "UPSTREAM_REPO", "https://github.com/Anmol-dot283/Black-Lightning"
    )
    ALIVE_PIC = os.environ.get(
        "ALIVE_IMAGE", "https://telegra.ph/file/7f72b0ea1893e84028298.mp4"
    )
    ALIVE_IMAGE = os.environ.get(
        "ALIVE_PIC", "https://telegra.ph/file/7f72b0ea1893e84028298.mp4"
    )
    ASSISTANT_START_PIC = os.environ.get(
        "ASSISTANT_START_PIC",
        "https://telegra.ph/file/b233f8b6332fbeb3f61dc.mp4",
    )
    TESSDATA_PREFIX = os.environ.get(
        "TESSDATA_PREFIX", "/usr/share/tesseract-ocr/4.00/tessdata"
    )
    OPEN_LOAD_LOGIN = os.environ.get("OPEN_LOAD_LOGIN", None)
    OPEN_LOAD_KEY = os.environ.get("OPEN_LOAD_KEY", None)
    NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", False))
    ENABLE_ASSISTANTBOT = os.environ.get("ENABLE_ASSISTANTBOT", "ENABLE")
    PM_DATA = os.environ.get("PM_DATA", "ENABLE")
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "Black Lightning")
    ANTISPAM_FEATURE = os.environ.get("ANTISPAM_FEATURE", "ENABLE")
    ANTI_SPAMINC_TOKEN = os.environ.get("ANTI_SPAMINC_TOKEN", None)
    SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY", None)
    ASSISTANT_LOG = int(os.environ.get("ASSISTANT_LOG", False))
    PRIVATE_GROUP_BOT_API_ID = os.environ.get("PRIVATE_GROUP_BOT_API_ID", None)
    if PRIVATE_GROUP_BOT_API_ID:
        PRIVATE_GROUP_BOT_API_ID = int(PRIVATE_GROUP_BOT_API_ID)
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    PMSECURITY = os.environ.get("PMSECURITY", "ON")
    # for autopic
    AUTOPIC_TEXT = os.environ.get(
        "AUTOPIC_TEXT", "Life Is too Short.\n And so is your TG account."
    )
    AUTO_PIC_FONT = os.environ.get("AUTOPIC_FONT", "DejaVuSans.ttf")
    AUTOPIC_FONT_COLOUR = os.environ.get("AUTOPIC_FONT_COLOUR", None)
    if AUTH_TOKEN_DATA is not None:
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        t_file = open(TEMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    LOAD_MYBOT = os.environ.get("LOAD_MYBOT", "True")
    UB_BLACK_LIST_CHAT = set(
        int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split()
    )
    PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID", None)
    if PRIVATE_GROUP_ID is not None:
        try:
            PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)
        except ValueError:
            raise ValueError(
                "Invalid Private Group ID. Make sure your ID is starts with -100 and make sure that it is only numbers."
            )

    PM_LOGGR_BOT_API_ID = os.environ.get("PM_LOGGR_BOT_API_ID", None)
    if PM_LOGGR_BOT_API_ID:
        PM_LOGGR_BOT_API_ID = int(PM_LOGGR_BOT_API_ID)


class Development(javesConfig):
    LOGGER = True
    # Here for later purposes
