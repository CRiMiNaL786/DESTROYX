#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

print("an online StringSession generator")


print("t ==> Telethon (docs.telethon.dev)")
print("Telethon UserBot ==> https://github.com/Javes786/javes-2.0")



def Javes2():
  print("you selected Telethon")
  # (c) https://t.me/TelethonChat/37677
  from telethon.sync import TelegramClient
  from telethon.sessions import StringSession
  APP_ID = int(input("Enter APP ID here: "))
  API_HASH = input("Enter API HASH here: ")
  with TelegramClient(
    StringSession(), 
    APP_ID, 
    API_HASH
  ) as client:
    session_str = client.session.save()
    s_m = client.send_message("me", session_str)
    s_m.reply("⬆️ This StringSession is generated using https://repl.it/@Javes786/Javes-20-String-session#main.py \nPlease subscribe https://t.me/javes_support ")
    print("please check your Telegram Saved Messages for the StringSession ")
Javes2()