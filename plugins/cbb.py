#(©)Codexbotz
#𖣘Recode By @yangmutebabi

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID, START_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"𖣘 𝐏𝐄𝐌𝐁𝐔𝐀𝐓 : <a href='https://t.me/OcongVer2'>𝑻𝑯𝑰𝑺 𝑷𝑬𝑹𝑺𝑶𝑵</a>\n𖣘 𝐎𝐖𝐍𝐄𝐑 : <a href='https://t.me/naatale'>𝑻𝑯𝑰𝑺 𝑷𝑬𝑹𝑺𝑶𝑵</a>\n𖣘 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 : <a href='https://t.me/romusaaid'>𝑫𝑰𝑺𝑰𝑵𝑰</a>\n𖣘 𝗚𝗥𝗢𝗨𝗣 : <a href='https://t.me/joinchat/Iw0ovQ8yt_1lZTM9'>𝑫𝑰𝑺𝑰𝑵𝑰</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 TUTUP COK", callback_data = "close"),
                    ]
                ]
            )
        )
    elif data == "close": 
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
