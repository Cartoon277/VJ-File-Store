# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re
import os
from os import environ

# Regular expression for validating IDs
id_pattern = re.compile(r'^\d+$')

# Helper function to determine boolean values from environment variables
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    return default

# Bot Information
API_ID = int(environ.get("API_ID", "28273838"))  # Default to 0 if not set
API_HASH = environ.get("API_HASH", "2dd5e06872a3db721757f9ecaa5506d4")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
PICS = environ.get('PICS', 'https://graph.org/file/ce1723991756e48c35aa1.jpg').split()  # Bot Start Picture
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6541199141').split()]
BOT_USERNAME = environ.get("BOT_USERNAME", "Nothingbut27bot")  # Without @
PORT = environ.get("PORT", "8080")

# Clone Info
CLONE_MODE = is_enabled(environ.get('CLONE_MODE', "False"), False)

# Clone settings (only used if CLONE_MODE is True)
CLONE_DB_URI = environ.get("CLONE_DB_URI", "")
CDB_NAME = environ.get("CDB_NAME", "clonetechvj")

# Database Information
DB_URI = environ.get("DB_URI", "mongodb+srv://cartoonist680:Y0BT4CfhqVZhviqr@cluster0.jabww.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "techvjbotz")

# Auto Delete Information
AUTO_DELETE_MODE = is_enabled(environ.get('AUTO_DELETE_MODE', "False"), True)

# Auto Delete settings (only used if AUTO_DELETE_MODE is True)
AUTO_DELETE = int(environ.get("AUTO_DELETE", "30"))  # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1800"))  # Time in Seconds

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002255000492"))  # Default to 0 if not set

# File Caption Information
# Assuming 'script' is an imported module with CAPTION; if not, replace with a string
try:
    from Script import script
    CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
except ImportError:
    CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "Default Caption")

BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable/Disable Public File Store
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)

# Verify Info
VERIFY_MODE = is_enabled(environ.get('VERIFY_MODE', "False"), False)

# Verify settings (only used if VERIFY_MODE is True)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "")  # Shortlink domain without https://
SHORTLINK_API = environ.get("SHORTLINK_API", "")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "")  # How to open link

# Website Info
WEBSITE_URL_MODE = is_enabled(environ.get('WEBSITE_URL_MODE', "True"), False)

# Website settings (only used if WEBSITE_URL_MODE is True)
WEBSITE_URL = environ.get("WEBSITE_URL", "https://allupdate05.blogspot.com/2025/03/nothing.html")

# File Stream Config
STREAM_MODE = is_enabled(environ.get('STREAM_MODE', "True"), True)

# Stream settings (only used if STREAM_MODE is True)
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', "60"))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
ON_HEROKU = 'DYNO' in environ
URL = environ.get("URL", "https://testofvjfilter-1fa60b1b8498.herokuapp.com/")

# Ensure all critical variables are set (optional basic validation)
if not API_ID or not API_HASH or not BOT_TOKEN:
    raise ValueError("API_ID, API_HASH, and BOT_TOKEN must be set in environment variables.")

# Credit Information (retained as a comment)
# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

# Optional: Print configuration for debugging (comment out in production)
if __name__ == "__main__":
    print("Bot Configuration Loaded Successfully")
    print(f"API_ID: {API_ID}")
    print(f"BOT_USERNAME: {BOT_USERNAME}")
    print(f"CLONE_MODE: {CLONE_MODE}")
    print(f"AUTO_DELETE_MODE: {AUTO_DELETE_MODE}")
    print(f"STREAM_MODE: {STREAM_MODE}")
​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
    
