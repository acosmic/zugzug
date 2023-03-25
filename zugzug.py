#! /usr/bin/python3
import discord
from discord.ext import commands
import requests
from settings import *
from datetime import datetime
from wowaccess import create_access_token
# from wow import *

BOT_PREFIX = '.'
bot = commands.Bot(command_prefix = BOT_PREFIX)
bot.remove_command('help')


# LOG IN
@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.online, activity=discord.Game('.zughelp'))
	for guild in bot.guilds:
		print(guild.id)
	print(f'{bot.user} has connected to Discord!')

@bot.event #check for commands in each message
async def on_message(message):
	await bot.process_commands(message)


# HELP COMMAND
@bot.command(pass_context=True, aliases=[])
async def zughelp(ctx):
	help_embed = discord.Embed(
				colour= discord.Colour(0xffe100),
				title= '.pvp <character name> <server>',
				description= 'Servers with apostrophes, Ex. Mug\'Thol --> mugthol.\n\n'
							 'Servers with multiple names, Ex. Bleeding Hollow --> bleeding-hollow.\n\n'
							 'Examples:\n'
							 '.pvp acosmic illidan\n'
							 '.pvp goreckj mugthol\n'
							 '.pvp wizk bleeding-hollow\n\n'
				)
	help_embed.set_author(name='ZUGZUG - Help')
	help_embed.add_field(name='\u200b', value='Currently only supporting the US region.\n', inline=False)
	help_embed.add_field(name='For issues, go to:', value='[https://github.com/acosmic/zugzug/issues](https://github.com/acosmic/zugzug/issues)')
	print("help function")
	await ctx.send(embed=help_embed)

# CREATE PROFILE
@bot.command(pass_context=True)
async def createprofile(ctx):
	await ctx.send('Please enter your character\'s name and the server name:')

# SET MAIN

# SET ALT



# CHARACTER LOOK UP
@bot.command(pass_context=True, aliases=[])
async def pvp(ctx, character_name, character_server):
	
	API_CHARACTER_URL = 'https://us.api.blizzard.com/profile/wow/character/'+str(character_server).lower()+'/'+str(character_name).lower()
	ACCESS_TOKEN = create_access_token(wowClientId, wowClientSecret)

	achievement_stats = str(API_CHARACTER_URL)+'/achievements/statistics?namespace=profile-us&locale=en_US&access_token='+str(ACCESS_TOKEN)

	url_2v2 = str(API_CHARACTER_URL)+'/pvp-bracket/2v2?namespace=profile-us&locale=en_US&access_token='+str(ACCESS_TOKEN)
	url_3v3 = str(API_CHARACTER_URL)+'/pvp-bracket/3v3?namespace=profile-us&locale=en_US&access_token='+str(ACCESS_TOKEN)
	url_rbg = str(API_CHARACTER_URL)+'/pvp-bracket/rbg?namespace=profile-us&locale=en_US&access_token='+str(ACCESS_TOKEN)
	url_character_image = str(API_CHARACTER_URL)+'/character-media?namespace=profile-us&locale=en_US&access_token='+str(ACCESS_TOKEN)
	character_armory = 'https://worldofwarcraft.com/en-us/character/us/'
	url_character_profile = str(API_CHARACTER_URL)+'?namespace=profile-us&locale=en_US&access_token='+str(ACCESS_TOKEN)

	achievement_stats_response = requests.get(achievement_stats)
	achievement_stats_data = achievement_stats_response.json()

	categories = achievement_stats_data['categories']
	category_names = [d['name'] for d in categories if 'name' in d]
	index_pvp = category_names.index('Player vs. Player')

	subcategories = categories[index_pvp]['sub_categories']
	subcategory_names = [d['name'] for d in subcategories if 'name' in d]

	if 'Rated Arenas' in subcategory_names:
		index_rated = subcategory_names.index('Rated Arenas')

		rated_arena = subcategories[index_rated]['statistics']
		rated_arena_names = [d['name'] for d in rated_arena if 'name' in d]
		index_3v3 = rated_arena_names.index('Highest 3v3 personal rating')
		index_2v2 = rated_arena_names.index('Highest 2v2 personal rating')

		xp_3v3 = int(rated_arena[index_3v3]['quantity'])
		xp_2v2 = int(rated_arena[index_2v2]['quantity'])
	else:
		xp_3v3 = 'pve nerd'
		xp_2v2 = 'pve nerd'


	url_2v2_response = requests.get(url_2v2)
	url_3v3_response = requests.get(url_3v3)
	url_rbg_response = requests.get(url_rbg)
	url_character_image_response = requests.get(url_character_image)
	url_character_profile = requests.get(url_character_profile).json()
	character_class_name = str(url_character_profile['character_class']['name'])
	character_active_spec = str(url_character_profile['active_spec']['name'])
	character_name = character_name.title()
	# avgilvl = '\n\n'+'Average Item Level: '+str(charprofile['average_item_level'])
	equipped_item_level = str(url_character_profile['equipped_item_level'])

	checkguild = 'guild' in url_character_profile
	if checkguild is True:
		guild = '\n<'+str(url_character_profile['guild']['name'])+'>'
	else:
		guild = ''

	checktitle = 'active_title' in url_character_profile
	if checktitle is True:
		title = str(url_character_profile['active_title']['display_string'])
		title = title.replace('{name}', character_name)
	else:
		title = character_name

	data_2v2 = url_2v2_response.json()
	check2v2 = 'rating' in data_2v2
	if check2v2 is True:
		rating_2v2 = str(data_2v2['rating'])
		games_played_2v2 = str(data_2v2['season_match_statistics']['played'])
		games_won_2v2 = str(data_2v2['season_match_statistics']['won'])
		games_lost_2v2 = str(data_2v2['season_match_statistics']['lost'])
	else:
		rating_2v2 = '0'
		games_played_2v2 = '0'
		games_won_2v2 = '0'
		games_lost_2v2 = '0'
	
	data_3v3 = url_3v3_response.json()
	check3v3 = 'rating' in data_3v3
	if check3v3 is True:
		rating_3v3 = str(data_3v3['rating'])
		games_played_3v3 = str(data_3v3['season_match_statistics']['played'])
		games_won_3v3 = str(data_3v3['season_match_statistics']['won'])
		games_lost_3v3 = str(data_3v3['season_match_statistics']['lost'])
	else:
		rating_3v3 = '0'
		games_played_3v3 = '0'
		games_won_3v3 = '0'
		games_lost_3v3 = '0'
	
	data_rbg = url_rbg_response.json()
	checkrbg = 'rating' in data_rbg
	if checkrbg is True:
		rating_rbg = str(data_rbg['rating'])
		games_played_rbg = str(data_rbg['season_match_statistics']['played'])
		games_won_rbg = str(data_rbg['season_match_statistics']['won'])
		games_lost_rbg = str(data_rbg['season_match_statistics']['lost'])
	else:
		rating_rbg = '0'
		games_played_rbg = '0'
		games_won_rbg = '0'
		games_lost_rbg = '0'

	character_image = url_character_image_response.json()
	covenant = '\n'+str(url_character_profile['covenant_progress']['chosen_covenant']['name'])
	renown = ' '+str(url_character_profile['covenant_progress']['renown_level'])

	
	r_embed = discord.Embed(
				colour= discord.Colour(0xffe100),
				title=
				'Current - 2v2: '+rating_2v2+'       3v3: '+rating_3v3+'       RBG: '+rating_rbg+'\n'+
				'Highest - 2v2: '+str(xp_2v2)+'       3v3: '+str(xp_3v3)
		,
				description= '['+'Armory'+']'+'('+str(character_armory)+')'
				)
	r_embed.set_author(name=title+' - '+str(character_server).title()+'   |   '+equipped_item_level+' '+character_active_spec+' '+character_class_name+covenant+renown+guild)
	r_embed.set_image(url=character_image['assets'][2]['value'])
	# r_embed.set_footer(text='['+'Armory Link'+']'+'('+str(charArmory)+')')
	if int(games_played_2v2) > 0:
		win_rate_2v2 = int(games_won_2v2)/int(games_played_2v2)*100
		win_rate_2v2 = str(round(win_rate_2v2))+'%'
	else:
		win_rate_2v2 = ''

	if int(games_played_3v3) > 0:
		win_rate_3v3 = int(games_won_3v3)/int(games_played_3v3)*100
		win_rate_3v3 = str(round(win_rate_3v3))+'%'
	else:
		win_rate_3v3 = ''

	if int(games_played_rbg) > 0:
		win_rate_rbg = int(games_won_rbg)/int(games_played_rbg)*100
		win_rate_rbg = str(round(win_rate_rbg))+'%'
	else:
		win_rate_rbg = ''

	# 2v2
	r_embed.add_field(name='2v2 Played:',value=games_played_2v2 +'  -  '+win_rate_2v2, inline=True)
	r_embed.add_field(name='Won:',value=games_won_2v2, inline=True)
	r_embed.add_field(name='Lost:',value=games_lost_2v2, inline=True)
	# 3v3
	r_embed.add_field(name='3v3 Played:',value=games_played_3v3 +'  -  '+win_rate_3v3, inline=True)
	r_embed.add_field(name='Won:',value=games_won_3v3, inline=True)
	r_embed.add_field(name='Lost:',value=games_lost_3v3, inline=True)
	# RBG
	r_embed.add_field(name='RBG Played:',value=games_played_rbg +'  -  '+win_rate_rbg, inline=True)
	r_embed.add_field(name='Won:',value=games_won_rbg, inline=True)
	r_embed.add_field(name='Lost:',value=games_lost_rbg, inline=True)
	
	await ctx.send(embed=r_embed)


# # @bot.command(pass_context=True, aliases=['',])
# # async def pve(ctx, charName, charServer):

# # 	def create_access_token(client_id, client_secret, region = 'us'):
# # 	    data = { 'grant_type': 'client_credentials' }
# # 	    response = requests.post('https://%s.battle.net/oauth/token' % region, data=data, auth=(client_id, client_secret))
# # 	    return response.json()
	
# # 	response = create_access_token(wowClientId, wowClientSecret)
# # 	access_token = response['access_token']


@bot.command(pass_context=True)
async def zugzug(ctx):
	await ctx.send('https://tenor.com/view/zug-zug-wo-w-world-of-warcraft-orc-dance-gif-12706638')


if __name__ == '__main__':
	bot.run(ZUGZUG)
