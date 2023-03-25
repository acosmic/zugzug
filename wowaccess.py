import requests
from settings import wowClientId, wowClientSecret, wowLocale, wowRegion

def create_access_token(client_id, client_secret, region = 'us'):
	data = { 'grant_type': 'client_credentials' }
	response = requests.post('https://%s.battle.net/oauth/token' % region, data=data, auth=(client_id, client_secret))
	response_data = response.json()
	return response_data['access_token']




