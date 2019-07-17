#!/usr/bin/env mysql
-- list cities tables where state name is California
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;

