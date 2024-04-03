from pyrogram import Client, filters
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters
from pyrogram.types import Message
import time
import psutil
import platform
import logging

import pyrogram
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.INFO)

# -------------------------------------------------------------------------------------

BOT_USERNAME = os.environ.get("BOT_USERNAME","MainCrunchyrollBot")

OWNER_ID = "5586770042"
# -------------------------------------------------------------------------------------

API_ID = "21279292" # 
API_HASH = "b9f12d911d85b4a60fa13ba9c2c09712"
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

app = Client('my_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ----------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------


start_txt = """<b>  ᴍᴀɪɴ ᴄʀᴜɴᴄʜʏʀᴏʟʟ ʜɪɴᴅɪ  </b>

ᴡᴇ ᴘʀᴇsᴇɴᴛs "ᴍᴀɪɴ ᴄʀᴜɴᴄʜʏʀᴏʟʟ ʜɪɴᴅɪ" ᴛᴏ ᴘʀᴏᴠɪᴅɪɴɢ ɴᴏɴ sᴛᴏᴘ ᴀɴɪᴍᴇ ᴏғ ᴀʟʟ ᴛɪᴍᴇ , ᴡᴇ ʜᴀᴠᴇ ᴡᴏʀᴋᴇᴅ ʜᴀʀᴅ ᴛᴏ ᴇɴꜱᴜʀᴇ ᴀ ᴄᴏɴꜱɪꜱᴛᴇɴᴛ ᴜᴘʟᴏᴀᴅ ꜱᴄʜᴇᴅᴜʟᴇ, ᴡᴇᴇᴋʟʏ ᴜᴘᴅᴀᴛᴇꜱ, ᴀʙɪʟɪᴛʏ ᴛᴏ ʀᴇQᴜᴇꜱᴛ ᴀɴɪᴍᴇ, ᴜꜱᴇʀ ꜰʀɪᴇɴᴅʟʏ ɪɴᴛᴇʀꜰᴀᴄᴇ, ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴀɴᴅ ᴏɴɢᴏɪɴɢ  ᴀɴɪᴍᴇ ᴜᴘʟᴏᴀᴅꜱ, ᴅɪꜱᴄᴜꜱꜱɪᴏɴ ɢʀᴏᴜᴘ ᴀɴᴅ ꜱᴏ ᴍᴜᴄʜ ᴍᴏʀᴇ."""

@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴍᴀɪɴ ᴄʀᴜɴᴄʜʏʀᴏʟʟ ʜɪɴᴅɪ", url=f"https://t.me/Main_Crunch_Roll_Hindii")
        ],
        [
          InlineKeyboardButton("ᴀɴɪᴍᴇ ᴅɪsᴄᴜss ɢʀᴏᴜᴘ", url=f"https://t.me/The_Sector_5")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/9851c002b99d2dc456392.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )

start_txt = """<b>  ᴍᴀɪɴ ᴄʀᴜɴᴄʜʏʀᴏʟʟ ʜɪɴᴅɪ  </b>

ᴡᴇ ᴘʀᴇsᴇɴᴛs "ᴍᴀɪɴ ᴄʀᴜɴᴄʜʏʀᴏʟʟ ʜɪɴᴅɪ" ᴛᴏ ᴘʀᴏᴠɪᴅɪɴɢ ɴᴏɴ sᴛᴏᴘ ᴀɴɪᴍᴇ ᴏғ ᴀʟʟ ᴛɪᴍᴇ , ᴡᴇ ʜᴀᴠᴇ ᴡᴏʀᴋᴇᴅ ʜᴀʀᴅ ᴛᴏ ᴇɴꜱᴜʀᴇ ᴀ ᴄᴏɴꜱɪꜱᴛᴇɴᴛ ᴜᴘʟᴏᴀᴅ ꜱᴄʜᴇᴅᴜʟᴇ, ᴡᴇᴇᴋʟʏ ᴜᴘᴅᴀᴛᴇꜱ, ᴀʙɪʟɪᴛʏ ᴛᴏ ʀᴇQᴜᴇꜱᴛ ᴀɴɪᴍᴇ, ᴜꜱᴇʀ ꜰʀɪᴇɴᴅʟʏ ɪɴᴛᴇʀꜰᴀᴄᴇ, ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴀɴᴅ ᴏɴɢᴏɪɴɢ  ᴀɴɪᴍᴇ ᴜᴘʟᴏᴀᴅꜱ, ᴅɪꜱᴄᴜꜱꜱɪᴏɴ ɢʀᴏᴜᴘ ᴀɴᴅ ꜱᴏ ᴍᴜᴄʜ ᴍᴏʀᴇ."""

@app.on_message(filters.command("anime"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴍᴀɪɴ ᴄʀᴜɴᴄʜʏʀᴏʟʟ ʜɪɴᴅɪ", url=f"https://t.me/Main_Crunch_Roll_Hindii")
        ],
        [
          InlineKeyboardButton("ᴀɴɪᴍᴇ ᴅɪsᴄᴜss ɢʀᴏᴜᴘ", url=f"https://t.me/The_Sector_5")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/9851c002b99d2dc456392.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )


gd_buttons = [              
        [
            InlineKeyboardButton("ᴏᴡɴᴇʀ", user_id=OWNER_ID),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/drakun_copyright"), 
        ],
    [
            InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="copyright_back"),
        ],
]


# ------------------------------------------------------------------------------- #


@app.on_callback_query(filters.regex("dil_back"))
async def dil_back(_, query: CallbackQuery):
    await query.message.edit_caption(start_txt,
                                    reply_markup=InlineKeyboardMarkup(gd_buttons),)
        

# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------


start_time = time.time()

def time_formatter(milliseconds: float) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

def size_formatter(bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            break
        bytes /= 1024.0
    return f"{bytes:.2f} {unit}"


@app.on_message(filters.command('users'))
async def get_users(client, message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    await msg.edit(f"{len(users)} users are using this bot")



@app.on_message(filters.command("ping"))
async def activevc(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    storage = psutil.disk_usage('/')

    python_version = platform.python_version()

    reply_text = (
        f"➪ᴜᴘᴛɪᴍᴇ: {uptime}\n"
        f"➪ᴄᴘᴜ: {cpu}%\n"
        f"➪ꜱᴛᴏʀᴀɢᴇ: {size_formatter(storage.total)} [ᴛᴏᴛᴀʟ]\n"
        f"➪{size_formatter(storage.used)} [ᴜsᴇᴅ]\n"
        f"➪{size_formatter(storage.free)} [ғʀᴇᴇ]\n"
        f"➪ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: {python_version},"
    )

    await message.reply(reply_text, quote=True)


    
# -------------------------------------------------------------------------------------



FORBIDDEN_KEYWORDS = ["", "", "", "", "", "", "", "", "", "", "", "", ""]

@app.on_message()
async def handle_message(client, message):
    if any(keyword in message.text for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
      #  user_mention = from_user.mention
        await message.reply_text(f"")
    elif any(keyword in message.caption for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
       # user_mention = from_user.mention
        await message.reply_text(f"")
        
        
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.delete()



# ----------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
def delete_long_messages(_, m):
    return len(m.text.split()) > 10

@app.on_message(filters.group & filters.private & delete_long_messages)
async def delete_and_reply(_, msg):
    await msg.delete()
    user_mention = msg.from_user.mention
    await app.send_message(msg.chat.id, f"")
    

# -----------------------------------------------------------------------------------


    
@app.on_message(filters.animation | filters.audio | filters.document | filters.photo | filters.sticker | filters.video)
async def keep_reaction_message(client, message: Message):
    pass 
# -------------------------------

async def delete_pdf_files(client, message):
    if message.document and message.document.mime_type == "":
        warning_message = f""
        await message.reply_text(warning_message)
        await message.delete()
    else:  
        pass

@app.on_message(filters.group & filters.document)
async def message_handler(client, message):
    await delete_pdf_files(client, message)

# -----------------------------------------------------------------------------------

print(f"""╔═════❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱════❍⊱❁۪۪║┏━━━━━━➣║┣⪼ ᴏᴡɴᴇʀ :- @DaxxSir3 ║┣⪼ ᴘᴀʀᴛ ᴏғ :- @ALLTYPECC║┗━━━━━━➣║╔═════ஜ۩۞۩ஜ════╗║अनंत अखंड अमर अविनाशी║कष्ट हरण है║शंभु कैलाशी║╚═════ஜ۩۞۩ஜ════╝╚═════════════════❍⊱❁ """)
app.run()
