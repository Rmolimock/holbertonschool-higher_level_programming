#!/usr/bin/env mysql
-- create table with a unique ID
CREATE TABLE IF NOT EXISTS unique_id
(id INT DEFAULT 1 UNIQUE, name VARCHAR(256) NOT NULL)

