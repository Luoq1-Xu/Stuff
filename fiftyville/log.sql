-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Finding the crime scene report relating to the theft of the duck
SELECT description FROM crime_scene_reports WHERE description LIKE '%duck%';

-- Gathering info on the pertinent crime scene report
SELECT id,year,month,day,street FROM crime_scene_reports WHERE description IN (SELECT description FROM crime_scene_reports WHERE description LIKE '%duck%');



