import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LINE Bot settings
LINE_CHANNEL_SECRET = os.environ.get("LINE_CHANNEL_SECRET")
LINE_CHANNEL_ACCESS_TOKEN = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")

# API Server settings
PORT = os.environ.get("PORT")
IP = os.environ.get("IP")
