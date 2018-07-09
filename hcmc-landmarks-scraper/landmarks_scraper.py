# pip install python-google-places
from googleplaces import GooglePlaces, types, lang
import pandas as pd
import simplejson as json
import time

API_KEY = 'AIzaSyAH3bqqPUCi4rrkZ0ShyoX6RFg7wj7j0Qg'
google_places = GooglePlaces(API_KEY)

hcmc_mod8_sites = pd.read_excel('hcmc-mod8-sites.xlsx', index = False)
landmarks = []
start_time = time.time()

for index, site in hcmc_mod8_sites.iterrows():
    geocode = {}
    geocode['lat'] = site.Latitude
    geocode['lng'] = site.Longitude

    try:
        query_result = google_places.nearby_search(
            lat_lng = geocode,
            radius = 5000
            # types = [types.TYPE_SCHOOL] or [types.TYPE_BUS_STATION]
        )

        if query_result.has_attributions:
            print(query_result.html_attributions)

        for place in query_result.places:
            place.get_details()
            landmarks.append(place.details)
            print(place.details)

    except Exception as ex:
        with open('log.txt', 'a') as logfile:
            i = 0
            logfile.write(str(i) + "Error: " + str(ex) + '\n')
            i += 1
        pass

print("Elapsed time: %s seconds" % (time.time() - start_time))

output_file = open('landmarks.json', 'w', encoding='utf-8')
for landmark in landmarks:
    json.dump(landmark, output_file) 
    output_file.write("\n")
