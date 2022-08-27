from bs4 import BeautifulSoup as bs
from requests import get


class Publication:
    def __init__(self, title='', price="") -> None:
        self.title = title
        self.price = price

    def __str__(self) -> str:
        return f'title: {self.title}, price: {self.price}'


def getPage(url):
    html = get(url)
    html = bs(html.text, 'html.parser')
    return html


def getPrice(html):
    try:
        div = html.find('div', {'class': 'MuiGrid-root css-rfnosa'})
        spans = div.find('span')
        spanWithPrice = spans[2]
        price = spanWithPrice.text
        return price
    except:
        return 'Error searching price'


def getTitle(html):
    try:
        title = html.find('h1')
        print(title)
        title = title.text
        return title
    except:
        return 'Error searching title'


def getPublication(url):
    html = getPage(url)
    print(html)
    title = getTitle(html=html)
    price = getPrice(html=html)
    publication = Publication(title=title, price=price)
    return publication


def getPublicationsForCompare(urls):
    publications = map(lambda url: getPublication(url), urls)
    publications = map(lambda p: str(p), publications)
    print(list(publications))


urls = ['https://www.narvaezbid.com.ar/oferta/fiat-pick-up-cabina-doble-strada-adventure-16-ano-2018-dom-ac683wl-ubicacion-san-fernando-provincia-de-buenos-aires-2477505']
getPublicationsForCompare(urls)
