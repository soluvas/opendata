# Python 2.7
# pip install requests
import requests

q = '''SELECT ?province ?provinceLabel ?geonamesId WHERE {
  ?province wdt:P31 wd:Q5098;
        wdt:P1566 ?geonamesId .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "id". }
}
ORDER BY ?provinceLabel
'''
params = {'query': q}
#headers = {'Accept': 'application/sparql-results+json'}
#headers = {'Accept': 'text/csv'}
#headers = {'Accept': 'text/tab-separated-values'}
#headers = {'Accept': 'application/sparql-results+xml'}
r = requests.get('https://query.wikidata.org/sparql', params=params, headers=headers)
print(r) 
print(r.text)
# s = sparql.Service(, "utf-8", "GET")
# result = s.query(q)
# for row in result.fetchall():
#     print(row)
