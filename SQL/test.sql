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

/*Q-17. From the following table, write a SQL query to calculate average price of the items for each company. Return average price and company code.*/

SELECT AVG(pro_price), pro_com FROM item_mast GROUP BY pro_com;

/*Q-18. Write an SQL query to report all the duplicate emails. Return the result table in any order.*/

select distinct p1.Email

from Person p1, Person p2

where p1.Id <> p2.Id and p1.Email = p2.Email

/*Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.*/

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


/*Write an SQL query to delete all the duplicate emails,
keeping only one unique email with the smallest id. Note that you are supposed to write a DELETE statement and not a SELECT one.*/

Delete p1
from Person p1, Person p2
where p1.Email = p2.Email and p1.Id > p2.Id



/*Inner join using asc*/

select first_name , item , amount 
from customers 
outer join orders 
on customers.customer_id = orders.customer_id 
order by amount asc


