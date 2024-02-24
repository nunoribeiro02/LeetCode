SELECT product_name, year,price 
FROM Sales as s
INNER JOIN Product as p ON s.product_id = p.product_id;

-- Or

SELECT p.product_name, s.year, s.price
FROM Sales as s, Product as p
WHERE s.product_id = p.product_id;