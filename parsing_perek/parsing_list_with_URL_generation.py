import os
import datetime
from bs4_classes import following_links
from bs4 import BeautifulSoup

from selenium import webdriver
# list_for_find = ['Бумага туалетная', 'Майонез', 'Морковь', 'Репа', 'Лук', 'Филе', 'Хлеб', 'Мыло', 'Молоко', 'Гречка',
#                  'рис', 'Яйца', 'полба', 'Изделия хлебобулочные', 'Котлета', 'корейская морковка', 'Картофель', 'кофе',
#                  'чай', 'помидоры', 'Кетчуп', 'Вода', 'Чипсы', 'Зубная паста', 'Какао', 'Лечо', 'икра кабачковая',
#                  'творог', 'Свинина', 'Сардельки', 'Овощная смесь', 'Шоколад', 'Сыр', 'Порошок стиральный', 'Пельмени',
#                  'Блины', 'Пиво']
list_for_find = ['творог рассыпчатый', 'помидоры', 'Кетчуп']
date = datetime.datetime.now()
date_now = date.strftime("%m-%d")

if not os.path.isdir(os.getcwd() + '\\data_with_URL_generation\\'):
    os.mkdir(os.getcwd() + '\\data_with_URL_generation\\')
if not os.path.isdir(os.getcwd() + '\\data_with_URL_generation\\' + date_now):
    os.mkdir(os.getcwd() + '\\data_with_URL_generation\\' + date_now)
if not os.path.isdir(os.getcwd() + '\\data_with_URL_generation\\' + date_now + '\\index\\'):
    os.mkdir(os.getcwd() + '\\data_with_URL_generation\\' + date_now + '\\index\\')

index = os.getcwd() + '\\data_with_URL_generation\\' + date_now + '\\index\\'

for product in list_for_find:
    product = '+'.join(product.split())
    url = "https://www.vprok.ru/catalog/search?text=" + product + "&sort=relevance_desc"
    html = following_links(url)
    product = '_'.join(product.split('+'))
    with open(index + product + '.html', 'w', encoding='UTF-8') as file:
        file.write(html)

####################################################################################################################
# soup_goods = BeautifulSoup(html, 'lxml')
# articles = soup_goods.find_all("li", class_="js-catalog-product _additionals xf-catalog__item")
# print("Всего в списке", len(articles), "товаров")
# n = 0
# # Ниже перебираем поштучно каталоги и забираем наименование товара
#
# with open(os.getcwd() + '\\data_in_URL\\' + date_now + '\\catalog.csv', 'w', newline="") as csvfile:
#     writer = csv.writer(csvfile, delimiter=";")
#     writer.writerow(["Наименование", "Актуальная цена ", "Цена указана за"])
#
# for tag_product_1 in articles:
#     name_product = tag_product_1.find("div", {"class": "xf-product__title xf-product-title"}).find("a")
#     n += 1
#     print("Товар номер", n, name_product.text.strip())
#
#     # Ниже перебираем характеристики товара и сохраняем их
#     tag_with_price = tag_product_1.find("div",
#                                         {"class": "xf-product__cost xf-product-cost xf-product-cost--highlight"})
#     if tag_with_price is not None:
#         item = Item(name=name_product.text.strip(), tag=tag_with_price)
#         print("Это тег highlight, в нем", item.defining_length_price(), "значений")
#         print("Его цена", item.defining_price(), ", его стоимость указана за", item.defining_unit())
#
#         with open(os.getcwd() + '\\data_in_URL\\' + date_now + '\\catalog.csv', 'a', newline="") as csvfile:
#             writer = csv.writer(csvfile, delimiter=";")
#             writer.writerow([item.name, item.defining_price(), item.defining_unit(), item.curd()])
#
#     else:
#         tag_with_price = tag_product_1.find("div", {"class": "xf-product__cost xf-product-cost"})
#         if tag_with_price is not None:
#             item = Item(name=name_product.text.strip(), tag=tag_with_price)
#             print("Это тег highlight, в нем", item.defining_length_price(), "значений")
#             print("Его цена", item.defining_price(), ", его стоимость указана за", item.defining_unit())
#
#             with open(os.getcwd() + '\\data_in_URL\\' + date_now + '\\catalog.csv', 'a', newline="") as csvfile:
#                 writer = csv.writer(csvfile, delimiter=";")
#                 writer.writerow([item.name, item.defining_price(), item.defining_unit(), item.curd()])
#
#         else:
#             print("Товара нет в наличии")