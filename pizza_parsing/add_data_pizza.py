import psycopg2
import pandas as pd

# Перемещаем данные из 'pizza_data/pizza_data.csv' в БД 'pizza_site_django_db':
pizza_data = pd.read_csv("pizza_data/pizza_data.csv")

try:
    # Подключаемся к БД:
    connection = psycopg2.connect('host=localhost port=5433 user=postgres password=postgres dbname=postgres')

    # Вносим данные в таблицу:
    with connection.cursor() as cursor:
        for data in range(pizza_data['name'].size):

            name = str(pizza_data['name'][data]).split('"')[1].lower()
            weight = str(pizza_data['size'][data])
            descriptions = str(pizza_data['text'][data])
            price = int(pizza_data['price'][data])
            image_url = str(pizza_data['image'][data])
            url = str(pizza_data['name'][data]).split('"')[1].replace(" ", "_").lower()

            cursor.execute(
                """INSERT INTO pizza_pizza (name, weight, descriptions, price, image_url, url) VALUES
                (%s, %s, %s, %s, %s, %s);""", (name, weight, descriptions, price, image_url, url)
            )

    # Сохраняем все внесенные в БД данные:
    connection.commit()
    connection.close()

except Exception as ex:
    print("[INFO] При переносе данных в БД произошла ошибка: ", ex)
finally:
    print("Операция по переносу данных завершена.")
