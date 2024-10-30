-- Create a new database and a new user for it.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user0_d_2' IDENTIFIED BY 'user0_d_2_pwd';

GRANT SELECT ON hbtn_0d_2.* TO 'user0_d_2'@'localhost';