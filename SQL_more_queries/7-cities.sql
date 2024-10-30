-- Create a new table cities in the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE hbtn_0d_usa.cities (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id),
);