#! /usr/bin/python3.8
import discord
from settings import *
# from wow import *
from datetime import datetime

# LOG IN
@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.online, activity=discord.Game('.pvp<Char><Server>'))
	print(f'{bot.user} has connected to Cold Dark Matter!')

wowApiChar = 'https://us.api.blizzard.com/profile/wow/character/'


@bot.command(pass_context=True, aliases=[])
async def pvp(ctx, charName, charServer):

	def create_access_token(client_id, client_secret, region = 'us'):
	    data = { 'grant_type': 'client_credentials' }
	    response = requests.post('https://%s.battle.net/oauth/token' % region, data=data, auth=(client_id, client_secret))
	    return response.json()

	"""
	check-pvp.fr     fix this shit
	need  format the link and change servers to normal format (malganis -> Mal'Ganis) (khaz-modan -> Khaz%20Modan)
	

	def create_checkpvp_link(charName, charServer):
		checkpvp = 'https://check-pvp.fr/us/'str()+
	"""

	response = create_access_token(wowClientId, wowClientSecret)
	access_token = response['access_token']

	achStats = str(wowApiChar) + str(charServer).lower() + '/' + str(
		charName).lower() + '/achievements/statistics?namespace=profile-us&locale=en_US&access_token=' + str(
		access_token)

	url2v2 = str(wowApiChar)+str(charServer).lower()+'/'+str(charName).lower()+'/pvp-bracket/2v2?namespace=profile-us&locale=en_US&access_token='+str(access_token)
	url3v3 = str(wowApiChar)+str(charServer).lower()+'/'+str(charName).lower()+'/pvp-bracket/3v3?namespace=profile-us&locale=en_US&access_token='+str(access_token)
	url10v10 = str(wowApiChar)+str(charServer).lower()+'/'+str(charName).lower()+'/pvp-bracket/rbg?namespace=profile-us&locale=en_US&access_token='+str(access_token)
	urlrender = str(wowApiChar)+str(charServer).lower()+'/'+str(charName).lower()+'/character-media?namespace=profile-us&locale=en_US&access_token='+str(access_token)
	charArmory = 'https://worldofwarcraft.com/en-us/character/us/'+str(charServer).lower()+'/'+str(charName).lower()
	urlprofile = str(wowApiChar)+str(charServer).lower()+'/'+str(charName).lower()+'?namespace=profile-us&locale=en_US&access_token='+str(access_token)

	rachStats = requests.get(achStats)
	aStats = rachStats.json()

	xplist = aStats['categories'][7]['sub_categories'][0]['statistics']
	xplist = [d['name'] for d in xplist if 'name' in d]
	index3v3 = xplist.index('Highest 3v3 personal rating')
	index2v2 = xplist.index('Highest 2v2 personal rating')
	xp3v3 = int(aStats['categories'][7]['sub_categories'][0]['statistics'][index3v3]['quantity'])
	xp2v2 = int(aStats['categories'][7]['sub_categories'][0]['statistics'][index2v2]['quantity'])


	r2v2 = requests.get(url2v2)
	r3v3 = requests.get(url3v3)
	r10v10 = requests.get(url10v10)
	rrender = requests.get(urlrender)
	charprofile = requests.get(urlprofile).json()
	wowclass = str(charprofile['character_class']['name'])
	spec = str(charprofile['active_spec']['name'])
	charName = charName.title()
	# avgilvl = '\n\n'+'Average Item Level: '+str(charprofile['average_item_level'])
	equilvl = str(charprofile['equipped_item_level'])

	checkguild = 'guild' in charprofile
	if checkguild is True:
		guild = '\n<'+str(charprofile['guild']['name'])+'>'
	else:
		guild = ''

	checktitle = 'active_title' in charprofile
	if checktitle is True:
		title = str(charprofile['active_title']['display_string'])
		title = title.replace('{name}', charName)
	else:
		title = charName

	pvp2v2 = r2v2.json()
	check2v2 = 'rating' in pvp2v2
	if check2v2 is True:
		rating2v2 = str(pvp2v2['rating'])
		played2v2 = str(pvp2v2['season_match_statistics']['played'])
		won2v2 = str(pvp2v2['season_match_statistics']['won'])
		lost2v2 = str(pvp2v2['season_match_statistics']['lost'])
	else:
		rating2v2 = 'pve nerd'
		played2v2 = '0'
		won2v2 = '0'
		lost2v2 = '0'
	
	pvp3v3 = r3v3.json()
	check3v3 = 'rating' in pvp3v3
	if check3v3 is True:
		rating3v3 = str(pvp3v3['rating'])
		played3v3 = str(pvp3v3['season_match_statistics']['played'])
		won3v3 = str(pvp3v3['season_match_statistics']['won'])
		lost3v3 = str(pvp3v3['season_match_statistics']['lost'])
	else:
		rating3v3 = 'pve nerd'
		played3v3 = '0'
		won3v3 = '0'
		lost3v3 = '0'
	
	pvp10v10 = r10v10.json()
	checkrbg = 'rating' in pvp10v10
	if checkrbg is True:
		ratingrbg = str(pvp10v10['rating'])
		playedrbg = str(pvp10v10['season_match_statistics']['played'])
		wonrbg = str(pvp10v10['season_match_statistics']['won'])
		lostrbg = str(pvp10v10['season_match_statistics']['lost'])
	else:
		ratingrbg = 'pve nerd'
		playedrbg = '0'
		wonrbg = '0'
		lostrbg = '0'

	charimg = rrender.json()
	covenant = '\n'+str(charprofile['covenant_progress']['chosen_covenant']['name'])
	renown = ' '+str(charprofile['covenant_progress']['renown_level'])

	r_embed = discord.Embed(
				colour= discord.Colour(0x190125),
				title=
				'Current - 2v2: '+rating2v2+'       3v3: '+rating3v3+'       RBG: '+ratingrbg+'\n'+
				'Highest - 2v2: '+str(xp2v2)+'       3v3: '+str(xp3v3)
		,
				description= '['+'Armory'+']'+'('+str(charArmory)+')'
				)
	r_embed.set_author(name=title+' - '+str(charServer).title()+'   |   '+equilvl+' '+spec+' '+wowclass+covenant+renown+guild)
	r_embed.set_image(url=charimg['assets'][2]['value'])
	# r_embed.set_footer(text='['+'Armory Link'+']'+'('+str(charArmory)+')')
	if int(played2v2) > 0:
		wr2v2 = int(won2v2)/int(played2v2)*100
		wr2v2 = str(round(wr2v2))+'%'
	else:
		wr2v2 = ''

	if int(played3v3) > 0:
		wr3v3 = int(won3v3)/int(played3v3)*100
		wr3v3 = str(round(wr3v3))+'%'
	else:
		wr3v3 = ''

	if int(playedrbg) > 0:
		wrrbg = int(wonrbg)/int(playedrbg)*100
		wrrbg = str(round(wrrbg))+'%'
	else:
		wrrbg = ''

	# 2v2
	r_embed.add_field(name='2v2 Played:',value=played2v2 +'  -  '+wr2v2, inline=True)
	r_embed.add_field(name='Won:',value=won2v2, inline=True)
	r_embed.add_field(name='Lost:',value=lost2v2, inline=True)
	# 3v3
	r_embed.add_field(name='3v3 Played:',value=played3v3 +'  -  '+wr3v3, inline=True)
	r_embed.add_field(name='Won:',value=won3v3, inline=True)
	r_embed.add_field(name='Lost:',value=lost3v3, inline=True)
	# RBG
	r_embed.add_field(name='RBG Played:',value=playedrbg +'  -  '+wrrbg, inline=True)
	r_embed.add_field(name='Won:',value=wonrbg, inline=True)
	r_embed.add_field(name='Lost:',value=lostrbg, inline=True)
	
	await ctx.send(embed=r_embed)


# @bot.command(pass_context=True, aliases=['',])
# async def pve(ctx, charName, charServer):

# 	def create_access_token(client_id, client_secret, region = 'us'):
# 	    data = { 'grant_type': 'client_credentials' }
# 	    response = requests.post('https://%s.battle.net/oauth/token' % region, data=data, auth=(client_id, client_secret))
# 	    return response.json()
	
# 	response = create_access_token(wowClientId, wowClientSecret)
# 	access_token = response['access_token']


@bot.command(pass_context=True, aliases=[])
async def zugzug(ctx):
	await ctx.send('https://tenor.com/view/zug-zug-wo-w-world-of-warcraft-orc-dance-gif-12706638')


if __name__ == '__main__':
	bot.run(ZUGZUG)