import asyncio
from time import time
from datetime import datetime
from Music import BOT_USERNAME
from Music.config import UPDATES_CHANNEL, ZAID_SUPPORT
from Music.MusicUtilities.helpers.filters import command
from Music.MusicUtilities.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6b3999a2e4a7eded83161.jpg",
        caption=f"""**👋Sᴀʟᴀᴍᴀ' Wᴀxᴀᴀɴ Aʜᴀʏ Bᴏᴛ Hᴇᴇɢᴀɴ ᴀʜ . Iɢᴜ Cᴀsᴜᴜᴍ Qᴏʟᴋᴀᴀɢᴀ Sɪ Aᴀɴ Kᴀᴀɢᴀ Cᴀᴀᴡɪʏᴏ Mᴀᴀᴍᴜʟɪᴅᴀ Gʀᴏᴜᴘ ᴋᴀᴀɢᴀ!...💙  Mᴀɴᴀɢᴇʀ Bᴏᴛ Rᴇᴀʟ [F͜͡𝖆𝖗𝖒𝖆𝖆](t.me/Maahirmohamed)😎Powered By [Osᴍᴀɴɪ Hᴇʟᴘᴇʀ](t.me/teamosmani) .....
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅꜱ", url=f"https://t.me/teamosmani"
                    ),
                    InlineKeyboardButton(
                        "😎 Oᴡɴᴇʀ 😎", url="https://t.me/ribajosmani"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📢 ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 🇸🇴", url=f"https://t.me/{ZAID_SUPPORT}"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1cbf94f1df06596632c7b.jpg",
        caption=f"""Thanks For Adding Me To Ur Chat, For Any Query U Can Join Our Support Groups 🔥♥️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🦁 ᴊᴏɪɴ ʜᴇʀᴇ 💙", url=f"https://t.me/{SUPPORT_GROUP}")
                ]
            ]
        ),
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cb4bac8c80b3f6e0c8c0a.jpg",
        caption=f"""Here Is The Owner home sit-down/rest  And take some Stars ✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😎 Oᴡɴᴇʀ 😎", url=f"https://t.me/ribajosmani")
                ]
            ]
        ),
    )
