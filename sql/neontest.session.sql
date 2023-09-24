-- SELECT * FROM person WHERE email LIKE '%.com' ORDER BY date_of_birth
-- SELECT country_of_birth, COUNT(*) FROM person GROUP BY country_of_birth HAVING COUNT(*) > 5 ORDER BY count DESC
-- SELECT first_name, last_name, gender, country_of_birth, date_of_birth, EXTRACT(YEAR FROM AGE(NOW(),date_of_birth)) AS age FROM person ORDER BY age DESC AND ORDER BY date_of_birth
-- ALTER TABLE person ADD CONSTRAINT unique_email UNIQUE(email)
-- SELECT DISTINCT(gender) FROM person

-- ALTER TABLE person ADD CONSTRAINT gender_constraint CHECK(
--     gender= 'Genderqueer' OR gender= 'Bigender' OR gender= 'Genderfluid' OR gender= 'Male' OR gender= 'Polygender' OR gender= 'Non-binary'
--     OR gender= 'Female' OR gender= 'Agender')

-- DELETE FROM person WHERE gender = 'female'
-- UPDATE person SET email = "ogdon@gmail.com" WHERE first_name = 'Ogdon' AND last_name = 'Giabuzzi'

-- INSERT INTO person (id, first_name, last_name, email, gender, date_of_birth, country_of_birth) 
-- VALUES (1629,'Beverley', 'Lintill', 'blintillhf@list-manage.com.tw', 'Female', '1985-08-01', 'Portugal')
-- ON CONFLICT(id) DO NOTHING;
-- ON CONFLICT(id) DO UPDATE SET email = EXCLUDED.email