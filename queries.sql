CREATE TABLE vacancies
(
	id_vac smallint PRIMARY KEY,
	id_emp smallint NOT NULL,
	salary smallint,
	link_vac varchar UNIQUE
)