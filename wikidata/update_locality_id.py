# Update cities and towns/regencies in Indonesia
# Python 2.7
# pip install sparql-client
# pip install unicodecsv
from collections import OrderedDict
import io
import re
import json
import unicodecsv as csv
import sparql

fn_csv = 'locality.id.csv'
fn_json = 'locality.id.json'

s = sparql.Service('https://query.wikidata.org/sparql', "utf-8", "GET")
q = '''SELECT ?locality ?localityLabel ?geonamesId ?place ?point ?kemendagriCode ?state ?stateLabel ?stateIso ?country ?countryIso WHERE {
  {
    { ?locality wdt:P31 wd:Q3199141 }
    UNION
    { ?locality wdt:P31 wd:Q4272761 }
    ?locality wdt:P131 ?state .
    VALUES ?place { "CITY" }
  }
  UNION {
    ?locality wdt:P31 wd:Q3191695 ;
              wdt:P131 ?state .
    VALUES ?place { "TOWN" }
  }
  OPTIONAL {
    ?locality wdt:P1566 ?geonamesId ;
              wdt:P625 ?point ;
              wdt:P2588 ?kemendagriCode .
  }
  ?state wdt:P300 ?stateIso ;
         wdt:P17 wd:Q252 .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "id", "en". }
  VALUES ?country { <http://www.wikidata.org/entity/Q252> }
  VALUES ?countryIso { "ID" }
}
ORDER BY ?localityLabel
'''
result = s.query(q)
jsons = [] 
csvs = []
print('Saving %s ...' % fn_csv)
POINT_PATTERN = re.compile('Point[(](.+) (.+)[)]')
with open(fn_csv, 'wb') as csvf:
  csvw = csv.writer(csvf, encoding='utf-8')
  csvw.writerow(['id', 'name', 'geonamesId', 'place', 'pointLat', 'pointLon', 'kemendagriCode',
    'stateId', 'stateName', 'stateIso', 'countryId', 'countryIso',])
  for row in result.fetchall():
      id = unicode(row[0]).replace('http://www.wikidata.org/entity/', '')
      stateId = unicode(row[6]).replace('http://www.wikidata.org/entity/', '')
      countryId = unicode(row[9]).replace('http://www.wikidata.org/entity/', '')
      m_point = POINT_PATTERN.match(str(row[4]))
      if m_point:
        pointLat = float(m_point.group(2))
        pointLon = float(m_point.group(1))
      else:
        pointLat = None
        pointLon = None
      # print(row[4])
      # print(m_point)
      # print(float(m_point.group(1)))
      # print(float(m_point.group(2)))
      # exit()
      rowJson = OrderedDict([
        ('id', id),
        ('name', unicode(row[1])),
        ('geonamesId', long(str(row[2])) if row[2] else ''),
        ('place', unicode(row[3])),
        ('pointLat', pointLat),
        ('pointLon', pointLon),
        ('kemendagriCode', unicode(row[5]) if row[5] else ''),
        ('stateId', stateId),
        ('stateName', unicode(row[7])),
        ('stateIso', unicode(row[8])),
        ('countryId', countryId),
        ('countryIso', unicode(row[10])),
      ])
      csvw.writerow(rowJson.values())
      jsons.append(rowJson)

print('Saving %s ...' % fn_json)
with io.open(fn_json, 'w', encoding='utf-8') as f:
  f.write(unicode(json.dumps(jsons, ensure_ascii=False)))
