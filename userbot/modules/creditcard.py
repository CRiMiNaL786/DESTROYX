# Ported by @CrimiNaL786
# Original By 
# @THE_B_LACK_HAT
# @danish_00
# Card Generator
##############################


import os
import asyncio
from userbot import faker
from faker import Faker as gand
from userbot.utils import admin_cmd as devil_cmd
from userbot import bot as devil
from userbot import bot
devil = bot




@devil.on(devil_cmd("cc"))
async def _devil(dark):
    cyber = gand()
    killer = cyber.name()
    kali = cyber.address()
    alain = cyber.credit_card_full()
    await dark.edit(f"ℕ𝕒𝕞𝕖:-\n{killer}\n\n𝔸𝕕𝕕𝕣𝕖𝕤𝕤:-\n{kali}\n\nℂ𝕒𝕣𝕕:-\n{alain}")
