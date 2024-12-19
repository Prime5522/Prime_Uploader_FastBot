# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import asyncio
from typing import (
    Union
)
from config import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def get_invite_link(bot: Client, chat_id: Union[str, int]):
    try:
        invite_link = await bot.create_chat_invite_link(chat_id=chat_id)
        return invite_link
    except FloodWait as e:
        print(f"Sleep of {e.value}s caused by FloodWait ...")
        await asyncio.sleep(e.value)
        return await get_invite_link(bot, chat_id)


async def handle_force_sub(bot: Client, update: Message):
    if Config.TECH_VJ_UPDATES_CHANNEL and str(Config.TECH_VJ_UPDATES_CHANNEL).startswith("-100"):
        channel_chat_id = int(Config.TECH_VJ_UPDATES_CHANNEL)
    elif Config.TECH_VJ_UPDATES_CHANNEL and (not Config.TECH_VJ_UPDATES_CHANNEL.startswith("-100")):
        channel_chat_id = Config.TECH_VJ_UPDATES_CHANNEL
    else:
        return 200
    try:
        user = await bot.get_chat_member(chat_id=channel_chat_id, user_id=update.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=update.from_user.id,
                text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/Prime_botz_Support).",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        try:
            invite_link = await get_invite_link(bot, chat_id=channel_chat_id)
        except Exception as err:
            print(f"Unable to do Force Subscribe to {Config.TECH_VJ_UPDATES_CHANNEL}\n\nError: {err}")
            return 200
        await bot.send_message(
            chat_id=update.from_user.id,
            text = (
    "Iғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜꜱᴇ ᴍᴇ ғɪʀꜱᴛ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ Jᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ.\n\n"
    "ғɪʀꜱᴛ, ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ '✇ Jᴏɪɴ Oᴜʀ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ✇' ʙᴜᴛᴛᴏɴ, "
    "ᴛʜᴇɴ, ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ 'ʀᴇᴏᴜᴇꜱᴛ ᴛᴏ Jᴏɪɴ' ʙᴜᴛᴛᴏɴ.\n\n"
    "ᴀғᴛᴇʀ ᴛʜᴀᴛ ᴄᴏᴍᴇ ʜᴇʀᴇ ᴀɢᴀɪɴ ᴀɴᴅ 🔄 ᴄʟɪᴄᴋ ᴛᴏ ᴛʀʏ ᴀɢᴀɪɴ ♻️."
            ),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("✇ Jᴏɪɴ Oᴜʀ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ✇", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("🔄 Refresh 🔄", callback_data="refreshForceSub")
                    ]
                ]
            )
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=update.from_user.id,
            text="Something went Wrong. Contact my [Support Group](https://t.me/Prime_botz_Support).",
            disable_web_page_preview=True
        )
        return 200
    return 200
