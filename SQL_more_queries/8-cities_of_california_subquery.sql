-- Desc: Display the id and name of all cities in the state of California, ordered by id.
SELECT `id`, `name` FROM `cities` WHERE `state_id` IN (SELECT `id` FROM `states` WHERE `name` = "California") ORDER BY `id`;
