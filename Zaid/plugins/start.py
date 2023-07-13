from Zaid import Zaid, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
ʜᴇʏᴀ! {}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ **ɪ'ᴍ ᴀ ꜱɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜꜱɪᴄ ᴀɴᴅ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ**.
‣ **ɪ ᴄᴀɴ ᴘʟᴀʏ ꜱᴏɴɢꜱ ɪɴ ʏᴏᴜʀ ᴠᴏɪᴄᴇ**.
‣ **ɪ ʜᴀᴠᴇ ᴀʟᴍᴏꜱᴛ ᴀʟʟ ꜰᴇᴀᴛᴜʀᴇꜱ ᴡʜɪᴄʜ ɴᴇᴇᴅꜱ ᴀ ᴍᴜꜱɪᴄ ʙᴏᴛ**
‣ **ᴛʜɪꜱ ʙᴏᴛ ʙᴀꜱᴇᴅ ᴏɴ ᴛᴇʟᴇᴛʜᴏɴ. ꜱᴏ ɪᴛ'ꜱ ᴘʀᴏᴠɪᴅᴇ ᴍᴏʀᴇ ꜱᴛᴀʙɪʟɪᴛʏ ꜰʀᴏᴍ ᴏᴛʜᴇʀ ʙᴏᴛꜱ**!
‣ **ɪ ᴄᴀɴ ᴅᴏ ᴏᴛʜᴇʀ ᴛʜɪɴɢꜱ ʟɪᴋᴇ ᴘɪɴꜱ ᴇᴛᴄꜱ**.
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ **Want to make money at home?**.
**Join us and click register below**.
"""

@Zaid.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ 𝐀𝐝𝐝 𝐦𝐞 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐜𝐡𝐚𝐭", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("📲 𝐑𝐞𝐠𝐢𝐬𝐭𝐞𝐫", f"http://www.9987up.cc/#/register?r_code=3272217765")],
        [Button.url("📁 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", f"https://t.me/TCearningtownbygeeta"), Button.url("👤 𝐂𝐨𝐧𝐭𝐚𝐜𝐭", f"https://t.me/geethaisback")],
        [Button.inline("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", data="help")]])
       return

    if event.is_group:
       await event.reply("**Hey Im online ✅**")
       return



@Zaid.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ 𝐀𝐝𝐝 𝐦𝐞 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐜𝐡𝐚𝐭", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("📲 𝐑𝐞𝐠𝐢𝐬𝐭𝐞𝐫", f"http://www.9987up.cc/#/register?r_code=3272217765")],
        [Button.url("📁 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", f"https://t.me/TCearningtownbygeeta"), Button.url("👤 𝐂𝐨𝐧𝐭𝐚𝐜𝐭", f"https://t.me/geethaisback")],
        [Button.inline("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", data="help")]])
       return


@Zaid.on(events.NewMessage(pattern="^[?!/]register$"))
async def start(event):
     if event.is_group:
       await event.reply("**https://www.9987up.cc/#/register?r_code=3272217765 📲**")
       return

@Zaid.on(events.NewMessage(pattern="^[?!/]money$"))
async def start(event):
     if event.is_group:
       await event.reply("**@TCearningtownbygeeta 🌐**")
       return

@Zaid.on(events.NewMessage(pattern="^[?!/]channel$"))
async def start(event):
     if event.is_group:
       await event.reply("**@geethaisback ✅**")
       return
