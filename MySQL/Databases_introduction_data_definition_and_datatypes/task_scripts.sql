-- LAB tasks

create database `gamebar`;
use `gamebar`;

-- 01. Create Tables
CREATE TABLE `employees` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `first_name` VARCHAR(36) NOT NULL,
    `last_name` VARCHAR(36) NOT NULL
);

CREATE TABLE `categories` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(36) NOT NULL
);

CREATE TABLE `products` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(36) NOT NULL,
    `category_id` INT NOT NULL
);

-- 02. Insert Data in Tables
INSERT INTO employees(first_name, last_name)
VALUES 
('test', 'test'),
('test', 'test'),
('test', 'test');

-- 03. Alter Tables
ALTER TABLE `employees`
ADD COLUMN `middle_name` VARCHAR(36) AFTER `first_name`;

-- 04. Adding Constraints 
ALTER TABLE `products`
ADD CONSTRAINT `fk_products_categeries`
FOREIGN KEY products(category_id)
REFERENCES categories(id);

-- 5. Modifying Columns
ALTER TABLE `employees`
CHANGE COLUMN `middle_name` `middle_name` VARCHAR(100);


-- Exercise tasks
	CREATE DATABASE `minions`;
    USE `minions`;
    
-- 01. Create Tables
CREATE TABLE `minions` (
    `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(30) NOT NULL,
    `age` INT NOT NULL
);

CREATE TABLE `towns` (
    `town_id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(30) NOT NULL
);

-- 02. Alter Minions Table
ALTER TABLE `minions`
ADD COLUMN `town_id` INT;

ALTER TABLE `minions`
ADD CONSTRAINT `fk_minions_towns`
FOREIGN KEY minions(town_id)
REFERENCES towns(id);

-- 03. Insert Records in Both Tables
INSERT INTO towns(`name`)
VALUES 
('Sofia'),
('Plovdiv'),
('Varna');

INSERT INTO minions(`name`, `age`, `town_id`)
VALUES 
('Kevin', 22, 1),
('Bob', 15, 3),
('Steward', null, 2);

-- 04. Truncate Table Minions
TRUNCATE TABLE minions;

-- 05. Drop All Tables
DROP TABLE `minions`;
DROP TABLE `towns`;

-- 06. Create Table People
CREATE TABLE `people` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(200) NOT NULL,
    `picture` BLOB,
    `height` DOUBLE(10 , 2 ),
    `weight` DOUBLE(10 , 2 ),
    `gender` CHAR(1) NOT NULL,
    `birthdate` DATE NOT NULL,
    `biography` TEXT
);

INSERT INTO `people`(`name`, `gender`, `birthdate`)
VALUES
('test', 'm', DATE(NOW())),
('test', 'm', DATE(NOW())),
('test', 'm', DATE(NOW())),
('test', 'm', DATE(NOW())),
('test', 'm', DATE(NOW()));

-- 07. Create Table Users
CREATE TABLE `users` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `username` VARCHAR(30) NOT NULL,
    `password` VARCHAR(26) NOT NULL,
    `profile_picture` BLOB,
    `last_login_time` DATETIME,
    `is_deleted` BOOLEAN
);

INSERT INTO `users`(`username`, `password`)
VALUES
('test', 'test'),
('test', 'test'),
('test', 'test'),
('test', 'test'),
('test', 'test');

-- 08. Change Primary Key 
ALTER TABLE users
DROP PRIMARY KEY,
ADD CONSTRAINT pk_users
PRIMARY KEY users(id, username);  

-- 09. Set Default Value of a Field
ALTER TABLE `users`
CHANGE COLUMN `last_login_time`
`last_login_time` DATETIME DEFAULT NOW();

-- 10. Set Unique Field 
ALTER TABLE `users`
DROP Primary KEY,
ADD CONSTRAINT pk_id
PRIMARY KEY users(id),
CHANGE COLUMN `username`
`username` VARCHAR(30) UNIQUE;

-- 11. Movies Database 
CREATE DATABASE `movies`;
USE `movies`;

CREATE TABLE `directors` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `director_name` VARCHAR(50) NOT NULL,
    `notes` TEXT
); 

INSERT INTO `directors`(`director_name`, `notes`)
VALUES 
('TestName1', 'TestNotes'),
('TestName2', 'TestNotes'),
('TestName3', 'TestNotes'),
('TestName4', 'TestNotes'),
('TestName5', 'TestNotes');

CREATE TABLE `genres` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `genre_name` VARCHAR(20) NOT NULL,
    `notes` TEXT
);

INSERT INTO `genres`(`genre_name`, `notes`)
VALUES 
('TestName1', 'TestNotes'),
('TestName2', 'TestNotes'),
('TestName3', 'TestNotes'),
('TestName4', 'TestNotes'),
('TestName5', 'TestNotes');

CREATE TABLE `categories` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `category_name` VARCHAR(20) NOT NULL,
    `notes` TEXT
);

INSERT INTO `categories`(`category_name`, `notes`)
VALUES 
('TestName1', 'TestNotes'),
('TestName2', 'TestNotes'),
('TestName3', 'TestNotes'),
('TestName4', 'TestNotes'),
('TestName5', 'TestNotes');

CREATE TABLE `movies` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `title` VARCHAR(40) NOT NULL,
    `director_id` INT,
    `copyright_year` INT,
    `length` INT,
    `genre_id` INT,
    `category_id` INT,
    `rating` DOUBLE,
    `notes` TEXT
);

INSERT INTO `movies` (`title`)
VALUES 
('TestMovie1'),
('TestMovie2'),
('TestMovie3'),
('TestMovie4'),
('TestMovie5');

-- 12. Car Rental Database
 CREATE database `car_rental`;
 USE car_rental;
 
CREATE TABLE `categories` (
    `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    `category` VARCHAR(20),
    `daily_rate` DOUBLE(5 , 2 ),
    `weekly_rate` DOUBLE(5 , 2 ),
    `monthly_rate` DOUBLE(5 , 2 ),
    `weekend_rate` DOUBLE(5 , 2 )
);
 
 INSERT INTO `categories` (`category`)
 VALUES
 ('test'),
 ('test'),
 ('test');
 
CREATE TABLE `cars` (
    `id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    `plate_number` INT(10),
    `make` VARCHAR(20),
    `model` VARCHAR(20),
    `car_year` YEAR,
    `category_id` INT NOT NULL,
    `doors` INT(1),
    `picture` BLOB,
    `car_condition` VARCHAR(10),
    `available` BOOLEAN
);
 
INSERT INTO `cars` (`model`)
VALUES
('test'),
('test'),
('test');
 
CREATE TABLE `employees` (
    `id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    `first_name` VARCHAR(20),
    `last_name` VARCHAR(20),
    `title` VARCHAR(20),
    `notes` TEXT
);
 
INSERT INTO `employees` (`first_name`)
VALUES
('test'),
('test'),
('test');
 
CREATE TABLE `customers` (
    `id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    `driver_licence_number` VARCHAR(20),
    `full_name` VARCHAR(20),
    `address` VARCHAR(20),
    `city` VARCHAR(20),
    `zip_code` INT(5),
    `notes` TEXT
);
 
INSERT INTO `customers` (`full_name`)
VALUES
('test'),
('test'),
('test');
 
CREATE TABLE `rental_orders` (
    `id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    `employee_id` INT,
    `customer_id` INT,
    `car_id` INT,
    `car_condition` BOOL,
    `tank_level` INT,
    `kilometrage_start` INT,
    `kilometrage_end` INT,
    `total_kilometrage` INT,
    `start_date` DATE,
    `end_date` DATE,
    `total_days` INT,
    `rate_applied` INT,
    `tax_rate` INT,
    `order_status` VARCHAR(20),
    `notes` TEXT
);
 
INSERT INTO `rental_orders` (`employee_id`, `customer_id`)
VALUES
(1, 2),
(2, 3),
(3, 1);

-- 13. Basic Insert
CREATE DATABASE `soft_uni`;
USE `soft_uni`;

CREATE TABLE `towns`(
`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
`name` VARCHAR(50)
);


CREATE TABLE addresses (
`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
`address_text` VARCHAR(50),
`town_id` INT
);


CREATE TABLE departments (
`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL, 
`name` VARCHAR(50)
);

CREATE TABLE `employees` (
`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
`first_name` VARCHAR(50), 
`middle_name` VARCHAR(50), 
`last_name` VARCHAR(50), 
`job_title` VARCHAR(50), 
`department_id` INT, 
`hire_date` DATE, 
`salary` INT, 
`address_id` INT
);

ALTER TABLE `employees`
ADD CONSTRAINT `fk_employees_department_id`
FOREIGN KEY `employees`(`department_id`)
REFERENCES `departments`(`id`);

ALTER TABLE `employees`
ADD CONSTRAINT `fk_employees_address_id`
FOREIGN KEY `employees`(`address_id`)
REFERENCES `addresses`(`id`);

INSERT INTO `towns`(`name`)
VALUES
('Sofia'),
('Plovdiv'),
('Varna'),
('Burgas'); 

INSERT INTO `departments`(`name`)
VALUES
('Engineering'),
('Sales'),
('Marketing'),
('Software Development'),
('Quality Assurance');

INSERT INTO `employees` (`first_name`, `middle_name`, `last_name`, `job_title`, `department_id`, `hire_date`,`salary`)
VALUES
('Ivan', 'Ivanov', 'Ivanov', '.NET Developer', 4, '2013-02-01', 3500.00),
('Petar', 'Petrov', 'Petrov', 'Senior Engineer', 1, '2004-03-02', 4000.00),
('Maria', 'Petrova', 'Ivanova', 'Intern', 5, '2016-08-28', 525.25),
('Georgi', 'Terziev', 'Ivanov', 'CEO', 2, '2007-12-09', 3000.00),
('Peter', 'Pan', 'Pan', 'Intern', 3, '2016-08-28', 599.88);

-- 14. Basic Select All Fields
SELECT * FROM `towns`;
SELECT * FROM `departments`;
SELECT * FROM `employees`;

-- 15. Basic Select All Fields and Order Them
SELECT * FROM `towns`
ORDER BY `name`;
SELECT * FROM `departments`
ORDER BY `name`;
SELECT * FROM `employees`
ORDER BY `salary` DESC;

-- 16. Basic Select Some Fields 
SELECT `name` FROM `towns`
ORDER BY `name`;
SELECT `name` FROM `departments`
ORDER BY `name`;
SELECT `first_name`, `last_name`, `job_title`, `salary` FROM `employees`
ORDER BY `salary` DESC;

-- 17. Increase Employees Salary
UPDATE `employees`
SET `salary` = `salary` * 1.1;
SELECT `salary` FROM `employees`;