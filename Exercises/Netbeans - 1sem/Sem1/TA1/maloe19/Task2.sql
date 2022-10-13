-- Insert your SQL code from Task 2 into this document. Please read "Assignments and instructions.pdf" for instructions.
CREATE TABLE person(
	id serial PRIMARY KEY,
	person_name VARCHAR(50) NOT NULL,
	age integer NOT NULL,
	street_name VARCHAR(50) UNIQUE NOT NULL,
	city VARCHAR(50) UNIQUE NOT NULL,
	zip integer UNIQUE NOT NULL
);

CREATE TABLE award(
	id serial PRIMARY KEY,
	award_name VARCHAR(50) NOT NULL,
	award_year integer NOT NULL
);

CREATE TABLE artist(
	id serial PRIMARY KEY,
	stage_name VARCHAR(50) NOT NULL
);

CREATE TABLE producer(
	id serial PRIMARY KEY,
	stage_name VARCHAR(50) NOT NULL
);

CREATE TABLE album(
	id serial PRIMARY KEY,
	album_name VARCHAR(50) NOT NULL,
	album_year integer NOT NULL
);

CREATE TABLE genre(
	id serial PRIMARY KEY,
	genre_name VARCHAR(50) NOT NULL
);

CREATE TABLE song(
	id serial PRIMARY KEY,
	song_name VARCHAR(50) NOT NULL
);
