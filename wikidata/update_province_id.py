# Python 2.7
# pip install sparql-client
from collections import OrderedDict
import io
import json
import csv
import sparql

fn_csv = 'province-ID.csv'
fn_json = 'province-ID.json'

s = sparql.Service('https://query.wikidata.org/sparql', "utf-8", "GET")
q = '''SELECT ?province ?provinceLabel ?geonamesId ?provinceIso ?capital ?capitalLabel ?country ?countryIso ?countryIso3 WHERE {
  ?province wdt:P31 wd:Q5098 ;
        wdt:P1566 ?geonamesId ;
        wdt:P300 ?provinceIso ;
        wdt:P36 ?capital ;
        wdt:P17 ?country .
  ?country wdt:P297 ?countryIso ;
    wdt:P298 ?countryIso3 .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "id". }
}
ORDER BY ?provinceLabel
'''
result = s.query(q)
jsons = [] 
csvs = []
print('Saving %s ...' % fn_csv)
with open(fn_csv, 'wb') as csvf:
  csvw = csv.writer(csvf)
  csvw.writerow(['id', 'name_id', 'geonamesId', 'provinceIso', 'capitalId', 'capitalName_id', 'countryId', 'countryIso', 'countryIso3'])
  for row in result.fetchall():
      #print(row[0]) 
      #print(row[1])
      #print(row[2])
      wikidataId = str(row[0]).replace('http://www.wikidata.org/entity/', '')
      capitalId = str(row[4]).replace('http://www.wikidata.org/entity/', '')
      countryId = str(row[6]).replace('http://www.wikidata.org/entity/', '')
      provinceJson = OrderedDict([
        ('id', wikidataId),
        ('name_id', str(row[1])),
        ('geonamesId', long(str(row[2]))),
        ('provinceIso', str(row[3])),
        ('capitalId', capitalId),
        ('capitalName_id', str(row[5])),
        ('countryId', countryId),
        ('countryIso', str(row[7])),
        ('countryIso3', str(row[8])),
      ])
      csvw.writerow(provinceJson.values())
      jsons.append(provinceJson)

print('Saving %s ...' % fn_json)
with io.open(fn_json, 'w', encoding='utf-8') as f:
  f.write(unicode(json.dumps(jsons, ensure_ascii=False)))
