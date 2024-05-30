#Задача №3. Заголовки запросов и ответов.

#Запрашиваем Русский язык через заголовок запроса ‘Accept-Language’.(как на прошлом уроке)

import requests

url = 'https://wttr.in'

weather_parameters = {
    '0': '',
    'T': '',
    'M': '',
}

request_headers = {
    'Accept-Language': 'ru'
}

#передаем параметры и заголовки в http-запрос
response = requests.get(url, params=weather_parameters, headers=request_headers)

print(response.text)