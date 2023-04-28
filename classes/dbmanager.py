from abc import abstractmethod
import psycopg2
class DBManager():

    # def __init__(self):
    #
    #     pass

    @abstractmethod
    def connection(self, rules:str):
        'Подкл к бд и возвращает инфу по sql запросу'
        with psycopg2.connect(
                host="localhost",
                database="cw_5_hh",
                user="postgres",
                password="12345678") as conn:
            with conn.cursor() as cur:
                cur.execute(rules)
                records = cur.fetchall()
            return records
    def get_companies_and_vacancies_count(self):
        'получает список всех компаний и количество вакансий у каждой компании.'
        req = 'SELECT emp_name, COUNT(*) as total_vacancies FROM vacancies LEFT JOIN employeers USING(id_emp) GROUP BY emp_name ORDER BY total_vacancies DESC, emp_name'
        data = self.connection(req)
        for i in data:
            print(f'Название комании: {i[0]} \n Кол-во вакансий: {i[1]}')
            print('__________________________________________________')


    def get_all_vacancies(self):
        '''получает список всех вакансий с указанием названия компании,
         названия вакансии и зарплаты и ссылки на вакансию'''
        pass
    def get_avg_salary(self):
        'получает среднюю зарплату по вакансиям'
        pass

    def get_vacancies_with_higher_salary(self):
        'получает список всех вакансий, у которых зарплата выше средней по всем вакансиям'
        pass

    def get_vacancies_with_keyword(self):
        'получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”'

x = DBManager()
#print(x.connection('SELECT * FROM employeers'))
x.get_companies_and_vacancies_count()