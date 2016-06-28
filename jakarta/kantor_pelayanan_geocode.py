# Configuration:
# Set environment variable GOOGLE_API_KEY to our Google API Key

import googlemaps, os, pprint, csv
from datetime import datetime

gmaps = googlemaps.Client(key=os.environ['GOOGLE_API_KEY'])

with open('18.-DKI-Kantor-Pelayanan-Kependudukan-dan-Pencatatan-Sipil--2015.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        # print(row[6])
        if row[6]:
            # address = 'Jl. Saad 18, Bandung'
            address = row[6] + ', Jakarta'
            geocode_result = gmaps.geocode(address)
            # print("%s ->" % address)
            # pprint.pprint(geocode_result)
            print("%s\t%s" % (geocode_result[0]['geometry']['location']['lat'], geocode_result[0]['geometry']['location']['lng']))
        else:
            print("")

exit

# Jl. Saad 18, Bandung ->
# [{'address_components': [{'long_name': '18',
#                           'short_name': '18',
#                           'types': ['street_number']},
#                          {'long_name': 'Jalan Saad',
#                           'short_name': 'Jl. Saad',
#                           'types': ['route']},
#                          {'long_name': 'Kebon Pisang',
#                           'short_name': 'Kb. Pisang',
#                           'types': ['administrative_area_level_4',
#                                     'political']},
#                          {'long_name': 'Sumur Bandung',
#                           'short_name': 'Sumur Bandung',
#                           'types': ['administrative_area_level_3',
#                                     'political']},
#                          {'long_name': 'Kota Bandung',
#                           'short_name': 'Kota Bandung',
#                           'types': ['administrative_area_level_2',
#                                     'political']},
#                          {'long_name': 'Jawa Barat',
#                           'short_name': 'Jawa Barat',
#                           'types': ['administrative_area_level_1',
#                                     'political']},
#                          {'long_name': 'Indonesia',
#                           'short_name': 'ID',
#                           'types': ['country', 'political']},
#                          {'long_name': '40112',
#                           'short_name': '40112',
#                           'types': ['postal_code']}],
#   'formatted_address': 'Jl. Saad No.18, Kb. Pisang, Sumur Bandung, Kota '
#                        'Bandung, Jawa Barat, Indonesia',
#   'geometry': {'bounds': {'northeast': {'lat': -6.9193731, 'lng': 107.6141655},
#                           'southwest': {'lat': -6.919377700000001,
#                                         'lng': 107.6141473}},
#                'location': {'lat': -6.9193731, 'lng': 107.6141473},
#                'location_type': 'RANGE_INTERPOLATED',
#                'viewport': {'northeast': {'lat': -6.918026419708498,
#                                           'lng': 107.6155053802915},
#                             'southwest': {'lat': -6.920724380291503,
#                                           'lng': 107.6128074197085}}},
#   'partial_match': True,
#   'place_id': 'Ek5KbC4gU2FhZCBOby4xOCwgS2IuIFBpc2FuZywgU3VtdXIgQmFuZHVuZywgS290YSBCYW5kdW5nLCBKYXdhIEJhcmF0LCBJbmRvbmVzaWE',
#   'types': ['street_address']}]
# -6.9193731      107.6141473
