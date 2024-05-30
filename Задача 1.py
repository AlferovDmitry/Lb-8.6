#Задача №1
#Запросим погодный сервис http://wttr.in по URL без параметров. А их зададим словарём weather_parameters. Функция get() должна принимать его, как отдельный аргумент params.

import requests

url = 'https://wttr.in'  # не изменяйте значение URL

weather_parameters = {
    '0': '',
    'T': ''
}

response = requests.get(url, params=weather_parameters)  # передайте параметры в http-запрос

print(response.text)