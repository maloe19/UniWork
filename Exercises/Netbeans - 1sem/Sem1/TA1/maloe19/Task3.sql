-- Insert your SQL code from Task 3 into this document. Please read "Assignments and instructions.pdf" for instructions.
CREATE TABLE publisher(
	id serial PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	founded VARCHAR(50) NOT NULL,
	headquarter VARCHAR(100) NOT NULL
);

INSERT INTO publisher (name, founded, headquarter) VALUES ('CD Project', 'mar-94', 'Warshaw, Poland');
INSERT INTO publisher (name, founded, headquarter) VALUES ('Electronic Arts', '01-05-1982', 'Redwood City, California');
INSERT INTO publisher (name, founded, headquarter) VALUES ('Rockstar Games', 'dec-98', 'New York City');
INSERT INTO publisher (name, founded, headquarter) VALUES ('Valve', 'maj-96', 'Bellevue Washington');

CREATE TABLE game(
	id serial PRIMARY KEY,
	name VARCHAR(50) UNIQUE NOT NULL,
	copies_sold VARCHAR(50) NOT NULL,
	writer VARCHAR(100) NOT NULL,
	release_date VARCHAR(50) NOT NULL,
	genre VARCHAR(50) NOT NULL,
	award VARCHAR(200) NOT NULL
);

CREATE TABLE developer(
	id serial PRIMARY KEY,
	name VARCHAR(50) UNIQUE NOT NULL,
	platform VARCHAR(100) NOT NULL,
	engine VARCHAR(100) NOT NULL
);