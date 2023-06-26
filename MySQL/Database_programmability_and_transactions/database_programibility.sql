-- LAB 
-- 1. Count Employees by Town 
CREATE FUNCTION ufn_count_employees_by_town(town_name VARCHAR(20))
RETURNS INT
DETERMINISTIC
RETURN (
SELECT COUNT(t.name) as count FROM employees as e
JOIN addresses as a ON e.address_id = a.address_id
JOIN towns as t ON a.town_id = t.town_id
WHERE t.name = town_name
);

-- 2. Employees Promotion
DELIMITER $$
CREATE PROCEDURE usp_raise_salaries(department_name VARCHAR(50))
BEGIN
UPDATE employees AS e
JOIN departments AS d ON e.department_id = d.department_id
SET e.salary = e.salary * 1.05
WHERE d.name = department_name;
END $$
DELIMITER ;

CALL usp_raise_salaries('Finance');
SELECT * FROM employees
WHERE department_id = 10;

3. Employees Promotion By ID 
DELIMITER $$
CREATE PROCEDURE  usp_raise_salary_by_id(id_to_promote INT)
BEGIN
START TRANSACTION;
IF ((SELECT COUNT(employee_id) FROM employees WHERE employee_id like id) <> 1) THEN
ROLLBACK;
ELSE
UPDATE employees AS e 
SET salary = salary * 1.05
WHERE e.employee_id = id_to_promote;
END IF;
END $$
DELIMITER ;

-- 4. Triggered
CREATE TABLE deleted_employees(
employee_id INT PRIMARY KEY AUTO_INCREMENT,
first_name VARCHAR(20),
last_name VARCHAR(20),
middle_name VARCHAR(20),
job_title VARCHAR(50),
department_id INT,
salary DOUBLE
);

DELIMITER $$
CREATE TRIGGER tr_deleted_employees
AFTER DELETE
ON employees
FOR EACH ROW
BEGIN
INSERT INTO deleted_employees (first_name,last_name,
middle_name,job_title,department_id,salary)
VALUES(OLD.first_name,OLD.last_name,OLD.middle_name,
OLD.job_title,OLD.department_id,OLD.salary);
END;
DELIMITER ;
;

-- Exercise
-- 1. Employees with Salary Above 35000
DELIMITER $$
CREATE PROCEDURE usp_get_employees_salary_above_35000()
BEGIN
SELECT first_name, last_name FROM employees
WHERE salary > 35000
ORDER BY first_name ASC, last_name ASC, employee_id ASC;
END $$
DELIMITER ;
;

CALL usp_get_employees_salary_above_35000();

-- 02. Employees with Salary Above Number
DELIMITER $$
CREATE PROCEDURE usp_get_employees_salary_above(salary_above DECIMAL(10, 4))
BEGIN
SELECT first_name, last_name FROM employees AS e
WHERE salary >= salary_above
ORDER BY first_name, last_name, employee_id;
END $$
DELIMITER ;
;

CALL usp_get_employees_salary_above(100000);

-- 03. Town Names Starting With 
DELIMITER $$
CREATE PROCEDURE usp_get_towns_starting_with(starting_string VARCHAR(50))
BEGIN
SELECT t.name FROM towns AS t
WHERE t.name LIKE CONCAT(starting_string, '%')
ORDER BY t.name ASC;
END $$
DELIMITER ;
;

CALL usp_get_towns_starting_with('c');

-- 4. Employees from Town
DELIMITER $$
CREATE PROCEDURE usp_get_employees_from_town(town_name VARCHAR(50))
BEGIN
SELECT first_name, last_name FROM employees AS e
JOIN addresses AS a ON e.address_id = a.address_id
JOIN towns AS t ON a.town_id = t.town_id
WHERE t.name = town_name
ORDER BY first_name, last_name;
END $$
DELIMITER ;
;

CALL usp_get_employees_from_town('Sofia');

-- 05. Salary Level Function 
DELIMITER $$
CREATE FUNCTION ufn_get_salary_level(salary_to_check DECIMAL(10, 2))
RETURNS VARCHAR(30)
DETERMINISTIC
RETURN(
CASE
WHEN salary_to_check < 30000 THEN 'Low'
WHEN salary_to_check <= 50000 THEN 'Average'
ELSE 'High'
END
) $$
DELIMITER ;
;

SELECT salary, ufn_get_salary_level(salary) FROM employees;

-- 06. Employees by Salary Level 
DELIMITER $$
CREATE PROCEDURE usp_get_employees_by_salary_level(salary_level VARCHAR(30))
BEGIN
SELECT first_name, last_name FROM employees
WHERE (SELECT ufn_get_salary_level(salary)) = salary_level
OR (SELECT ufn_get_salary_level(salary)) = salary_level
OR (SELECT ufn_get_salary_level(salary)) = salary_level
ORDER BY first_name DESC, last_name DESC;
END $$
DELIMITER ;
;

CALL usp_get_employees_by_salary_level('High');

-- 07. Define Function
DELIMITER $$
CREATE FUNCTION ufn_is_word_comprised(set_of_letters VARCHAR(50), word VARCHAR(50))
RETURNS BIT
DETERMINISTIC
RETURN (
word REGEXP (CONCAT('(?i)','[', set_of_letters,']'))
); 
$$
DELIMITER ;

SELECT ufn_is_word_comprised('oistmiahf', '');

-- 08. Find Full Name 

