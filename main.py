from utils.utils import get_vacancies_in_table, refresh_tables
from classes.dbmanager import DBManager

'обнуляем таблицу и вносим свежие данные'
refresh_tables()
emploeys = [2515455, 869045, 43140, 9790209, 8918357, 2354030, 46587, 561525, 640251, 1740]

for i in emploeys:
    get_vacancies_in_table(i)
data = DBManager()

main_exit = True  # ключи для более наглядного завершения программы
menu_exit = True

'Начало работы интерфейса'

while main_exit is True:
    while menu_exit is True:
        print('Здравствуйте, выберете вариант пункта меню')
        print('1 - показать список компаний и кол-во вакансий относящихся к ним')
        print('2 - показать список всех вакансий')
        print('3 - показать среднею зарплату по имеющимся вакансиям')
        print('4 - показать список все хвакансий у которых зарплата выше средней')
        print('5 - найти вакансию по названию')
        print('0 - для выхода из программы')

        option_menu = input()
        if option_menu not in ['1', '2', '3', '4', '5', '0']:
            print('Некорректный вариант действий, выберете корректный!')
            continue

        if option_menu == '1':
            data.get_companies_and_vacancies_count()

        if option_menu == '2':
            data.get_all_vacancies()

        if option_menu == '3':
            print(f'Средняя зарплата: {data.get_avg_salary()}')

        if option_menu == '4':
            data.get_vacancies_with_higher_salary()

        if option_menu == '5':
            print('Введите название:')
            vacancie_name = input()
            data.get_vacancies_with_keyword(vacancie_name)

        if option_menu == '0':
            print('Спасибо...')
            main_exit = False
            menu_exit = False