# https://www.wikidata.org/w/api.php?action=help&modules=wbgetclaims
# pip install requests requests-oauthlib
import requests
from requests_oauthlib import OAuth1
from config import *
import sys
import json

entityId = sys.argv[1]
propId = sys.argv[2]
value = sys.argv[3]

auth = OAuth1(api_key, api_secret, token, token_secret)

print('Checking existing claim for %s %s ...' % (entityId, propId))
params = {'format': 'json', 'action': 'wbgetclaims', 'entity': entityId}
r = requests.get(url='https://www.wikidata.org/w/api.php', 
    auth=auth, params=params)
print(r)
j = json.loads(r.text)
#print(j)

if propId in j['claims']:
    print('Claim already exists, avoiding unintentional duplicates: %s %s %s' % 
        (entityId, propId, j['claims'][propId][0]['mainsnak']['datavalue']['value']))
else:
    print('Adding %s %s %s, getting csrftoken...' % (entityId, propId, value))

    params = {'format': 'json', 'action': 'query', 'meta': 'tokens'}
    r = requests.get(url='https://www.wikidata.org/w/api.php', auth=auth, params=params)
    csrftoken = json.loads(r.text)['query']['tokens']['csrftoken']
    print('csrftoken: %s' % csrftoken)

    params = {'format': 'json', 'action': 'wbcreateclaim', 'token': csrftoken,
        'entity': entityId, 'snaktype': 'value', 'property': propId, 'value': value}
    r = requests.post(url='https://www.wikidata.org/w/api.php', auth=auth, data=params)
    print(r)
    print(r.text)
