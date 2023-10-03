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
        DENCE_RANK() OVER(PARTITION BY d.Name ORDER BY e.salary DESC) AS rank
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