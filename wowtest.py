from settings import *

from datetime import datetime


# acosmicCharId = 201745243
# slycatxCharId = 202594517

charName = 'boysnight'
charServer = 'illidan'
wowApiChar = 'https://us.api.blizzard.com/profile/wow/character/'

def create_access_token(client_id, client_secret, region = 'us'):
    data = { 'grant_type': 'client_credentials' }
    response = requests.post('https://%s.battle.net/oauth/token' % region, data=data, auth=(client_id, client_secret))
    return response.json()

response = create_access_token(wowClientId, wowClientSecret)
access_token = response['access_token']

achStats = str(wowApiChar)+str(charServer).lower()+'/'+str(charName).lower()+'/achievements/statistics?namespace=profile-us&locale=en_US&access_token='+str(access_token)
url2v2 = str(wowApiChar)+str(charServer).lower()+'/'+str(charName).lower()+'/pvp-bracket/2v2?namespace=profile-us&locale=en_US&access_token='+str(access_token)
url3v3 = str(wowApiChar)+str(charServer).lower()+'/'+str(charName).lower()+'/pvp-bracket/3v3?namespace=profile-us&locale=en_US&access_token='+str(access_token)
url10v10 = str(wowApiChar)+str(charServer).lower()+'/'+str(charName).lower()+'/pvp-bracket/rbg?namespace=profile-us&locale=en_US&access_token='+str(access_token)
urlrender = str(wowApiChar)+str(charServer).lower()+'/'+str(charName).lower()+'/character-media?namespace=profile-us&locale=en_US&access_token='+str(access_token)
urlstats = str(wowApiChar)+str(charServer).lower()+'/'+str(charName).lower()+'/statistics?namespace=profile-us&locale=en_US&access_token='+str(access_token)
urlprofile = str(wowApiChar)+str(charServer).lower()+'/'+str(charName).lower()+'?namespace=profile-us&locale=en_US&access_token='+str(access_token)


#mythic+ str(wowApiChar)+str(charServer).lower()+'/'+str(charName).lower()+'/mythic-keystone-profile?namespace=profile-us&locale=en_US&access_token='+str(access_token)
#titles str(wowApiChar)+str(charServer).lower()+'/'+str(charName).lower()+'/titles?namespace=profile-us&locale=en_US&access_token='+str(access_token)
#pvprewards 'https://us.api.blizzard.com/data/wow/pvp-season/27/pvp-reward/index?namespace=dynamic-us&locale=en_US&access_token='+str(access_token)
#pvpleaderboards 'https://us.api.blizzard.com/data/wow/pvp-season/29/pvp-leaderboard/3v3?namespace=dynamic-us&locale=en_US&access_token='+str(access_token)



charprofile = requests.get(urlprofile).json()

wowclass = str(charprofile['character_class']['name'])
spec = str(charprofile['active_spec']['name'])
# guild = '<'+str(charprofile['guild']['name'])+'>'
# title = charprofile['active_title']['display_string']
# title = title.replace('{name}',charName)

rachStats = requests.get(achStats)
r2v2 = requests.get(url2v2)
r3v3 = requests.get(url3v3)
r10v10 = requests.get(url10v10)
rrender = requests.get(urlrender)
rstats = requests.get(urlstats)

aStats = rachStats.json()
pvp2v2 = r2v2.json()
pvp3v3 = r3v3.json()
pvp10v10 = r10v10.json()
rating_in_dict = 'rating' in pvp10v10
charimg = rrender.json()
charStats = rstats.json()

xplist = aStats['categories'][7]['sub_categories'][0]['statistics']
xplist = [d['name'] for d in xplist if 'name' in d]
index3v3 = xplist.index('Highest 3v3 personal rating')
index2v2 = xplist.index('Highest 2v2 personal rating')
xp3v3 = int(aStats['categories'][7]['sub_categories'][0]['statistics'][index3v3]['quantity'])
xp2v2 = int(aStats['categories'][7]['sub_categories'][0]['statistics'][index2v2]['quantity'])


print(index3v3)

print(xp3v3)
print(index2v2)

print(xp2v2)
# print(charprofile['active_title']['display_string'])


# print(rating_in_dict)
# # print(charStats)
# print()
# print()
# print('strength: ' +str(charStats['strength']['effective']))
# print('agility: ' +str(charStats['agility']['effective']))
# print('intellect: ' +str(charStats['intellect']['effective']))
# print('stamina: ' +str(charStats['stamina']['effective']))
# print('crit: ' +str(charStats['melee_crit']['value']))
# print('haste: ' +str(charStats['melee_haste']['value']))
# print('mastery: ' +str(charStats['mastery']['value']))
# print('versatility: ' +str(charStats['versatility']))
# print('spell crit: ' +str(charStats['spell_crit']['value']))
# print('corruption: ' +str(charStats['corruption']['corruption']))
# print('corruption corruption_resistance: ' +str(charStats['corruption']['corruption_resistance']))
# print('effective_corruption: ' +str(charStats['corruption']['effective_corruption']))