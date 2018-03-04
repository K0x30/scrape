import requests
from bs4 import BeautifulSoup

url = "http://ekikara.jp/newdata/ekijikoku/2702011/up1_28204051.htm"

response = requests.get(url)
print(response.status_code)
#print(response.content)

#bs = BeautifulSoup(response.content, "lxml")
bs = BeautifulSoup(response.content, 'html.parser')

topics = bs.select('.l')
for topic in topics:
    print(topic.text)

topics = bs.select('.s')
for topic in topics:
    print(topic.text)

topics = bs.select('.ll')
for topic in topics:
    print(topic.text)

topics = bs.select('table')
for topic in topics:
    print(topic.text)
