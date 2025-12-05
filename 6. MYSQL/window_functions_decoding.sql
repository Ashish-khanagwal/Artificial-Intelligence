-- USE demosql;

-- CREATE TABLE sales (
--     id INT PRIMARY KEY,
--     employee VARCHAR(10),
--     sale_amount DECIMAL(10,2),
--     sale_date DATE
-- );

-- INSERT INTO sales (id, employee, sale_amount, sale_date) VALUES
-- (1, 'A', 1000, '2024-01-01'),
-- (2, 'A', 1500, '2024-01-05'),
-- (3, 'A', 2000, '2024-01-12'),
-- (4, 'B', 800,  '2024-01-02'),
-- (5, 'B', 900,  '2024-01-06');

SELECT * FROM sales;

-- RANKING WINDOW FUNCTIONS
-- ROW_NUMBER()

SELECT employee, sale_amount,
	ROW_NUMBER() OVER(PARTITION BY employee ORDER BY sale_amount DESC) AS rn
FROM sales;

-- RANK()
SELECT employee, sale_amount,
	RANK() OVER(PARTITION BY employee ORDER BY sale_amount DESC)
FROM sales;
-- Example: if two rows tie for rank 1 → next rank will be 3.

-- DENSE_RANK()
SELECT employee, sale_amount,
	DENSE_RANK() OVER(PARTITION BY employee ORDER BY sale_amount DESC)
FROM sales;
-- Same as RANK() but does NOT skip numbers.

-- Aggregate Window Functions
-- SUM()
SELECT employee, sale_date, sale_amount,
	SUM(sale_amount) OVER(PARTITION BY employee ORDER BY sale_date) AS running_total
FROM sales;

-- AVG()
SELECT employee, sale_amount, sale_date,
	AVG(sale_amount) OVER(PARTITION BY employee ORDER BY sale_date ROWS 2 PRECEDING) AS moving_avg
FROM sales;
-- This takes average of current + previous 2 rows.

-- COUNT()
SELECT employee, COUNT(*) OVER(PARTITION BY employee)
FROM sales;

-- LAG() → Look at previous row
SELECT
    employee,
    sale_date,
    sale_amount,
    LAG(sale_amount) OVER(
        PARTITION BY employee ORDER BY sale_date
    ) AS previous_sale
FROM sales;
-- Used for: ✔ Day-to-day difference ✔ Compare current vs previous

-- LEAD() → Look at next row
SELECT
    employee,
    sale_date,
    sale_amount,
    LEAD(sale_amount) OVER(PARTITION BY employee ORDER BY sale_date) AS next_sale
FROM sales;

-- FIRST_VALUE()
SELECT
    employee,
    sale_date,
    sale_amount,
    FIRST_VALUE(sale_amount) OVER(
		PARTITION BY employee ORDER BY sale_date ) AS first_sale
FROM sales;
-- Gets first sale of each employee.

-- ALL COMBINED
SELECT
    employee,
    sale_date,
    sale_amount,
    SUM(sale_amount) OVER w AS running_total,
    AVG(sale_amount) OVER w AS running_avg,
    LAG(sale_amount) OVER w AS prev_sale,
    LEAD(sale_amount) OVER w AS next_sale
FROM sales
WINDOW w AS (PARTITION BY employee ORDER BY sale_date);