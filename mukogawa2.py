import requests
from bs4 import BeautifulSoup, Comment

url = "http://ekikara.jp/newdata/ekijikoku/2702011/up1_28204051.htm"

response = requests.get(url)
print(response.status_code)
#print(response.content)

bs = BeautifulSoup(response.content, "lxml")
#bs = BeautifulSoup(response.content, 'html.parser')

for comments in bs.findAll(text=lambda text:isinstance(text, Comment)):
    print(comments.extract())
