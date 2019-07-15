#!/usr/bin/env mysql
-- update the value of a row's attribute
UPDATE `second_table`
SET
`score` = 10
WHERE `second_table`.`name` = 'Bob'

