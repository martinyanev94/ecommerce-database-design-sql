SELECT departments.department_name, AVG(employees.salary) AS average_salary
FROM employees
JOIN departments ON employees.department_id = departments.department_id
GROUP BY departments.department_name;
