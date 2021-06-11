from datetime import datetime
from covid import Covid
covid = Covid(source="worldometers")
from userbot import CMD_HELP
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.javes_main.commands import bot, rekcah05, javes05
javes = bot


@javes05(outgoing=True, pattern="^!corona$")
async def iqless(e):
    await e.edit("Antivirus scan was completed \n⚠️ Warning! This  donkey has Corona Virus")      
    

    
@javes05(outgoing=True, pattern="^!covid (.*)")
async def corona(event):
    await event.edit("`Processing...`")
    country = event.pattern_match.group(1)
    covid = Covid()
    country_data = covid.get_status_by_country_name(country)
    deaths = covid.get_total_deaths()
    if country_data:
        output_text =  f"`Confirmed`   :   {country_data['confirmed']}\n"
        output_text += f"`Active`          :   {country_data['active']}\n"
        output_text += f"`Deaths`          :   {country_data['deaths']}\n"
        output_text += f"`Recovered`   :   {country_data['recovered']}\n\n"        
        output_text += f"---------TOTAL----------\n\n"                
        output_text += f"`Deaths`          :   {covid.get_total_deaths()}\n"
        output_text += f"`Recovered`   :   {covid.get_total_recovered()}\n"
        output_text += f"`Confirmed`   :   {covid.get_total_confirmed_cases()}\n"
        output_text += f"`Active`          :   {covid.get_total_active_cases()}\n\n"
        output_text += ("`Update`        :  "f"{datetime.utcfromtimestamp(country_data['last_update'] // 1000).strftime('%H:%M')}[GMT]\n")
    else:
        output_text = "Invalid Country name"
    await event.edit(f"Corona Virus Info in {country}:\n\n{output_text}")

@javes05(outgoing=True, pattern="^!covid2 (.*)")
async def _(event):
    if event.fwd_from:
        return 
    input_str = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    chat = "@NovelCoronaBot"
    await event.edit("`Processing covid Info...`")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1124136160))
              await event.client.send_message(chat, "{}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```please unlock @NovelCoronaBot```")
              return
          if response.text.startswith("Country"):
             await event.edit("`Invalid Country name`")
          else:              
             await event.client.send_message(event.chat_id, response.message)


@javes.on(rekcah05(pattern=f"corona$", allow_sudo=True))
async def iqless(e):
    await e.reply("Antivirus scan was completed \n⚠️ Warning! This  donkey has Corona Virus")      
    

@javes.on(rekcah05(pattern=f"covid (.*)", allow_sudo=True))
async def corona(event):
    rk = await event.reply("`Processing...`")
    country = event.pattern_match.group(1)
    covid = Covid()
    country_data = covid.get_status_by_country_name(country)
    deaths = covid.get_total_deaths()
    if country_data:
        output_text =  f"`Confirmed`   :   {country_data['confirmed']}\n"
        output_text += f"`Active`          :   {country_data['active']}\n"
        output_text += f"`Deaths`          :   {country_data['deaths']}\n"
        output_text += f"`Recovered`   :   {country_data['recovered']}\n\n"        
        output_text += f"---------TOTAL----------\n\n"                
        output_text += f"`Deaths`          :   {covid.get_total_deaths()}\n"
        output_text += f"`Recovered`   :   {covid.get_total_recovered()}\n"
        output_text += f"`Confirmed`   :   {covid.get_total_confirmed_cases()}\n"
        output_text += f"`Active`          :   {covid.get_total_active_cases()}\n\n"
        output_text += ("`Update`        :  "f"{datetime.utcfromtimestamp(country_data['last_update'] // 1000).strftime('%H:%M')}[GMT]\n")
    else:
        output_text = "Invalid Country name"
    await rk.edit(f"Corona Virus Info in {country}:\n\n{output_text}")


@javes.on(rekcah05(pattern=f"covid2 (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    input_str = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    chat = "@NovelCoronaBot"
    rk = await event.reply("```Processing...```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1124136160))
              await event.client.send_message(chat, "{}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await rk.reply("```please unlock @NovelCoronaBot```")
              return
          if response.text.startswith("Country"):
             await rk.edit("`Invalid Country name`")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update({
    "covid":
    "!corona\
\nUsage: slap the taged user\
\n\n!covid <country>\
\nUsage: Get an information about data covid-19 in your country..\
\n\n!covid2 <country>\
\nUsage: same like !covid  \
\n\nSudo Commands ( type !help sudo for more info)\
\n.covid  , .covid2 , .corona \
"
})

