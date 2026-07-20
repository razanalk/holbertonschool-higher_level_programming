-- Lists records with a valid name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
