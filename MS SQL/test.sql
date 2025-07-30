SELECT * 
FROM employee
GROUP BY employee_id, name, department, salary
HAVING COUNT(*) > 1;
