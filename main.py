from utils.for_bd import get_vacancies_in_table, refresh_tables


refresh_tables()
emploeys = [2515455, 869045, 43140, 9790209, 8918357, 2354030, 46587, 8918357, 561525, 640251]

for i in emploeys:
    get_vacancies_in_table(i)

