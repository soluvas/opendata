# pip install requests requests-oauthlib
import requests
from requests_oauthlib import OAuth1
from config import *

auth = OAuth1(api_key, api_secret, token, token_secret)
params = {'format': 'json', 'action': 'query', 'meta': 'tokens'}
r = requests.get(url='https://www.wikidata.org/w/api.php', auth=auth, params=params)
print(r)
print(r.text)
