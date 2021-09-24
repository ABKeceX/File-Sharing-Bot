#(©)Codexbotz

import pyromod.listen
from pyrogram import Client
import sys

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, CHANNEL_ID

class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()

        if FORCE_SUB_CHANNEL:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot Tidak bisa mengekspor link di Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Silahkan Cek Ulang Apakah ID FORCE_SUB_CHANNEL Benar dan Pastikan Bot Sudah Menjadi Admin Di Channel Di Invite Dengan Izin Link, Force Sub Channel Di: {FORCE_SUB_CHANNEL}")
                self.LOGGER(__name__).info("\nBot Terhenti. Tanyakan https://t.me/yangmutebabi for support")
                sys.exit()
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Pastikan Bot Sudah Admin Di DB Channel, dan cek juga ID Channel Apakah Benar, ID di {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Terhenti. Tanyakan https://t.me/yangmutebabi for support")
            sys.exit()

        self.set_parse_mode("html")
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by 『A̶̢̹̩̯̗̰̣͔̠͛̐͒͛̐̒̐̌ ̸̝͎̦́̔͠Β̸͌͂̑̆𖣘』乂 K͜͜͡ᴇꮯᴇꪎꤪ\nhttps://t.me/yangmutebabi")
        self.username = usr_bot_me.username

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot Terhenti.")
