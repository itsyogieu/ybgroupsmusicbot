from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I am an Telegram YB Groups Music bot! [ð¶](https://telegra.ph/file/ae4fecebac9d00089adf9.jpg) 
        I let you play music in your group's voice chat.

Bot Maintained By @YogeshBots 
â ï¸You must Join our channel in order to use með

The commands I currently support are:

/play - ð¶ Play the replied audio file or YouTube video 
/pause - â¶ï¸ Pause the audio stream 
/resume - â¸ Resume the audio stream 
/skip - âªï¸ Skip the current audio stream
/mute - ð Mute the userbot
/unmute - ð Unmute the userbot
/stop - ðð Clear the queue and remove the userbot from the call
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Subscribe", url="https://bit.ly/3ezKasi"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/YogeshBots"
                    )
                ]
            ]
        )
    )
