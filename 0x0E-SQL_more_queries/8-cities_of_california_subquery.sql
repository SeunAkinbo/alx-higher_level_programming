-- Script that lists cities
SELECT cty.id, cty.name FROM cities cty, states sta
WHERE cty.id = sta.id
ORDER BY cty.id ASC;
