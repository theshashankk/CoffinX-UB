
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
   ALIVE_MESSAGE = "**π±π²πΎπ΅π΅πΈπ½ π πΈπ π°ππ°πΊπ΄π± \n\n\n**"
   ALIVE_MESSAGE += "`MΚ Κα΄α΄ sα΄α΄α΄α΄s\n\n\n`"
   ALIVE_MESSAGE += f"`Tα΄Κα΄α΄Κα΄Ι΄: TELETHON-1.19.0 \n\n`"
   ALIVE_MESSAGE += f"`PΚα΄Κα΄Ι΄: PYTHON-3.8.5 \n\n`"
   ALIVE_MESSAGE += "`I'll Be With You Master Till My Dyno Ends!!β  \n\n`"
   ALIVE_MESSAGE += f"`Sα΄α΄α΄α΄Κα΄ GΚα΄α΄α΄` : @CoffinXsupport \n\n"
   ALIVE_MESSAGE += f"`MΚ Κα΄ssπ€`: {DEFAULTUSER} \n\n "
                
            
#@command(outgoing=True, pattern="^.awake$")
@borg.on(admin_cmd(pattern=r"awake"))
async def amireallyalive(awake):
    """ For .awake command, check if the bot is running.  """
    await awake.delete() 
    await borg.send_file(awake.chat_id, ALIVE_PIC,caption=ALIVE_MESSAGE)
