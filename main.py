from turtle import pu
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = ChromeDriverManager()
pathToChrome = chrome.install()
service = Service(pathToChrome)


class Publication:
    def __init__(self, title='', price='') -> None:
        self.title = title
        self.price = price

    def __str__(self) -> str:
        return f'Publication[title: {self.title}, price: {self.price}]'


def getPrice(driver) -> str:
    attempts = 5
    state = 'incomplete'
    price = 'price not found'
    while state == 'incomplete' and attempts > 0:
        try:
            # div = html.find('div', {'class': 'MuiGrid-root css-rfnosa'})
            div = driver.find_element(
                By.XPATH, '//div[@class="MuiGrid-root css-rfnosa"]')
            span = div.find_element(By.XPATH, './/span[3]')
            text = span.text.split(sep=' ')
            price = text[4]
            state = 'complete'
        except:
            attempts -= 1

    return price


def getTitle(driver) -> str:
    attempts = 5
    state = 'incomplete'
    title = 'title not found'
    while state == 'incomplete' and attempts > 0:
        try:
            title = driver.find_element(By.XPATH, '//h1')
            title = title.text
            state = 'complete'
        except:
            attempts -= 1

    title = title.replace(',', '-')
    return title


def getPublication(url):
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    title = getTitle(driver)
    price = getPrice(driver)
    publication = Publication(title=title, price=price)
    driver.close()
    return publication


def getPublicationsForCompare(urls):
    publications = map(lambda url: getPublication(url), urls)
    with open('./publicaciones.csv', 'w') as file:
        file.write('description, price\n')
        for publication in publications:
            file.write(f'{publication.title}, {publication.price}\n')

    # publications = map(lambda p: str(p), publications)
    # print(list(publications))


urls = ['https://www.narvaezbid.com.ar/oferta/fiat-pick-up-cabina-doble-strada-adventure-16-ano-2018-dom-ac683wl-ubicacion-san-fernando-provincia-de-buenos-aires-2477505',
        'https://www.narvaezbid.com.ar/oferta/fiat-sedan-5-puertas-punto-hlx-18-ano-2009-dom-hsi807-ubicacion-san-fernando-provincia-de-buenos-aires-2477501']
getPublicationsForCompare(urls)
