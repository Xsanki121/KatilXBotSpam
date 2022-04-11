import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import Kat, Kat2, Kat3, Kat4, Kat5, Kat6, Kat7, Kat8, Kat9, Kat10, ALIVE_PIC, OWNER_ID
from KatilXSpam.plugins.help import *


KAT_IMG = ALIVE_PIC if ALIVE_PIC else "LOGO"

Kat_Button = [
        [
        Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/@KatilXSupport")
        ],
        [
        Button.inline("⚡ ᴄᴏᴍᴍᴀɴᴅs ⚡", data="help_back")
        ]
        ]
               
KatX_Button = [
        [
        Button.url("✨ ᴄʜᴀɴɴᴇʟ ✨", "https://t.me/KatilXUpdates"),
        Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/KatilXSupport")
        ],
        [
        Button.url("🔥 ʀᴇᴘᴏ 🔥", "https://github.com/bhumiharsaurabh/KatilXBotSpam")
        ]
        ]
        
        
#USERS 


@Kat.on(events.NewMessage(pattern="/start"))
@Kat2.on(events.NewMessage(pattern="/start"))
@Kat3.on(events.NewMessage(pattern="/start"))
@Kat4.on(events.NewMessage(pattern="/start"))
@Kat5.on(events.NewMessage(pattern="/start"))
@Kat6.on(events.NewMessage(pattern="/start"))
@Kat7.on(events.NewMessage(pattern="/start"))
@Kat7.on(events.NewMessage(pattern="/start"))
@Kat8.on(events.NewMessage(pattern="/start"))
@Kat9.on(events.NewMessage(pattern="/start"))
@Kat10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       KatBot = await event.client.get_me()
       bot_name = KatBot.first_name
       bot_id = KatBot.id
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       Thekatil = event.chat_id
       firstname = replied_user.user.first_name
       userid = replied_user.user.id
       ownermsg = f"**Hello Boss !!, It's Me {bot_name}, Your Spam Bot !! \n\n Click Below Buttons For Help. 🌚**"
       usermsg = f"**Hello !! [{firstname}](tg://user?id={userid})\nNice To Meet You, Well I Am [{bot_name}](tg://user?id={bot_id}), A Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Given Below.** \n\n**Powered By : [Katil 𝙓 𝙎𝙥𝙖𝙢](https://t.me/KatilXSpam)**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(Thekatil,
                  KAT_IMG,
                  caption=ownermsg, 
                  buttons=Kat_Button)
       else:
            await event.client.send_file(Thekatil,
                  KAT_IMG,
                  caption=usermsg, 
                  buttons=KatX_Button)
                
