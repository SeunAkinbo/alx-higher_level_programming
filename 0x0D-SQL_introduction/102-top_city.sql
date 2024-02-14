-- Script that displays the top 3 of cities temperature 
-- during July and August ordered by temperature
SELECT city, AVG(value) AS avg_temp FROM
(SELECT city, month, value FROM temperatures
WHERE month=7 OR month=8) AS A
GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
