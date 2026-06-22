-- Revenue by Product Category

SELECT
    product_category,
    SUM(total_amount) AS revenue
FROM sales
GROUP BY product_category
ORDER BY revenue DESC;


-- Revenue by Gender

SELECT
    gender,
    SUM(total_amount) AS revenue
FROM sales
GROUP BY gender
ORDER BY revenue DESC;


-- Revenue by Age Group

SELECT
    age_group,
    SUM(total_amount) AS revenue
FROM sales
GROUP BY age_group
ORDER BY revenue DESC;
