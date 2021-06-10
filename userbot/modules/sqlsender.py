from datetime import datetime

from userbot import CMD_HELP
from userbot.events import zzaacckkyy

DELETE_TIMEOUT = 5
import asyncio

from userbot import CMD_HELP, JAVES_MSG, JAVES_NAME

JAVES_NNAME = str(JAVES_NAME) if JAVES_NAME else str(JAVES_MSG)


@zzaacckkyy(pattern="^!sqlsend (?P<shortname>\w+)$", outgoing=True)
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    input_str = event.pattern_match["shortname"]
    the_plugin_file = "./userbot/modules/sql_helper/{}.py".format(input_str)
    start = datetime.now()
    await event.client.send_file(  # pylint:disable=E0602
        event.chat_id,
        the_plugin_file,
        force_document=True,
        allow_cache=False,
        reply_to=message_id,
    )
    end = datetime.now()
    time_taken_in_ms = (end - start).seconds
    await event.edit("Uploaded {} in {} seconds".format(input_str, time_taken_in_ms))
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


CMD_HELP.update(
    {
        "sqlsender": "`!sqlsend <sql_helpername>`\
\n**Usage:** send the sql helper\
\n\n``\
\n****\
"
    }
)
