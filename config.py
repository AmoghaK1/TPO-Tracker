import os
from dotenv import load_dotenv, dotenv_values

# Load .env into process env (without clobbering by default), then
# read raw .env values directly so they can still override OS vars like USERNAME.
load_dotenv()
_ENV_FILE_VALUES = dotenv_values()


def _get_config(*keys):
	for key in keys:
		file_val = _ENV_FILE_VALUES.get(key)
		if file_val not in (None, ""):
			return file_val
		env_val = os.getenv(key)
		if env_val not in (None, ""):
			return env_val
	return None

USERNAME = _get_config("TPO_USERNAME", "USERNAME")
PASSWORD = _get_config("TPO_PASSWORD", "PASSWORD")

BOT_TOKEN = _get_config("TELEGRAM_BOT_TOKEN", "BOT_TOKEN")
CHAT_ID = _get_config("TELEGRAM_CHAT_ID", "CHAT_ID")

TPO_URL = "https://tpo.vierp.in"
COMPANY_PAGE = "https://tpo.vierp.in/apply_company"