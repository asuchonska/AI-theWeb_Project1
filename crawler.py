import requests
from bs4 import BeautifulSoup

r = requests.get('https://erasmus-plus.ec.europa.eu')
print(r.status_code)
print(r.headers)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.title.text)
for l in soup.find_all("a"):
    print (l['href'])
    print (l.text)
