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
 
## Phase 3

Dari Wikidata SPARQL, GeoNames API, dibuatlah script [`geonames_match.py`](geonames_match.py) untuk mencocokkan kota dan kabupaten dari Wikidata
dan menambahkan informasi dari GeoNames: GeoNames ID dan lokasi, menghasilkan file [`geonames_match-ID.csv`](geonames_match-ID.csv).

[`wbcreateclaim.py`](wbcreateclaim.py) merupakan script umum untuk menambahkan claim baru.

Dengan mengolah file [`geonames_match-ID.csv`](geonames_match-ID.csv) di LibreOffice Calc untuk meng-generate command line,
maka dihasilkan mass edit scripts:

* [oneoff/fix_geonames_2016-12-12.cmd](oneoff/fix_geonames_2016-12-12.cmd)
* [oneoff/fix_point_2016-12-12.cmd](oneoff/fix_point_2016-12-12.cmd) 

Per 12 Desember 2016 awal hari sebelum mass edit script ini dijalankan, dari 514 kota dan kabupaten, yang memiliki GeoNames ID
berjumlah 209 entity, dan yang memiliki koordinat GPS berjumlah 370 entity.

Setelah script ini dijalankan, diharapkan seluruh 514 entities tersebut memiliki GeoNames ID maupun koordinat GPS. 

Judul draft paper: Automatic submissions for Wikidata information of all cities and regencies in Indonesia with GeoNames IDs and GPS coordinates 

## wikidata.org Wikibase API

### action=wbgetclaims

Kota Kediri - GeoNames ID:

    "P1566": [
      {
        "mainsnak": {
          "snaktype": "value",
          "property": "P1566",
          "datavalue": {
            "value": "1640660",
            "type": "string"
          },
          "datatype": "external-id"
        },
        "type": "statement",
        "id": "Q11443$29E336E7-150A-4B2D-BB36-0893343CE9FD",
        "rank": "normal",
        "references": [
          {
            "hash": "d6193e4d78598db1a6aaa453fface1553022f1f2",
            "snaks": {
              "P143": [
                {
                  "snaktype": "value",
                  "property": "P143",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 830106,
                      "id": "Q830106"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "snaks-order": [
              "P143"
            ]
          }
        ]
      }
    ],

Coordinates:

    "P625": [
      {
        "mainsnak": {
          "snaktype": "value",
          "property": "P625",
          "datavalue": {
            "value": {
              "latitude": -7.8166111111111,
              "longitude": 112.01191666667,
              "altitude": null,
              "precision": 0.00027777777777778,
              "globe": "http://www.wikidata.org/entity/Q2"
            },
            "type": "globecoordinate"
          },
          "datatype": "globe-coordinate"
        },
        "type": "statement",
        "id": "q11443$C265D679-5FF2-454A-A789-8282753B308B",
        "rank": "normal",
        "references": [
          {
            "hash": "7eb64cf9621d34c54fd4bd040ed4b61a88c4a1a0",
            "snaks": {
              "P143": [
                {
                  "snaktype": "value",
                  "property": "P143",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 328,
                      "id": "Q328"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "snaks-order": [
              "P143"
            ]
          }
        ]
      }
    ],


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

### wbcreateclaim.py

Contoh eksekusi:

    [py27] C:\Users\ceefour\git\opendata\wikidata>python wbcreateclaim.py Q5672 P1566 \"6713333\"

    Checking existing claim for Q5672 P1566 ...
    <Response [200]>
    Adding Q5672 P1566 "6713333", getting csrftoken...
    csrftoken: 01057b6cedd9bdd8695a643e2eee584f584eace6+\
    <Response [200]>
    {"pageinfo":{"lastrevid":415880644},"success":1,"claim":{"mainsnak":{"snaktype":"value","property":"P1566","datavalue":{"value":"6713333","type":"string"},"datatype":"external-id"},"type":"statement","i
    d":"Q5672$CB69C74A-6D80-41C6-BCBC-3A93C978B9AA","rank":"normal"}}
