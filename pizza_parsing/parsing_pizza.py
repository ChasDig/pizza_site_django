"""
    Скрипт для получения данных о пицце с сайта 'http://суши-пицца24.рф/'
"""

from bs4 import BeautifulSoup
import requests
import csv
import json


# Получаем копию сайта и сохраняем в формате html:
site_url = 'http://суши-пицца24.рф/catalog/category/pizza'

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0',
}

pizza_html_data = requests.get(url=site_url, headers=headers)

with open('pizza_data/pizza_data.html', 'w') as file:
    file.write(pizza_html_data.text)

with open('pizza_data/pizza_data.html', 'r') as file:
    pizza_page_data = file.read()


# Извлекаем данные из html файла и сохраняем в формате 'csv':
soup = BeautifulSoup(pizza_page_data, 'lxml')


def get_pizza_data(soup):

    # Словарь, в котором будем хранить первичную информацию о пицце:
    pizza_dict_data_all = {}
    pizza_dict_list = []
    counter = 0

    # Получаем поля с характеристиками пиццы:
    pizza_name = soup.find(class_='product-items').select('.name')
    pizza_size = soup.find(class_='product-items').select('.size')
    pizza_text = soup.find(class_='product-items').select('.text')
    pizza_price = soup.find(class_='product-items').select('.price')
    pizza_image = soup.find(class_='product-items').find_all('img')

    # Сохраняем поля в словарь:
    for item in pizza_name:
        pizza_dict_data = {'name': item.text.strip(),
                           'size': pizza_size[counter].text.strip(),
                           'text': pizza_text[counter].text.strip(), 'price': pizza_price[counter].text.strip(),
                           'image': f"http://суши-пицца24.рф{pizza_image[counter]['src']}"}
        pizza_dict_list.append(pizza_dict_data)
        counter += 1

    pizza_dict_data_all[0] = pizza_dict_list

    return pizza_dict_data_all.pop(0)


pizza_data_result = get_pizza_data(soup=soup)

# Создаем json-файл data_pizza:
with open('pizza_data/pizza_data.json', 'w') as file:
    json.dump(pizza_data_result, file, indent=4, ensure_ascii=False)

# Создаем заголовок для csv-файл data_pizza:
with open('pizza_data/pizza_data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(
        ['name', 'size', 'text', 'price', 'image']
    )

# Загружаем все данные в csv-файл data_pizza:
for item in pizza_data_result:
    with open('pizza_data/pizza_data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(
            item.values()
        )
