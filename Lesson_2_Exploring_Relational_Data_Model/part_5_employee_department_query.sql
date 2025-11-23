SELECT employees.name, departments.department_name, employees.salary
FROM employees
JOIN departments ON employees.department_id = departments.department_id;
