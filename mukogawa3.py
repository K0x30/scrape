import requests
from bs4 import BeautifulSoup

url = "http://ekikara.jp/newdata/ekijikoku/2702011/up1_28204051.htm"

response = requests.get(url)
print(response.status_code)
#print(response.content)

bs = BeautifulSoup(response.content, "lxml")
#bs = BeautifulSoup(response.content, 'html.parser')

topics = bs.findAll('td', class_='lowBg06')
for topic in topics:
    print(topic.text)

topics = bs.findAll('td', class_='lowBgFFF')
for topic in topics:
    print(topic.text)
topics = bs.findAll('td', class_='lowBg12')
for topic in topics:
    print(topic.text)
