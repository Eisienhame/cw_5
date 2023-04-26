import requests, json

def getdata_hh():
    '''Загружаем данные с ХХ в список'''
    vacan_data = []
    params = {
        'employer_id': 869045,
    }
    vacan_data.append(requests.get('https://api.hh.ru/vacancies', params).json())
    return vacan_data

