-- Since we are checking different column, UNION is more efficient than OR
SELECT name, population, area
FROM World
WHERE area >= 3000000 
UNION
SELECT name, population, area
FROM World
WHERE population >= 25000000 