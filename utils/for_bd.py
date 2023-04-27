from hh_api import getdata_hh, get_udated_list
import psycopg2
def get_vacancies_in_table(id):
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

get_vacancies_in_table(640251)


def refresh_tables():
    with psycopg2.connect(
            host="localhost",
            database="cw_5_hh",
            user="postgres",
            password="12345678") as conn:
        with conn.cursor() as cur:
            cur.execute('truncate table vacancies')
            cur.execute('truncate table employeers')