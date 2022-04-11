from KatilXSpam import Kat, Kat2, Kat3, Kat4, Kat5, Kat6, Kat7, Kat8, Kat9, Kat10, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from KatilXSpam import CMD_HNDLR as hl
    
HELP_PIC = "logo"

Kat_Help = "★ 𝐊𝐚𝐭𝐢𝐥𝙓𝙎𝙥𝙖𝙢 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪 ★\n𝐂𝐥𝐢𝐜𝐤 𝐎𝐧 𝐁𝐞𝐥𝐨𝐰 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐅𝐨𝐫 𝐇𝐞𝐥𝐩"


@Kat.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Kat2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Kat3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Kat4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Kat5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Kat6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Kat7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Kat8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Kat9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Kat10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Mig_Help,
                                  buttons=[
           [
            Button.inline("🔥 Spam 🔥", data="spam"),
            Button.inline("😈 Raid 😈", data="raid"),
           ],
           [
            Button.inline("⚡ Extra ⚡", data="extra"),
           ],
           [    
            Button.url("✨ ᴄʜᴀɴɴᴇʟ ✨", "https://t.me/KatilXUpdates")
           ],
           [
           Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/KatilXSupport")
           ],
           ],
           )              

  
  
extra_msg = f"""
**Help Extra Cmds**

**UserBot :** Userbot Cmds
Command :
1) {hl}ping 
2) {hl}alive
3) {hl}restart
4) {hl}addsudo <reply to user> || Owner Cmd ||

**Echo :** To Active Echo On Any User
Command :
1) {hl}addecho <reply to user>
2) {hl}rmecho <reply to user>

**Leave :** To Leave Group/Channel
Command :
1) {hl}leave <group/chat id>
2) {hl}leave : Type in the Group bot will auto leave that group

**PackSpam :** Sticker Pack Spam
1) {hl}packspam (replying to any sticker)

**© @KatilXSpam**
"""

                 
raid_msg = f"""
**Help Raid Cmds**


**Raid :** Activates Raid on Any individual User For Given Range.
Command :
1) {hl}raid <count> <username
2) {hl}raid <count> <reply to user>

**DelayRaid :** Activates Raid on Any individual User For Given Range.
Command :
1) {hl}delayraid <delay> <count> <Username of User>
2) {hl}delayraid <delay> <count> <reply to a User>

**ReplyRaid :** Activates Reply Raid on The User!!
Command :
1) {hl}replyraid <replying to user>
2) {hl}dreplyraid <username>

**DReplyRaid :** Deactivates Reply Raid on The User!!
Command :
1) {hl}dreplyraid <replying to user>
2) {hl}dreplyraid <username>


**© @KatilXSpam**
"""

spam_msg = f"""
**Help Spam Cmds**

**Spam :** Spams a Message For Given Counter(<= 100).
Command :
1) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
2) {hl}spam <count> <replying any message>

**BigSpam :** Spams a Message For Given Counter.
Command :
1) {hl}bigspam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
2) {hl}bigspam <count> <replying any message>

**DelaySpam :** Delay Spam a Text For Given Counter After Given Time.
Command :
1) {hl}delayspam <delay> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
2) {hl}delayspam <delay> <count> <replying any message>

**PormSpam :** Pormography Spam.
Command :
1) {hl}pornspam <count>

**Hang :** Spams Hanging Message For Given Counter.
Command :
1) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)

** © @KatilXSpam**
"""                     
           
           
@Kat.on(events.CallbackQuery(pattern=r"help_back"))
@Kat2.on(events.CallbackQuery(pattern=r"help_back"))
@Kat3.on(events.CallbackQuery(pattern=r"help_back"))
@Kat4.on(events.CallbackQuery(pattern=r"help_back"))
@Kat5.on(events.CallbackQuery(pattern=r"help_back"))
@Kat6.on(events.CallbackQuery(pattern=r"help_back"))
@Kat7.on(events.CallbackQuery(pattern=r"help_back"))
@Kat8.on(events.CallbackQuery(pattern=r"help_back"))
@Kat9.on(events.CallbackQuery(pattern=r"help_back"))
@Kat10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            Kat_Help,
            buttons=[
           [
            Button.inline("🔥 Spam 🔥", data="spam"),
            Button.inline("😈 Raid 😈", data="raid"),
           ],
           [
            Button.inline("⚡ Extra ⚡", data="extra"),
           ],
           [    
            Button.url("✨ ᴄʜᴀɴɴᴇʟ ✨", "https://t.me/KatilXUpdates")
           ],
           [
           Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/KatilXSupport")
           ],
           ],
        )           
   else:
        Alert = (
                "Noob !! Make Your Own Katil X Spam Bots !! @KatilXSpam"
            )
        await event.answer(Alert, cache_time=0, alert=True)
      
           
                      
@Kat.on(events.CallbackQuery(pattern=r"spam"))
@Kat2.on(events.CallbackQuery(pattern=r"spam"))
@Kat3.on(events.CallbackQuery(pattern=r"spam"))
@Kat4.on(events.CallbackQuery(pattern=r"spam"))
@Kat5.on(events.CallbackQuery(pattern=r"spam"))
@Kat6.on(events.CallbackQuery(pattern=r"spam"))
@Kat7.on(events.CallbackQuery(pattern=r"spam"))
@Kat8.on(events.CallbackQuery(pattern=r"spam"))
@Kat9.on(events.CallbackQuery(pattern=r"spam"))
@Kat10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(
            spam_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            ) 
   else:
        Alert = (
                "Noob !! Make Your Own Katil X Spam Bots !! @KatilXSpam"
            )
        await event.answer(Alert, cache_time=0, alert=True)
                 
                                                       
@Kat.on(events.CallbackQuery(pattern=r"raid"))
@Kat2.on(events.CallbackQuery(pattern=r"raid"))
@Kat3.on(events.CallbackQuery(pattern=r"raid"))
@Kat4.on(events.CallbackQuery(pattern=r"raid"))
@Kat5.on(events.CallbackQuery(pattern=r"raid"))
@Kat6.on(events.CallbackQuery(pattern=r"raid"))
@Kat7.on(events.CallbackQuery(pattern=r"raid"))
@Kat8.on(events.CallbackQuery(pattern=r"raid"))
@Kat9.on(events.CallbackQuery(pattern=r"raid"))
@Kat10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(
            raid_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            )  
     else:
        Alert = (
                "Noob !! Make Your Own Katil X Spam Bots !! @KatilXSpam"
            )
        await event.answer(Alert, cache_time=0, alert=True)
       


@Kat.on(events.CallbackQuery(pattern=r"extra"))
@Kat2.on(events.CallbackQuery(pattern=r"extra"))
@Kat3.on(events.CallbackQuery(pattern=r"extra"))
@Kat4.on(events.CallbackQuery(pattern=r"extra"))
@Kat5.on(events.CallbackQuery(pattern=r"extra"))
@Kat6.on(events.CallbackQuery(pattern=r"extra"))
@Kat7.on(events.CallbackQuery(pattern=r"extra"))
@Kat8.on(events.CallbackQuery(pattern=r"extra"))
@Kat9.on(events.CallbackQuery(pattern=r"extra"))
@Kat10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(
            extra_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),                        
            ],
            ],
            )
   else:
        Alert = (
                "Noob !! Make Your Own Katil X Spam Bots !! @KatilXSpam"
            )
        await event.answer(Alert, cache_time=0, alert=True)
