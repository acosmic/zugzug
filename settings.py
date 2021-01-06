import os
import requests
import praw
from discord.ext import commands
from dotenv import load_dotenv

BOT_PREFIX = '.'
bot = commands.Bot(command_prefix = BOT_PREFIX)
bot.remove_command('help')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN2 = os.getenv('DISCORD_TOKEN2')
ZUGZUG = os.getenv('ZUGZUGTOKEN')
WOW_CLIENT_ID = str(os.getenv('WOW_CLIENT_ID'))
WOW_CLIENT_SECRET = str(os.getenv('WOW_CLIENT_SECRET'))
WOW_REGION = str(os.getenv('WOW_REGION'))
WOW_LOCALE = str(os.getenv('WOW_LOCALE'))

# os.chdir(r'/home/cdm/Documents/Discord_Bot-10-2020')

reddit = praw.Reddit(
	client_id = os.getenv('client_id_env'),
	client_secret = os.getenv('client_secret_env'),
	user_agent = os.getenv('user_agent_env'),
	username = os.getenv('username_env '),
	password = os.getenv('password_env'))

wowClientId = os.getenv('WOW_CLIENT_ID') 
wowClientSecret = os.getenv('WOW_CLIENT_SECRET') 
wowRegion = os.getenv('WOW_REGION') 
wowLocale = os.getenv('WOW_LOCALE') 