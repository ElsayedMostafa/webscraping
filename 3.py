import requests
url = requests.get("https://analytics.usa.gov/data/live/ie.json")
print(url.json()['totals']['ie_version']['6.0'])