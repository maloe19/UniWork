CREATE TABLE privatkunder(
id serial PRIMARY KEY,
_name VARCHAR (50) NOT NULL,
cpr_nummber integer UNIQUE NOT NULL,
telefon_nummber integer UNIQUE NOT NULL,
e-mail VARCHAR (355) UNIQUE NOT NULL
);

CREATE TABLE erhvervkunder(
id serial PRIMARY KEY,
_name VARCHAR (50) NOT NULL,
cpr_nummber integer UNIQUE NOT NULL,
telefon_nummber integer UNIQUE NOT NULL,
email VARCHAR (355) UNIQUE NOT NULL,
cvr_nummer integer UNIQUE NOT NULL,
firma_telefon_nummber integer UNIQUE NOT NULL,
firmanavn VARCHAR (50) UNIQUE NOT NULL,
);

CREATE TABLE kørekort(
id serial PRIMARY KEY,
privatbil VARCHAR (355) NOT NULL,
taxakørekort VARCHAR (355) NOT NULL
);

CREATE TABLE køretime(
id serial PRIMARY KEY,
kørelærer VARCHAR (50) NOT NULL,
længde integer NOT NULL,
dato TIMESTAMP NOT NULL
);

CREATE TABLE testforsøg(
id serial PRIMARY KEY,
teori VARCHAR (355) NOT NULL,
praksis VARCHAR (355) NOT NULL
);