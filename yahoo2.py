import requests
from bs4 import BeautifulSoup

url = "https://news.yahoo.co.jp/topics"

response = requests.get(url)
print(response.status_code)
#print(response.content)

#bs = BeautifulSoup(response.content, "lxml")
bs = BeautifulSoup(response.content, 'html.parser')

print(bs.select('a')[0])
print(bs.select('ul'))

topics = bs.select('.fl, .fr')
print(topics[0])

news_topics = {}
for news in topics:
    topic = news.select('li')[0].text
    news_topics[topic] = [news_topic.text for news_topic in news.select('li')[1:-2]]
print(news_topics['IT'])
