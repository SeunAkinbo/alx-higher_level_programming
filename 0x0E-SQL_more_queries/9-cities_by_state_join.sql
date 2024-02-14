-- Script that lists all cities contained in the databiase
SELECT cty.id, cty.name, sta.name
FROM cities cty, states sta
WHERE cty.state_id = sta.id
ORDER BY cty.id ASC;
