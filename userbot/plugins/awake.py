
"""Check if userbot awake or not . 

"""
import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname

ALIVE_PIC = Config.ALIVE_PHOTTO
if ALIVE_PIC is None:
   ALIVE_PIC = "https://telegra.ph/file/37ee8db6262b2ea00dbcf.jpg"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

ALIVE_MESSAGE = Config.ALIVE_MSG
if ALIVE_MESSAGE is None:
   ALIVE_MESSAGE = "**🔱𝙲𝙾𝙵𝙵𝙸𝙽 𝚇 𝙸𝚂 𝙰𝚆𝙰𝙺𝙴🔱 \n\n\n**"
   ALIVE_MESSAGE += "`Mʏ ʙᴏᴛ sᴛᴀᴛᴜs\n\n\n`"
   ALIVE_MESSAGE += f"`Tᴇʟᴇᴛʜᴏɴ: TELETHON-1.19.0 \n\n`"
   ALIVE_MESSAGE += f"`Pʏᴛʜᴏɴ: PYTHON-3.8.5 \n\n`"
   ALIVE_MESSAGE += "`I'll Be With You Master Till My Dyno Ends!!☠ \n\n`"
   ALIVE_MESSAGE += f"`Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ` : @CoffinXsupport \n\n"
   ALIVE_MESSAGE += f"`Mʏ ʙᴏss🤗`: {DEFAULTUSER} \n\n "
                
            
#@command(outgoing=True, pattern="^.awake$")
@borg.on(admin_cmd(pattern=r"awake"))
async def amireallyalive(awake):
    """ For .awake command, check if the bot is running.  """
    await awake.delete() 
    await borg.send_file(awake.chat_id, ALIVE_PIC,caption=ALIVE_MESSAGE)
