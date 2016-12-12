## Phase 1

Hendy originally tried to collect countries, provinces/states, and cities (kotamadya) + towns (regencies=kabupaten) information from Wikidata,
while making sure there are appropriate links to GeoNames.

But then thought about using GeoNames directly.
Especially using the SQL import tool at https://github.com/codigofuerte/GeoNames-MySQL-DataImport

## Phase 2

But after trying to use GeoNames, which would be okay on a global level, my use case is for Indonesian level.
And I want cities and towns/regencies (distinguished) related to their provinces in Indonesia. GeoNames don't provide that. But Wikidata does.
So for countries information, GeoNames is good, and Wikidata is good too.

But for Indonesian data, provinces and cities and towns, with relationships, Wikidata seems to be better.
 
## wikidata.org Wikibase API

### wbgetclaims.py

Contoh eksekusi:

    [py27] C:\Users\ceefour\git\opendata\wikidata>python wbgetclaims.py Q11443

    <Response [200]>
    (u'P646', u'/m/025vkkq')
    (u'P131', {u'id': u'Q3586', u'entity-type': u'item', u'numeric-id': 3586})
    (u'P1376', {u'id': u'Q756895', u'entity-type': u'item', u'numeric-id': 756895})
    (u'P94', u'Lambang Kota Kediri.jpg')
    (u'P373', u'Kediri')
    (u'P1566', u'1640660')
    (u'P625', {u'latitude': -7.8166111111111, u'globe': u'http://www.wikidata.org/entity/Q2'
    , u'altitude': None, u'precision': 0.00027777777777778, u'longitude': 112.01191666667})
    (u'P2044', {u'amount': u'+3', u'lowerBound': u'+2', u'upperBound': u'+4', u'unit': u'htt
    p://www.wikidata.org/entity/Q11573'})
    (u'P1082', {u'amount': u'+252000', u'lowerBound': u'+252000', u'upperBound': u'+252000',
    u'unit': u'1'})
    (u'P856', u'http://www.kotakediri.go.id/')
    (u'P17', {u'id': u'Q252', u'entity-type': u'item', u'numeric-id': 252})
    (u'P18', u'Kediri East Java.jpg')
    (u'P31', {u'id': u'Q3199141', u'entity-type': u'item', u'numeric-id': 3199141})
    (u'P2588', u'35.71')
    (u'P982', u'30f770a8-43b1-4d8d-9de3-15aabb797287')

P1566 = GeoNames ID
P625 = Geo position / coordinates in WGS84
