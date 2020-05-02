import requests
import config
url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "Authorization": "Bearer " + config.apiKey
}
params = {
    "term": "Barber",
    "location": "NYC"
}
resp = requests.get(url, headers=headers, params=params)
businesses = resp.json()["businesses"]
names = [b["name"] for b in businesses if b["rating"] > 4.5]
print(names)
