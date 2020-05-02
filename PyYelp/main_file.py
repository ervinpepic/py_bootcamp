import requests

url = "https://api.yelp.com/v3/businesses/search"
apiKey = "8CwqCwTMexHL84WQmrCksReZqu-_FgAUQPFnAzxeHU2n5gW4qBR8tVtwZmu4qZwcjqrqNrMMmSJpr-NMbYJB8y2L76Y-0Yl2itPXtNI8js5dPvI-X3FJUJ3ZFXWtXnYx"
headers = {
    "Authorization": "Bearer " + apiKey
}
params = {
    "term": "Barber",
    "location": "NYC"
}
resp = requests.get(url, headers=headers, params=params)
businesses = resp.json()["businesses"]
names = [b["name"] for b in businesses if b["rating"] > 4.5]
print(names)
