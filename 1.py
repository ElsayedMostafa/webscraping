import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.data.gov/")
soup = BeautifulSoup(response.text,'html.parser')
print(soup.small.a.string)
