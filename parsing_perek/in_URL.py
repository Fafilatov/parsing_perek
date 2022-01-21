import datetime
import os
from bs4 import BeautifulSoup
import csv
from bs4_classes import following_links
from bs4_classes import Item


url_category = "https://www.vprok.ru/catalog/1392?category=1392&page=1&sort=rate_desc"
date = datetime.datetime.now()
date_now = date.strftime("%m-%d")

if not os.path.isdir(os.getcwd() + '\\data_in_URL\\'):
    os.mkdir(os.getcwd() + '\\data_in_URL\\')
if not os.path.isdir(os.getcwd() + '\\data_in_URL\\' + date_now):
    os.mkdir(os.getcwd() + '\\data_in_URL\\' + date_now)
if not os.path.isdir(os.getcwd() + '\\data_in_URL\\' + date_now + '\\index\\'):
    os.mkdir(os.getcwd() + '\\data_in_URL\\' + date_now + '\\index\\')

html = following_links(url_category)
soup_goods = BeautifulSoup(html, 'lxml')
articles = soup_goods.find_all("li", class_="js-catalog-product _additionals xf-catalog__item")
print("Всего в списке", len(articles), "товаров")
n = 0
# Ниже перебираем поштучно каталоги и забираем наименование товара

with open(os.getcwd() + '\\data_in_URL\\' + date_now + '\\catalog.csv', 'w', newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(["Наименование", "Актуальная цена ", "Цена указана за"])

for tag_product_1 in articles:
    name_product = tag_product_1.find("div", {"class": "xf-product__title xf-product-title"}).find("a")
    n += 1
    print("Товар номер", n, name_product.text.strip())

    # Ниже перебираем характеристики товара и сохраняем их
    tag_with_price = tag_product_1.find("div",
                                        {"class": "xf-product__cost xf-product-cost xf-product-cost--highlight"})
    if tag_with_price is not None:
        item = Item(name=name_product.text.strip(), tag=tag_with_price)
        print("Это тег highlight, в нем", item.defining_length_price(), "значений")
        print("Его цена", item.defining_price(), ", его стоимость указана за", item.defining_unit())

        with open(os.getcwd() + '\\data_in_URL\\' + date_now + '\\catalog.csv', 'a', newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=";")
            writer.writerow([item.name, item.defining_price(), item.defining_unit(), item.curd()])

    else:
        tag_with_price = tag_product_1.find("div", {"class": "xf-product__cost xf-product-cost"})
        if tag_with_price is not None:
            item = Item(name=name_product.text.strip(), tag=tag_with_price)
            print("Это тег highlight, в нем", item.defining_length_price(), "значений")
            print("Его цена", item.defining_price(), ", его стоимость указана за", item.defining_unit())

            with open(os.getcwd() + '\\data_in_URL\\' + date_now + '\\catalog.csv', 'a', newline="") as csvfile:
                writer = csv.writer(csvfile, delimiter=";")
                writer.writerow([item.name, item.defining_price(), item.defining_unit(), item.curd()])

        else:
            print("Товара нет в наличии")
