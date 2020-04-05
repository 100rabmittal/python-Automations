import requests
from bs4 import BeautifulSoup
from api_blogger import blog
import re
import json

mediumScrapperData = {
    'url': "https://medium.com/search?q=python",
    'classes': ['postArticle-content']
}

def scapper():
    response = requests.get(mediumScrapperData['url'])
    soup = BeautifulSoup(response.text, 'lxml')
    headings = soup.find_all('div', mediumScrapperData['classes'])
    return headings[0]

def postScrapper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    #print(jsonify(soup.findAll('article')))
    data = soup.findAll('div', class_='z ab ac ae af fm ah ai')
    #data = soup.findAll('article')[0]
    return json.dumps(str(data))

data = scapper()
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(data))
x = postScrapper("https://medium.com/free-code-camp/learning-python-from-zero-to-hero-120ea540b567?source=search_post---------0")
#count = 00
#for url in set(urls):
#    x = postScrapper(url)
service = blog.svc()
print(blog.getUsers(service))
print(blog.getPosts(service, x, "15"))
#count+=1