import re
import random
import time
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import math


class Item():

    def __init__(self, name, tag, keyword=None):
        self.name = name
        self.tag = tag
        self.keyword = keyword

    def defining_price(self):
        product_detail = self.tag.find_all("span")
        price = product_detail[-2].text.strip()
        price = price.replace(".", ",")
        return price

    def defining_unit(self):
        product_detail = self.tag.find_all("span")
        unit = product_detail[-3].text.strip()
        return unit

    def defining_length_price(self):
        product_detail = self.tag.find_all("span")
        length_price = len(product_detail)
        return length_price

    def curd(self):  # Сделано для творога
        gramme = self.name[-4:-1]
        return gramme


def following_links(url):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options,
                              executable_path=r"C:\Users\fafil\Crome_driver_selenium\chromedriver.exe")
    driver.get(url=url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    total_number_of_goods = soup.find('span', class_='js-list-total__total-count')
    print('Количество товаров в категории', total_number_of_goods.text)
    html = driver.find_element(By.TAG_NAME, 'html')
    page = math.ceil(int(total_number_of_goods.text) / 30)
    print("Всего товаров на", page, "страниц")
    for i in range(1, page):
        # html.send_keys(Keys.PAGE_DOWN)  # мотает страничку вниз
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print('Смотрим страницу', i)
        time.sleep(2)

    html = driver.page_source
    driver.close()
    driver.quit()
    return html
