#! /usr/bin/python3
import os
from dotenv import load_dotenv




load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN2 = os.getenv('DISCORD_TOKEN2')
ZUGZUG = os.getenv('ZUGZUGTOKEN')
ZUGTEST = os.getenv('ZUGTEST')
WOW_CLIENT_ID = str(os.getenv('WOW_CLIENT_ID'))
WOW_CLIENT_SECRET = str(os.getenv('WOW_CLIENT_SECRET'))
WOW_REGION = str(os.getenv('WOW_REGION'))
WOW_LOCALE = str(os.getenv('WOW_LOCALE'))
wowClientId = os.getenv('WOW_CLIENT_ID') 
wowClientSecret = os.getenv('WOW_CLIENT_SECRET') 
wowRegion = os.getenv('WOW_REGION') 
wowLocale = os.getenv('WOW_LOCALE')

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')