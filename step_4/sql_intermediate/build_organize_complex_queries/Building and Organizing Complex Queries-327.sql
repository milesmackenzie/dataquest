## 3. The With Clause ##

WITH sub AS
    (
     SELECT
         pl.playlist_id playlist_id,
         pl.name playlist_name,
         tr.name track_name,
         (tr.milliseconds / 1000) length_seconds
     FROM playlist pl
     LEFT JOIN playlist_track pltr ON pltr.playlist_id = pl.playlist_id
     LEFT JOIN track tr ON pltr.track_id = tr.track_id
    )

SELECT
    playlist_id,
    playlist_name,
    COUNT(track_name) number_of_tracks,
    SUM(length_seconds) length_seconds
FROM sub
GROUP BY 1, 2
ORDER BY 1;


## 4. Creating Views ##

CREATE VIEW chinook.customer_gt_90_dollars AS
     SELECT c.* FROM chinook.invoice i
     INNER JOIN chinook.customer c ON i.customer_id = c.customer_id
     GROUP BY 1
     HAVING SUM(i.total) > 90;

SELECT * FROM chinook.customer_gt_90_dollars;


## 5. Combining Rows With Union ##

SELECT * FROM customer_usa

UNION

SELECT * FROM customer_gt_90_dollars


## 6. Combining Rows Using Intersect and Except ##

WITH customers_usa_gt_90 AS
    (
     SELECT * FROM customer_usa

     INTERSECT

     SELECT * FROM customer_gt_90_dollars
    )

SELECT
    e.first_name || " " || e.last_name employee_name,
    COUNT(c.customer_id) customers_usa_gt_90
FROM employee e
LEFT JOIN customers_usa_gt_90 c ON c.support_rep_id = e.employee_id
WHERE e.title = 'Sales Support Agent'
GROUP BY 1 ORDER BY 1;


## 7. Multiple Named Subqueries ##

WITH
    india AS
        (
        SELECT * FROM customer
        WHERE country = "India"
        ),
    sales AS
        (
         SELECT
             customer_id,
             SUM(total) total
         FROM invoice
         GROUP BY 1
        )

SELECT
    india.first_name || " " || india.last_name customer_name,
    sales.total total_purchases
FROM india
INNER JOIN sales ON india.customer_id = sales.customer_id
ORDER BY 1;


## 8. Challenge: Each Countrys Best Customer ##

WITH
    customers AS
        (SELECT c.first_name || " " || c.last_name customer_name,
         c.customer_id customer_id,
         c.country country
         FROM customer c
         GROUP BY 1
        ),
    purchased AS
        (SELECT customer_id,
         SUM(total) total_purchased
         FROM invoice
         GROUP BY 1
        ),
    max_purchase AS
        (SELECT c.country, c.customer_name, total_purchased
         FROM customers c
         INNER JOIN purchased p ON p.customer_id = c.customer_id
         ORDER BY 3
        )

SELECT * FROM max_purchase
GROUP BY 1
ORDER BY 1;
