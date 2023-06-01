-- LAB
-- 1. Departments Info

SELECT `id`, `first_name`,
`last_name`, `department_id`, MAX(`salary`) AS 'max_salary' FROM `employees`
GROUP BY `department_id`;

