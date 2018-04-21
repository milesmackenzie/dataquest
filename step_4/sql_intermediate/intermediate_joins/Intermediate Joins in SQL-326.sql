## 2. Joining Three Tables ##

SELECT tr.track_id, tr.name track_name, mt.name track_type, il.unit_price, il.quantity 
FROM invoice_line il 
INNER JOIN track tr ON il.track_id = tr.track_id 
INNER JOIN media_type mt ON mt.media_type_id = tr.media_type_id 
WHERE il.invoice_id = 4;

## 3. Joining More Than Three Tables ##

SELECT tr.track_id, tr.name track_name, ar.name artist_name, mt.name track_type, il.unit_price, il.quantity
FROM invoice_line il 
INNER JOIN track tr ON il.track_id = tr.track_id 
INNER JOIN media_type mt ON mt.media_type_id = tr.media_type_id 
INNER JOIN album al ON al.album_id = tr.album_id
INNER JOIN artist ar ON ar.artist_id = al.artist_id
WHERE il.invoice_id = 4;

## 4. Combining Multiple Joins with Subqueries ##


SELECT
    ta.album_title album, ta.artist_name artist,
    COUNT(*) tracks_purchased
FROM invoice_line il
INNER JOIN (
            SELECT
                t.track_id,
                al.title album_title,
                ar.name artist_name
            FROM track t
            INNER JOIN album al ON al.album_id = t.album_id
            INNER JOIN artist ar ON ar.artist_id = al.artist_id
           ) ta
           ON ta.track_id = il.track_id
GROUP BY 1
ORDER BY 3 DESC LIMIT 5;

## 5. Recursive Joins ##

SELECT em.first_name || " " || em.last_name employee_name, em.title employee_title, em2.first_name || " " || em2.last_name supervisor_name, em2.title supervisor_title FROM employee em LEFT JOIN employee em2 ON em.reports_to = em2.employee_id ORDER BY 1;

## 6. Pattern Matching Using Like ##

SELECT first_name, last_name, phone FROM customer WHERE first_name LIKE "%Belle%";

## 7. Generating Columns With The Case Statement ##

SELECT 
    c.first_name || " " || c.last_name customer_name, 
    COUNT(iv.invoice_id) number_of_purchases, 
    SUM(iv.total) total_spent, 
    CASE 
        WHEN SUM(iv.total) < 40 THEN 'small spender' 
        WHEN SUM(iv.total) > 100 THEN 'big spender' 
        ELSE 'regular' 
        END
        AS customer_category
FROM invoice iv 
INNER JOIN customer c ON iv.customer_id = c.customer_id GROUP BY 1 ORDER BY 1;