CREATE TABLE vacancies
(
	id_vac int PRIMARY KEY,
	vac_name varchar NOT NULL,
	salary int,
	id_emp int NOT NULL,
	emp_name varchar NOT NULL,
	link_vac varchar UNIQUE
)

CREATE TABLE employeers
(
	id_emp int PRIMARY KEY,
	emp_name varchar UNIQUE,
	vacancies int
)