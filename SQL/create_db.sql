############################################################

CREATE TABLE employees (
    Id INT,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Sex VARCHAR(10),
    Salary INT,
    Department VARCHAR(255),
    Bonus INT
);

INSERT INTO employees (Id, FirstName, LastName, Sex, Salary, Department, Bonus)
VALUES (1, 'Tirtho', 'Debnath', 'Male', 1000, 'IT', 500),
       (2, 'Archi', 'Mallick', 'Male', 2000, 'HR', 600),
       (3, 'Sahin', 'Akbal', 'Female', 6000, 'Finance', 200),
       (4, 'Gam', 'Tate', 'Female', 7000, 'IT', 588),
       (5, 'Sahbaz', 'Khatoon', 'Female', 3000, 'HR', 457),
       (6, 'Lontu', 'Khan', 'Male', 9000, 'Support', 467),
       (7, 'Sahbab', 'Khatua', 'Male', 30000, 'Accounts', 657);


##############################


