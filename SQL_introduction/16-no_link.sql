-- 16. Select the score and name of all the players who have a name that is not an empty string, ordered by score in descending order.
SELECT score, name 
FROM second_table
WHERE name != ""
ORDER BY score DESC;
