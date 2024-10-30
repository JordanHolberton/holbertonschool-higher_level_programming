-- Order all the cities in the state of California by the cities.id value.
SELECT citiesid, cities.name;
FROM cities
WHERE cities.state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
    LIMIT 1
)
ORDER BY cities.id ASC;
