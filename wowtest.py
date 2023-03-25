#! /usr/bin/python3
from settings import *
import requests
from datetime import datetime
from wowaccess import create_access_token


ACCESS_TOKEN = create_access_token(wowClientId, WOW_CLIENT_SECRET)

# acosmicCharId = 201745243
# slycatxCharId = 202594517

charName = 'acosmic'
charServer = 'illidan'
wowApiChar = 'https://us.api.blizzard.com/profile/wow/character/'






achievement_stats = str(wowApiChar)+str(charServer).lower()+'/'+str(charName).lower()+'/achievements/statistics?namespace=profile-us&locale=en_US&access_token='+str(ACCESS_TOKEN)
url2v2 = str(wowApiChar)+str(charServer).lower()+'/'+str(charName).lower()+'/pvp-bracket/2v2?namespace=profile-us&locale=en_US&access_token='+str(ACCESS_TOKEN)
url3v3 = str(wowApiChar)+str(charServer).lower()+'/'+str(charName).lower()+'/pvp-bracket/3v3?namespace=profile-us&locale=en_US&access_token='+str(ACCESS_TOKEN)
url10v10 = str(wowApiChar)+str(charServer).lower()+'/'+str(charName).lower()+'/pvp-bracket/rbg?namespace=profile-us&locale=en_US&access_token='+str(ACCESS_TOKEN)
urlrender = str(wowApiChar)+str(charServer).lower()+'/'+str(charName).lower()+'/character-media?namespace=profile-us&locale=en_US&access_token='+str(ACCESS_TOKEN)
urlstats = str(wowApiChar)+str(charServer).lower()+'/'+str(charName).lower()+'/statistics?namespace=profile-us&locale=en_US&access_token='+str(ACCESS_TOKEN)
urlprofile = str(wowApiChar)+str(charServer).lower()+'/'+str(charName).lower()+'?namespace=profile-us&locale=en_US&access_token='+str(ACCESS_TOKEN)


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

rachStats = requests.get(achievement_stats)
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

categories = aStats['categories']
categoryNames = [d['name'] for d in categories if 'name' in d]
indexpvp = categoryNames.index('Player vs. Player')

subcategories = categories[indexpvp]['sub_categories']
subcategoryNames = [d['name'] for d in subcategories if 'name' in d]




if 'Rated Arenas' in subcategoryNames:
    indexrated = subcategoryNames.index('Rated Arenas')
    ratedarena = subcategories[indexrated]['statistics']
    ratedarenaNames = [d['name'] for d in ratedarena if 'name' in d]
    index3v3 = ratedarenaNames.index('Highest 3v3 personal rating')
    index2v2 = ratedarenaNames.index('Highest 2v2 personal rating')
    xp3v3 = int(ratedarena[index3v3]['quantity'])
    xp2v2 = int(ratedarena[index2v2]['quantity'])
else:
    xp3v3 = 0
    xp2v2 = 0






if __name__ == '__main__':


    print(xp3v3)

    print(xp2v2)





    # print(aStats)



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