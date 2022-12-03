import requests
import pprint
import json


DOMAIN = 'https://api.hh.ru/'
url_vacancies = f'{DOMAIN}vacancies'
params = {
        'text': 'Excel AND Powerpoint', # Текст фильтра.
        'area': 1, # Поиск ощуществляется по вакансиям города Москва
        'page': 1, # Индекс страницы поиска на HH
    }

result = requests.get(url_vacancies, params=params)
pprint.pprint(result.json())
resultJson = result.json()

#сохраняем в файл
with open ('hh_vacan.json', 'w') as f:
    json.dump(resultJson,f)
