USE startersql;

-- DELIMITER //
-- CREATE TRIGGER before_salary_update
-- BEFORE UPDATE ON users
-- FOR EACH ROW
-- BEGIN
-- IF NEW.salary < 10000 THEN
-- 	SET NEW.salary = 10000;
-- END IF;
-- END //

-- DELIMITER ;

UPDATE users SET salary = 5000 WHERE id = 1;