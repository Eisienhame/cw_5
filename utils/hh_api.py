import requests, json

def getdata_hh():
    '''Загружаем данные с ХХ в список'''
    vacan_data = []

    # for n in range(1, 10):
    #     params = {
    #         'area': 113,  # Поиск в Ru зоне
    #         'page': n,    # Номер страницы
    #         'per_page': 100  # Кол-во вакансий на 1 странице
    #     }
    #     vacan_data.append(requests.get('https://api.hh.ru/vacancies', params).json())
    params = {
        'area': 113,  # Поиск в Ru зоне
        'page': 1,  # Номер страницы
        'per_page': 30  # Кол-во вакансий на 1 странице
    }
    vacan_data.append(requests.get('https://api.hh.ru/vacancies', params).json())
    return vacan_data

print(type(getdata_hh()))