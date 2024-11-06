SELECT e.firstname, e.salary, d.departmentname
FROM employee AS e
INNER JOIN department AS d
ON e.Department_id = d.Department_Id;


