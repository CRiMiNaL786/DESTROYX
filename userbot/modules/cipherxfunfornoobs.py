# Original written by @Hackintush

import asyncio
import time
from collections import deque

from telethon import events
from userbot.util import admin_cmd as friday_on_cmd

from userbot import CMD_HELP
from userbot.utils import register
from userbot import bot as friday

@friday.on(events.NewMessage(pattern=r"\.slash", outgoing=True))
async def kek(keks):
    """ Check yourself ;)"""
    uio = ["/", "\\"]
    for i in range(1, 15):
        time.sleep(0.3)
        await keks.edit(":" + uio[i % 2])


@friday.on(events.NewMessage(pattern=r"\.para", outgoing=True))
async def kek(keks):
    """ Check yourself ;)"""
    uio = [")", "("]
    for i in range(1, 15):
        time.sleep(0.3)
        await keks.edit(":" + uio[i % 2])


@friday.on(events.NewMessage(pattern=r"\.question", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("?¿?¿?¿"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.oof", outgoing=True))
async def Oof(e):
    t = "Oof"
    for j in range(15):
        t = t[:-1] + "of"
        await e.edit(t)


@friday.on(friday_on_cmd("bigoof"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "nope":
    await event.edit(
        "┏━━━┓╋╋╋╋┏━━━┓ \n┃┏━┓┃╋╋╋╋┃┏━┓┃ \n┃┃╋┃┣┓┏┓┏┫┃╋┃┃ \n┃┃╋┃┃┗┛┗┛┃┃╋┃┃ \n┃┗━┛┣┓┏┓┏┫┗━┛┃ \n┗━━━┛┗┛┗┛┗━━━┛"
    )
    animation_chars = [
        "╭━━━╮╱╱╱╭━╮ \n┃╭━╮┃╱╱╱┃╭╯ \n┃┃╱┃┣━━┳╯╰╮ \n┃┃╱┃┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃┃┃ \n╰━━━┻━━╯╰╯ ",
        "╭━━━╮╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃┃┃ \n ╰━━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 40])


@friday.on(events.NewMessage(pattern=r"\.ok", outgoing=True))
async def Ok(e):
    t = "Ok"
    for j in range(15):
        t = t[:-1] + "k"
        await e.edit(t)


@friday.on(events.NewMessage(pattern=r"\.meme", outgoing=True))
async def meme(event):
    if event.fwd_from:
        return
    memeVar = event.text
    sleepValue = 3
    memeVar = memeVar[6:]

    await event.edit("-------------" + memeVar)
    await event.edit("------------" + memeVar + "-")
    await event.edit("-----------" + memeVar + "--")
    await event.edit("----------" + memeVar + "---")
    await event.edit("---------" + memeVar + "----")
    await event.edit("--------" + memeVar + "-----")
    await event.edit("-------" + memeVar + "------")
    await event.edit("------" + memeVar + "-------")
    await event.edit("-----" + memeVar + "--------")
    await event.edit("----" + memeVar + "---------")
    await event.edit("---" + memeVar + "----------")
    await event.edit("--" + memeVar + "-----------")
    await event.edit("-" + memeVar + "------------")
    await event.edit(memeVar + "-------------")
    await event.edit(memeVar)
    await asyncio.sleep(sleepValue)


@friday.on(events.NewMessage(pattern=r"\.flower", outgoing=True))
async def meme(event):
    if event.fwd_from:
        return
    flower = " 🌹"
    sleepValue = 5

    await event.edit(flower + "        ")
    await event.edit(flower + flower + "       ")
    await event.edit(flower + flower + flower + "      ")
    await event.edit(flower + flower + flower + flower + "     ")
    await event.edit(flower + flower + flower + flower + flower + "    ")
    await event.edit(
        flower + flower + flower + flower + flower + flower + flower + "   "
    )
    await event.edit(
        flower + flower + flower + flower + flower + flower + flower + flower + "  "
    )
    await event.edit(
        flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + " "
    )
    await event.edit(
        flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
    )
    await asyncio.sleep(sleepValue)


@friday.on(events.NewMessage(pattern=r"\.tlol", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.kiss", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😗😚😘😗😚😘😗😚😘"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.butterfly", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🦋✨🦋✨🦋✨🦋✨"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.box", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🟥🟧🟨🟩🟦🟪🟫⬛⬜"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.clock", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.moon", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.earth", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.smile", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🙂🙃🙂🙃🙂🙃"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.laugh", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😄😁😄😁😄😁"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.cat", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😺😸😹😺😸😹😺😸😹"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.poker", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😐😑😐😑😐😑"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.wow", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😧😦😧😦😧😦"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.monkey", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🙉🙈🙉🙈🙉🙈"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.starheart", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😍🤩😍🤩😍🤩"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.wink", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😶😉😶😉😶😉"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(friday_on_cmd("cheart ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("❤️")
        await asyncio.sleep(0.3)
        await event.edit("💙")
        await asyncio.sleep(0.3)
        await event.edit("💛")
        await asyncio.sleep(0.3)
        await event.edit("💚")
        await asyncio.sleep(0.3)
        await event.edit("🧡")
        await asyncio.sleep(0.3)
        await event.edit("💜")
        await asyncio.sleep(0.3)
        await event.edit("🤎")
        await asyncio.sleep(0.3)
        await event.edit("🖤")
        await asyncio.sleep(0.3)
        await event.edit("🤍")
        await asyncio.sleep(0.3)
        await event.edit("💜")
        await asyncio.sleep(0.3)
        await event.edit("🤎")
        await asyncio.sleep(0.3)
        await event.edit("🤍")
        await asyncio.sleep(0.3)
        await event.edit("🧡")
        await asyncio.sleep(0.3)
        await event.edit("💚")
        await asyncio.sleep(0.3)
        await event.edit("💛")
        await asyncio.sleep(0.3)
        await event.edit("💙")
        await asyncio.sleep(0.3)
        await event.edit("❤️")
        await asyncio.sleep(0.3)
        await event.edit("💝")


@friday.on(events.NewMessage(pattern=r"\.angry", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😡🤬😡🤬😡🤬"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.sad", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😒😏😒😏😒😏"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.amaze", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😳😲😳😲😳😲"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.omg", outgoing=True))
async def _(event):

    if event.fwd_from:
        return
    deq = deque(list("🙄😳🙄😳🙄😳"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.tongue", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😛😝😛😝😛😝"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.sun", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🔅🔆🔅🔆🔅🔆"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.speaker", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🔈🔊🔈🔊🔈🔊"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.heart", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("💖💝💖💝💖💝💖💝"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.sand", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("⏳⌛️⏳⌛️⏳⌛️"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.storm", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌧⛈🌧⛈🌧⛈"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.floodwarn", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("💙💛💓💔💘💕💜💚💝💞💟"))
    for _ in range(64):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.rain", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("☁️⛈Ř/~\İŇ🌬⚡🌪"))
    for _ in range(64):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(events.NewMessage(pattern=r"\.solar", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 64)
    animation_chars = [
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 64])


@friday.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 110)

    input_str = event.pattern_match.group(1)

    if input_str == "smoon":

        await event.edit(input_str)

        animation_chars = [
            "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
            "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
            "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
            "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
            "🌓🌓🌓🌓🌓\n🌓🌓🌓🌓🌓\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
            "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
            "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
            "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 110])


@friday.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "tmoon":

        await event.edit(input_str)

        animation_chars = [
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 100])


@friday.on(friday_on_cmd(pattern=r"lmoon"))
async def test(event):
    if event.fwd_from:
        return
    await event.edit(
        "🌕🌕🌕🌕🌕🌕🌕🌕\n🌕🌕🌖🌔🌖🌔🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌖🌓🌗🌔🌕🌕\n🌕🌕🌗🌑🌑🌓🌕🌕\n🌕🌕🌗👀🌑🌓🌕🌕\n🌕🌕🌘👄🌑🌓🌕🌕\n🌕🌕🌗🌑🌑🌒🌕🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌕🌘🌑🌑🌑🌑🌒🌕\n🌖🌑🌑🌑🌑🌑🌑🌔\n🌕🤜🏻🌑🌑🌑🌑🤛🏻🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌘🌑🌑🌑🌑🌑🌑🌒\n🌕🌕🌕🌕🌕🌕🌕🌕"
    )


@friday.on(friday_on_cmd(pattern=r"city"))
async def test(event):
    if event.fwd_from:
        return
    await event.edit(
        """☁☁🌞      ☁           ☁
       ☁  ✈         ☁    🚁    ☁    ☁        ☁          ☁     ☁   ☁

🏬🏨🏫🏢🏤🏥🏦🏪🏫
              🌲/     l🚍\🌳👭
           🌳/  🚘 l  🏃 \🌴 👬                       👬  🌴/            l  🚔    \🌲
      🌲/   🚖     l               \
   🌳/🚶           |   🚍         \ 🌴🚴🚴
🌴/                    |                     \🌲"""
    )


@friday.on(events.NewMessage(pattern=r"\.bombs", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")
    await asyncio.sleep(1)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n")
    await asyncio.sleep(0.5)
    await event.edit("RIP...")


@friday.on(events.NewMessage(pattern=r"\.plane", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("✈-------------")
    await event.edit("-✈------------")
    await event.edit("--✈-----------")
    await event.edit("---✈----------")
    await event.edit("----✈---------")
    await event.edit("-----✈--------")
    await event.edit("------✈-------")
    await event.edit("-------✈------")
    await event.edit("--------✈-----")
    await event.edit("---------✈----")
    await event.edit("----------✈---")
    await event.edit("-----------✈--")
    await event.edit("------------✈-")
    await event.edit("-------------✈")
    await asyncio.sleep(3)
    await event.delete()


@friday.on(friday_on_cmd(pattern="lalol"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(
        "😂\n😂\n😂\n😂\n😂😂😂😂\n\n   😂😂😂\n 😂         😂\n😂           😂\n 😂         😂\n   😂😂😂\n\n😂\n😂\n😂\n😂\n😂😂😂😂"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟥🟥🟥🟥🟥🟥🟥🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟩🟩🟨🟧🟥\n🟥🟧🟨🟨🟨🟨🟧🟥\n🟥🟧🟧🟧🟧🟧🟧🟥\n🟥🟥🟥🟥🟥🟥🟥🟥"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟧🟧🟧🟧🟧🟧🟧🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟥🟥🟩🟨🟧\n🟧🟨🟩🟩🟩🟩🟨🟧\n🟧🟨🟨🟨🟨🟨🟨🟧\n🟧🟧🟧🟧🟧🟧🟧🟧"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟧🟧🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟥🟥🟥🟥🟩🟨\n🟨🟩🟩🟩🟩🟩🟩🟨\n🟨🟨🟨🟨🟨🟨🟨🟨"
    )


@friday.on(friday_on_cmd(pattern=r"lit"))
async def lit(event):
    if event.fwd_from:
        return
    await event.edit(
        "🟩🟩🟩🟩🟩🟩🟩🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟨🟨🟧🟥🟩\n🟩🟥🟧🟧🟧🟧🟥🟩\n🟩🟥🟥🟥🟥🟥🟥🟩\n🟩🟩🟩🟩🟩🟩🟩🟩"
    )


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"love"))
async def love(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜\n❤️🧡💛💚💙💜")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️\n🧡💛💚💙💜❤️")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡\n💛💚💙💜❤️🧡")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛\n💚💙💜❤️🧡💛")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚\n💙💜❤️🧡💛💚")


@friday.on(friday_on_cmd(pattern=r"my"))
async def my(event):
    if event.fwd_from:
        return
    await event.edit("💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙\n💜❤️🧡💛💚💙")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️❤️❤️\n🧡🧡🧡🧡\n💛💛💛💛\n💚💚💚💚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙💙💙\n💜💜💜💜\n🖤🖤🖤🖤\n🤎🤎🤎🤎")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 ")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("ʟᴏᴅɪɴɢ ᴛʏᴘᴇ........𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💓💓")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("❤️❤️𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔❤️❤️")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💓💓")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💜💜𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💜💜")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💓💓")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💛💛𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💛💛")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓??𝒆𝒏𝒅𝒔💓💓")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💚💚𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💚💚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💓💓")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("🧡🧡𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔🧡🧡")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💓💓𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💓💓")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💙💙")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💜💜𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💜💜")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💚💚𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💚💚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💛💛𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💛💛")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("🖤🖤𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔🖤🖤")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💙💙𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💙💙")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💜💜𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💜💜")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💚💚𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💚💚")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💛💛𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💛💛")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💝💝𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💝💝")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💕💕𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💕💕")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💖💖𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💖💖")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💕💕𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💕💕")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💝💝𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💝💝")


@friday.on(friday_on_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("💕💕𝑰 𝒍𝒐𝒗𝒆 𝒚𝒐𝒖 𝒂𝒍𝒍 𝒇𝒓𝒊𝒆𝒏𝒅𝒔💕💕")


@friday.on(friday_on_cmd(pattern=r"car"))
async def car(event):
    if event.fwd_from:
        return
    await event.edit(
        "┈╱▔▔▔▔▔▔▔▔╲┈┈┈┈\n ╱▔▔▔▔▔▔▔▔╲╱┈┈┈┈\n▏┳╱╭╮┓┏┏┓▕╱▔▔╲┈\n▏┃╱┃┃┃┃┣▏▕▔▔╲╱▏\n▏┻┛╰╯╰╯┗┛▕▕▉▕╱╲\n▇▇▇▇▇▇▇▇▇▇▔▔▔╲▕\n▇▇╱▔╲▇▇▇▇▇╱▔╲▕╱\n┈┈╲▂╱┈┈┈┈┈╲▂╱▔┈"
    )


# ================= CONSTANT =================


GAMBAR_TITIT = """
🍆🍆
🍆🍆🍆
  🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
          🍆🍆🍆
      🍆🍆🍆🍆
 🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆       🍆🍆
"""

# ===========================================


@register(outgoing=True, pattern=r"^\.(?:penis|dick)\s?(.)?")
async def emoji_penis(e):
    emoji = e.pattern_match.group(1)
    titid = GAMBAR_TITIT
    if emoji:
        titid = titid.replace("🍆", emoji)
    await e.edit(titid)


@register(outgoing=True, pattern="^.figlol$")
async def figlol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "`\n╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱ `"
            "`\n╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱ `"
            "`\n╱┃┗━━┓┃╰━╯┃┃┗━━┓╱ `"
            "`\n╱┗━━━┛╰━━━╯┗━━━┛╱ `"
        )


@register(outgoing=True, pattern="^.fighi$")
async def fighi(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "\n╔┓┏╦━╦┓╔┓╔━━╗" "\n║┗┛║┗╣┃║┃║X X║" "\n║┏┓║┏╣┗╣┗╣╰╯║" "\n╚┛┗╩━╩━╩━╩━━╝"
        )


@register(outgoing=True, pattern="^.figtrump$")
async def figtrump(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "\n⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⡉⣉⡛⣛⠿⣿⣿⣿⣿⣿⣿⣿⣿"
            "\n⣿⣿⣿⡿⠋⠁⠄⠄⠄⠄⠄⢀⣸⣿⣿⡿⠿⡯⢙⠿⣿⣿⣿⣿"
            "\n⣿⣿⡿⠄⠄⠄⠄⠄⡀⡀⠄⢀⣀⣉⣉⣉⠁⠐⣶⣶⣿⣿⣿⣿"
            "\n⣿⣿⡇⠄⠄⠄⠄⠁⣿⣿⣀⠈⠿⢟⡛⠛⣿⠛⠛⣿⣿⣿⣿⣿"
            "\n⣿⣿⡆⠄⠄⠄⠄⠄⠈⠁⠰⣄⣴⡬⢵⣴⣿⣤⣽⣿⣿⣿⣿⣿"
            "\n⣿⣿⡇⠄⢀⢄⡀⠄⠄⠄⠄⡉⠻⣿⡿⠁⠘⠛⡿⣿⣿⣿⣿⣿"
            "\n⣿⡿⠃⠄⠄⠈⠻⠄⠄⠄⠄⢘⣧⣀⠾⠿⠶⠦⢳⣿⣿⣿⣿⣿"
            "\n⣿⣶⣤⡀⢀⡀⠄⠄⠄⠄⠄⠄⠻⢣⣶⡒⠶⢤⢾⣿⣿⣿⣿⣿"
            "\n⣿⡿⠋⠄⢘⣿⣦⡀⠄⠄⠄⠄⠄⠉⠛⠻⠻⠺⣼⣿⠟⠛⠿⣿"
            "\n⠋⠁⠄⠄⠄⢻⣿⣿⣶⣄⡀⠄⠄⠄⠄⢀⣤⣾⣿⡀⠄⠄⠄⢹"
            "\n⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣷⡤⠄⠰⡆⠄⠄⠈⠛⢦⣀⡀⡀⠄"
            "\n⠄⠄⠄⠄⠄⠄⠈⢿⣿⠟⡋⠄⠄⠄⢣⠄⠄⠄⠄⠄⠈⠹⣿⣀"
            "\n⠄⠄⠄⠄⠄⠄⠄⠘⣷⣿⣿⣷⠄⠄⢺⣇⠄⠄⠄⠄⠄⠄⠸⣿"
            "\n⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⡇⠄⠄⠸⣿⡄⠄⠈⠁⠄⠄⠄⣿"
            "\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⡇⠄⠄⠄⢹⣧⠄⠄⠄⠄⠄⠄⠘"
        )


@register(outgoing=True, pattern="^.figputin$")
async def figputin(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣵⣿⣿⣿⠿⡟⣛⣧⣿⣯⣿⣝⡻⢿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⠋⠁⣴⣶⣿⣿⣿⣿⣿⣿⣿⣦⣍⢿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⢷⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢼⣿⣿⣿⣿\n"
            "⢹⣿⣿⢻⠎⠔⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿\n"
            "⢸⣿⣿⠇⡶⠄⣿⣿⠿⠟⡛⠛⠻⣿⡿⠿⠿⣿⣗⢣⣿⣿⣿⣿\n"
            "⠐⣿⣿⡿⣷⣾⣿⣿⣿⣾⣶⣶⣶⣿⣁⣔⣤⣀⣼⢲⣿⣿⣿⣿\n"
            "⠄⣿⣿⣿⣿⣾⣟⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⢟⣾⣿⣿⣿⣿\n"
            "⠄⣟⣿⣿⣿⡷⣿⣿⣿⣿⣿⣮⣽⠛⢻⣽⣿⡇⣾⣿⣿⣿⣿⣿\n"
            "⠄⢻⣿⣿⣿⡷⠻⢻⡻⣯⣝⢿⣟⣛⣛⣛⠝⢻⣿⣿⣿⣿⣿⣿\n"
            "⠄⠸⣿⣿⡟⣹⣦⠄⠋⠻⢿⣶⣶⣶⡾⠃⡂⢾⣿⣿⣿⣿⣿⣿\n"
            "⠄⠄⠟⠋⠄⢻⣿⣧⣲⡀⡀⠄⠉⠱⣠⣾⡇⠄⠉⠛⢿⣿⣿⣿\n"
            "⠄⠄⠄⠄⠄⠈⣿⣿⣿⣷⣿⣿⢾⣾⣿⣿⣇⠄⠄⠄⠄⠄⠉⠉\n"
            "⠄⠄⠄⠄⠄⠄⠸⣿⣿⠟⠃⠄⠄⢈⣻⣿⣿⠄⠄⠄⠄⠄⠄⠄\n"
            "⠄⠄⠄⠄⠄⠄⠄⢿⣿⣾⣷⡄⠄⢾⣿⣿⣿⡄⠄⠄⠄⠄⠄⠄\n"
            "⠄⠄⠄⠄⠄⠄⠄⠸⣿⣿⣿⠃⠄⠈⢿⣿⣿⠄⠄⠄⠄⠄⠄⠄\n"
        )


@register(outgoing=True, pattern="^.figchina$")
async def figchina(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "⣿⣿⣿⣿⠟⠋⢁⢁⢁⢁⢁⢁⢁⢁⠈⢻⢿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⡀⠭⢿⣿⣿⣿⣿\n"
            "⣿⣿⣿⡟⠄⢀⣾⣿⣿⣿⣷⣶⣿⣷⣶⣶⡆⠄⠄⠄⣿⣿⣿⣿\n"
            "⣿⣿⣿⡇⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⢸⣿⣿⣿⣿\n"
            "⣿⣿⣿⣇⣼⣿⣿⠿⠶⠙⣿⡟⠡⣴⣿⣽⣿⣧⠄⢸⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣾⣿⣿⣟⣭⣾⣿⣷⣶⣶⣴⣶⣿⣿⢄⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⣿⡟⣩⣿⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣹⡋⠘⠷⣦⣀⣠⡶⠁⠈⠁⠄⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣍⠃⣴⣶⡔⠒⠄⣠⢀⠄⠄⠄⡨⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⣿⣿⣿⣦⡘⠿⣷⣿⠿⠟⠃⠄⠄⣠⡇⠈⠻⣿⣿⣿⣿\n"
            "⣿⣿⣿⡿⠟⠋⢁⣷⣠⠄⠄⠄⠄⣀⣠⣾⡟⠄⠄⠄⠄⠉⠙⠻\n"
            "⡿⠟⠁⠄⠄⠄⢸⣿⣿⡯⢓⣴⣾⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄\n"
            "⠄⠄⠄⠄⠄⠄⣿⡟⣷⠄⠹⣿⣿⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄\n"
            "⠄⠄⠄⠄⠄⣸⣿⡷⡇⠄⣴⣾⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
            "⠄⠄⠄⠄⠄⣿⣿⠃⣦⣄⣿⣿⣿⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
            "⠄⠄⠄⠄⢸⣿⠗⢈⡶⣷⣿⣿⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
        )


@register(outgoing=True, pattern="^.figthink$")
async def figthink(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "⠀⠀⠀⠀⢀⣀⣀⣀\n"
            "⠀⠀⠀⠰⡿⠿⠛⠛⠻⠿⣷\n"
            "⠀⠀⠀⠀⠀⠀⣀⣄⡀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⡀\n"
            "⠀⠀⠀⠀⠀⢸⣿⣿⣷⠀⠀⠀⠀⠛⠛⣿⣿⣿⡛⠿⠷\n"
            "⠀⠀⠀⠀⠀⠘⠿⠿⠋⠀⠀⠀⠀⠀⠀⣿⣿⣿⠇\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁\n"
            "⠀\n"
            "⠀⠀⠀⠀⣿⣷⣄⠀⢶⣶⣷⣶⣶⣤⣀\n"
            "⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠈⠙⠻⠗\n"
            "⠀⠀⠀⣰⣿⣿⣿⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⡄\n"
            "⠀⣠⣾⣿⣿⣿⣥⣶⣶⣿⣿⣿⣿⣿⠿⠿⠛⠃\n"
            "⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄\n"
            "⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁\n"
            "⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁\n"
            "⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟\n"
        )


@register(outgoing=True, pattern="^.figdick$")
async def figdick(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠲⢄\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⠁⠀⠀⠀⠀⢱\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⠀⠀⠀⠀⠀⠀⠀⣸\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⠀⠀⠀⠀⢀⡠⠖⠁\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⠁⠀⠀\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣯⣿⣿⣿⣿⣿⠇⠀⠀⠀\n"
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⣻⣿⣿⣿⣿⣯⠏⠀⠀⠀⠀\n"
            "⠀⠀⠀⠀⠀⠀⠀⣠⠾⣽⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀\n"
            "⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀\n"
            "⠀⠀⠀⠀⣴⣻⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀\n"
            "⠀⠀⣠⢾⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
            "⠀⣼⣷⣿⣿⣿⣿⣿⣿⣟⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
            "⢸⢿⣿⣿⣿⣿⣿⣿⣿⣯⣻⡟⡆⠀⠀⠀⠀⠀⠀⠀⠀\n"
            "⠸⣿⣿⣿⣿⣿⣿⣿⣿⣹⣿⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀\n"
            "⠀⠹⣟⣿⣿⣿⣿⡿⣷⡿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀\n"
            "⠀⠀⠈⠛⠯⣿⡯⠟⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        )


@register(outgoing=True, pattern="^.fighappyfrog$")
async def fighappyfrog(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "⠄⠄⠄⠄⠄⣀⣀⣤⣶⣿⣿⣶⣶⣶⣤⣄⣠⣴⣶⣿⣶⣦⣄⠄\n"
            "⠄⣠⣴⣾⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦\n"
            "⢠⠾⣋⣭⣄⡀⠄⠙⠻⣿⣿⡿⠛⠋⠉⠉⠉⠙⠛⠿⣿⣿⣿⣿\n"
            "⡎⡟⢻⣿⣷⠄⠄⠄⠄⡼⣡⣾⣿⣿⣦⠄⠄⠄⠄⠄⠈⠛⢿⣿\n"
            "⡇⣷⣾⣿⠟⠄⠄⠄⢰⠁⣿⣇⣸⣿⣿⠄⠄⠄⠄⠄⠄⠄⣠⣼\n"
            "⣦⣭⣭⣄⣤⣤⣴⣶⣿⣧⡘⠻⠛⠛⠁⠄⠄⠄⠄⣀⣴⣿⣿⣿\n"
            "⢉⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿\n"
            "⡿⠛⠛⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⡇⠄⠄⢀⣀⣀⠄⠄⠄⠄⠉⠉⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⠈⣆⠄⠄⢿⣿⣿⣷⣶⣶⣤⣤⣀⣀⡀⠄⠄⠉⢻⣿⣿⣿⣿⣿\n"
            "⠄⣿⡀⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠄⢠⣿⣿⣿⣿⣿\n"
            "⠄⣿⡇⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄⢀⣼⣿⣿⣿⣿⣿\n"
            "⠄⣿⡇⠄⠠⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿\n"
            "⠄⣿⠁⠄⠐⠛⠛⠛⠉⠉⠉⠉⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⠄⠻⣦⣀⣀⣀⣀⣀⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋\n"
        )


@register(outgoing=True, pattern="^.figdeadfrog$")
async def figdeadfrog(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⡇⠄⣿⣿⣿⡿⠋⣉⣉⣉⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
            "⣿⣿⣿⠃⠄⠹⠟⣡⣶⢟⣛⣛⡻⢿⣦⣩⣤⣬⡉⢻⣿⣿⣿⣿\n"
            "⣿⣿⣿⠄⢀⢤⣾⣿⣿⣿⡿⠿⠿⠿⢮⡃⣛⡻⢿⠈⣿⣿⣿⣿\n"
            "⣿⡟⢡⣴⣯⣿⣿⣿⠤⣤⣭⣶⣶⣶⣮⣔⡈⠛⢓⠦⠈⢻⣿⣿\n"
            "⠏⣠⣿⣿⣿⣿⣿⣿⣯⡪⢛⠿⢿⣿⣿⣿⡿⣼⣿⣿⣮⣄⠙⣿\n"
            "⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⡭⠴⣶⣶⣽⣽⣛⡿⠿⠿⠇⣿\n"
            "⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣷⣝⣛⢛⢋⣥⣴⣿⣿\n"
            "⣿⣿⣿⣿⣿⢿⠱⣿⣛⠾⣭⣛⡿⢿⣿⣿⣿⣿⣿⡀⣿⣿⣿⣿\n"
            "⠑⠽⡻⢿⣮⣽⣷⣶⣯⣽⣳⠮⣽⣟⣲⠯⢭⣿⣛⡇⣿⣿⣿⣿\n"
            "⠄⠄⠈⠑⠊⠉⠟⣻⠿⣿⣿⣿⣷⣾⣭⣿⠷⠶⠂⣴⣿⣿⣿⣿\n"
            "⠄⠄⠄⠄⠄⠄⠄⠁⠙⠒⠙⠯⠍⠙⢉⣡⣶⣿⣿⣿⣿⣿⣿⣿\n"
            "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        )


@register(outgoing=True, pattern="^.fuck$")
async def gtfo(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "\n...................................../´¯/) "
            "\n...................................,/¯../ "
            "\n.................................../.../ "
            "\n................................../´.¯/"
            "\n................................./´¯./"
            "\n...............................,/¯../ "
            "\n.............................../.../ "
            "\n............................../´¯./"
            "\n............................./´¯./"
            "\n...........................,/¯../ "
            "\n.........................../.../ "
            "\n........................../´¯./"
            "\n........................./´¯./"
            "\n.......................,/¯../ "
            "\n......................./.../ "
            "\n....................../´¯./"
            "\n....................,/¯../ "
            "\n.................../..../ "
            "\n............./´¯/'...'/´¯¯`·¸ "
            "\n........../'/.../..../......./¨¯\ "
            "\n........('(...´...´.... ¯~/'...') "
            "\n.........\.................'...../ "
            "\n..........''...\.......... _.·´ "
            "\n............\..............( "
            "\n..............\.............\..."
        )


@friday.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 60)

    input_str = event.pattern_match.group(1)

    if input_str == "jagh":

        await event.edit(input_str)

        animation_chars = [
            "8✊️===D",
            "8=✊️==D",
            "8==✊️=D",
            "8===✊️D",
            "8==✊️=D",
            "8=✊️==D",
            "8✊️===D",
            "8===✊️D💦",
            "8==✊️=D💦💦",
            "8=✊️==D💦💦💦",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 8])


CMD_HELP.update(
    {
        "CipherXFun": ".slash\
\n\n.para\
\n\n.question\
\n\n.oof\
\n\n.bigoof\
\n\n.ok\
\n\n.meme\
\n\n.flower\
\n\n.tlol\
\n\n.kiss\
\n\n.butterfly\
\n\n.box\
\n\n.clock\
\n\n.moon\
\n\n.earth\
\n\n.smile\
\n\n.laugh\
\n\n.cat\
\n\n.poker\
\n\n.wow\
\n\n.monkey\
\n\n.starheart\
\n\n.wink\
\n\n.cheart\
\n\n.angry\
\n\n.sad\
\n\n.amaze\
\n\n.omg\
\n\n.tongue\
\n\n.sun\
\n\n.speaker\
\n\n.heart\
\n\n.sand\
\n\n.storm\
\n\n.floodwarn\
\n\n.rain\
\n\n.solar\
\n\n.smoon\
\n\n.tmoon\
\n\n.lmoon\
\n\n.city\
\n\n.bombs\
\n\n.lalol\
\n\n.lit\
\n\n.love\
\n\n.my\
\n\n.hi\
\n\n.car\
\n\n.penis;dick\
\n\n.figlol\
\n\n.fighi\
\n\n.figtrump\
\n\n.figputin\
\n\n.figchina\
\n\n.figthink\
\n\n.figdick\
\n\n.fighappyfrog\
\n\n.figdeadfrog\
\n\n.fuck\
\n\n.jagh\
nUsage: List of All Available Commands."
    }
)
