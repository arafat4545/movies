# Telegram Movie Provider Bot

## Overview
This is a Telegram bot for providing movies and media files. It includes features like file filtering, user management, premium subscriptions, and a web server for media streaming.

## Architecture

### Core Components
- **bot.py** - Main entry point that initializes the bot and web server
- **info.py** - Configuration and environment variables
- **utils.py** - Utility functions and temp storage
- **Script.py** - Script templates and messages

### Directories
- **database/** - MongoDB database handlers
  - `config_db.py` - Bot configuration
  - `ia_filterdb.py` - Media/file database
  - `users_chats_db.py` - User and chat management
  - `topdb.py` - Top users/stats tracking
  - `jsreferdb.py` - Referral system

- **Jisshu/** - Core bot framework
  - `bot/` - Bot client initialization
  - `server/` - Web server exceptions
  - `template/` - HTML templates for streaming
  - `util/` - Utilities (file handling, streaming, etc.)

- **plugins/** - Bot command handlers and features
  - `Extra/` - Additional features (premium, ads, fsub)
  - `helper/` - Helper functions (bans, channels, fonts)
  - `route.py` - Web server routes for media streaming

### Key Features
- Auto-filter for movies/files
- Premium subscription system
- File streaming via web server
- Force subscription to channels
- Referral system
- Multi-language support

## Configuration
Environment variables are defined in `info.py`:
- `BOT_TOKEN` - Telegram bot token
- `API_ID`, `API_HASH` - Telegram API credentials
- `DATABASE_URI` - MongoDB connection string
- `LOG_CHANNEL` - Telegram channel for logs
- `PORT` - Web server port (default: 5000)

## Running the Bot
```bash
python bot.py
```

The bot runs on port 5000 with an aiohttp web server for media streaming.

## Tech Stack
- Python 3.10
- Pyrogram/Pyrofork (Telegram MTProto library)
- MongoDB (via Motor async driver)
- aiohttp (Web server for streaming)
- Jinja2 (HTML templates)

## Recent Changes
- **2026-01-07**: Initial Replit setup
  - Installed Python 3.10
  - Configured dependencies from requirements.txt
  - Set up workflow for bot execution on port 5000
