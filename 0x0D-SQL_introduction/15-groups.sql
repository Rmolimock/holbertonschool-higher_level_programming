#!/usr/bin/env mysql
-- list number of records with same score
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score DESC

