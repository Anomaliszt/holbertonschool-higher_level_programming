-- Desc: Display the name of the player with the highest score in the second_table.
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BY `score` DESC;