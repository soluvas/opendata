# GeoNames match from localities with GeoNames ID
# Python 3 recommended
# pip install unicodecsv requests
from collections import OrderedDict
import io
import re
import json
import unicodecsv as csv
import requests

fn_csv = 'locality-ID.csv'
fn_out = 'geonames_match-ID.csv'
print('Reading %s writing to %s ...' % (fn_csv, fn_out))
with open(fn_out, 'wb') as outf:
    with open(fn_csv, 'rb') as csvf:
        csvw = csv.DictWriter(outf, encoding='utf-8', fieldnames=['id', 'name', 'geonamesId', 'geonamesName', 'lat', 'lon'])
        csvw.writeheader()
        csvr = csv.DictReader(csvf, encoding='utf-8')
        for row in csvr:
            if not row['geonamesId']:
                gnName = ('Kabupaten ' if row['place'] == 'TOWN' else 'Kota ') + row['name']
                print(row['id'], gnName, row['place'], row['geonamesId'])
                
                params = {'username': 'ceefour', 'country': 'ID', 'name': gnName}
                r = requests.get('http://api.geonames.org/searchJSON', params=params)
                # print(r)
                # print(r.text)
                results = json.loads(r.text)
                if results['totalResultsCount'] >= 1:
                    row = {'id': row['id'], 'name': row['name'],
                        'geonamesId': results['geonames'][0]['geonameId'],
                        'geonamesName': results['geonames'][0]['name'],
                        'lat': results['geonames'][0]['lat'],
                        'lon': results['geonames'][0]['lng']}
                    csvw.writerow(row)
                else:
                    # not found
                    None
