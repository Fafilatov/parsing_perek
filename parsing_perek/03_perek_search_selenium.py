from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import datetime
import os

# list_for_find = ['Бумага туалетная', 'Майонез', 'Морковь', 'Репа', 'Лук', 'Филе', 'Хлеб', 'Мыло', 'Молоко', 'Гречка',
#                  'рис', 'Яйца', 'полба', 'Изделия хлебобулочные', 'Котлета', 'корейская морковка', 'Картофель', 'кофе',
#                  'чай', 'помидоры', 'Кетчуп', 'Вода', 'Чипсы', 'Зубная паста', 'Какао', 'Лечо', 'икра кабачковая',
#                  'творог', 'Свинина', 'Сардельки', 'Овощная смесь', 'Шоколад', 'Сыр', 'Порошок стиральный', 'Пельмени',
#                  'Блины', 'Пиво']
list_for_find = ['творог рассыпчатый']
url = "https://www.vprok.ru/"
date = datetime.datetime.now()
date_now = date.strftime("%m-%d")

if not os.path.isdir(os.getcwd() + '\\data\\'):
    os.mkdir(os.getcwd() + '\\data\\')
if not os.path.isdir(os.getcwd() + '\\data\\' + date_now):
    os.mkdir(os.getcwd() + '\\data\\' + date_now)
if not os.path.isdir(os.getcwd() + '\\data\\' + date_now + '\\index\\'):
    os.mkdir(os.getcwd() + '\\data\\' + date_now + '\\index\\')

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--headless")

driver = webdriver.Chrome(options=options,
                          executable_path=r"C:\Users\fafil\Chrome_driver_selenium\chromedriver.exe")

driver.get(url=url)  # Открываем страницу
elem = ''

for product_name in list_for_find:
    elems = driver.find_elements(By.TAG_NAME, "input")  # вписывает в поисковую строкуууу!!! от сих
    n = 0
    for elem in elems:
        n += 1
        try:
            elem.send_keys((product_name, Keys.ARROW_DOWN))
            driver.execute_script("window.scrollTo(0, document.body.scrollUp);")
            print('Ok, итерация', n)
            break
        except:
            print('Except, итерация', n)  # до сих

    print('Ввели слово для поиска')

    time.sleep(1)

    elems_buttom = driver.find_elements(By.CLASS_NAME,
                                        "xfnew-header-search-bar--new__img")  # нажимает кнопку поискаааа!!! от сих
    m = 0                              #
    print('Начали искать кнопку для поиска')
    for elem_b in elems_buttom:
        m += 1
        try:
            elem_b.click()
            driver.execute_script("window.scrollTo(0, document.body.scrollUp);")
            print('Ok, итерация', m)
            break
        except:
            print('Except, итерация', m)  # до сих
    time.sleep(1)

    # try:
    #     elems_filter = driver.find_elements(By.CLASS_NAME, 'xf-filter-section-item__text')
    #     print('Ищем по 1 фильтру из', str(len(elems_filter)), 'вариантов')
    #     elem_f = elems_filter[0]
    #     elem_f.click()
    # except:
    #     elems_buttom = driver.find_elements(By.CLASS_NAME,
    #                                         "xfnew-search-results--new__more-wrap")  # нажимает кнопку поискаааа!!!
    #     # от сих                             xfnew-search-results--new__more-wrap
    #     m = 0
    #     print('Начали искать кнопку для поиска')
    #     for elem_b in elems_buttom:
    #         m += 1
    #         try:
    #             elem_b.click()
    #             driver.execute_script("window.scrollTo(0, document.body.scrollUp);")
    #             print('Ok, итерация', m)
    #             break
    #         except:
    #             print('Except, итерация', m)  # до сих
    #     time.sleep(1)

        # elems_filter = driver.find_elements(By.CLASS_NAME, 'xf-filter-section-item__text')
        # print('Ищем по 1 фильтру из', str(len(elems_filter)), 'вариантов')
        # elem_f = elems_filter[0]
        # elem_f.click()

    html = driver.find_element(By.TAG_NAME, 'html')
    for _ in range(random.randint(10, 15)):
        html.send_keys(Keys.PAGE_DOWN)  # мотает страничку вниз
        time.sleep(random.randint(1, 11) / 10)

    file_reference = os.getcwd() + '\\data\\' + date_now + '\\index\\index_input_selenium_' + product_name + ".html"

    with open(file_reference, "w", encoding="UTF-8") as file:
        file.write(driver.page_source)

        elems = driver.find_elements(By.TAG_NAME, "input")  # ищет поисковую строкуууу!!! от сих
        n = 0
        for elem in elems:
            n += 1
            try:
                elem.send_keys((Keys.CONTROL + "a"))
                elem.send_keys(Keys.DELETE)
                driver.execute_script("window.scrollTo(0, document.body.scrollUp);")
                print('Ok, итерация', n)
                break
            except:
                print('Except, итерация', n)  # до сих

        print('Удалили слово для поиска')

driver.close()
driver.quit()
