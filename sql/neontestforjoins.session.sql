-- UPDATE person SET car_id = 1 WHERE id = 1;
-- SELECT * FROM person WHERE car_id IS NOT NULL;

-- SELECT * FROM person 
-- LEFT JOIN cars ON person.car_id = cars.id
-- WHERE car.* IS NOT NULL;

SELECT * FROM person 
JOIN cars ON person.car_id = cars.id ORDER BY car_id;

\copy (SELECT * FROM person JOIN cars ON person.car_id = cars.id ORDER BY car_id) TO './result.csv' DELIMITER ',' CSV HEADER;