import requests
from bs4 import BeautifulSoup
import json


def postScrapper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    #print(soup)
    #print(jsonify(soup.findAll('article')))
    data = soup.findAll('div', class_="yt-lockup-content")
    print(data)
    #x = str(data)
    #print(type(x))
    #d = json.dumps(x)
    #print(d, type(d))
    return 'data'

x = postScrapper("https://www.youtube.com/results?search_query=python")