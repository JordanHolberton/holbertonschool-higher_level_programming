--  15.1. List the number of students who have each score in the second_table, ordered by the number of students who have each score in descending order.
SELECT score, COUNT(*) AS number 
FROM second_table
GROUP BY score
ORDER BY number DESC;