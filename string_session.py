print(
    "ㅤ\nㅤ\n\n\n\nㅤ\n┈┈┏━╮╭━┓┈╭━━━━━━╮\n┈┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ ┃\n┈┈╰┓▋▋┏╯╯╰━━━━━━╯\n┈╭━┻╮╲┗━━━━╮╭╮┈\n┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n┈┈┈┈┈┗┻┛┗┻┛┈┈"
)
print("\n\n\n\n\nHello vmro!!, I'm Here to Generate Telethon String Session For You")
print("\n\nCOFFINX UB")

print("\n\nProperly Fill APP_ID ,HASH and Number.\n")

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")
with TelegramClient(StringSession(), APP_ID, API_HASH) as hehe:
	dcsession = hehe.session.save()
	dcobra = hehe.send_message(
	    "me",
	    f"`{dcsession}`\n\n**Your CoffinX UB String Session Here VMRO 🤓\nClick on above Code to Copy it\n\nFor Support Join** @CoffinXsupport"
	)

print("\n\n############################\n")
print(
    "check your Telegram Saved Messages For Ur New String String Session 👀 or see below. ")

print("\n############################\n")


print(f"{dcsession}")

Print(" ")
