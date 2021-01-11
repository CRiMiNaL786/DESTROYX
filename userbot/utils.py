from userbot import bot as borg
from userbot.events import *
from userbot.config import Config

sedprint = logging.getLogger("MODULES")
cmdhandler = CMD_HNDLR = os.environ.get("CMD_HNDLR", "\.")
bothandler = BOT_HANDLER = os.environ.get("BOT_HANDLER", "\`")
sudo_hndlr = SUDO_HNDLR = os.environ.get("SUDO_HNDLR", "\!")

async def edit_or_reply(event, text, parse_mode=None, link_preview=None):
    link_preview = link_preview or False
    parse_mode = parse_mode or "md"
    if event.sender_id in Config.SUDO_USERS:
        reply_to = await event.get_reply_message()
        if reply_to:
            return await reply_to.reply(
                text, parse_mode=parse_mode, link_preview=link_preview
            )
        return await event.reply(text, parse_mode=parse_mode, link_preview=link_preview)
    return await event.edit(text, parse_mode=parse_mode, link_preview=link_preview)

def admin_cmd(pattern=None, **args):
    args["func"] = lambda e: e.via_bot_id is None

    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    allow_sudo = args.get("allow_sudo", False)

    # get the pattern from the decorator
    if pattern is not None:
        if pattern.startswith("\#"):
            # special fix for snip.py
            args["pattern"] = re.compile(pattern)
        else:
            args["pattern"] = re.compile(cmdhandler + pattern)
            cmd = cmdhandler + pattern
            try:
                CMD_LIST[file_test].append(cmd)
            except:
                CMD_LIST.update({file_test: [cmd]})

    args["outgoing"] = True
    # should this command be available for other users?
    if allow_sudo:
        args["from_users"] = list(Config.SUDO_USERS)
        # Mutually exclusive with outgoing (can only set one of either).
        args["incoming"] = True
        del args["allow_sudo"]

    # error handling condition check
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True

    # add blacklist chats, UB should not respond in these chats
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        args["allow_edited_updates"]
        del args["allow_edited_updates"]

    # check if the plugin should listen for outgoing 'messages'

    return events.NewMessage(**args)
