CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(50)
);

ALTER TABLE employees
ADD COLUMN department_id INT,
ADD FOREIGN KEY (department_id) REFERENCES departments(department_id);
