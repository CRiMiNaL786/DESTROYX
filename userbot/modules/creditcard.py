# Ported by @CrimiNaL786
# Original By 
# @THE_B_LACK_HAT
# @danish_00
# Card Generator
##############################


import os
import asyncio
from telethon import events
from userbot.events import javes05
from faker import Faker as badhiya
from userbot.utils import admin_cmd, register
from userbot import bot as borg
from userbot import bot
borg = bot
import 



@borg.on(admin_cmd("cc"))
async def _events(dark):
    cyber = badhiya()
    killer = cyber.name()
    kali = cyber.address()
    alain = cyber.credit_card_full()
    await dark.edit(f"ℕ𝕒𝕞𝕖:-\n{killer}\n\n𝔸𝕕𝕕𝕣𝕖𝕤𝕤:-\n{kali}\n\nℂ𝕒𝕣𝕕:-\n{alain}")
