import requests
import json

# read api key
api_file = open("key.txt", 'r')
api_key = api_file.read()
api_file.close()

addres1 = "33 stern Jerusalem, Israel"
addres2 = "21 havaad haleumi Jerusalem Israel"
addres3 = "אריה אלטמן 4 ירושלים"

url_find_location = "https://maps.googleapis.com/maps/api/geocode/json?address=" + addres3 + \
                    "&key=" + str(api_key)

r = requests.get(url_find_location)

# print(json.dumps(r.json()["results"][0]["geometry"], indent=2))

lat = r.json()["results"][0]["geometry"]["location"]["lat"]
lon = r.json()["results"][0]["geometry"]["location"]["lng"]
category = "restaurant"
distance = 5000
url_find_place = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(lat) + "," + str(lon) + \
                 f"&radius={distance}&type={category}&keyword=cruise&key=" + str(api_key)

place_req = requests.get(url_find_place)

# for item in res:
#     print(item['resuls']['name'])

# for item in json.dumps(place_req.json(), indent=2):
#     for data_item in item['result']:
#         print(data_item['name'])
#
for item in place_req.json()['results']:
    print(item['name'])
    print(item['vicinity'])
    print(item['rating'])
    print("Open now?? " + str(item['opening_hours']['open_now']) + "\n")


# print(place_req.json()['results'][0]['name'])
# print(json.dumps(place_req.json(), indent=2))
