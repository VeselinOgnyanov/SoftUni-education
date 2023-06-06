-- LAB
-- 1. Departments Info
SELECT department_id, COUNT(department_id) FROM employees
GROUP BY department_id;


-- 2. Average Salary
SELECT department_id, ROUND(AVG(salary), 2) AS 'Average salary' FROM employees
GROUP BY department_id
ORDER BY department_id;

-- 3. Minimum Salary 
SELECT department_id, ROUND(MIN(salary), 2) AS 'Min salary' FROM employees
GROUP BY department_id
HAVING `Min salary` > 800
ORDER BY department_id;

-- 4. Appetizers Count 
SELECT COUNT(name) FROM products
WHERE category_id = 2 AND price > 8;

-- 5. Menu Prices
SELECT category_id, ROUND(AVG(price), 2) AS 'Average Price', ROUND(MIN(price), 2) AS 'Cheapest Produc',
 ROUND(MAX(price), 2) AS 'Most Expensive Product'
FROM products
GROUP BY category_id;

-- Exercise
-- 01. Records’ Count 
SELECT COUNT(id) AS 'count' FROM wizzard_deposits;

-- 02. Longest Magic Wand
SELECT MAX(magic_wand_size) AS 'longest_magic_wand' FROM wizzard_deposits;

-- 03. Longest Magic Wand per Deposit Groups 
SELECT deposit_group, MAX(magic_wand_size) AS 'longest_magic_wand' FROM wizzard_deposits
GROUP BY deposit_group
ORDER BY `longest_magic_wand`, deposit_group;

-- 04. Smallest Deposit Group per Magic Wand Size
SELECT deposit_group FROM wizzard_deposits
GROUP BY deposit_group
ORDER BY MIN(magic_wand_size)
LIMIT 1;

-- 05. Deposits Sum 
SELECT deposit_group, SUM(deposit_amount) AS 'total_sum' FROM wizzard_deposits
GROUP BY deposit_group
ORDER BY `total_sum`;

-- 06. Deposits Sum for Ollivander Family 
SELECT deposit_group, SUM(deposit_amount) AS 'total_sum' FROM wizzard_deposits
WHERE magic_wand_creator = 'Ollivander family'
GROUP BY deposit_group
ORDER BY deposit_group ASC;

-- 07. Deposits Filter 
SELECT deposit_group, SUM(deposit_amount) AS 'total_sum' FROM wizzard_deposits
WHERE magic_wand_creator = 'Ollivander family'
GROUP BY deposit_group
HAVING `total_sum` < 150000
ORDER BY total_sum DESC;

-- 08. Deposit Charge 
SELECT deposit_group, magic_wand_creator, MIN(deposit_charge) AS 'min_deposit_charge' FROM wizzard_deposits
GROUP BY deposit_group, magic_wand_creator
ORDER BY magic_wand_creator, deposit_group;

-- 09. Age Groups
SELECT 
CASE
WHEN age <= 10 THEN '[0-10]'
WHEN age <= 20 THEN '[11-20]'
WHEN age <= 30 THEN '[21-30]'
WHEN age <= 40 THEN '[31-40]'
WHEN age <= 50 THEN '[41-50]'
WHEN age <= 60 THEN '[51-60]'
ELSE '[61+]'
END AS 'age_group', COUNT(`age`) AS 'wizzard_count' FROM wizzard_deposits
GROUP BY `age_group`
ORDER BY `age_group`;

-- 10. First Letter
SELECT DISTINCT(SUBSTRING(first_name, 1, 1)) AS 'first_letter'FROM wizzard_deposits
WHERE deposit_group = 'Troll Chest'
ORDER BY `first_letter`;

-- 11. Average Interest 
SELECT deposit_group, is_deposit_expired, AVG(deposit_interest) AS 'average_interest' FROM wizzard_deposits
WHERE deposit_start_date > '1985-01-01'
GROUP BY deposit_group, is_deposit_expired
ORDER BY deposit_group DESC, is_deposit_expired ASC;

-- 12. Employees Minimum Salaries
SELECT department_id, MIN(salary) FROM employees
WHERE DATE(hire_date) > '2000-01-01'
GROUP BY department_id
HAVING department_id IN (2, 5, 7)
ORDER BY department_id ASC;

-- 13. Employees Average Salaries 
CREATE TABLE `high_paid_employees_over_30000` AS
SELECT * FROM employees
WHERE salary > 30000;

DELETE FROM `high_paid_employees_over_30000`
WHERE manager_id  = 42;

UPDATE `high_paid_employees_over_30000`
SET salary = salary + 5000
WHERE department_id = 1;

SELECT department_id, AVG(salary) AS 'avg_salary' FROM `high_paid_employees_over_30000`
GROUP BY department_id
ORDER BY department_id ASC;

-- 14. Employees Maximum Salaries 
SELECT department_id, MAX(salary) AS 'max_salary' FROM employees
GROUP BY department_id
HAVING `max_salary` < 30000 OR `max_salary` > 70000
ORDER BY department_id ASC; 

-- 15. Employees Count Salaries 
SELECT COUNT(employee_id) AS 'count' FROM employees
WHERE manager_id IS NULL; 

-- 16. 3rd Highest Salary
SELECT DISTINCT department_id, (
    SELECT DISTINCT salary FROM employees AS e1
    WHERE e1.department_id = employees.department_id
    ORDER BY salary DESC
    LIMIT 1 OFFSET 2
    ) AS 'third_highest_salary'
FROM employees
HAVING `third_highest_salary` IS NOT NULL
ORDER BY department_id ASC;

-- 17. Salary Challenge 
SELECT first_name, last_name, department_id FROM employees AS e1
WHERE salary > (
	SELECT AVG(salary) FROM employees AS e2
    WHERE e1.department_id = e2.department_id
)
ORDER BY department_id, employee_id
LIMIT 10;

-- 18. Departments Total Salaries
SELECT department_id, SUM(salary) AS 'total_SUM' FROM employees
GROUP BY department_id
ORDER BY department_id;