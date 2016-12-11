# Update cities and towns/regencies in Indonesia
# Python 2.7
# pip install sparql-client
# pip install unicodecsv
from collections import OrderedDict
import io
import json
import unicodecsv as csv
import sparql

fn_csv = 'locality.id.csv'
fn_json = 'locality.id.json'

s = sparql.Service('https://query.wikidata.org/sparql', "utf-8", "GET")
q = '''SELECT ?locality ?localityLabel ?geonamesId ?place ?state ?stateIso ?country ?countryIso WHERE {
  {
    { ?locality wdt:P31 wd:Q3199141 }
    UNION
    { ?locality wdt:P31 wd:Q4272761 }
    ?locality wdt:P131 ?state .
    OPTIONAL { ?locality wdt:P1566 ?geonamesId . }
    VALUES ?place { "city" }
  }
  UNION {
    ?locality wdt:P31 wd:Q3191695 ;
          wdt:P1566 ?geonamesId ;
          wdt:P131 ?state .
    ?locality wdt:P131 ?state .
    OPTIONAL { ?locality wdt:P1566 ?geonamesId . }
    VALUES ?place { "town" }
  }
  ?state wdt:P300 ?stateIso ;
         wdt:P17 wd:Q252 .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "id", "en". }
  VALUES ?country { <http://www.wikidata.org/entity/Q252> }
  VALUES ?countryIso { "ID" }
}
'''
result = s.query(q)
jsons = [] 
csvs = []
print('Saving %s ...' % fn_csv)
with open(fn_csv, 'wb') as csvf:
  csvw = csv.writer(csvf, encoding='utf-8')
  csvw.writerow(['id', 'name', 'geonamesId', 'place', 'stateId', 'stateIso', 'countryId', 'countryIso',])
  for row in result.fetchall():
      id = str(row[0]).replace('http://www.wikidata.org/entity/', '')
      stateId = str(row[4]).replace('http://www.wikidata.org/entity/', '')
      countryId = str(row[6]).replace('http://www.wikidata.org/entity/', '')
      rowJson = OrderedDict([
        ('id', id),
        ('name', unicode(row[1])),
        ('geonamesId', long(str(row[2]))),
        ('place', unicode(row[3])),
        ('stateId', stateId),
        ('stateIso', unicode(row[5])),
        ('countryId', countryId),
        ('countryIso', unicode(row[7])),
      ])
      csvw.writerow(rowJson.values())
      jsons.append(rowJson)

print('Saving %s ...' % fn_json)
with io.open(fn_json, 'w', encoding='utf-8') as f:
  f.write(unicode(json.dumps(jsons, ensure_ascii=False)))
