PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS employees;
CREATE TABLE employees (employee_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, employee_fio VARCHAR (50) NOT NULL,
employee_position INTEGER, FOREIGN KEY (employee_position) REFERENCES positions (position_id));

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;