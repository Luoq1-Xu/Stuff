-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Finding the crime scene report relating to the theft of the duck
SELECT description
  FROM crime_scene_reports
 WHERE description
  LIKE '%duck%';

-- Getting all interviews on the date of the theft
SELECT name,
       transcript
  FROM interviews
 WHERE year = 2021
   AND month = 7
   AND day = 28;

-- Ruth, Eugene and Raymond provide useful information relating to the theft.

-- Let's Follow Eugene's Lead

-- Check for all transactions on that day
SELECT account_number, amount , transaction_type
  FROM atm_transactions
 WHERE year = 2021
   AND month = 7
   AND day = 28
   AND atm_location = 'Leggett Street'
   AND transaction_type = 'withdraw';

-- 1 : Get a list of possible suspects based on Eugene's lead
SELECT name
  FROM people
 WHERE id IN
       (SELECT person_id
          FROM bank_accounts
         WHERE account_number IN
               (SELECT account_number
                  FROM atm_transactions
                 WHERE year = 2021
                   AND month = 7
                   AND day = 28
                   AND atm_location = 'Leggett Street'
                   AND transaction_type = 'withdraw'));

-- Now let's try Raymond's Lead

-- 2 : List of possible suspects based on Raymond's Lead
SELECT name
  FROM people
 WHERE phone_number IN
       (SELECT caller
          FROM phone_calls
         WHERE year = 2021
           AND month = 7
           AND day = 28
           AND duration < 60 );

-- Now let's try Ruth's Lead

-- Possible license plates of cars that fit the bill
SELECT license_plate
  FROM bakery_security_logs
 WHERE year = 2021
   AND month = 7
   AND day = 28
   AND hour = 10
   AND minute BETWEEN 15 AND 25
   AND activity = 'exit';

-- 3 : Names of the owners of the possible vehicles
SELECT name
  FROM people
 WHERE license_plate IN
       (SELECT license_plate
          FROM bakery_security_logs
         WHERE year = 2021
           AND month = 7
           AND day = 28
           AND hour = 10
           AND minute BETWEEN 15 AND 25
           AND activity = 'exit');


-- Let's go back to Raymond's clue about the flight

-- Earliest Possible Flight out of fiftyville on 29-7-2021
SELECT id
 FROM flights
WHERE origin_airport_id IN
      (SELECT id
         FROM airports
        WHERE city = 'Fiftyville')
  AND year = 2021
  AND month = 7
  AND day = 29
ORDER BY hour,minute LIMIT 1;

-- 4 : Passengers on that flight
SELECT name
  FROM people
 WHERE passport_number IN
       (SELECT passport_number
          FROM passengers
         WHERE flight_id IN
               (SELECT id
                  FROM flights
                 WHERE origin_airport_id IN
                       (SELECT id
                          FROM airports
                         WHERE city = 'Fiftyville')
                   AND year = 2021
                   AND month = 7
                   AND day = 29
                 ORDER BY hour,minute LIMIT 1));

-- Now let's try to see if there are overlaps between 1, 2, 3 and 4 which would give us the thief.
SELECT name
  FROM people
 WHERE name IN
       (SELECT name
          FROM people
         WHERE id IN
               (SELECT person_id
                  FROM bank_accounts
                 WHERE account_number IN
                       (SELECT account_number
                          FROM atm_transactions
                         WHERE year = 2021
                           AND month = 7
                           AND day = 28
                           AND atm_location = 'Leggett Street'
                           AND transaction_type = 'withdraw')))
   AND name IN (SELECT name
                  FROM people
                 WHERE phone_number IN
                       (SELECT caller
                          FROM phone_calls
                         WHERE year = 2021
                           AND month = 7
                           AND day = 28
                           AND duration < 60 ))
   AND name IN (SELECT name
                  FROM people
                 WHERE license_plate IN
                       (SELECT license_plate
                          FROM bakery_security_logs
                         WHERE year = 2021
                           AND month = 7
                           AND day = 28
                           AND hour = 10
                           AND minute BETWEEN 15 AND 25
                           AND activity = 'exit'))
   AND name IN (SELECT name
                  FROM people
                 WHERE passport_number IN
                       (SELECT passport_number
                          FROM passengers
                         WHERE flight_id IN
                               (SELECT id
                                  FROM flights
                                 WHERE origin_airport_id IN
                                       (SELECT id
                                          FROM airports
                                         WHERE city = 'Fiftyville')
                                           AND year = 2021
                                           AND month = 7
                                           AND day = 29
                                         ORDER BY hour,minute LIMIT 1)));

-- Aha! Bruce is the thief! Now we know this, we can work back to determine his accomplice and the city he escaped to.

-- Let's find the city he escaped to first.
SELECT city FROM airports WHERE id IN (SELECT destination_airport_id FROM flights WHERE id IN (SELECT id
  FROM flights
  WHERE origin_airport_id IN
     (SELECT id
        FROM airports
       WHERE city = 'Fiftyville')
 AND year = 2021
 AND month = 7
 AND day = 29
ORDER BY hour,minute LIMIT 1));

-- Tada! The thief escaped to New York City.

-- Now, the Accomplice.
SELECT name
  FROM people
 WHERE phone_number IN
       (SELECT receiver
          FROM phone_calls
         WHERE caller IN
               (SELECT phone_number
                  FROM people
                 WHERE name = 'Bruce')
           AND year = 2021
           AND month = 7
           AND day = 28
           AND duration < 60);

-- So, now we finally know that the Thief is Bruce, his accomplice is Robin, and the city he escaped to is New York City. Yay!