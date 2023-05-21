-- LAB tasks

create database `gamebar`;
use `gamebar`;

-- 01. Create Tables
CREATE TABLE `employees` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `first_name` varchar(36) not null,
    `last_name` varchar(36) not null
);

CREATE TABLE `categories`(
	`id` INT primary key AUTO_INCREMENT,
    `name` VARCHAR(36) NOT NULL
);

CREATE TABLE `products`(
	`id` INT primary key AUTO_INCREMENT,
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
CREATE TABLE `minions`(
`id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
`name` VARCHAR(30) NOT NULL,
`age` INT NOT NULL
);

CREATE TABLE `towns`(
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
CREATE TABLE `people`(
`id` INT PRIMARY KEY AUTO_INCREMENT,
`name` VARCHAR(200) NOT NULL,
`picture` BLOB,
`height` DOUBLE (10, 2),
`weight` DOUBLE (10, 2),
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
CREATE TABLE `users`(
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

CREATE TABLE `directors`(
`id` INT PRIMARY KEY AUTO_INCREMENT,
`director_name` VARCHAR(50) NOT NULL,
`notes` TEXT
); 

INSERT INTO `directors`(`director_name`)
VALUES
('test'),
('test'),
('test'),
('test'),
('test');

CREATE TABLE `genres`(
`id` INT PRIMARY KEY AUTO_INCREMENT,
`genre_name` VARCHAR(50) NOT NULL,
`notes` TEXT
);
INSERT INTO `genres`(`genre_name`)
VALUES
('test'),
('test'),
('test'),
('test'),
('test');

CREATE TABLE `categories`(
`id` INT PRIMARY KEY AUTO_INCREMENT,
`category_name` VARCHAR(50) NOT NULL,
`notes` TEXT
);
INSERT INTO `categories`(`category_name`)
VALUES
('test'),
('test'),
('test'),
('test'),
('test');

CREATE TABLE `movies`(
`id` INT PRIMARY KEY AUTO_INCREMENT,
`title` VARCHAR(50) NOT NULL,
`director_id` INT,
`copyright_year` YEAR,
`length` DOUBLE (10,2),
`genre_id` INT,
`category_id` INT,
`rating` DOUBLE (10, 2),
`notes` TEXT,
FOREIGN KEY fk_movies_directors (`director_id`)
REFERENCES directors(`id`),
FOREIGN KEY fk_movies_genre (genre_id)
REFERENCES genres(`id`),
FOREIGN KEY fk_movies_categories (category_id)
REFERENCES categories(`id`)
);

INSERT INTO `movies` (`title`, `director_id`, `genre_id`, `category_id`)
VALUES
('test', 1, 2, 3),
('test', 1, 2, 3),
('test', 1, 2, 3),
('test', 1, 2, 3),
('test', 1, 2, 3);

-- 