-- Script that lists all Comedy shows
SELECT ts.title
FROM tv_shows AS ts
INNER JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
INNER JOIN tv_genre AS tg ON tsg.genre_id = tg.id
WHERE tg.name = "Comedy"
ORDER BY ts.title;
