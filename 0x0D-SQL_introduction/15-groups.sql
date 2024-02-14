-- Script that lists all the number of
-- records of the table with same score
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score
ORDER BY score DESC;
