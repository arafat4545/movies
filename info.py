import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# ---------------------------------------------------------
# 1. CONFIGURATION
# ---------------------------------------------------------
# Replace '8552478417:AAGyzSgqyhaR22byNig5zoTn2hEq3zET4EQ' with the token you got from @BotFather
BOT_TOKEN = '8552478417:AAGyzSgqyhaR22byNig5zoTn2hEq3zET4EQ'

bot = telebot.TeleBot(BOT_TOKEN)

# ---------------------------------------------------------
# 2. YOUR MOVIE DATABASE
# ---------------------------------------------------------
# This dictionary acts as your database. 
# Key = Movie Name (lowercase)
# Value = Details (Image link, Quality, Audio, Direct Link)
movies_db = {
    "avatar": {
        "title": "Avatar: The Way of Water",
        "year": "2022",
        "quality": "1080p IMAX Web-DL",
        "audio": "Hindi (Org 5.1) + English",
        "subtitle": "English [Softcoded]",
        "image_url": "https://m.media-amazon.com/images/M/MV5BYjhiNjBlODctY2ZiOC00YjVlLWFlNzAtNTVhNzM1YjI1NzMxXkEyXkFqcGdeQXVyMjQ4ODgkHA@@._V1_.jpg",
        "link": "https://terabox.com/s/your_file_link_here" 
    },
    "kalki": {
        "title": "Kalki 2898 AD",
        "year": "2024",
        "quality": "4K HDRip",
        "audio": "Telugu + Hindi + Tamil",
        "subtitle": "English",
        "image_url": "https://m.media-amazon.com/images/M/MV5BMmM2YmY0NGEtNjRiZi00ZWY1LThkZjItOWY5NWM0Y2FjYTFkXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
        "link": "https://terabox.com/s/another_link_here"
    }
    # Add more movies here following the same format
}

# ---------------------------------------------------------
# 3. BOT LOGIC
# ---------------------------------------------------------

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome! Send me a movie name (e.g., 'Avatar') and I'll give you the link.")

@bot.message_handler(func=lambda message: True)
def search_movie(message):
    # Convert user input to lowercase to make search easy
    user_query = message.text.lower().strip()

    # Check if the movie exists in our database
    movie_data = movies_db.get(user_query)

    if movie_data:
        # --- 1. Create the Caption (Text info) ---
        caption_text = (
            f"🎬 **Title:** {movie_data['title']} ({movie_data['year']})\n"
            f"💿 **Quality:** {movie_data['quality']}\n"
            f"🔊 **Audio:** {movie_data['audio']}\n"
            f"🎭 **Subtitle:** {movie_data['subtitle']}\n\n"
            f"✅ *File is ready to download!*"
        )

        # --- 2. Create the Single Button ---
        markup = InlineKeyboardMarkup()
        # You can change "Watch Online / Download" to whatever text you want
        btn = InlineKeyboardButton("📥 Watch Online / Download", url=movie_data['link'])
        markup.add(btn)

        # --- 3. Send Photo + Caption + Button ---
        try:
            bot.send_photo(
                chat_id=message.chat.id,
                photo=movie_data['image_url'],
                caption=caption_text,
                parse_mode="Markdown", # Allows bolding like **text**
                reply_markup=markup
            )
        except Exception as e:
            bot.reply_to(message, "Error sending movie details. Please check the image URL.")
            print(e)
    else:
        # Logic if movie is NOT found
        bot.reply_to(message, "❌ Movie not found in my database.\nTry typing the exact name, like 'Avatar' or 'Kalki'.")

# ---------------------------------------------------------
# 4. START THE BOT
# ---------------------------------------------------------
print("Bot is running...")
bot.infinity_polling()
import re
from os import environ,getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
#---------------------------------------------------------------
#---------------------------------------------------------------         ,
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '37245359'))
API_HASH = environ.get('API_HASH', 'e87f2fa53d612bdd793562f75c89995b')
BOT_TOKEN = environ.get('BOT_TOKEN', '8552478417:AAGyzSgqyhaR22byNig5zoTn2hEq3zET4EQ')
#---------------------------------------------------------------
#---------------------------------------------------------------
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5017705882').split()]
USERNAME = environ.get('USERNAME', "https://t.me/Innocent_babe_dead") # ADMIN USERNAME
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1003626988364'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/anime_channel70')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1003546862505').split()]
#---------------------------------------------------------------
#---------------------------------------------------------------
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Aniflare:Aniflare@aniflare.qqzzwoi.mongodb.net/?appName=Aniflare")
DATABASE_NAME = environ.get('DATABASE_NAME', "aniflare")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
#---------------------------------------------------------------
#---------------------------------------------------------------
#----------- There will be channel id add in all these ---------
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '0'))  
BIN_CHANNEL = int(environ.get('BIN_CHANNEL','0'))
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','0'))
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '0'))
auth_channel = environ.get('AUTH_CHANNEL', '')
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '0'))
request_channel = environ.get('REQUEST_CHANNEL', '0')
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '0'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/') #Support group link ( make sure bot is admin )
#---------------------------------------------------------------
#---------------------------------------------------------------
IS_VERIFY = is_enabled('IS_VERIFY', True)
#---------------------------------------------------------------
TUTORIAL = environ.get("TUTORIAL", "https://t.me/")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "3097623f852197a9ce40d1212aaa8bbf2803e799")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'omegalinks.in')
SHORTENER_API2 = environ.get("SHORTENER_API2", "3097623f852197a9ce40d1212aaa8bbf2803e799")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'omegalinks.in')
SHORTENER_API3 = environ.get("SHORTENER_API3", "3097623f852197a9ce40d1212aaa8bbf2803e799")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", 'omegalinks.in')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))
#---------------------------------------------------------------
#---------------------------------------------------------------
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 30
PREMIUM_POINT = 1500
#---------------------------------------------------------------
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
START_IMG = (environ.get('START_IMG', 'https://i.ibb.co/qpxpGmC/image.jpg https://i.ibb.co/DQ35zLZ/image.jpg')).split()
FORCESUB_IMG = environ.get('FORCESUB_IMG', 'https://i.ibb.co/ZNC1Hnb/ad3f2c88a8f2.jpg')
REFER_PICS = (environ.get("REFER_PICS", "https://envs.sh/PSI.jpg")).split() 
PAYPICS = (environ.get('PAYPICS', 'https://envs.sh/_kA.jpg')).split()
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/9f3f47c690bbcc67633c2.jpg'))
REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', False)
PORT = environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or Flase
# Online Stream and Download

MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("FQDN", "")

#---------------------------------------------------------------
#---------------------------------------------------------------
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'tutorial': TUTORIAL,
            'shortner': SHORTENER_WEBSITE,
            'api': SHORTENER_API,
            'shortner_two': SHORTENER_WEBSITE2,
            'api_two': SHORTENER_API2,
            'log': LOG_VR_CHANNEL,
            'imdb': IMDB,
            'link': LINK_MODE, 
            'is_verify': IS_VERIFY, 
            'verify_time': TWO_VERIFY_GAP,
            'shortner_three': SHORTENER_WEBSITE3,
            'api_three': SHORTENER_API3,
            'third_verify_time': THREE_VERIFY_GAP
}
