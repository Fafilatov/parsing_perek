# https://hh.ru/vacancy/49183752?from=vacancy_search_list
import os


for dir, subdir, files in os.walk("F:\\"):
    for file in files:
        path = dir + '\\' + file
        try:
            if path.endswith(".txt") and os.path.getsize(path) <= 2000:
                with open(path, "r+") as txt_file:
                    lines = txt_file.readlines()
                    txt_file.seek(0)
                    txt_file.write("A. Filatov")
                    for line in lines:
                        txt_file.write(line)
                    txt_file.close()

        except:
            continue

            # title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text - так
            # можно??

