#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

print("
┏━━┳━┳━━┳━━┳━┳━┳━┳┓
┗┓┓┃┳┫━━╋┓┏┫╋┃┃┣┓┃┣┳┓
┏┻┛┃┻╋━━┃┃┃┃┓┫┃┣┻┓┣┃┫
┗━━┻━┻━━┛┗┛┗┻┻━┻━━┻┻┛")


print("t ==> Telethon (docs.telethon.dev) FsaaD Ki JaaD ")
print("Telethon UseRBot ==> https://github.com/CRIMINAL786/DESTROYX")


def DESTROYX():
    print("DESTROYX OFFICIAL STRING SESSION GENERATOR")
    # (c) https://t.me/TelethonChat/37677
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient

    APP_ID = int(input("Enter APP ID here: "))
    API_HASH = input("Enter API HASH here: ")
    with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
        session_str = client.session.save()
        s_m = client.send_message("me", session_str)
        s_m.reply(
            "⬆️ THIS STRING SESSION GENERATOR IS END TO END ENCRYPTED :)"
        )
        print("please check your Telegram Saved Messages for the StringSession ")


DESTROYX()
