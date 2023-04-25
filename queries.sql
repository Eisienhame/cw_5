CREATE TABLE vacancies
(
	id_vac smallint PRIMARY KEY,
	id_emp smallint NOT NULL,
	salary smallint,
	link_vac varchar UNIQUE
)

CREATE TABLE employeers
(
	id_emp smallint PRIMARY KEY,
	emp_name varchar UNIQUE,
	vacancies int
)