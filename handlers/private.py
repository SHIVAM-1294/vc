from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def help_(client: Client, message: Message):
      await message.reply_text("""ððð², ð'ð¦ ðð ðð¨ð­â¤ï¸ð¥. 
ð ððð§ ðð¥ðð² ðð®ð¬ð¢ð ðð§ ðð¨ð®ð« ðð«ð¨ð®ð© ðð¨ð¢ðð ðð¡ðð­.
ððð ðð ðð¨ ðð¨ð®ð« ðð«ð¨ð®ð© ðð§ð ðð¥ðð² ðð®ð¬ð¢ð ðð«ððð¥ð²! 
/help - ðð¨ ððð­ ðð¨ð¦ð¦ðð§ðð¬.â""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ÃÆSÅ¦ÄªÆS Zá¾ÐÆ", url="https://t.me/BONDOFBESTIZZ")
                ]
            ]
        )
   )
