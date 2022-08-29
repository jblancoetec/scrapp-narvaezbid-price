from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from pandas import DataFrame

MAX_ATTEMPTS = 5
NOT_FOUND_STATE = 1
FOUND_STATE = 2

chrome = ChromeDriverManager()
pathToChrome = chrome.install()
service = Service(pathToChrome)


def getPrice(browser) -> str:
    attempts = MAX_ATTEMPTS
    state = NOT_FOUND_STATE
    price = 'price not found'
    while state == NOT_FOUND_STATE and attempts > 0:
        try:
            div = browser.find_element(
                By.XPATH, '//div[@class="MuiGrid-root css-rfnosa"]')
            span = div.find_element(By.XPATH, './/span[3]')
            text = span.text.split(sep=' ')
            price = text[4]
            state = FOUND_STATE
        except:
            attempts -= 1

    return price


def getTitle(browser) -> str:
    attempts = MAX_ATTEMPTS
    state = NOT_FOUND_STATE
    title = 'title not found'
    while state == NOT_FOUND_STATE and attempts > 0:
        try:
            title = browser.find_element(By.XPATH, '//h1')
            title = title.text
            state = FOUND_STATE
        except:
            attempts -= 1

    return title


def getPublication(url):
    browser = webdriver.Chrome(service=service)
    browser.get(url)
    title = getTitle(browser)
    price = getPrice(browser)
    browser.close()
    return [title, price]


def getPublicationsForCompare(urls):
    publications = map(lambda url: getPublication(url), urls)
    df = DataFrame(data=publications, columns=['title', 'price'])
    df.to_excel('publicaciones.xlsx')


urls = ['https://www.narvaezbid.com.ar/oferta/fiat-pick-up-cabina-doble-strada-adventure-16-ano-2018-dom-ac683wl-ubicacion-san-fernando-provincia-de-buenos-aires-2477505',
        'https://www.narvaezbid.com.ar/oferta/fiat-sedan-5-puertas-punto-hlx-18-ano-2009-dom-hsi807-ubicacion-san-fernando-provincia-de-buenos-aires-2477501']
getPublicationsForCompare(urls)
