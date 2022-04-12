# Katil X Spam | @KatilXSpam
# Keep Credits Madafaka !!
import os
import asyncio
import sys
import git
import heroku3
from KatilXSpam import Kat, Kat2, Kat3, Kat4, Kat5 , Kat6, Kat7, Kat8, Kat9, Kat10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, Katilversion
from KatilXSpam import CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
from KatilXSpam import ALIVE_NAME, ALIVE_PIC, ALIVE_TEXT
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

KAT_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/2ada1cd833d9361c35a78.jpg"

KAT_TEXT = ALIVE_TEXT if ALIVE_TEXT else "╚»★ 𝐊𝐚𝐭𝐢𝐥𝗫𝗦𝗽𝗮𝗺 𝗶𝘀 𝗛𝗲𝗿𝗲 ★«╝"

mention = f"[{ALIVE_NAME}](tg://user?id={OWNER_ID})"
                                  
@Kat.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Kat2.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Kat3.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Kat4.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Kat5.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Kat6.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Kat7.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Kat8.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Kat9.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Kat10.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
  if event.sender_id in SUDO_USERS:
      start = datetime.now()
      text = "𝘊𝘩𝘦𝘤𝘬𝘪𝘯𝘨..."
      check = await event.reply(text, parse_mode=None, link_preview=None )
      end = datetime.now()
      ms = (end-start).microseconds / 1000
      await check.delete()
      await event.client.send_file(event.chat_id,
                                  KAT_PIC, caption=f"""{KAT_TEXT}\n\n═══════════════════\n⚡ 𝐏𝐢𝐧𝐠  : `{ms}ᵐˢ`\n⚡ 𝐎𝐰𝐧𝐞𝐫 : {mention}\n⚡ 𝐊𝐚𝐭𝐢𝐥 𝐗 𝐒𝐩𝐚𝐦 : `{Katilversion}`\n⚡ 𝐏𝐲𝐭𝐡𝐨𝐧 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : `3.9.6`\n⚡ 𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : `{version.__version__}`\n═══════════════════\n\n""", buttons=[
        [
        Button.url("✨ ᴄʜᴀɴɴᴇʟ ✨", "https://t.me/KatilXUpdates"),
        Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/KatilXSupport")
        ],
        [
        Button.url("🔥 ʀᴇᴘᴏ 🔥", "https://github.com/bhumiharsaurabh/KatilXBotSpam")
        ]
        ]
        )
    
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

@Kat.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Kat2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Kat3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Kat4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Kat5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Kat6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Kat7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Kat8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Kat9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Kat10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "𝙋𝙤𝙣𝙜!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        message = await event.get_reply_message()
        user = await event.client(GetFullUserRequest(message.sender_id))
        firstname = user.user.first_name
        userid = user.user.id
    if userid == OWNER_ID:
        await event.edit(f"▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀\n▒█▀▀▄ ▒█░░▒█ ░▒█░░\n▒█▄▄█ ▒█▄▄▄█ ░▒█░░\n\n    ⚡ 𝐊𝐚𝐭𝐢𝐥 𝐗 𝐒𝐩𝐚𝐦 ⚡\n\n𝐏𝐢𝐧𝐠 : `{ms}` ᴍs\n𝐎𝐰𝐧𝐞𝐫 : [{firstname}](tg://user?id={userid})")
    else:
        await event.edit(f"▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀\n▒█▀▀▄ ▒█░░▒█ ░▒█░░\n▒█▄▄█ ▒█▄▄▄█ ░▒█░░\n\n    ⚡ 𝐊𝐚𝐭𝐢𝐥 𝐗 𝐒𝐩𝐚𝐦 ⚡\n\n𝐏𝐢𝐧𝐠 : `{ms}` ᴍs\n𝐒𝐮𝐝𝐨 𝐔𝐬𝐞𝐫 : [{firstname}](tg://user?id={userid})")
        
        

@Kat.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Kat2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Kat3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Kat4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Kat5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Kat6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Kat7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Kat8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Kat9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Kat10.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "𝗥𝗲𝘀𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝐊𝐚𝐭𝐢𝐥 𝗫 𝗦𝗽𝗮𝗺... | Please Wait For Few Seconds."
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await Kat.disconnect()
        except Exception:
            pass
        try:
            await Kat2.disconnect()
        except Exception:
            pass
        try:
            await Kat3.disconnect()
        except Exception:
            pass
        try:
            await Kat4.disconnect()
        except Exception:
            pass
        try:
            await Kat5.disconnect()
        except Exception:
            pass
        try:
            await Kat6.disconnect()
        except Exception:
            pass
        try:
            await Kat7.disconnect()
        except Exception:
            pass
        try:
            await Kat8.disconnect()
        except Exception:
            pass
        try:
            await Kat9.disconnect()
        except Exception:
            pass
        try:
            await Kat10.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
        

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USER", None)

@Kat.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def tb(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply("Adding User As Sudo...")
        katil = "SUDO_USER"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply To a User !!")
        if sudousers:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"**Added** `{target}` **As Sudo User** ✨ | Restarting... Please Wait Few Seconds.")
        heroku_var[katil] = newsudo   
   
     
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target
