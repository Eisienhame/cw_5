import requests, json, psycopg2, os

def getdata_hh(id):
    '''Загружаем данные с ХХ в список'''
    vacan_data = []
    params = {
        'employer_id': id,
    }
    vacan_data.append(requests.get('https://api.hh.ru/vacancies', params).json())
    return vacan_data

def get_udated_list(id):
    'формируем список с нужными данными'
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

def get_vacancies_in_table(id):
    'из списка вгружаем данные в СОЗДАННЫЕ заранее таблицы'
    data_for_bd = get_udated_list(id)
    with psycopg2.connect(
            host="localhost",
            database="cw_5_hh",
            user="postgres",
            password="12345678") as conn:
        with conn.cursor() as cur:
            for row in data_for_bd:
                cur.execute('INSERT INTO vacancies(id_vac, vac_name, salary, id_emp, link_vac)'
                            'VALUES(%s, %s, %s, %s, %s)', (row["id_vac"], row["name"], row["salary"], row["id_emp"], row["url"]))
                e_id = row["id_emp"]
                e_name = row["emp_name"]
            cur.execute('INSERT INTO employeers(id_emp, emp_name)'
                        'VALUES(%s, %s)',
                        (e_id, e_name))

def refresh_tables():
    'обнуляем данные в таблицах'
    with psycopg2.connect(
            host="localhost",
            database="cw_5_hh",
            user="postgres",
            password="12345678") as conn:
        with conn.cursor() as cur:
            cur.execute('truncate table vacancies, employeers')

def create_table():
    'создадим таблицы'
    with psycopg2.connect(
            host="localhost",
            database="cw_5_hh",
            user="postgres",
            password=bd_cw_5_pass) as conn:
        with conn.cursor() as cur:
            cur.execute('CREATE TABLE vacancies (id_vac int PRIMARY KEY, vac_name varchar NOT NULL,	salary int,	id_emp int NOT NULL, link_vac varchar UNIQUE)')
            cur.execute('CREATE TABLE employeers (id_emp int PRIMARY KEY, emp_name varchar UNIQUE)')

create_table()