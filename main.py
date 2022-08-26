from bs4 import BeautifulSoup as bs
from requests import get


def getPage(url):
    html = get(url)
    html = bs(html.text, 'html.parser')
    return html


def getTitle(url):
    try:
        html = getPage(url)
        title = html.find('h1').text
        return title
    except:
        return ''


def getTitles(url):
    try:
        html = getPage(url)
        links = html.findAll('a', {'class': 'link_article'})
        titles = map(lambda link: getTitle(url + link['href']), links)
        print(list(titles))
    except:
        print('I cant get page')


getTitles('https://www.clarin.com')
