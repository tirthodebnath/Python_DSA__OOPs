select * from employee_salary

--1. Find the second highest salary among all employees.
SELECT MAX(salary) AS second_highest_salary FROM employees WHERE salary < (SELECT MAX(salary) FROM employees);

--2. Retrieve the department-wise average salary, but only show departments where the average salary is greater than 80,000.
select department,AVG(salary) as avg_sal from employee_salary group by department having AVG(salary) > 80000

--3. List all employees who joined before 2020 and have a designation that contains the word "Manager".
select name, designation, joining_date from employee_salary where joining_date < '2020-01-01' and designation like '%manager%'

--4. Find the highest paid employee in each department.
select name, department, salary from (select *, ROW_NUMBER() over(partition by department order by salary desc) as rank_no
from employee_salary) as t where rank_no = 1

--5. Count the number of employees in each designation, but only display designations that have more than 1 employee.
select count(emp_id), designation from employee_salary group by designation having count(emp_id) > 1

