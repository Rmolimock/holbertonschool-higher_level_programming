#!/usr/bin/env mysql
-- list cities by id - city - state
SELECT DISTINCT cities.id, cities.name, states.name
FROM cities
JOIN states
ON cities.state_id = states.id

