-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Finding the crime scene report relating to the theft of the duck
SELECT description FROM crime_scene_reports WHERE description LIKE '%duck%';

-- Gathering info on the pertinent crime scene report
SELECT id,year,month,day,street FROM crime_scene_reports WHERE description IN (SELECT description FROM crime_scene_reports WHERE description LIKE '%duck%');

-- Now we know the crime occured in 2021 , 7th month, 28 day on Humphrey Street

-- Getting all interviews on the date of the theft
SELECT name, transcript FROM interviews WHERE year =2021 AND month = 7 AND day = 28;

-- Ruth, Eugene and Raymond provide useful information relating to the theft.

--



