CREATE DATABASE library;

\c library 

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    published_year INT
);
