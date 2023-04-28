'Создание таблиц'

CREATE TABLE vacancies
(
	id_vac int PRIMARY KEY,
	vac_name varchar NOT NULL,
	salary int,
	id_emp int NOT NULL,
	link_vac varchar UNIQUE
)

CREATE TABLE employeers
(
	id_emp int PRIMARY KEY,
	emp_name varchar UNIQUE
)

'список всех компаний и количество вакансий у каждой компании'

SELECT emp_name, COUNT(*) as total_vacancies
FROM vacancies
LEFT JOIN employeers USING(id_emp)
GROUP BY emp_name
ORDER BY total_vacancies DESC, emp_name

'получает список всех вакансий с указанием названия компании,названия вакансии и зарплаты и ссылки на вакансию'

SELECT employeers.emp_name, vac_name, salary, link_vac
FROM vacancies
INNER JOIN employeers USING(id_emp)
GROUP BY salary, link_vac, employeers.emp_name, vac_name
ORDER BY employeers.emp_name, salary DESC

'получает среднюю зарплату по вакансиям, 0 не берем т.к. там зп неизвестна'

SELECT ROUND(AVG(salary)) as avg_salary
FROM vacancies
WHERE salary > 0

'получает список всех вакансий, у которых зарплата выше средней по всем вакансиям'

SELECT vac_name, salary, link_vac
FROM vacancies
WHERE salary > (SELECT AVG(salary) FROM vacancies WHERE salary > 0)
ORDER BY salary DESC, vac_name

'получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”'

SELECT *
FROM vacancies
WHERE vac_name ILIKE '%python%'
ORDER BY salary DESC