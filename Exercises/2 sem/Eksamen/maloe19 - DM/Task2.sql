CREATE TABLE movies_credit(
id serial PRIMARY KEY,
actors VARCHAR(50) NOT NULL,
directors VARCHAR(50) NOT NULL
);

CREATE TABLE movies_dates(
id serial PRIMARY KEY,
release_year integer NOT NULL,
box_office_date VARCHAR(100) NOT NULL
);

CREATE TABLE movies_info(
id serial PRIMARY KEY,
title VARCHAR(50) NOT NULL,
genre VARCHAR(100) NOT NULL
);