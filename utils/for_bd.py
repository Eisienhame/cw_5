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
                cur.execute('INSERT INTO vacancies(id_vac, vac_name, salary, id_emp, emp_name, link_vac)'
                            'VALUES(%s, %s, %s, %s, %s, %s)', (row["id_vac"], row["name"], row["salary"], row["id_emp"], row["emp_name"], row["url"]))


get_vacancies_in_table(869045)
# print(get_udated_list(869045))
# for i in get_udated_list(869045):
#     print(i)
