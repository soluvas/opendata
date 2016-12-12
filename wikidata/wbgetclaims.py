# https://www.wikidata.org/w/api.php?action=help&modules=wbgetclaims
# pip install requests requests-oauthlib
import requests
from requests_oauthlib import OAuth1
from config import *
import sys
import json

auth = OAuth1(api_key, api_secret, token, token_secret)
params = {'format': 'json', 'action': 'wbgetclaims', 'entity': sys.argv[1]}
r = requests.get(url='https://www.wikidata.org/w/api.php', 
    auth=auth, params=params)
print(r)
j = json.loads(r.text)
#print(j)

for key, value in j['claims'].iteritems():
    print(key, value[0]['mainsnak']['datavalue']['value'])
