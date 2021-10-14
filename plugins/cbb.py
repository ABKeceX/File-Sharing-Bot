#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID, START_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>𖣘 𝐏𝐄𝐌𝐁𝐔𝐀𝐓 : <a href='https://t.me/OcongVer2'>𝑻𝑯𝑰𝑺 𝑷𝑬𝑹𝑺𝑶𝑵</a>\n𖣘 𝐎𝐖𝐍𝐄𝐑 : <a href='https://t.me/gasbakuhantamm'>𝑻𝑯𝑰𝑺 𝑷𝑬𝑹𝑺𝑶𝑵</a>\n𖣘 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝟏 : <a href='https://t.me/Tantekugirang'>𝑫𝑰𝑺𝑰𝑵𝑰</a>\n𖣘 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝟐 : <a href='https://t.me/Tantekusemok'>𝑫𝑰𝑺𝑰𝑵𝑰</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 TUTUP COK", callback_data = "close")],
                    [
                        InlineKeyboardButton("↩️ Kembali", callback_data = "start"),
                    ]
                ]
            )
        )
    if data == "start":
          reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔱 𝐎𝐖𝐍𝐄𝐑", url=f'https://t.me/gasbakuhantam/url')],
                [
                    InlineKeyboardButton("😎 𝙏𝙚𝙣𝙩𝙖𝙣𝙜  𝙎𝙖𝙮𝙖", callback_data = "about"),
                    InlineKeyboardButton("❌ 𝗧𝗨𝗧𝗨𝗣 𝗘𝗨𝗬", callback_data = "close")],
                [
                    InlineKeyboardButton("🔞 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝟏  ", url=f'https://t.me/tantekugirang/url')],
                [
                    InlineKeyboardButton("🔞 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝟐  ", url=f'https://t.me/tantekusemok/url'),
                ]
            ]
        )
        await query.message.reply_text(
            text = START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
            disable_web_page_preview = True,
            quote = True
        )
        return

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
