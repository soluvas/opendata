# Python 2.7
# pip install sparql-client
# pip install unicodecsv
from collections import OrderedDict
import io
import json
import unicodecsv as csv
import sparql

fn_csv = 'country.csv'
fn_json = 'country.json'

s = sparql.Service('https://query.wikidata.org/sparql', "utf-8", "GET")
#  wdt:P36 ?capital .
# cannot include the capital because some countries like Sri Lanka have multiple capitals over time
q = '''SELECT ?country ?countryLabel ?geonamesId ?iso ?iso3 WHERE {
  ?country wdt:P31 wd:Q6256 ;
    wdt:P1566 ?geonamesId ;
    wdt:P297 ?iso ;
    wdt:P298 ?iso3 .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en", "id". }
}
ORDER BY ?countryLabel
'''
result = s.query(q)
jsons = [] 
csvs = []
print('Saving %s ...' % fn_csv)
with open(fn_csv, 'wb') as csvf:
  csvw = csv.writer(csvf, encoding='utf-8')
  csvw.writerow(['id', 'name', 'geonamesId', 'iso', 'iso3'])
  for row in result.fetchall():
      #print(row[0]) 
      #print(row[1])
      #print(row[2])
      countryId = str(row[0]).replace('http://www.wikidata.org/entity/', '')
      #capitalId = str(row[5]).replace('http://www.wikidata.org/entity/', '')
      rowJson = OrderedDict([
        ('id', countryId),
        ('name', unicode(row[1])),
        ('geonamesId', long(str(row[2]))),
        ('iso', unicode(row[3])),
        ('iso3', unicode(row[4])),
        #('capitalId', capitalId),
        #('capitalName', unicode(row[6])),
      ])
      csvw.writerow(rowJson.values())
      jsons.append(rowJson)

print('Saving %s ...' % fn_json)
with io.open(fn_json, 'w', encoding='utf-8') as f:
  f.write(unicode(json.dumps(jsons, ensure_ascii=False)))
