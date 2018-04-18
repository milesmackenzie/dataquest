## 1. Query that returns all columns from the facts and cities tables ##

SELECT * FROM facts INNER JOIN cities ON cities.facts_id = facts.id LIMIT 10;

## 2. Query that foins facts to cities and the name column
from facts aliased to country_name ##

SELECT c.*, f.name country_name FROM facts f INNER JOIN cities c ON f.id = c.facts_id LIMIT 5;

## 3. Query returning column of contry names and column of countrys capitals ##

SELECT f.name country, c.name capital_city FROM facts f INNER JOIN cities c ON f.id = c.facts_id WHERE c.capital =1;

### 4. Using LEFT JOIN to explore contries in the facts table that do not
 exist in the cities table ##

 SELECT f.name country, f.population FROM facts f LEFT JOIN cities c ON f.id = c.facts_id WHERE c.name is NULL;

## 5. Query returning the 10 capital cities with the highest population. ##

SELECT c.name capital_city, f.name country, c.population FROM facts f LEFT JOIN cities c ON f.id = c.facts_id WHERE c.capital = 1 ORDER BY 3 desc LIMIT 10;

## 6. Using join and Subquery that returns capital cities with populations > 10 million. ##

SELECT c.name capital_city, f.name country, c.population population FROM facts f INNER JOIN (SELECT * FROM cities WHERE capital = 1 AND population > 10000000) c ON c.facts_id = f.id ORDER BY 3 DESC;

## 7. Writing query to find the countries where the urban center (city) population is more than half of the country's total population. ##

SELECT f.name country, c.urban_pop, f.population total_pop, CAST(c.urban_pop as float) / CAST(f.population as float) urban_pct FROM facts f INNER JOIN (SELECT facts_id, SUM(population) urban_pop FROM cities GROUP BY 1) c ON f.id = c.facts_id WHERE urban_pct > 0.5 ORDER BY 4 ASC;
