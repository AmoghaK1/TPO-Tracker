import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

TPO_URL = "https://tpo.vierp.in"
COMPANY_PAGE = "https://tpo.vierp.in/apply_company"