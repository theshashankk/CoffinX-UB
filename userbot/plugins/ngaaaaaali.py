"""Check if your userbot is working."""
# Kang with credits else gay...
import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, version
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME, Lastupdate
from . import dcdef
from telethon.tl.types import ChannelParticipantsAdmins

# ======CONSTANTS=========#
CUSTOM_ALIVE = (
    Var.CUSTOM_ALIVE
    if Var.CUSTOM_ALIVE
    else "Hey! I'm alive. All systems online and functioning normally!"
)
ALV_PIC = Var.ALIVE_PIC if Var.ALIVE_PIC else None
telemoji = Var.CUSTOM_ALIVE_EMOJI if Var.CUSTOM_ALIVE_EMOJI else "**✵**"
if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"
# ======CONSTANTS=========#


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Coffin X user"


@telebot.on(admin_cmd(outgoing=True, pattern="alive"))
@telebot.on(sudo_cmd(outgoing=True, pattern="alive", allow_sudo=True))
async def amireallyalive(alive):
    start = datetime.now()
    myid = bot.uid
    """ For .alive command, check if the bot is running.  """
    end = datetime.now()
    (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    if ALV_PIC:
        tele = f"**Welcome To CoffinX **\n\n"
        tele += f"`{CUSTOM_ALIVE}`\n\n"
        tele += (
            f"{telemoji} **CoffinX version**: `1.17`\n{telemoji} **Python**: `3.8.3`\n"
        )
        tele += f"{telemoji} **CoffinX Version**: `{telever}`\n"
        tele += f"{telemoji} **More Info**: @CoffinXsupport\n"
        tele += f"{telemoji} **Sudo** : `{sudo}`\n"
        tele += f"{telemoji} **Coffin Uptime**: `{uptime}`\n"
        tele += f"{telemoji} **Database Status**: `All OK 👌!`\n"
        tele += (
            f"{telemoji} **My pro owner** : [{DEFAULTUSER}](tg://user?id={myid})\n\n"
        )
        tele += "    [✨ GitHub Repository ✨](https://github.com/theshashankk/CoffinX-UB)"
        await alive.get_chat()
        await alive.delete()
        """ For .alive command, check if the bot is running.  """
        await borg.send_file(alive.chat_id, ALV_PIC, caption=tele, link_preview=False)
        await alive.delete()
        return
    req = requests.get("https://telegra.ph/file/38ce0e8131aed6b44453e.jpg")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_message(
            alive.chat_id,
            f"**Welcome To TeleBot **\n\n"
            f"`{CUSTOM_ALIVE}`\n\n"
            f"{telemoji} **Telethon version**: `1.17`\n{telemoji} **Python**: `3.8.3`\n"
            f"{telemoji} **Coffin X Version**: `{telever}`\n"
            f"{telemoji} **More Info**: @CoffinXsupport\n"
            f"{telemoji} **Sudo** : `{sudo}`\n"
            f"{telemoji} **COFFIN X Uptime**: `{uptime}`\n"
            f"{telemoji} **Database Status**: `All OK 👌!`\n"
            f"{telemoji} **My pro owner** : [{DEFAULTUSER}](tg://user?id={myid})\n\n"
            "    [✨ GitHub Repository ✨](https://github.com/theshashankk/CoffinX-UB)",
            link_preview=False,
        )
        await borg.send_file(alive.chat_id, file=sticker)
        await alive.delete()


CMD_HELP.update({"alive": "➟ `.alive`\nUse - Check if your bot is working."})