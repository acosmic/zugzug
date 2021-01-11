import os
import requests
from discord.ext import commands
from dotenv import load_dotenv

BOT_PREFIX = '.'
bot = commands.Bot(command_prefix = BOT_PREFIX)
bot.remove_command('help')

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