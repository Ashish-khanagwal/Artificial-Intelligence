USE startersql;

-- DELIMITER //
-- CREATE PROCEDURE AddUser(
-- IN p_name VARCHAR(150),
-- IN p_email VARCHAR(200),
-- IN p_gender ENUM('Male', 'Female', 'Other'),
-- IN p_dob DATE,
-- IN p_salary INT
-- )

-- BEGIN
-- INSERT INTO users (name, email, gender, date_of_birth, salary)
-- VALUES (p_name, p_email, p_gender, p_dob, p_salary);
-- SELECT * FROM users;
-- END //
-- DELIMITER ;

-- CALL AddUser('Ashish', 'ashish@gmail.com', 'Male', '2001-01-12', 80000); 
-- SHOW PROCEDURE STATUS WHERE Db = 'startersql'; 

-- DELIMITER //

-- CREATE TRIGGER after_user_inserted
-- AFTER INSERT ON users
-- FOR EACH ROW
-- BEGIN
-- INSERT INTO user_log(user_id, name)
-- VALUES(NEW.id, NEW.name);
-- END //

-- DELIMITER ;

-- INSERT INTO users (name, email, gender, date_of_birth, salary) VALUES
-- ('Manish', 'Manish@gmail.com', 'Male', '2002-08-24', 70000);
