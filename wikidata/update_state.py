# Python 2.7
# pip install sparql-client
# pip install unicodecsv
from collections import OrderedDict
import io
import json
import unicodecsv as csv
import sparql

fn_csv = 'state.id.csv'
fn_json = 'state.id.json'

s = sparql.Service('https://query.wikidata.org/sparql', "utf-8", "GET")
q = '''SELECT ?state ?stateLabel ?geonamesId ?stateIso ?capital ?capitalLabel ?country WHERE {
  ?state wdt:P1566 ?geonamesId.
  ?state wdt:P300 ?stateIso.
  ?state wdt:P36 ?capital.
  ?state wdt:P17 ?country.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "id", "en". }
}
ORDER BY ?country ?stateLabel
'''
result = s.query(q)
jsons = [] 
csvs = []
print('Saving %s ...' % fn_csv)
with open(fn_csv, 'wb') as csvf:
  csvw = csv.writer(csvf, encoding='utf-8')
  csvw.writerow(['id', 'name', 'geonamesId', 'stateIso', 'capitalId', 'capitalName', 'countryId'])
  for row in result.fetchall():
      id = str(row[0]).replace('http://www.wikidata.org/entity/', '')
      capitalId = str(row[4]).replace('http://www.wikidata.org/entity/', '')
      countryId = str(row[6]).replace('http://www.wikidata.org/entity/', '')
      rowJson = OrderedDict([
        ('id', id),
        ('name', unicode(row[1])),
        ('geonamesId', long(str(row[2]))),
        ('stateIso', unicode(row[3])),
        ('capitalId', capitalId),
        ('capitalName', unicode(row[5])),
        ('countryId', countryId),
      ])
      csvw.writerow(rowJson.values())
      jsons.append(rowJson)

print('Saving %s ...' % fn_json)
with io.open(fn_json, 'w', encoding='utf-8') as f:
  f.write(unicode(json.dumps(jsons, ensure_ascii=False)))
