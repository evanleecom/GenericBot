import os
import logging
from dotenv import load_dotenv, find_dotenv

# Load .evn settings
Settings = {}
load_dotenv(find_dotenv())
keys = os.getenv('ENV_KEYS').split(',')
for key in keys:
    Settings[key] = os.getenv(key.upper(),'')

# Setup default logging config
logging.basicConfig(format=Settings['text_format'],
                    datefmt=Settings['date_format'], level=logging.INFO)
