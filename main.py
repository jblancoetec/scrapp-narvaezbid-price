from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from pandas import DataFrame
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import TimeoutException


class Publication(webdriver.Chrome):
    __chrome__ = ChromeDriverManager()
    __pathToChromeDriver__ = __chrome__.install()
    __service__ = Service(__pathToChromeDriver__)

    def __init__(self, url: str):
        super().__init__(service=Publication.__service__)
        self.get(url=url)

    def getTitle(self) -> str:
        wait = WebDriverWait(driver=self, timeout=20)
        title = wait.until(
            method=presence_of_element_located((By.TAG_NAME, 'h1')),
            message="timeout"
        )
        return title.text

    def getPrice(self) -> str:
        wait = WebDriverWait(driver=self, timeout=20)
        div = wait.until(
            method=presence_of_element_located(
                (By.XPATH, '//div[@class="MuiGrid-root css-rfnosa"]')),
            message="timeout"
        )
        span = div.find_element(By.XPATH, './/span[3]')
        text = span.text.split(sep=' ')
        price = text[4]
        return price

    def getPriceAndTitle(self) -> tuple[str, str]:
        try:
            title = self.getTitle()
            price = self.getPrice()
            return (title, price)
        except TimeoutException as err:
            return (err.msg, err.msg)
        except BaseException:
            return ("titile not found", "price not foud")
        finally:
            self.close()


def readUrls() -> list[str]:
    with open('urls.txt', 'r') as file:
        urls = file.read().splitlines()
        return urls


def main():
    urls = readUrls()
    publications = [Publication(url) for url in urls]
    data = [publication.getPriceAndTitle()
            for publication in publications]
    publications = [publication.quit() for publication in publications]
    df = DataFrame(data=data, columns=['title', 'price'])
    df.to_excel('publicaciones.xlsx', index=False)


main()
