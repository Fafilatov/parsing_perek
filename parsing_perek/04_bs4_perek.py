from bs4 import BeautifulSoup
import lxml
import csv
from bs4_classes import Item
import datetime
import os

date = datetime.datetime.now()
date_now = date.strftime("%m-%d")
time_now = date.strftime("%H-%M")
file_reference_input = os.getcwd() + '\\data\\' + date_now + '\\index\\'
file_reference_output = os.getcwd() + '\\data\\' + date_now + '\\'

# Ниже создаем таблицу с заголовками
file_directory_and_name_csv_table = file_reference_output + 'processed_' + time_now + '.csv'
with open(file_directory_and_name_csv_table, 'w', newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(["Keyword", "Наименование", "Актуальная цена ", "Цена указана за", "Грамм (только для 'творог рассыпчатый'!!!)"])

for keyword in os.listdir(file_reference_input):
    message = file_reference_input + "index_input_selenium_" + keyword[21:]
    print(message)

    with open(message, encoding="UTF-8") as file:
        src = file.read()

    # Ниже собираем все каталоги с товарами и помещаем в список articles
    soup = BeautifulSoup(src, "lxml")
    articles = soup.find_all("li", class_="js-catalog-product _additionals xf-catalog__item")
    print("Всего в списке", len(articles), "товаров")
    n = 0

    # Ниже перебираем поштучно каталоги и забираем наименование товара
    for tag_product_1 in articles:
        name_product = tag_product_1.find("div", {"class": "xf-product__title xf-product-title"}).find("a")
        n += 1
        print("Товар номер", n, name_product.text.strip())

        # Ниже перебираем характеристики товара и сохраняем их
        tag_with_price = tag_product_1.find("div", {"class": "xf-product__cost xf-product-cost xf-product-cost--highlight"})
        if tag_with_price is not None:
            item = Item(name=name_product.text.strip(), tag=tag_with_price, keyword=keyword)
            print("Это тег highlight, в нем", item.defining_length_price(), "значений")
            print("Его цена", item.defining_price(), ", его стоимость указана за", item.defining_unit())

            with open(file_directory_and_name_csv_table, 'a', newline="") as csvfile:
                writer = csv.writer(csvfile, delimiter=";")
                writer.writerow([keyword[21:-5], item.name, item.defining_price(), item.defining_unit(), item.curd()])

        else:
            tag_with_price = tag_product_1.find("div", {"class": "xf-product__cost xf-product-cost"})
            if tag_with_price is not None:
                item = Item(name=name_product.text.strip(), tag=tag_with_price, keyword=keyword)
                print("Это тег highlight, в нем", item.defining_length_price(), "значений")
                print("Его цена", item.defining_price(), ", его стоимость указана за", item.defining_unit())

                with open(file_directory_and_name_csv_table, 'a', newline="") as csvfile:
                    writer = csv.writer(csvfile, delimiter=";")
                    writer.writerow([keyword[21:-5], item.name, item.defining_price(), item.defining_unit(), item.curd()])

            else:
                print("Товара нет в наличии")





