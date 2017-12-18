from bs4 import BeautifulSoup
import requests
response = requests.get('http://catalog.data.gov/dataset?q=&sort=metadata_created+desc')
soup = BeautifulSoup(response.text,'html.parser')
print(soup.find_all('h3',{"class":"dataset-heading"})[0].a.string)