import math
import os
import re
from userbot import Config as Var
from telethon import Button, custom, events
from userbot import bot as tgbot
from userbot import ALIVE_NAME, CMD_LIST

NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD = os.environ.get(
    "NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD", 3
)
EMOJI_TO_DISPLAY_IN_HELP = os.environ.get("EMOJI_TO_DISPLAY_IN_HELP", None)

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@Shivam_Patel"
if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("Userbot"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article(
                "©Javes2.0 Help",
                text="{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_LIST)),
                buttons=buttons,
                link_preview=False,
            )
        if event.query.user_id == bot.uid and query == "stats":
            result = builder.article(
                title="Stats",
                text=f"**Showing Stats For {DEFAULTUSER}'s userbot** \nNote --> Only Owner Can Check This \n(C) @Shivam_Patel",
                buttons=[
                    [custom.Button.inline("Show Stats 🚶", data="terminator")],
                    [
                        Button.url(
                            "Repo 🛡️", "https://github.com/Sh1vam/javes-2.0"
                        )
                    ],
                    [Button.url("Join Channel 📃", "t.me/daShivam_Patel,
                ],
            )
        await event.answer([result] if result else None)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_next\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number + 1, CMD_LIST, "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_popp_up_alert = "Hey don't touch buttons!!! Who give u permission 🧐??!"
            await event.answer(reply_popp_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_prev\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1, CMD_LIST, "helpme"  # pylint:disable=E0602
            )
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Hey don't touch buttons!!! Who  give you permission 🧐??"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await event.edit("♒menu closed by @Shivam_Patel♒")

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"us_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            plugin_name = event.data_match.group(1).decode("UTF-8")
            help_string = ""
            try:
                for i in CMD_LIST[plugin_name]:
                    help_string += i
                    help_string += "\n"
            except:
                pass
            if help_string is "":
                reply_pop_up_alert = "{} is useless".format(plugin_name)
            else:
                reply_pop_up_alert = help_string
            reply_pop_up_alert += "\n Use .unload {} to remove this plugin\n\
                © Javes2.0".format(
                plugin_name
            )
            try:
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
            except:
                halps = "Do .ihelp {} to get the list of commands.".format(plugin_name)
                await event.answer(halps, cache_time=0, alert=True)
        else:
            reply_pop_up_alert = "Hey don't touch buttons!! Who give u permission 🧐??"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"terminator")))
    async def rip(event):
        if event.query.user_id == bot.uid:
            text = inlinestats
            await event.answer(text, alert=True)
        else:
            txt = "You Can't View My Masters Stats"
            await event.answer(txt, alert=True)


def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = Config.NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD
    number_of_cols = Config.NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD
    helpable_plugins = [p for p in loaded_plugins if not p.startswith("_")]
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        custom.Button.inline(
            "{} {} {}".format(
                Config.EMOJI_TO_DISPLAY_IN_HELP, x, Config.EMOJI_TO_DISPLAY_IN_HELP
            ),
            data="us_plugin_{}".format(x),
        )
        for x in helpable_plugins
    ]
    if number_of_cols == 1:
        pairs = list(zip(modules[::number_of_cols]))
    elif number_of_cols == 2:
        pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    else:
        pairs = list(
            zip(
                modules[::number_of_cols],
                modules[1::number_of_cols],
                modules[2::number_of_cols],
            )
        )
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    elif len(modules) % number_of_cols == 2:
        pairs.append((modules[-2], modules[-1]))
    max_num_pages = math.ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "⌫", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline("❎", data="close"),
                custom.Button.inline(
                    "⌦", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs
