from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from pandas import DataFrame

urls = ['https://www.narvaezbid.com.ar/oferta/fiat-pick-up-cabina-doble-strada-adventure-16-ano-2018-dom-ac683wl-ubicacion-san-fernando-provincia-de-buenos-aires-2477505',
        'https://www.narvaezbid.com.ar/oferta/fiat-sedan-5-puertas-punto-hlx-18-ano-2009-dom-hsi807-ubicacion-san-fernando-provincia-de-buenos-aires-2477501']

MAX_ATTEMPTS = 5

chrome = ChromeDriverManager()
pathToChrome = chrome.install()
service = Service(pathToChrome)


def getPublication(url):
    __brouser__ = webdriver.Chrome(service=service)
    __brouser__.get(url)

    def trySearch(callback) -> str:
        attempts = MAX_ATTEMPTS
        while attempts > 0:
            try:
                result = callback()
                return result
            except:
                attempts -= 1
                __brouser__.refresh()
        return 'not found'

    def getPrice() -> str:
        div = __brouser__.find_element(
            By.XPATH, '//div[@class="MuiGrid-root css-rfnosa"]')
        span = div.find_element(By.XPATH, './/span[3]')
        text = span.text.split(sep=' ')
        price = text[4]
        return price

    def getTitle() -> str:
        title = __brouser__.find_element(By.XPATH, '//h1')
        title = title.text
        return title

    title = trySearch(getTitle)
    price = trySearch(getPrice)
    __brouser__.close()
    return [title, price]


def getPublicationsForCompare(urls):
    publications = map(lambda url: getPublication(url), urls)
    df = DataFrame(data=publications, columns=['title', 'price'])
    df.to_excel('publicaciones.xlsx', index=False)


getPublicationsForCompare(urls)
