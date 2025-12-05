-- USE demosql;

-- CREATE TABLE menu_itmes (
-- 	menu_items_id INT PRIMARY KEY,
--     item_name VARCHAR(20),
--     category VARCHAR(20),
--     price INT
-- );

-- INSERT INTO menu_itmes (menu_items_id, item_name, category, price) VALUES
-- (101, 'Hamburger', 'American', 12.95),
-- (102, 'Cheeseburger', 'American', 13.95),
-- (103, 'Hot dog', 'American', 9.00),
-- (104, 'Veggie burger', 'American',  10.50),
-- (105, 'Mac and Cheese', 'American',  7.00),
-- (106, 'French fries', 'American', 7.00),
-- (107, 'Margretta pizza', 'Italian',  16.50),
-- (108, 'Soup', 'Thai',  4.00);

SELECT * FROM menu_itmes;

-- how many categories have a maximum price below $10?

-- 1a. What's the max price for the each category?
SELECT category, MAX(price) AS max_price
FROM menu_itmes
GROUP BY category;

-- 1b. How many maximum prices are below $10?
SELECT COUNT(*) FROM
	(SELECT category, MAX(price) AS max_price
	FROM menu_itmes
	GROUP BY category) AS mp
WHERE max_price < 10;

-- CTE (COMMON TABLE EXPRESSION)
WITH mp AS (SELECT category, MAX(price) AS max_price
	FROM menu_itmes
	GROUP BY category)
    
SELECT COUNT(*) FROM mp
WHERE max_price < 10;

-- CTE: Multiple expression
WITH mp AS (SELECT category, MAX(price) AS max_price
	FROM menu_itmes
	GROUP BY category)
    
SELECT COUNT(*) FROM mp
WHERE max_price < (SELECT AVG(max_price) FROM mp);

-- CTE: Multiple Tables
WITH mp AS (SELECT category, MAX(price) AS max_price
	FROM menu_itmes
	GROUP BY category),    
	ci AS (SELECT * FROM menu_itmes
			WHERE item_name LIKE '%burger%')
SELECT * FROM ci
LEFT JOIN mp ON ci.category = mp.category;

-- RECURSSIVE CTEs

-- CREATE TABLE stocks(
-- 	Date DATE,
--     price FLOAT
-- );

-- INSERT INTO stocks(Date ,price) VALUES
-- ('2024-06-01', 668.27),
-- ('2024-06-03', 678.83),
-- ('2024-06-04', 635.40),
-- ('2024-06-06', 591.01);

SELECT * FROM stocks;

WITH RECURSIVE my_dates(dt) AS (SELECT '2024-06-01'
									UNION ALL
                                    SELECT dt + INTERVAL 1 DAY
                                    FROM my_dates
                                    WHERE dt < '2024-06-06')
SELECT d.dt, COALESCE(s.price, LAG(price) OVER())
FROM my_dates d LEFT JOIN stocks s ON d.dt = s.date;