from pyrogram import filters
from pyrogram.types import Message

from NOBITA_MUSIC import app
from NOBITA_MUSIC.core.call import NOBITA

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await VILLAIN.stop_stream_force(message.chat.id)
