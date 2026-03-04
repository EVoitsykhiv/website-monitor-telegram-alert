import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
WEBSITE_URL = os.getenv("WEBSITE_URL")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 60))
