import requests, json

def getdata_hh(id):
    '''Загружаем данные с ХХ в список'''
    vacan_data = []
    params = {
        'employer_id': id,
    }
    vacan_data.append(requests.get('https://api.hh.ru/vacancies', params).json())
    return vacan_data

def get_udated_list(id):
    work_dic_hh = []
    dic_hh = getdata_hh(id)
    for i in dic_hh:
        for n in range(len(i['items'])):
            'Значение зп всместо от и до будет иметь 1 значение, и знач от в приоритете'
            if i['items'][n]['salary'] is None:
                salary_single = 0
            elif i['items'][n]['salary']['from'] is None and i['items'][n]['salary']['to'] is None:
                salary_single = 0
            elif i['items'][n]['salary']['from'] is None and i['items'][n]['salary']['to'] > 0:
                salary_single = i['items'][n]['salary']['to']
            else:
                salary_single = i['items'][n]['salary']['from']

            next_item = {'id_vac': i['items'][n]['id'],
                    'name': i['items'][n]['name'],
                    'salary': salary_single,
                    'id_emp': i['items'][n]['employer']['id'],
                    'emp_name': i['items'][n]['employer']['name'],
                    'url': i['items'][n]['url']}


            work_dic_hh.append(next_item)

    return work_dic_hh