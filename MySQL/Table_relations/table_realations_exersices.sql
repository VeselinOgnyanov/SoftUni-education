-- LAB
-- 1. Mountains and Peaks 
CREATE TABLE `mountains`(
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
`name` VARCHAR(50) NOT NULL
);

CREATE TABLE `peaks`(
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
`name` VARCHAR(50),
`mountain_id` INT NOT NULL, 
CONSTRAINT fk_peaks_moutains_mountains_id
FOREIGN KEY (mountain_id)
REFERENCES mountains(id)
);

-- 2. Trip Organization 
SELECT driver_id, vehicle_type, CONCAT(first_name, ' ', last_name) AS 'driver_name' FROM vehicles AS v
JOIN campers AS c
ON v.driver_id = c.id;

-- 3. SoftUni Hiking 
SELECT starting_point AS 'route_starting_point', end_point AS 'route_ending_point',
c.id, CONCAT(c.first_name, ' ', c.last_name) FROM routes AS r
JOIN campers AS c
ON r.leader_id = c.id;

-- 4. Delete Mountains 
CREATE TABLE `mountains`(
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
`name` VARCHAR(50) NOT NULL
);

CREATE TABLE `peaks`(
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
`name` VARCHAR(50),
`mountain_id` INT NOT NULL,
CONSTRAINT fk_mountains_id_peaks
FOREIGN KEY (mountain_id)
REFERENCES mountains(id)
ON DELETE CASCADE
);

-- Exercise
-- 01. One-To-One Relationship 
CREATE DATABASE table_relations;
USE table_relations;

drop table people;
drop table passports;

CREATE TABLE `people`(
person_id INT UNIQUE NOT NULL AUTO_INCREMENT,
first_name VARCHAR(50) NOT NULL,
salary DECIMAL(10, 2) NOT NULL,
passport_id INT UNIQUE
);

CREATE TABLE `passports`(
passport_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
passport_number VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO people(first_name, salary, passport_id)
VALUES
('Roberto', 43300.00, 102),
('Tom', 56100.00, 103),
('Yana', 60200.00, 101);

INSERT INTO passports(passport_id, passport_number)
VALUES
(101, 'N34FG21B'),
(102, 'K65LO4R7'),
(103, 'ZE657QP2');

ALTER TABLE `people`
ADD CONSTRAINT pk_people
PRIMARY KEY (person_id),
ADD CONSTRAINT fk_people_passports
FOREIGN KEY (passport_id)
REFERENCES passports(passport_id);

-- 02. One-To-Many Relationship 
CREATE TABLE `manufacturers`(
manufacturer_id INT AUTO_INCREMENT PRIMARY KEY,
`name` VARCHAR(30),
established_on DATE
);

CREATE TABLE `models`(
model_id INT AUTO_INCREMENT PRIMARY KEY,
`name` VARCHAR(30),
manufacturer_id INT,
FOREIGN KEY (manufacturer_id) REFERENCES `manufacturers`(manufacturer_id)
)AUTO_INCREMENT = 101;

INSERT INTO manufacturers(`name`, established_on)
VALUES
('BMW', '1916-03-01'),
('Tesla', '2003-01-01'),
('Lada', '1966-05-01');

INSERT INTO models(`name`, manufacturer_id)
VALUES
('X1', 1),
('i6', 1),
('Model S', 2), 
('Model X', 2), 
('Model 3', 2), 
('Nova', 3);

-- 03. Many-To-Many Relationship
CREATE TABLE `students`(
student_id INT AUTO_INCREMENT PRIMARY KEY,
`name` VARCHAR(30)
);

CREATE TABLE `exams`(
exam_id INT AUTO_INCREMENT PRIMARY KEY,
`name` VARCHAR(30)
)AUTO_INCREMENT = 101;

CREATE TABLE `students_exams`(
student_id INT,
exam_id INT,
CONSTRAINT pk_student_id_exam_id
PRIMARY KEY (student_id, exam_id),
CONSTRAINT fk_student_id_students
FOREIGN KEY (student_id)
REFERENCES `students`(student_id),
CONSTRAINT fk_exam_id_exams
FOREIGN KEY (exam_id)
REFERENCES `exams`(exam_id)
);

INSERT INTO `students`(`name`)
VALUES
('Mila'),
('Toni'),
('Ron');

INSERT INTO `exams`(`name`)
VALUES
('Spring MVC'),
('Neo4j'),
('Oracle 11g');

INSERT INTO `students_exams`(`student_id`, `exam_id`)
VALUES
(1, 101),
(1, 102),
(2, 101),
(3, 103),
(2, 102),
(2, 103);

-- 04. Self-Referencing 
CREATE TABLE `teachers`(
teacher_id INT NOT NULL UNIQUE AUTO_INCREMENT, 
`name` VARCHAR(30), 
manager_id INT NULL
)AUTO_INCREMENT = 101;

INSERT INTO `teachers`(`name`, manager_id)
VALUES
('John', NULL),
('Maya', 106),
('Silvia', 106),
('Ted', 105),
('Mark', 101),
('Greta', 101);

ALTER TABLE `teachers`
ADD CONSTRAINT pk_teacher_id
PRIMARY KEY (teacher_id),
ADD CONSTRAINT fk_manager_teacher
FOREIGN KEY (manager_id)
REFERENCES `teachers`(teacher_id);

-- 05. Online Store Database 
CREATE TABLE `cities`(
city_id INT PRIMARY KEY AUTO_INCREMENT,
`name` VARCHAR(50)
);

CREATE TABLE `customers`(
customer_id INT PRIMARY KEY AUTO_INCREMENT,
`name` VARCHAR(50),
birthday DATE,
city_id INT,
CONSTRAINT fk_customers_cities
FOREIGN KEY(city_id)
REFERENCES `cities`(city_id)
);

CREATE TABLE `orders`(
order_id INT PRIMARY KEY AUTO_INCREMENT,
customer_id INT,
CONSTRAINT fk_oreders_customers
FOREIGN KEY(customer_id)
REFERENCES `customers`(customer_id)
);

CREATE TABLE `item_types`(
item_type_id INT PRIMARY KEY AUTO_INCREMENT,
`name` VARCHAR(50)
);

CREATE TABLE `items`(
item_id INT PRIMARY KEY AUTO_INCREMENT,
`name` VARCHAR(50),
item_type_id INT,
CONSTRAINT fk_items_item_types
FOREIGN KEY(item_type_id)
REFERENCES `item_types`(item_type_id)
);

CREATE TABLE `order_items`(
order_id INT,
item_id INT,
CONSTRAINT pk_order_items
PRIMARY KEY(order_id, item_id),
CONSTRAINT fk_order_items_items
FOREIGN KEY (item_id)
REFERENCES `items`(item_id),
CONSTRAINT fk_order_items_orders
FOREIGN KEY (order_id)
REFERENCES `orders`(order_id) 
);

-- 06. University Database 
CREATE TABLE `subjects`(
subject_id INT(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
subject_name VARCHAR(50)
);

CREATE TABLE `majors`(
major_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
`name` VARCHAR(50)
);

CREATE TABLE `students`(
student_id INT(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
student_number VARCHAR(12),
student_name VARCHAR(50),
major_id INT(11),
CONSTRAINT fk_students_majors
FOREIGN KEY(major_id)
REFERENCES `majors`(major_id)
);

CREATE TABLE `payments`(
payment_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
payment_date DATE,
payment_amount DECIMAL(8, 2),
student_id INT(11),
CONSTRAINT fk_payments_students
FOREIGN KEY (student_id)
REFERENCES `students`(student_id) 
);

CREATE TABLE `agenda`(
student_id INT(11),
subject_id INT(11),
CONSTRAINT pk_agenda
PRIMARY KEY (student_id, subject_id),
CONSTRAINT fk_agenda_subjects
FOREIGN KEY (subject_id)
REFERENCES `subjects`(subject_id),
CONSTRAINT fk_agenda_students
FOREIGN KEY (student_id)
REFERENCES `students`(student_id) 
);

-- 09. Peaks in Rila 
SELECT m.mountain_range, p.peak_name, p.elevation as 'peak_elevation' FROM peaks AS p
JOIN mountains AS m ON p.mountain_id = m.id
WHERE mountain_range = 'Rila'
ORDER BY `peak_elevation` DESC;


