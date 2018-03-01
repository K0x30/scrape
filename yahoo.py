from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint

url = 'http://news.yahoo.co.jp/'
with urlopen(url) as res:
    html = res.read().decode("utf-8")

soup = BeautifulSoup(html, 'html.parser')

titles = soup.select('.ttl a')
titles = [t.contents[0] for t in titles]
pprint(titles)


