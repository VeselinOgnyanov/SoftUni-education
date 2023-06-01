-- LAB
-- 01. Find Book Titles
SELECT `title` FROM `books`
WHERE substring(`title`, 1, 3) = 'The'
ORDER BY `id`;

-- 02. Replace Titles
SELECT replace(`title`, 'The', '***') FROM `books`
WHERE substring(`title`, 1, 3) = 'The'
ORDER BY `id`;

-- 03. Sum Cost of All Books 
SELECT round(sum(`cost`), 2) FROM `books`;

-- 04. Days Lived 
SELECT concat_ws(' ', `first_name`, `last_name`) AS `Full name`,
TIMESTAMPDIFF(DAY, `born`, `died`) AS `Days lived`
FROM `authors`;

-- 05. Harry Potter Books 
SELECT `title` FROM `books`
WHERE substring(`title`, 1, 5) = 'Harry'
ORDER BY `id`;

-- Exercise
-- 01. Find Names of All Employees by First Name
SELECT `first_name`, `last_name` FROM `employees`
WHERE SUBSTRING(`first_name`, 1, 2) = 'sa'
ORDER BY `employee_id`;

-- 02. Find Names of All Employees by Last Name 
SELECT `first_name`, `last_name` FROM `employees`
WHERE `last_name` LIKE '%ei%'
ORDER BY `employee_id`;

-- 03. Find First Names of All Employess
SELECT `first_name` FROM `employees`
WHERE `department_id` IN (3, 10)
-- AND (YEAR(`hire_date`) >= 1995 AND YEAR(`hire_date`) <= 2005)
AND YEAR(`hire_date`) BETWEEN 1995 AND 2005
ORDER BY `employee_id`;

-- 04. Find All Employees Except Engineers 
SELECT `first_name`, `last_name` FROM `employees`
WHERE `job_title` NOT LIKE '%engineer%'
-- WHERE `job_title` != 'engineer'
ORDER BY `employee_id`;

-- 05. Find Towns with Name Length
SELECT `name` FROM `towns`
WHERE  length(`name`) BETWEEN 5 and 6
ORDER BY `name`;

-- 06. Find Towns Starting With 
SELECT `town_id`, `name` FROM `towns`
WHERE `name` LIKE 'm%'
OR `name` LIKE 'k%'
OR `name` LIKE 'b%'
OR `name` LIKE 'e%'
ORDER BY `name`;

-- 07. Find Towns Not Starting With
SELECT `town_id`, `name` FROM `towns`
WHERE `name` NOT LIKE 'r%'
AND `name` NOT LIKE 'b%'
AND `name` NOT LIKE 'd%'
ORDER BY `name`;

-- 08. Create View Employees Hired After 
CREATE VIEW `v_employees_hired_after_2000` AS
SELECT `first_name`, `last_name` FROM `employees`
WHERE YEAR(`hire_date`) > 2000;

SELECT * FROM `v_employees_hired_after_2000`;

-- 09. Length of Last Name 
SELECT `first_name`, `last_name` FROM `employees`
WHERE length(`last_name`) = 5;

-- 10. Countries Holding 'A' 
SELECT `country_name`, `iso_code` FROM `countries`
WHERE `country_name` LIKE '%a%a%a%'
ORDER BY `iso_code`;

-- 11. Mix of Peak and River Names 
SELECT 
    `p`.`peak_name`,
    `r`.`river_name`,
    LOWER(CONCAT((`peak_name`), RIGHT(`river_name`, LENGTH(`river_name`) - 1))) AS 'mix'
FROM
    `peaks` AS `p`,
    `rivers` AS `r`
WHERE
    LOWER(RIGHT(`peak_name`, 1) = LEFT(`river_name`, 1))
ORDER BY `mix`;

-- 12. Games From 2011 and 2012 Year 
SELECT `name`,
DATE_FORMAT(`start`, '%Y-%m-%d') AS `start`
FROM `games`
WHERE YEAR(`start`) IN (2011, 2012)
ORDER BY `start`, `name`
LIMIT 50;

-- 13. User Email Providers
SELECT `user_name`, 
SUBSTRING_INDEX(`email`, "@", -1) AS `email provider`
FROM `users`
ORDER BY `email provider`, `user_name`;

-- 14. Get Users with IP Address Like Pattern 
SELECT `user_name`, `ip_address` FROM `users`
WHERE `ip_address` LIKE '___.1%.%.___'
ORDER BY `user_name`;

-- 15. Show All Games with Duration
SELECT `name` AS `game`,
CASE
	WHEN (HOUR(`start`) >= 0 and HOUR(`start`) < 12) THEN 'Morning'
	WHEN (HOUR(`start`) >= 12 and HOUR(`start`) < 18) THEN 'Afternoon'
	WHEN (HOUR(`start`) >= 18 and HOUR(`start`) < 24) THEN 'Evening'
END AS `Part of the day`,
CASE
	WHEN(`duration` <= 3) THEN 'Extra Short'
    WHEN(`duration` <= 6) THEN 'Short'
    WHEN(`duration` <= 10) THEN 'Long'
    ELSE('Extra Long')
END AS `Duration`
FROM `games`;

-- 16. Orders Table
SELECT `product_name`, `order_date`,
DATE_ADD(`order_date`, INTERVAL 3 DAY) as `pay_due`,
DATE_ADD(`order_date`, INTERVAL 1 MONTH) as `deliver_due`
FROM `orders`;




