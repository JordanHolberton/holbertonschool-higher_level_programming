-- 1. Create a user with the name user0_d_1 and password user0_d_1_pwd. Grant all privileges on all databases to this user. If the user already exists, do not throw an error.
CREATE USER IF NOT EXISTS 'user0_d_1' IDENTIFIED BY 'user0_d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user0_d_1'@'localhost';