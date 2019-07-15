#!/usr/bin/env mysql
-- list records with name by score in descending order
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC

