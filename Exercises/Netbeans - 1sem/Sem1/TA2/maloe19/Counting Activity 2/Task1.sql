/*
Question 1: What is a transaction and why is it important. State your answer below

Question 1 Answer:
A transaction is an (all or nothing) operation, and it is important because it makes sure (of consistency with more than) that one users can use it (at the same time)    
*/

/*
Question 2: In the SQL code at the bottom of the file, insert transactions at the right place to ensure account balance consistency
*/

/*
Question 3: In your own words; what is a stored procedure?

Question 3 Answer:
Stored procedure is method to process results
*/

/*
Question 4: The client wants to optimize the interaction with the database, so they asked you to introduce procedures to update the accounts.
    a. Create a procedure, that adds a value to the balance of a specific account
    b. Create a procedure, that subtracts a value from the balance of a specific account
*/

/*
Question 5: The client has added a new requirement, now he wants the database to update the customers credit worthieness.
    a. Create a trigger, that updates a specific customers credit_worthy, so that it is True, if the balance is over 10.000
*/

/*
Question 6: Since the Bank employees tend to first search for the customers credit worthieness, he wants you to optimise this interaction.
    a. Create an Index on credit_worthy.
*/

BEGIN;
CREATE TABLE Customers
(
    id            SERIAL PRIMARY KEY,
    name          VARCHAR(100) NOT NULL,
    credit_worthy boolean
);

CREATE TABLE Accounts
(
    id      SERIAL PRIMARY KEY,
    balance BIGINT
);

CREATE TABLE Customer_Accounts
(
    customer_id INT REFERENCES Customers,
    account_id  INT REFERENCES Accounts,
    PRIMARY KEY (customer_id, account_id)
);

INSERT INTO Customers (name, credit_worthy)
VALUES ('Thomas Borgen', false),
       ('Jakob Hviid', true);

INSERT INTO Accounts (balance)
VALUES (15000000000),
       (15000);

INSERT INTO Customer_Accounts
VALUES (1, 1); -- Thomas Borgens account
INSERT INTO Customer_Accounts
VALUES (2, 2);
-- Jakob Hviid account

-- transferring 15 billions from Thomas Borgens to Jakob Hviid

UPDATE Accounts
SET balance = balance + 15000000000
WHERE id IN (
    SELECT id
    FROM Customers
    WHERE name = 'Jakob Hviid'
);
SAVEPOINT new_savepoint;
UPDATE Accounts
SET balance = balance - 15000000000
WHERE id IN (
    SELECT id
    FROM Customers
    WHERE name = 'Thomas Borgen'
);

CREATE OR REPLACE PROCEDURE !!!!(add)
AS $$
DECLARE 
	!!!!
BEGIN
	!!!!
END; $$
LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE !!!!(subtract)
AS $$
DECLARE 
	!!!!
BEGIN
	!!!!
END; $$
LANGUAGE plpgsql;

CREATE TRIGGER !!!!
AFTER UPDATE !!!!
(FOR EACH ROW)
(WHEN !!!!)
EXECUTE PROCEDURE !!!!

CREATE UNIQUE INDEX ON credit_worthy(!);

COMMIT;
