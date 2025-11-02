CREATE TABLE users (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
gender ENUM('Male', 'Female', 'Other'),
date_of_birth DATE,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (name, email, gender, date_of_birth)
VALUES
('Alice', 'alice@mail.com', 'Female', '2000-02-15'),
('Bob', 'bob@mail.com', 'Male', '1998-11-30'),
('Charlie', 'charlie@mail.com', 'Other', '2001-05-10');


USE startermysql;

SELECT * FROM users;

ALTER TABLE users ADD COLUMN is_active BOOLEAN DEFAULT true;

UPDATE users SET is_active = false WHERE is_active = true;

UPDATE users SET country = 'India' WHERE name = 'Bob';

ALTER TABLE users MODIFY COLUMN email VARCHAR(100) AFTER id;
