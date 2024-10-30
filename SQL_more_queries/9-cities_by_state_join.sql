-- Join the tables cities and states to display all the cities with their corresponding state names.
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;