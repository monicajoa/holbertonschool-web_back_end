-- We are all unique! (Task 0)
-- Creates a table users with the attributes (id, email, name)
CREATE table IF NOT EXIST users (
    id PRIMARY KEY INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
