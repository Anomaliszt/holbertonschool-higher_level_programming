-- Desc: This script is used to group data in a table by a specific column.
SELECT 'score', COUNT(*) AS 'number' FROM 'second_table' GROUP BY 'score' ORDER BY 'number' DESC;