import requests
import json

# read api key
api_file = open("key.txt", 'r')
api_key = api_file.read()
api_file.close()

addres1 = "33 stern Jerusalem, Israel"
addres2 = "21 havaad haleumi Jerusalem Israel"



url_find_location = "https://maps.googleapis.com/maps/api/geocode/json?address=" + addres2 + \
"&key=" + str(api_key)

r = requests.get(url_find_location)

#print(json.dumps(r.json()["results"][0]["geometry"], indent=2))

lat = r.json()["results"][0]["geometry"]["location"]["lat"]
lon = r.json()["results"][0]["geometry"]["location"]["lng"]

url_find_place = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(lat) + "," + str(lon) + \
                 "&radius=1500&type=restaurant&keyword=cruise&key=" + str(api_key)
place_req = requests.get(url_find_place)
print(json.dumps(place_req.json(), indent=2))
