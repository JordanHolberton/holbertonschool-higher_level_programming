-- Create a new table cities in the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT NOT NULL FOREIGN KEY REFERENCES hbtn_0d_usa.states(id),
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL
);