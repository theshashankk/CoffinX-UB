# Thanks to Sipak bro and Aryan.. 
# animation Idea by @ItzSipak && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
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
# π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "π²πΎπ΅π΅πΈπ½ π πππ΄π"

# Thanks to Sipak bro and Aryan.. 
# animation Idea by @ItzSipak && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)
# mod For Coffin With Credit
global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/37ee8db6262b2ea00dbcf.jpg"
""" =======================CONSTANTS====================== """


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))

async def hmm(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    await yes.delete()
    uptime = await dcdef.get_readable_time((time.time() - Lastupdate))
    pm_caption = "** π²πΎπ΅π΅πΈπ½ π πΈπ πΎπ½π»πΈπ½π΄ **\n\n"
    pm_caption += "**Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n"
    pm_caption += "β About My System β\n\n"
    pm_caption += f"β **ππππππππ πππππππ** β {version.__version__}\n"
    pm_caption += "β **πππππππ πΎππΌππππ** β [α΄α΄ΙͺΙ΄](https://t.me/CoffinX_Updates)\n"
    pm_caption += "β **πππΎππππ**  β [ππ΄π°πΌ π²πΎπ΅π΅πΈπ½](https://github.com/theshashankk)\n"
    pm_caption += "β **πΎππππππππ π½π** β [π²πΎπ΅π΅πΈπ½ π ππ±](https://github.com/theshashankk/CoffinX-UB)\n\n"
    pm_caption += f"β **πΎπππππ ππππππ** β {uptime}\n\n"
    pm_caption += f"β **ππ ππππ ππΌππππ** β [{DEFAULTUSER}](tg://user?id={ghanti})\n"
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    
