from abc import abstractmethod
import psycopg2
class DBManager():

    def __init__(self):

        pass

    @abstractmethod
    def connection(self, rules:str):
        with psycopg2.connect(
                host="localhost",
                database="cw_5_hh",
                user="postgres",
                password="12345678") as conn:
            with conn.cursor() as cur:
                cur.execute(rules)
                records = cur.fetchall()
            return records
    def get_companies_and_vacancies_count():
        'получает список всех компаний и количество вакансий у каждой компании.'
        pass

    def get_all_vacancies():
        '''получает список всех вакансий с указанием названия компании,
         названия вакансии и зарплаты и ссылки на вакансию'''
        pass
    def get_avg_salary():
        'получает среднюю зарплату по вакансиям'
        pass

    def get_vacancies_with_higher_salary():
        'получает список всех вакансий, у которых зарплата выше средней по всем вакансиям'
        pass

    def get_vacancies_with_keyword():
        'получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”'

x = DBManager()
print(x.connection('SELECT * FROM employeers'))