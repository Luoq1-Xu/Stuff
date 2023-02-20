SELECT title
  FROM movies
 WHERE id IN
       (SELECT movie_id
       FROM (SELECT movie_id, COUNT(*) AS times
               FROM (SELECT movie_id
                       FROM stars
                      WHERE person_id IN
                            (SELECT id
                               FROM people
                              WHERE name = 'Johnny Depp'
                                 OR name = 'Helena Bonham Carter'))
                              GROUP BY movie_id)
         WHERE times > 1);