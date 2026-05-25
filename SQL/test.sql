/* Q-1. Write an SQL query to fetch “FIRST_NAME” from Worker table using the alias name as <WORKER_NAME>. */
SELECT first_name as worker_name FROM Worker


/* Q-2. Write an SQL query to fetch “FIRST_NAME” from Worker table in upper case. */

select upper (first_name) from Worker


/* Q-3. Write an SQL query to fetch unique values of DEPARTMENT from Worker table. */

SELECT UNIQUE(department) from Worker


/* Q-4. Write an SQL query to print the first three characters of  FIRST_NAME from Worker table. */

select substring(first_name,1,3) from worker


/* Q-5. Write an SQL query to find the position of the alphabet (‘a’) in the first name column ‘Amitabh’ from Worker table.*/

Select INSTR(FIRST_NAME, BINARY'a') from Worker where FIRST_NAME = 'Amitabh';

/*Q-6. Write an SQL query to print the FIRST_NAME from Worker table after removing white spaces from the right side.*/

Select RTRIM(FIRST_NAME) from Worker;

/* Q-8. Write an SQL query that fetches the unique values of DEPARTMENT from Worker table and prints its length.*/

Select distinct length(DEPARTMENT) from Worker;

/* Q-9. Write an SQL query to print the FIRST_NAME from Worker table after replacing ‘a’ with ‘A’.*/

SELECT REPLACE(first_name,"a","A") FROM worker

/* Q-10. Write an SQL query to print the FIRST_NAME and LAST_NAME from Worker table into a single column COMPLETE_NAME. 
A space char should separate them.*/

SELECT concat('first_name',' ','LAST_NAME') as 'completeName' from worker;

/* Q-11. Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME Ascending.*/

select * from worker ORDER BY first_name ASC;

/* Q-12. Write an SQL query to print all Worker details from the Worker table 
order by FIRST_NAME Ascending and DEPARTMENT Descending.*/

SELECT * from worker  ORDER BY first_name asc, department DESC;


/* Q-13. Write an SQL query to print details for Workers with the first name as “Vipul” and “Satish” from Worker table.*/

select * from worker where first_name in("vipul","satish");

/* Q-14. Write an SQL query to print details of workers excluding first names, “Vipul” and “Satish” from Worker table.*/

Select * from Worker where FIRST_NAME not in ('Vipul','Satish');

/* Q-15. Write an SQL query to print details of Workers with DEPARTMENT name as “Admin”.*/

select * from worker where department like "Admin%"

/*Q-16. From the following table, write a SQL query to find the cheapest item(s). Return pro_name and, pro_price*/

SELECT pro_name, pro_price FROM item_mast WHERE pro_price = (SELECT MIN(pro_price) FROM item_mast);


/* Write an SQL query to print details of the Workers whose FIRST_NAME contains ‘a’*/

Select * from Worker where FIRST_NAME like '%a%'


/*Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘h’ and contains six alphabets.*/

Select * from Worker where FIRST_NAME like '_____h';


/*Q-17. From the following table, write a SQL query to calculate average price of the items for each company. Return average price and company code.*/


/*Select first 3 letters from the firstname column*/

select substring(first_name,1,3) from customers 

SELECT AVG(pro_price), pro_com FROM item_mast GROUP BY pro_com;

/*Q-18. Write an SQL query to report all the duplicate emails. Return the result table in any order.*/

select distinct p1.Email

from Person p1, Person p2

where p1.Id <> p2.Id and p1.Email = p2.Email


/*Inner join using asc*/

select first_name , item , amount 
from customers 
outer join orders 
on customers.customer_id = orders.customer_id 
order by amount asc


/*Suppose that a website contains two tables, the Customers table and the Orders table. 
Write a SQL query to find all customers who never order anything.*/

select name Customers from Customers
where id not in (select distinct(customerID) from Orders)

/************OR**********************/

select
    Name as Customers
from
    Customers
where
    Id
not in(
    select CustomerId from Orders
);


/*delete all the duplicate emails,
keeping only one unique email with the smallest id. Note that you are supposed to write a DELETE statement and not a SELECT one.*/

Delete p1
from Person p1, Person p2
where p1.Email = p2.Email and p1.Id > p2.Id


/*Find Duplicate element in sql 1st medthos*/

select country, count(country) as Dup_No
from customers 
group by country
having count(*) > 1

/*---OR----*/

select distinct p1.Email
from Person p1, Person p2
where p1.Id <> p2.Id and p1.Email = p2.Email

/*3rd Highest salary*/

select age 
from customers
order by age desc 
limit 1 offset 2


/*3rd Highest salary using window function*/

SELECT salary
FROM (
  SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rank
  FROM employees
) AS ranked_employees
WHERE rank = 3;

-- OR

/*3rd Highest salary using window function*/
select s.Salary
  from employee s                                                
  where 3=(select count(distinct(salary))
            from employee r
            where r.Salary>=s.Salary)

/*
-----OR---  Using JOIN*/
SELECT *
FROM (
    SELECT e.*,
           DENSE_RANK() OVER (PARTITION BY d.Department_Id ORDER BY e.Salary DESC) AS Rank
    FROM Employee AS e
    LEFT JOIN Department AS d ON e.Department_Id = d.Department_Id
) AS new_tbl
WHERE Rank = 3;


/*Sum of no of rows in a table*/
select sum(amount) from(select * from orders order by amount asc limit 1, 6) as amount_new 


/*Partition By country*/

SELECT first_Name, Age, country, COUNT(*) OVER (PARTITION BY country) AS count_by_country
FROM customers;


/*Case Statement*/

SELECT First_Name, Last_Name, Age,
CASE
WHEN Age > 30 THEN 'Old'
WHEN Age BETWEEN 27 AND 30 THEN 'Young'
ELSE 'Baby'
END
from customers


/*Q2 - Find All employees who earn more than their managers*/

select CONCAT(e.FName,'',e.LName)as Name, e.Salary
from Employees as e
join Employees as m on m.ManagerId = e.Id
where e.Salary > m.Salary


/*How to Delete Duplicate Rows student_name in SQL from student table */

DELETE FROM students
WHERE student_id NOT IN 
(
    SELECT MIN(student_id)
    FROM students
    GROUP BY student_name
);


/* Write an SQL query to print the FIRST_NAME from the Worker table after removing white spaces from the right/left side.*/

Select RTRIM(FIRST_NAME) from Worker;  --For Right

Select LTRIM(FIRST_NAME) from Worker;  --For Left


/*Write an SQL query that fetches the unique values of DEPARTMENT from the Worker table and prints its length.*/

select distinct length(department) from worker 


/*Write an SQL query to print details of the Workers who joined in Feb’2014.*/

Select * from Worker where year(JOINING_DATE) = 2014 and month(JOINING_DATE) = 2;


/*Write an SQL query to print details of the Workers who are also Managers.*/

select w.first_name,t.worker_title from worker as w 
inner join title as t on w.worker_id = t.worker_ref_id
where t.worker_title = "manager"


/*Write an SQL query to show only odd rows from a table.*/

SELECT * FROM Worker WHERE MOD (WORKER_ID, 2) <> 0;


/*Write an SQL query to fetch the names of workers who earn the highest salary.*/

select department, sum(salary) from worker
group by department


/*Write an SQL query to print the name of employees having the highest salary in each department.*/

SELECT Department, first_Name, Salary
FROM worker
WHERE (Department, Salary) IN (
  SELECT Department, MAX(Salary)
  FROM worker
  GROUP BY Department
);


/*Write a query to retrieve two minimum and maximum salaries from the EmployeePosition table.*/

SELECT *
FROM (
    SELECT bonus_amount
    FROM bonus
    ORDER BY bonus_amount ASC
    LIMIT 2
) AS min_salaries
UNION
SELECT *
FROM (
    SELECT bonus_amount
    FROM bonus
    ORDER BY bonus_amount DESC
    LIMIT 2
) AS max_salaries;


/*Customers Who Never Order*/

select name Customers from Customers
where id not in (select distinct(customerID) from Orders)



/*Employees Earning More Than Their Managers*/

select e1.name as employee
from Employee e1, Employee e2
where e1.managerID = e2.id 
and e1.salary> e2.salary

OR

select e1.name as Employee from employee as e1
join Employee e2
on e1.managerId = e2.id 
where e1.salary > e2.salary


/*Write an SQL query to report the name and bonus amount of each employee with a bonus less than 1000*/

select e1.name, e2.bonus from
Employee as e1
join Bonus e2
on e1.empId = e2.empId
where e2.bonus < 1000


OR

select
    a.name,
    b.bonus 
from
    employee a 
left outer join
    bonus b 
on (a.empid = b.empid)
where ifnull(bonus,-1) < 1000



/*Left Join (Write an SQL query that reports the product_name, year, and price for each sale_id in the Sales table.)*/

select product_name, year, price from Sales 
left join Product
on Sales.product_id = Product.product_id


/*Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.*/

select project_id , round(avg(experience_years), 2) as average_years
from project as p
left join employee as e
on p.employee_id = e.employee_id
group by project_id


/*Write an SQL query to find all the authors that viewed at least one of their own articles.*/

select author_id as id
from Views
where author_id = viewer_id
group by author_id
order by author_id asc


/*Creating CTE(Common TABLE Expression)*/

WITH CTE1 as (select concat(FName,' ',LName)as Full_Name from employees order by DepartmentId)
select * from CTE1  



/*SP(Store PROCEDURE) Example*/

CREATE DEFINER=`root`@`localhost` PROCEDURE `1st_procedure_employees`()
BEGIN
select * from employees;
END


/*Find for each date the number of different products sold and their names.

The sold products names for each date should be sorted lexicographically.

Return the result table ordered by sell_date.

The result format is in the following example.*/

select sell_date,
       count(distinct(product)) as num_sold,
       group_concat(distinct product order by product asc separator ',') as products

from activities
group by sell_date
order by sell_date


/*write a sql query to count of flights where destination and souse flight are not from same country*/

select count(*) from
(select f.source, c1.state src_state, f.destination, c2.state dst_state, f.flight from flights f
left join cities c1 on f.source = c1.city left join cities c2 on f.destination = c2.city) temp1 where src_state <> dst_state;

/*##############OR#####################################*/

SELECT Flight AS FlightCount
FROM flights f
JOIN cities as d_source ON f.source = d_source.city
JOIN cities as d_dest ON f.destination = d_dest.city
WHERE d_source.state <> d_dest.state;



/*there are two tables orders and customers, now write a sql query to show which gender ordered the most between two dates*/

SELECT c.gender, COUNT(*) AS order_count
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_date >= '2023-07-10' AND o.order_date <= '2023-07-15'
GROUP BY c.gender
ORDER BY order_count DESC;


/*Compareing the score of the students using windows lag*/

select *, lag(score) over(partition by dep_name order by student_id) as previous_record
from student_score


/*Compareing the score of the students using windows lead*/

select *, lead(score) over(partition by dep_name order by student_id) as next_record
from student_score


/*Department wise MAX salary using partition by*/

select d.Name as Department, e.FName as Employee, MAX(Salary) 
OVER (PARTITION BY d.Name ORDER BY Salary) AS Salary
FROM Employees as e JOIN Departments as d ON e.Id = d.Id

/*Department wise MAX salary using partition by and department wise ranking*/

select d.Name as Department, e.FName as Employee, Salary, Rank() OVER (PARTITION BY d.Name ORDER BY Salary ASC) AS Rankl
FROM Employees as e 
JOIN Departments as d ON e.DepartmentId = d.Id


/*How to CREATE index in sql*/

CREATE INDEX idx_employees_department ON employees (department);
 

 /*Question: Retrieve the top 5 highest paid employees for each department, sorted by salary in descending order.
 Using Join, Partition by and row_number*/

 SELECT name, salary
FROM (
    SELECT
        d.name,
        e.salary,
            DENSE_RANK() OVER(PARTITION BY d.Name ORDER BY e.salary DESC) AS rank
    FROM
        employees AS e
    LEFT JOIN
        departments AS d ON e.DepartmentId = d.Id
) AS RankedEmployees
WHERE rank <= 5;



/*Question: List the departments where the average salary is
higher than the company's overall average salary.*/

WITH DepartmentAvg AS ( 
    SELECT
        d.name AS department_name,
        AVG(e.salary) AS avg_salary
    FROM
        employees AS e
    LEFT JOIN
        departments AS d ON e.DepartmentId = d.Id
    GROUP BY
        d.name
)
SELECT
    department_name
FROM
    DepartmentAvg
WHERE
    avg_salary > (SELECT AVG(avg_salary) FROM DepartmentAvg);


/*Find all numbers that appear at least three times consecutively. Return the result table in any order. Using Lead & Lag*/

SELECT DISTINCT num as ConsecutiveNums
FROM (
    SELECT 
        num,
        LEAD(num, 1) OVER (ORDER BY id) AS next_num,
        LAG(num, 1) OVER (ORDER BY id) AS prev_num
    FROM Logs
) AS subquery
WHERE num = next_num AND num = prev_num;


/*Output=
Tirtho(M)
Archi(M)
Sahin(F)
*/

select concat(Firstname, '(', SUBSTRING(sex, 1,1),')') from employee


/*Multiple left joins */

select distribution_centers.*, tbl_5,* from bigquery-public-data.thelook_ecommerce.distribution_centers as distribution_centers left join (SELECT inventory_items.*, tbl_4.*
FROM bigquery-public-data.thelook_ecommerce.inventory_items AS inventory_items
LEFT JOIN (
    SELECT products.*, tbl_3.*
    FROM bigquery-public-data.thelook_ecommerce.products AS products
    LEFT JOIN (
        SELECT order_items.*, tbl_2.*
        FROM bigquery-public-data.thelook_ecommerce.order_items AS order_items
        LEFT JOIN (
            SELECT orders.*, tbl_1.*
            FROM bigquery-public-data.thelook_ecommerce.orders AS orders
            LEFT JOIN (
                SELECT users.*, events.*
                FROM bigquery-public-data.thelook_ecommerce.users AS users
                LEFT JOIN bigquery-public-data.thelook_ecommerce.events AS events
                ON users.id = events.user_id
            ) AS tbl_1
            ON orders.user_id = tbl_1.user_id
        ) AS tbl_2
        ON order_items.order_id = tbl_2.order_id
    ) AS tbl_3
    ON products.id = tbl_3.product_id
) AS tbl_4
ON inventory_items.product_id = tbl_4.product_id) as tbl_5
on distribution_centers.id = tbl_5.distribution_center_id

/*Multiple nested query is slow, so we are using CTE which is faster*/

WITH enriched_order_data AS (
    SELECT
        orders.*,
        users.*,
        events.*
    FROM
        bigquery-public-data.thelook_ecommerce.orders AS orders
    LEFT JOIN
        bigquery-public-data.thelook_ecommerce.users AS users
    ON
        orders.user_id = users.id
    LEFT JOIN
        bigquery-public-data.thelook_ecommerce.events AS events
    ON
        users.id = events.user_id
),
enriched_order_items AS (
    SELECT
        order_items.*,
        enriched_order_data.*
    FROM
        bigquery-public-data.thelook_ecommerce.order_items AS order_items
    LEFT JOIN
        enriched_order_data
    ON
        order_items.order_id = enriched_order_data.order_id
),
enriched_products AS (
    SELECT
        products.*,
        enriched_order_items.*
    FROM
        bigquery-public-data.thelook_ecommerce.products AS products
    LEFT JOIN
        enriched_order_items
    ON
        products.id = enriched_order_items.product_id
),
enriched_inventory_items AS (
    SELECT
        inventory_items.*,
        enriched_products.*
    FROM
        bigquery-public-data.thelook_ecommerce.inventory_items AS inventory_items
    LEFT JOIN
        enriched_products
    ON
        inventory_items.product_id = enriched_products.product_id
)
SELECT
    distribution_centers.*,
    enriched_inventory_items.*
FROM
    bigquery-public-data.thelook_ecommerce.distribution_centers AS distribution_centers
LEFT JOIN
    enriched_inventory_items
ON
    distribution_centers.id = enriched_inventory_items.distribution_center_id;


/*Sql case with grades*/
SELECT
    FirstName,
    Salary,
    CASE
        WHEN salary >= 4000 THEN 'A'
        WHEN salary >= 3000 THEN 'B'
        WHEN salary >= 2000 THEN 'C'
        WHEN salary >= 1000 THEN 'D'
        ELSE 'F'
    END AS grade
FROM
    employee;


/*Emp_ID - Emp_Name - WrkStn_ID - Manager_ID - Dept_ID - Salary
101    -  ABC     -  1001     -  NULL      -  IT     -  50,000
102    -  DEF     -  1002     -  NULL      -  HR     -  70,000
103    -  GHI     -  1005     -  101       -  IT     -  20,000
104    -  JKL     -  NULL     -  102       -  HR     -  10,000
105    -  MNO     -  NULL     -  101       -  IT     -  15,000


Write an SQL query to find the top-paying employee in each department who is not a manager.*/


WITH RankedSalaries AS (
  SELECT
    Emp_ID,
    Emp_Name,
    WrkStn_ID,
    Manager_ID,
    Dept_ID,
    Salary,
    ROW_NUMBER() OVER (PARTITION BY Dept_ID ORDER BY Salary DESC) AS SalaryRank
  FROM
    YourTableName -- Replace with your actual table name
  WHERE
    Manager_ID IS NULL -- To filter out managers
)
SELECT
  Emp_ID,
  Emp_Name,
  WrkStn_ID,
  Manager_ID,
  Dept_ID,
  Salary
FROM
  RankedSalaries
WHERE
  SalaryRank = 1;



--Customers Who Never Order
SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
WHERE o.customerId is NULL;


--Department wise 2nd highestsalary using partition by and department wise ranking

select dept, salary 
from (select *, dense_rank() over(partition by dept order by salary desc) as rank
from employees) as t where rank = 2;


--Delete Duplicate Rows in SQL(Using CTE and row_number)
WITH duplicate_rows AS (
    SELECT customer_id,
           ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY customer_id) AS row_num
    FROM invoice_data
)
delete from duplicate_rows WHERE row_num > 1;


--Count of subjects taught by each teacher
select teacher_id, count(distinct subject_id) as cnt from Teacher group by teacher_id


--Find employees who earn less than 30000 and do not have a manager
SELECT Employee.employee_id
FROM Employees AS Employee
LEFT JOIN Employees AS Manager
  ON (Employee.manager_id = Manager.employee_id)
WHERE
  Employee.salary < 30000
  AND Employee.manager_id IS NOT NULL
  AND Manager.employee_id IS NULL



---Find the department with the highest number of employee.
WITH new_table AS (
  SELECT 
    department, 
    COUNT(*) AS dep_emp_count 
  FROM employee 
  GROUP BY department
)
SELECT TOP 1 department, dep_emp_count
FROM new_table
ORDER BY dep_emp_count DESC;


----Duplicate data using window function
select * from 
(select *, ROW_NUMBER() over(partition by department order by id)as row_num 
from employee) as new_table
where row_num > 1


--Find departments where average salary is greater than 70000
WITH avg_sal_dep AS (
    SELECT 
        d.department_name,
        AVG(e.salary) AS avg_salary
    FROM employees e
    JOIN departments d 
        ON e.department_id = d.department_id
    GROUP BY d.department_name
)
SELECT 
    department_name, 
    avg_salary
FROM avg_sal_dep
WHERE avg_salary > 70000;



--Department wise 2nd highest salary using DENSE_RANK()
 select * from 
 (select *, DENSE_RANK() over(Partition By department order by salary desc) as dep_rank 
 from [employee_salary]) as table_1 where dep_rank =2 



--Sales Analysis by Region
SELECT 
    c.region,
    SUM(s.amount) AS total_revenue,
    COUNT(s.order_id) AS total_orders,
    AVG(s.amount) AS avg_order_value,
    CASE 
        WHEN AVG(s.amount) >= 1000 THEN 'High'
        WHEN AVG(s.amount) BETWEEN 500 AND 999.99 THEN 'Medium'
        ELSE 'Low'
    END AS revenue_category
FROM sales s
JOIN customers c 
    ON s.customer_id = c.customer_id
GROUP BY c.region
ORDER BY total_revenue DESC;

-- Write an SQL query to calculate the time difference 
-- in seconds between each user's consecutive actions.
-- user_id | timestamp
-- -------- | -------------------
-- U1      | 2025-10-20 09:00:00
-- U1      | 2025-10-20 09:00:30
-- U2      | 2025-10-20 09:00:10
-- U1      | 2025-10-20 09:01:45
-- U2      | 2025-10-20 09:02:00

SELECT 
    user_id,
    timestamp,
    LAG(timestamp) OVER (PARTITION BY user_id ORDER BY timestamp) AS prev_timestamp,
    TIMESTAMPDIFF(SECOND, 
                  LAG(timestamp) OVER (PARTITION BY user_id ORDER BY timestamp), 
                  timestamp) AS time_diff_seconds
FROM your_table;

--Write a SQL query that returns each department's name and the average salary of employees 
--in that department, rounded to 2 decimal places, only for departments whose average salary 
--is greater than 50,000, ordered by average salary descending.

SELECT 
    d.dept_name,
    ROUND(AVG(e.salary), 2) AS avg_salary
FROM employees e
JOIN departments d 
    ON e.dept_id = d.dept_id
GROUP BY d.dept_id, d.dept_name
HAVING AVG(e.salary) > 50000
ORDER BY avg_salary DESC;


--Write a SQL query to find the employees with the highest salary in each department.
SELECT 
    d.dept_name,
    e.emp_name,
    e.salary
FROM employees e
JOIN departments d 
    ON e.dept_id = d.dept_id
WHERE e.salary = (
    SELECT MAX(salary)
    FROM employees
    WHERE dept_id = e.dept_id
)
ORDER BY e.salary DESC;


--OR

SELECT 
    dept_name,
    emp_name,
    salary
FROM (
    SELECT 
        d.dept_name,
        e.emp_name,
        e.salary,
        DENSE_RANK() OVER(
            PARTITION BY e.dept_id 
            ORDER BY e.salary DESC
        ) AS rnk
    FROM employees e
    JOIN departments d 
        ON e.dept_id = d.dept_id
) t
WHERE rnk = 1
ORDER BY salary DESC;



--Write a SQL query to find the previous day's sales amount for each salesman.
SELECT
    salesman_id,
    sales_date,
    amount,
    LAG(amount) OVER (PARTITION BY salesman_id ORDER BY sales_date) AS prev_day_amount
FROM sales;


--Write a SQL query to find the next higher salary for each employee within the same department.
SELECT 
    emp_id,
    emp_name,
    department,
    salary,
    LEAD(salary) OVER (PARTITION BY department ORDER BY salary) AS next_salary
FROM employee_salary;

--Write a SQL query to calculate the month-over-month revenue change for each product.
SELECT
    product_id,
    revenue_month,
    revenue_amount,
    revenue_amount - LAG(revenue_amount) OVER (PARTITION BY product_id ORDER BY revenue_month) AS change_from_prev_month
FROM monthly_revenue;

--Write a SQL query to find the difference in bonus amounts between consecutive years for each employee.
SELECT
    emp_id,
    emp_name,
    bonus_year,
    bonus_amount,
    LEAD(bonus_amount) OVER (PARTITION BY emp_id ORDER BY bonus_year) AS next_year_bonus,
    bonus_amount - LEAD(bonus_amount) OVER (PARTITION BY emp_id ORDER BY bonus_year) AS diff_with_next_year
FROM employee_bonus;


--Write a SQL query to fetch details of employees who were hired in the last 6 months.
SELECT emp_id, emp_name, dept_id, hire_date
FROM employees
WHERE hire_date >= DATEADD(MONTH, -6, CURRENT_DATE);



-- Find the users who logged in on two consecutive days.

-- option 1:
SELECT DISTINCT user_id
FROM (
    SELECT user_id,
           login_date,
           LAG(login_date) OVER (
               PARTITION BY user_id
               ORDER BY login_date
           ) AS prev_login_date
    FROM Logins
) t
WHERE login_date = DATE_ADD(prev_login_date, 1);


-- option 2:
SELECT DISTINCT l1.user_id
FROM Logins l1
JOIN Logins l2
  ON l1.user_id = l2.user_id
 AND l1.login_date = DATE_ADD(l2.login_date, 1);


--Write an SQL query to find employees who earn more than the average salary of their own department.
SELECT emp_name
FROM (
    SELECT emp_name,
           salary,
           AVG(salary) OVER (PARTITION BY department) AS dept_avg
    FROM Employees
) t
WHERE salary > dept_avg;


--Write an SQL query to find customers who have never placed any order.

-- option 1:
SELECT c.customer_name
FROM customers c
LEFT JOIN orders o
  ON c.customer_id = o.customer_id
WHERE o.customer_id IS NULL;


-- option 2:
SELECT customer_name
FROM customers
WHERE customer_id NOT IN (
    SELECT customer_id
    FROM orders
    WHERE customer_id IS NOT NULL
);

-----Write a SQL query to find users who logged in within 10 minutes of their previous login.
SELECT DISTINCT user_id
FROM (
    SELECT
        user_id,
        login_time,
        LAG(login_time) OVER (
            PARTITION BY user_id
            ORDER BY login_time
        ) AS prev_login
    FROM logins
) t
WHERE TIMESTAMPDIFF(MINUTE, prev_login, login_time) <= 10;


--Input +---------+--------------+------------+--------+
| OrderID | CustomerName | OrderDate  | Amount |
+---------+--------------+------------+--------+
|   101   | Alice        | 2025-01-01 |   200  | 
|   102   | Bob          | 2025-01-02 |   150  | 
|   103   | Alice        | 2025-01-05 |   300  | 
|   104   | Charlie      | 2025-01-07 |   100  | 
|   105   | Bob          | 2025-01-10 |   250  | 
|   106   | Alice        | 2025-01-12 |   400  | 
|   107   | Charlie      | 2025-01-15 |   200  | 
+---------+--------------+------------+--------+

--Output

| OrderID | CustomerName | OrderDate  | Amount | Sum Amount |
+---------+--------------+------------+--------++--------+ 
|   101   | Alice        | 2025-01-01 |   200  |    200
|   102   | Bob          | 2025-01-02 |   150  |    150
|   103   | Alice        | 2025-01-05 |   300  |    500
|   104   | Charlie      | 2025-01-07 |   100  |    100
|   105   | Bob          | 2025-01-10 |   250  |    400
|   106   | Alice        | 2025-01-12 |   400  |    900
|   107   | Charlie      | 2025-01-15 |   200  |    300

--Ans--
SELECT
    OrderID,
    CustomerName,
    OrderDate,
    Amount,
    SUM(Amount) OVER (
        PARTITION BY CustomerName
        ORDER BY OrderDate
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS "Sum Amount"
FROM orders
ORDER BY OrderDate;

--Write an SQL query to find employees who were present for at least 2 consecutive days.
SELECT DISTINCT emp_id
FROM (
    SELECT emp_id,
           work_date,
           status,
           LAG(work_date) OVER (PARTITION BY emp_id ORDER BY work_date) AS prev_date,
           LAG(status) OVER (PARTITION BY emp_id ORDER BY work_date) AS prev_status
    FROM employee_attendance
) t
WHERE status = 'Present'
  AND prev_status = 'Present'
  AND work_date = prev_date + INTERVAL '1 day';


-- For each user, find the number of login sessions.
-- A session is defined as:
-- A new session starts if the time difference between two consecutive logins is more than 30 minutes.

SELECT user_id,
       COUNT(*) AS session_count
FROM (
    SELECT user_id,
           login_time,
           CASE
               WHEN LAG(login_time) OVER (PARTITION BY user_id ORDER BY login_time) IS NULL
                    THEN 1
               WHEN login_time >
                    LAG(login_time) OVER (PARTITION BY user_id ORDER BY login_time)
                    + INTERVAL '30 minute'
                    THEN 1
               ELSE 0
           END AS new_session_flag
    FROM login_logs
) t
WHERE new_session_flag = 1
GROUP BY user_id;


-- Find the second highest salary in each department.
-- If a department has fewer than 2 employees, do not include it in the result.

SELECT dept_id,
       salary AS second_highest_salary
FROM (
    SELECT dept_id,salary,DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk,
    COUNT(*) OVER (PARTITION BY dept_id) AS emp_count FROM employees) t
WHERE rnk = 2 AND emp_count >= 2;


--Write a SQL query to find the salary difference between each employee's current and previous salary event.

SELECT
    emp_id,
    event_date,
    salary,
    LAG(salary) OVER (PARTITION BY emp_idORDER BY event_date) AS prev_salary, 
    salary - LAG(salary) OVER (PARTITION BY emp_id ORDER BY event_date) AS diff,
    CASE
        WHEN salary > LAG(salary) OVER (PARTITION BY emp_id ORDER BY event_date) THEN 'Y' ELSE 'N'
    END AS increase_flag
FROM employee_events;



--Write a SQL query to find customers who have placed more than 3 orders in the last year. 
--Return the customer_id, customer_name, and total number of orders.

SELECT 
    c.customer_id,
    c.customer_name,
    COUNT(o.order_id) AS total_orders
FROM Customers c
JOIN Orders o 
    ON c.customer_id = o.customer_id
WHERE o.order_date >= DATEADD(YEAR, -1, GETDATE())
GROUP BY 
    c.customer_id, 
    c.customer_name
HAVING COUNT(o.order_id) > 3;

----Write a SQL query to find customers who have placed more than 3 orders in the last year.(Based on year)

SELECT 
    c.customer_id,
    c.customer_name,
    COUNT(o.order_id) AS total_orders
FROM Customers c
JOIN Orders o
    ON c.customer_id = o.customer_id
WHERE YEAR(o.order_date) = YEAR(GETDATE()) - 1
GROUP BY 
    c.customer_id,
    c.customer_name
HAVING COUNT(o.order_id) > 3;

--Find departments with the highest average salary.

WITH dept_avg AS (
    SELECT department_name, AVG(salary) AS avg_salary
    FROM table1
    GROUP BY department_name
)
SELECT department_name, avg_salary
FROM dept_avg
WHERE avg_salary = (SELECT MAX(avg_salary) FROM dept_avg);


--Write a SQL query to find the top 2 products,
--with the highest revenue in each category.

WITH ctc AS (
    SELECT 
        product_id,
        product_category,
        SUM(price_per_unit * quantity) AS revenue
<<<<<<< HEAD
    FROM orders
=======
    FROM table_name
>>>>>>> 315ffd7d00d0f3762ba7e73404d0676bc524ba76
    GROUP BY product_id, product_category
)
SELECT *,
       ROW_NUMBER() OVER (
           PARTITION BY product_category 
           ORDER BY revenue DESC
       ) AS row_rank
FROM ctc
WHERE row_rank <= 2;

--Write a SQL query to find the numbers which consecutively occur 3 times.
SELECT numbers
FROM (
SELECT numbers,
LEAD(numbers, 1) OVER (ORDER BY id) AS next_num,
LEAD(numbers, 2) OVER (ORDER BY id) AS next_next_num
FROM table_name
<<<<<<< HEAD
) t
WHERE numbers = next_num AND numbers = next_next_num;

--Write a SQL query to find the highest salary in each department
--along with the employee name and supervisor name.

WITH cte AS (
    SELECT 
        e.employee_id,
        e.employee_name,
        e.salary,
        e.dept_id,
        m.employee_name AS supervisor_name
    FROM employee_new1 e
    LEFT JOIN employee_new1 m
        ON e.supervisor_id = m.employee_id
)
SELECT 
    employee_id,
    employee_name,
    supervisor_name,
    salary,
    MAX(salary) OVER (PARTITION BY dept_id) AS dept_highest_salary,
    FIRST_VALUE(employee_name) OVER (
        PARTITION BY dept_id 
        ORDER BY salary DESC
    ) AS dept_highest_paid_employee
FROM cte;

--Write a SQL query to find all the employees who have been with the company 
--for at least 3 consecutive years.

WITH cte AS (
    SELECT 
        pid,
        year,
        LEAD(year, 1) OVER (PARTITION BY pid ORDER BY year) AS next_year,
        LEAD(year, 2) OVER (PARTITION BY pid ORDER BY year) AS next_year_2
    FROM event_table
)
SELECT DISTINCT pid
FROM cte
WHERE next_year = year + 1
  AND next_year_2 = year + 2;


--Write a SQL query to find the current day's sales amount for each product,
--along with the next day's and previous day's sales amount for the same product.
SELECT 
    PRODUCT,
    SALE_DATE,
    AMOUNT AS CURRENT_DAY_SALE,
    LEAD(AMOUNT) OVER (PARTITION BY PRODUCT ORDER BY SALE_DATE) AS NEXT_DAY_SALE,
    LAG(AMOUNT) OVER (PARTITION BY PRODUCT  ORDER BY SALE_DATE) AS PREVIOUS_DAY_SALE
FROM sales_data_1
ORDER BY PRODUCT desc


--Write a SQL query to calculate the total sales amount for each product for each month and year.
WITH cte AS (
    SELECT 
        product,
        YEAR(sale_date) AS sale_year,
        MONTH(sale_date) AS sale_month,
        amount
    FROM sales_data_1
)
SELECT 
    product,
    sale_year,
    sale_month,
    SUM(amount) AS total_amount
FROM cte
GROUP BY product, sale_year, sale_month
ORDER BY product, sale_year, sale_month;

-- Option 2 Write a SQL query to calculate the total sales amount for each product for each month and year.
SELECT 
    product,
    YEAR(sale_date) AS sale_year,
    MONTH(sale_date) AS sale_month,
    SUM(amount) AS total_amount
FROM sales_data_1
GROUP BY 
    product,
    YEAR(sale_date),
    MONTH(sale_date)
ORDER BY product, sale_year, sale_month;

--Write a SQL query to calculate the difference in days between 
--each sale and the previous sale for the same product.
WITH cte AS (
    SELECT  
        product, 
        sale_date,
        LAG(sale_date) OVER (
            PARTITION BY product 
            ORDER BY sale_date
        ) AS previous_sale_date
    FROM sales_data_1
)
SELECT 
    product,
    sale_date,
    ISNULL(previous_sale_date, '1900-01-01') AS previous_sale_date,
    ISNULL(DATEDIFF(DAY, previous_sale_date, sale_date), 0) AS days_diff
FROM cte
where DATEDIFF(DAY, previous_sale_date, sale_date) = 1;


--Write a SQL query to find the top 2 products with the highest revenue in each category,
WITH product_revenue AS (
    SELECT 
        product_category,
        product_id,
        SUM(quantity * price_per_unit) AS revenue
    FROM orders
    WHERE status = 'Delivered'
    GROUP BY product_category, product_id
)
SELECT *
FROM (
    SELECT *, 
        DENSE_RANK() OVER (
            PARTITION BY product_category 
            ORDER BY revenue DESC
        ) AS rnk
    FROM product_revenue
) t1
WHERE rnk <= 2;

--Write a SQL query to calculate the total number of orders 
--and the number of delivered orders for each city.
SELECT 
    city,
    COUNT(*) AS total_orders,
    SUM(CASE 
            WHEN [status] = 'Delivered' THEN 1 
            ELSE 0 
        END) AS delivered_orders
FROM orders
GROUP BY city;

--Write a SQL query to calculate the total number of orders,
--the number of delivered orders, the number of returned orders,
SELECT 
    city,
    SUM(CASE WHEN [status] = 'Delivered' THEN 1 ELSE 0 END) AS delivered_orders,
    SUM(CASE WHEN [status] = 'Returned' THEN 1 ELSE 0 END) AS returned_orders,
    SUM(CASE WHEN [status] = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_orders
FROM orders
GROUP BY city;

--Write a SQL query to find the gap in days between each order and the previous order,
-- for the same customer,
WITH cte AS (
    SELECT 
        customer_id,
        order_id,
        order_date,
        LAG(order_date) OVER (
            PARTITION BY customer_id 
            ORDER BY order_date
        ) AS previous_order_date
    FROM orders
)
SELECT 
    customer_id,
    order_id,
    order_date,
    previous_order_date,
    DATEDIFF(DAY, previous_order_date, order_date) AS days_gap,
    CASE 
        WHEN previous_order_date IS NULL THEN 'New Order'
        WHEN DATEDIFF(DAY, previous_order_date, order_date) <= 30 THEN 'Repeat Order'
        ELSE 'New Order'
    END AS order_type
FROM cte
ORDER BY customer_id, order_date;

--Write a SQL query to compare the revenue of each order 
--with the previous order for the same customer and indicate whether the revenue has
-- increased, decreased, or remained the same.

WITH cte AS (
    SELECT 
        customer_id, 
        order_id, 
        order_date, 
        (quantity * price_per_unit) AS current_revenue,
        LAG(quantity * price_per_unit) OVER (
            PARTITION BY customer_id 
            ORDER BY order_date
        ) AS previous_revenue
    FROM orders
)
SELECT *,
    CASE
        WHEN previous_revenue IS NULL THEN 'First Order'
        WHEN current_revenue > previous_revenue THEN 'Increased'
        WHEN current_revenue < previous_revenue THEN 'Decreased'
        ELSE 'Same'
    END AS revenue_trend
FROM cte;

--Write a SQL query to calculate the running total of revenue for each city,
SELECT 
    city,
    order_date,
    (quantity * price_per_unit) AS revenue,
    SUM(quantity * price_per_unit) OVER (
        PARTITION BY city, 
                     YEAR(order_date), 
                     MONTH(order_date)
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM orders
WHERE [status] = 'Delivered';

--Write a SQL query to calculate the total revenue for each city and month,
with cte as(select city, MONTH(order_date) as month, (quantity * price_per_unit) as revenue,
sum(quantity * price_per_unit) over (partition by city, YEAR(order_date), MONTH(order_date) order by order_date
rows between UNBOUNDED PRECEDING and current row) as running_total
from orders
where [status] = 'Delivered'
)
select city, month, sum(revenue) as total_revenue, max(running_total) as total_running_revenue
from cte group by city, month
order by city, month;


--Running total of Delivered revenue per customer
--BUT reset the running total whenever there is a gap of more than 20 days between consecutive orders.

WITH cte AS (
    SELECT 
        customer_id,
        order_date,
        quantity * price_per_unit AS revenue,
        LAG(order_date) OVER (
            PARTITION BY customer_id 
            ORDER BY order_date
        ) AS prev_order_date
    FROM orders
    WHERE [status] = 'Delivered'
),

flag_cte AS (
    SELECT *,
        CASE 
            WHEN prev_order_date IS NULL THEN 1
            WHEN DATEDIFF(DAY, prev_order_date, order_date) > 20 THEN 1
            ELSE 0
        END AS new_group_flag
    FROM cte
),

group_cte AS (
    SELECT *,
        SUM(new_group_flag) OVER (
            PARTITION BY customer_id 
            ORDER BY order_date
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS grp
    FROM flag_cte
)


--Find all orders where the order amount (quantity * price_per_unit)
-- is greater than the average order amount of the same product_category.
SELECT 
    order_id,
    product_category,
    quantity * price_per_unit AS order_amount
FROM orders o
WHERE (quantity * price_per_unit) >
(
    SELECT AVG(quantity * price_per_unit)
    FROM orders
    GROUP BY product_category
    having product_category = o.product_category
);

--Write a SQL query to find employees 
--whose salary is greater than the average salary of their own department.
SELECT *
FROM (
    SELECT e.EmpName,
           e.Salary,
           d.DeptName,
           AVG(e.Salary) OVER (PARTITION BY e.DeptID) AS DepartmentAvgSalary
    FROM Employee e
    JOIN Department d 
        ON e.DeptID = d.DeptID
) t
=======
) t
WHERE numbers = next_num AND numbers = next_next_num;

--Write a SQL query to find the highest salary in each department
--along with the employee name and supervisor name.

WITH cte AS (
    SELECT 
        e.employee_id,
        e.employee_name,
        e.salary,
        e.dept_id,
        m.employee_name AS supervisor_name
    FROM employee_new1 e
    LEFT JOIN employee_new1 m
        ON e.supervisor_id = m.employee_id
)
SELECT 
    employee_id,
    employee_name,
    supervisor_name,
    salary,
    MAX(salary) OVER (PARTITION BY dept_id) AS dept_highest_salary,
    FIRST_VALUE(employee_name) OVER (
        PARTITION BY dept_id 
        ORDER BY salary DESC
    ) AS dept_highest_paid_employee
FROM cte;

--Write a SQL query to find all the employees who have been with the company 
--for at least 3 consecutive years.

WITH cte AS (
    SELECT 
        pid,
        year,
        LEAD(year, 1) OVER (PARTITION BY pid ORDER BY year) AS next_year,
        LEAD(year, 2) OVER (PARTITION BY pid ORDER BY year) AS next_year_2
    FROM event_table
)
SELECT DISTINCT pid
FROM cte
WHERE next_year = year + 1
  AND next_year_2 = year + 2;


--Write a SQL query to find the current day's sales amount for each product,
--along with the next day's and previous day's sales amount for the same product.
SELECT 
    PRODUCT,
    SALE_DATE,
    AMOUNT AS CURRENT_DAY_SALE,
    LEAD(AMOUNT) OVER (
        PARTITION BY PRODUCT 
        ORDER BY SALE_DATE
    ) AS NEXT_DAY_SALE,
    LAG(AMOUNT) OVER (
        PARTITION BY PRODUCT  
        ORDER BY SALE_DATE
    ) AS PREVIOUS_DAY_SALE
FROM sales_data_1
ORDER BY PRODUCT desc


--Write a SQL query to calculate the total sales amount for each product for each month and year.
WITH cte AS (
    SELECT 
        product,
        YEAR(sale_date) AS sale_year,
        MONTH(sale_date) AS sale_month,
        amount
    FROM sales_data_1
)
SELECT 
    product,
    sale_year,
    sale_month,
    SUM(amount) AS total_amount
FROM cte
GROUP BY product, sale_year, sale_month
ORDER BY product, sale_year, sale_month;

-- Option 2 Write a SQL query to calculate the total sales amount for each product for each month and year.
SELECT 
    product,
    YEAR(sale_date) AS sale_year,
    MONTH(sale_date) AS sale_month,
    SUM(amount) AS total_amount
FROM sales_data_1
GROUP BY 
    product,
    YEAR(sale_date),
    MONTH(sale_date)
ORDER BY product, sale_year, sale_month;

--Write a SQL query to calculate the difference in days between 
--each sale and the previous sale for the same product.
WITH cte AS (
    SELECT  
        product, 
        sale_date,
        LAG(sale_date) OVER (
            PARTITION BY product 
            ORDER BY sale_date
        ) AS previous_sale_date
    FROM sales_data_1
)
SELECT 
    product,
    sale_date,
    ISNULL(previous_sale_date, '1900-01-01') AS previous_sale_date,
    ISNULL(DATEDIFF(DAY, previous_sale_date, sale_date), 0) AS days_diff
FROM cte
where DATEDIFF(DAY, previous_sale_date, sale_date) = 1;


--Write a SQL query to find the top 2 products with the highest revenue in each category,
WITH product_revenue AS (
    SELECT 
        product_category,
        product_id,
        SUM(quantity * price_per_unit) AS revenue
    FROM orders
    WHERE status = 'Delivered'
    GROUP BY product_category, product_id
)
SELECT *
FROM (
    SELECT *, 
        DENSE_RANK() OVER (
            PARTITION BY product_category 
            ORDER BY revenue DESC
        ) AS rnk
    FROM product_revenue
) t1
WHERE rnk <= 2;

--Write a SQL query to calculate the total number of orders 
--and the number of delivered orders for each city.
SELECT 
    city,
    COUNT(*) AS total_orders,
    SUM(CASE 
            WHEN [status] = 'Delivered' THEN 1 
            ELSE 0 
        END) AS delivered_orders
FROM orders
GROUP BY city;

--Write a SQL query to calculate the total number of orders,
--the number of delivered orders, the number of returned orders,
SELECT 
    city,
    SUM(CASE WHEN [status] = 'Delivered' THEN 1 ELSE 0 END) AS delivered_orders,
    SUM(CASE WHEN [status] = 'Returned' THEN 1 ELSE 0 END) AS returned_orders,
    SUM(CASE WHEN [status] = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_orders
FROM orders
GROUP BY city;

--Write a SQL query to find the gap in days between each order and the previous order,
-- for the same customer,
WITH cte AS (
    SELECT 
        customer_id,
        order_id,
        order_date,
        LAG(order_date) OVER (
            PARTITION BY customer_id 
            ORDER BY order_date
        ) AS previous_order_date
    FROM orders
)
SELECT 
    customer_id,
    order_id,
    order_date,
    previous_order_date,
    DATEDIFF(DAY, previous_order_date, order_date) AS days_gap,
    CASE 
        WHEN previous_order_date IS NULL THEN 'New Order'
        WHEN DATEDIFF(DAY, previous_order_date, order_date) <= 30 THEN 'Repeat Order'
        ELSE 'New Order'
    END AS order_type
FROM cte
ORDER BY customer_id, order_date;

--Write a SQL query to compare the revenue of each order 
--with the previous order for the same customer and indicate whether the revenue has
-- increased, decreased, or remained the same.

WITH cte AS (
    SELECT 
        customer_id, 
        order_id, 
        order_date, 
        (quantity * price_per_unit) AS current_revenue,
        LAG(quantity * price_per_unit) OVER (
            PARTITION BY customer_id 
            ORDER BY order_date
        ) AS previous_revenue
    FROM orders
)
SELECT *,
    CASE
        WHEN previous_revenue IS NULL THEN 'First Order'
        WHEN current_revenue > previous_revenue THEN 'Increased'
        WHEN current_revenue < previous_revenue THEN 'Decreased'
        ELSE 'Same'
    END AS revenue_trend
FROM cte;

--Write a SQL query to calculate the running total of revenue for each city,
SELECT 
    city,
    order_date,
    (quantity * price_per_unit) AS revenue,
    SUM(quantity * price_per_unit) OVER (
        PARTITION BY city, 
                     YEAR(order_date), 
                     MONTH(order_date)
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM orders
WHERE [status] = 'Delivered';

--Write a SQL query to calculate the total revenue for each city and month,
with cte as(select city, MONTH(order_date) as month, (quantity * price_per_unit) as revenue,
sum(quantity * price_per_unit) over (partition by city, YEAR(order_date), MONTH(order_date) order by order_date
rows between UNBOUNDED PRECEDING and current row) as running_total
from orders
where [status] = 'Delivered'
)
select city, month, sum(revenue) as total_revenue, max(running_total) as total_running_revenue
from cte group by city, month
order by city, month;


--Running total of Delivered revenue per customer
--BUT reset the running total whenever there is a gap of more than 20 days between consecutive orders.

WITH cte AS (
    SELECT 
        customer_id,
        order_date,
        quantity * price_per_unit AS revenue,
        LAG(order_date) OVER (
            PARTITION BY customer_id 
            ORDER BY order_date
        ) AS prev_order_date
    FROM orders
    WHERE [status] = 'Delivered'
),

flag_cte AS (
    SELECT *,
        CASE 
            WHEN prev_order_date IS NULL THEN 1
            WHEN DATEDIFF(DAY, prev_order_date, order_date) > 20 THEN 1
            ELSE 0
        END AS new_group_flag
    FROM cte
),

group_cte AS (
    SELECT *,
        SUM(new_group_flag) OVER (
            PARTITION BY customer_id 
            ORDER BY order_date
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS grp
    FROM flag_cte
)



--Find all orders where the order amount (quantity * price_per_unit)
-- is greater than the average order amount of the same product_category.
SELECT 
    order_id,
    product_category,
    quantity * price_per_unit AS order_amount
FROM orders o
WHERE (quantity * price_per_unit) >
(
    SELECT AVG(quantity * price_per_unit)
    FROM orders
    GROUP BY product_category
    having product_category = o.product_category
);

--Write a SQL query to find employees 
--whose salary is greater than the average salary of their own department.
SELECT *
FROM (
    SELECT e.EmpName,
           e.Salary,
           d.DeptName,
           AVG(e.Salary) OVER (PARTITION BY e.DeptID) AS DepartmentAvgSalary
    FROM Employee e
    JOIN Department d 
        ON e.DeptID = d.DeptID
) t
>>>>>>> 315ffd7d00d0f3762ba7e73404d0676bc524ba76
WHERE Salary > DepartmentAvgSalary;

--Write a SQL query to find the manager who has the 
--most employees reporting to them, along with the count of employees.
SELECT TOP 1 
       m.EmpName AS ManagerName,
       COUNT(e.EmpID) AS NumberOfEmployees
FROM Employee e
JOIN Employee m 
     ON e.ManagerID = m.EmpID
WHERE e.ManagerID IS NOT NULL
GROUP BY m.EmpName
ORDER BY COUNT(e.EmpID) DESC;  

--Daily Active User
SELECT 
    CAST(event_timestamp AS Week) AS activity_date,
    COUNT(DISTINCT user_id) AS DAU
FROM user_activity
GROUP BY CAST(event_timestamp AS Week)
ORDER BY activity_date;

--Weekly Active User
SELECT 
    DATEPART(YEAR, event_timestamp) AS yr,
    DATEPART(WEEK, event_timestamp) AS wk,
    COUNT(DISTINCT user_id) AS WAU
FROM user_activity
GROUP BY 
    DATEPART(YEAR, event_timestamp),
    DATEPART(WEEK, event_timestamp)
ORDER BY yr, wk;

--Monthly Active User
SELECT 
    DATEPART(YEAR, event_timestamp) AS yr,
    DATEPART(MONTH, event_timestamp) AS mn,
    COUNT(DISTINCT user_id) AS MAU
FROM user_activity
GROUP BY 
    DATEPART(YEAR, event_timestamp),
    DATEPART(MONTH, event_timestamp)
ORDER BY yr, mn;

--Yearly Active User
SELECT 
    DATEPART(YEAR, event_timestamp) AS yr,
    COUNT(DISTINCT user_id) AS YAU
FROM user_activity
GROUP BY DATEPART(YEAR, event_timestamp)
ORDER BY yr;

--Delete duplicate rows in SQL using CTE and row_number
with cte as(select * from (select city, state, stars, row_number() over(partition by state order by stars desc) as rn
from [test_database].[dbo].[hotel]) t)
delete from cte where rn > 1;
<<<<<<< HEAD


--For each user, calculate the running total of revenue over time 
--(only for purchase events),
SELECT 
    l.user_id,
    l.event_timestamp AS login_time,
    p.event_timestamp AS purchase_time,
    DATEDIFF(MINUTE, l.event_timestamp, p.event_timestamp) AS time_diff_minutes
FROM user_activity l
JOIN user_activity p 
    ON l.user_id = p.user_id
    AND CAST(l.event_timestamp AS DATE) = CAST(p.event_timestamp AS DATE)
WHERE l.event_type = 'login'
    AND p.event_type = 'purchase'
    AND DATEDIFF(MINUTE, l.event_timestamp, p.event_timestamp) BETWEEN 0 AND 120;


--Write a SQL query to find the employees who joined in a year when more than one department 
--had new joiners, along with the count of departments that had new joiners in that year.
SELECT e.EmpName, d.DeptName, 
       YEAR(e.JoiningDate) AS JoiningYear,
       yd.DeptCount
FROM Employee e
JOIN Department d ON e.DeptID = d.DeptID
JOIN (
    -- Step 1: Per year, count how many distinct depts have joiners
    SELECT YEAR(JoiningDate) AS JoiningYear,
           COUNT(DISTINCT DeptID) AS DeptCount
    FROM Employee
    GROUP BY YEAR(JoiningDate)
    HAVING COUNT(DISTINCT DeptID) > 1        -- Only multi-dept years
) yd ON YEAR(e.JoiningDate) = yd.JoiningYear
ORDER BY JoiningYear


--Write a SQL query to calculate the time difference in hours between a user's 
--first login and their first purchase.
WITH first_login AS (
    SELECT 
        user_id,
        MIN(event_timestamp) AS first_login_time
    FROM user_activity
    WHERE event_type = 'login'
    GROUP BY user_id
),
first_purchase AS (
    SELECT 
        user_id,
        MIN(event_timestamp) AS first_purchase_time
    FROM user_activity
    WHERE event_type = 'purchase'
    GROUP BY user_id
)
SELECT 
    fl.user_id,
    fl.first_login_time,
    fp.first_purchase_time,
    CAST(DATEDIFF(SECOND, fl.first_login_time, fp.first_purchase_time) / 3600.0 AS DECIMAL(10,2)) AS hours_to_convert
FROM first_login fl
INNER JOIN first_purchase fp 
    ON fl.user_id = fp.user_id
WHERE fp.first_purchase_time > fl.first_login_time
ORDER BY hours_to_convert ASC;

--Consecutive Login Days
WITH login_days AS (
    SELECT DISTINCT
        user_id,
        CAST(event_timestamp AS DATE) AS login_date
    FROM user_activity
    WHERE event_type = 'login'
),
with_prev AS (
    SELECT
        user_id,
        login_date,
        LAG(login_date) OVER (PARTITION BY user_id ORDER BY login_date) AS prev_login_date
    FROM login_days
)
SELECT
    user_id,
    COUNT(*) AS consecutive_login_pairs
FROM with_prev
WHERE DATEDIFF(DAY, prev_login_date, login_date) = 1
GROUP BY user_id
ORDER BY consecutive_login_pairs DESC, user_id ASC;


--Write a SQL query to find the date when each customer
--first reached a cumulative purchase amount of $1000 or more.
WITH RunningCTE AS (
    SELECT
        CustomerID,
        TxnDate,
        SUM(Amount) OVER (PARTITION BY CustomerID 
                          ORDER BY TxnDate
                          ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS RunningTotal
    FROM Transactions
),
RankedCTE AS (
    SELECT *,
        ROW_NUMBER() OVER (PARTITION BY CustomerID ORDER BY TxnDate) AS rnk
    FROM RunningCTE
    WHERE RunningTotal >= 1000
)
SELECT CustomerID, TxnDate, RunningTotal
FROM RankedCTE
WHERE rnk = 1;



----SCD Type 2 Code

-- PASS 1 : Expire old rows where salary has changed
MERGE INTO target_table AS trg
USING source_table AS src
    ON  trg.id = src.id
    AND trg.is_current = 1

WHEN MATCHED AND trg.salary <> src.salary THEN
    UPDATE SET
        trg.end_date   = GETDATE(),
        trg.is_current = 0;
=======
>>>>>>> 315ffd7d00d0f3762ba7e73404d0676bc524ba76

-- PASS 2 : Insert new current row for changed + net-new records
MERGE INTO target_table AS trg
USING source_table AS src
    ON  trg.id         = src.id
    AND trg.is_current = 1        -- only active rows qualify as a match

<<<<<<< HEAD
WHEN NOT MATCHED BY TARGET THEN   -- no active row found = new ID or just-expired
    INSERT (id, salary, start_date, end_date, is_current)
    VALUES (src.id, src.salary, GETDATE(), NULL, 1);
=======
--For each user, calculate the running total of revenue over time 
--(only for purchase events),
SELECT 
    l.user_id,
    l.event_timestamp AS login_time,
    p.event_timestamp AS purchase_time,
    DATEDIFF(MINUTE, l.event_timestamp, p.event_timestamp) AS time_diff_minutes
FROM user_activity l
JOIN user_activity p 
    ON l.user_id = p.user_id
    AND CAST(l.event_timestamp AS DATE) = CAST(p.event_timestamp AS DATE)
WHERE l.event_type = 'login'
    AND p.event_type = 'purchase'
    AND DATEDIFF(MINUTE, l.event_timestamp, p.event_timestamp) BETWEEN 0 AND 120;


--Write a SQL query to find the employees who joined in a year when more than one department 
--had new joiners, along with the count of departments that had new joiners in that year.
SELECT e.EmpName, d.DeptName, 
       YEAR(e.JoiningDate) AS JoiningYear,
       yd.DeptCount
FROM Employee e
JOIN Department d ON e.DeptID = d.DeptID
JOIN (
    -- Step 1: Per year, count how many distinct depts have joiners
    SELECT YEAR(JoiningDate) AS JoiningYear,
           COUNT(DISTINCT DeptID) AS DeptCount
    FROM Employee
    GROUP BY YEAR(JoiningDate)
    HAVING COUNT(DISTINCT DeptID) > 1        -- Only multi-dept years
) yd ON YEAR(e.JoiningDate) = yd.JoiningYear
ORDER BY JoiningYear


--Write a SQL query to calculate the time difference in hours between a user's 
--first login and their first purchase.
WITH first_login AS (
    SELECT 
        user_id,
        MIN(event_timestamp) AS first_login_time
    FROM user_activity
    WHERE event_type = 'login'
    GROUP BY user_id
),
first_purchase AS (
    SELECT 
        user_id,
        MIN(event_timestamp) AS first_purchase_time
    FROM user_activity
    WHERE event_type = 'purchase'
    GROUP BY user_id
)
SELECT 
    fl.user_id,
    fl.first_login_time,
    fp.first_purchase_time,
    CAST(DATEDIFF(SECOND, fl.first_login_time, fp.first_purchase_time) / 3600.0 AS DECIMAL(10,2)) AS hours_to_convert
FROM first_login fl
INNER JOIN first_purchase fp 
    ON fl.user_id = fp.user_id
WHERE fp.first_purchase_time > fl.first_login_time
ORDER BY hours_to_convert ASC;

--Consecutive Login Days
WITH login_days AS (
    SELECT DISTINCT
        user_id,
        CAST(event_timestamp AS DATE) AS login_date
    FROM user_activity
    WHERE event_type = 'login'
),
with_prev AS (
    SELECT
        user_id,
        login_date,
        LAG(login_date) OVER (PARTITION BY user_id ORDER BY login_date) AS prev_login_date
    FROM login_days
)
SELECT
    user_id,
    COUNT(*) AS consecutive_login_pairs
FROM with_prev
WHERE DATEDIFF(DAY, prev_login_date, login_date) = 1
GROUP BY user_id
ORDER BY consecutive_login_pairs DESC, user_id ASC;
>>>>>>> 315ffd7d00d0f3762ba7e73404d0676bc524ba76
