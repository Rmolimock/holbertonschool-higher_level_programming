#!/usr/bin/env mysql
-- create a table with an id and name, where id can not be NULL
CREATE TABLE IF NOT EXISTS id_not_null
(id INT DEFAULT 1, name VARCHAR(256) NOT NULL)

