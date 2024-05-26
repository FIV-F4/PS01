"""Задание 1: Получение данных

1. Импортируйте библиотеку `requests`.

2. Отправьте GET-запрос к открытому API (например, [https://api.github.com](https://api.github.com/)) с параметром для поиска репозиториев с кодом html.

3. Распечатайте статус-код ответа.

4. Распечатайте содержимое ответа в формате JSON.

Задание 2: Параметры запрос

1. Используйте API, который позволяет фильтрацию данных через URL-параметры (например, https://jsonplaceholder.typicode.com/posts).

2. Отправьте GET-запрос с параметром `userId`, равным `1`.

3. Распечатайте полученные записи.

Задание 3: Отправка данных

1. Используйте API, которое принимает POST-запросы для создания новых данных (например, https://jsonplaceholder.typicode.com/posts).

2. Создайте словарь с данными для отправки (например, `{'title': 'foo', 'body': 'bar', 'userId': 1}`).

3. Отправьте POST-запрос с этими данными.

4. Распечатайте статус-код и содержимое ответа.

В поле для ответа загрузи скриншоты сделанных заданий или ссылку на Git.
"""

import requests
import pprint
#################### №1 ####################
params = {'q': "html"}
response = requests.get('https://api.github.com/search/repositories', params=params)
print(response.status_code)
pprint.pprint(response.json())

print("-----------------------------------------------------------------------")


#################### №2 ####################

response = requests.get('https://jsonplaceholder.typicode.com/posts', params={'userId': 1})

print(response.status_code)
pprint.pprint(response.json())

print("-----------------------------------------------------------------------")


#################### №3 ####################


response = requests.post('https://jsonplaceholder.typicode.com/posts', data={'title': 'foo', 'body': 'bar', 'userId': 1, 'Реклама': 'Здесь могла быть ваша реклама'})


print(response.status_code)
pprint.pprint(response.json())