#!/usr/bin/env mysql
-- create database with table that has unique ID's for rows
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states
(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
name VARCHAR(256) NOT NULL);

