import simplejson as json
import pandas as pd

landmarks = []
with open('landmarks.json', encoding = 'utf-8') as f:
	for line in f:
		landmarks.append(json.loads(line))

no_of_landmarks = len(landmarks)
landmarks_df = pd.DataFrame(columns = ['name', 'address', 'latitude', 'longitude', 'type', 'all_types'])
for i in range(no_of_landmarks):
	name = landmarks[i].get('name') # Will return None if the key is not in dict
	addr = landmarks[i].get('formatted_address')
	geocode = landmarks[i].get('geometry').get('location')
	lat = geocode.get('lat') if geocode is not None else None
	lng = geocode.get('lng') if geocode is not None else None
	landmark_types = landmarks[i].get('types')
	type0 = landmark_types[0]
	all_types = ','.join(landmark_types)
	landmarks_df.loc[i] = [name, addr, lat, lng, type0, all_types]

landmarks_df.to_excel('hcmc_landmarks.xlsx', index = False)