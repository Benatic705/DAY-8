CREATE DATABASE employee_db;
USE employee_db;
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2)
);

INSERT INTO employees (name, department, salary)
VALUES
('Rithan','IT',30000),
('John','HR',25000),
('Sara','Finance',35000);

SELECT * FROM employees;