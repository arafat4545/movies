import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# ---------------------------------------------------------
# 1. CONFIGURATION
# ---------------------------------------------------------
# Replace 'YOUR_BOT_TOKEN_HERE' with the token you got from @BotFather
BOT_TOKEN = 'AAGyzSgqyhaR22byNig5zoTn2hEq3zET4EQ'

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
