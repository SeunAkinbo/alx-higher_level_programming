-- Script that lists all shows
SELECT show.title, genre.genre_id
FROM tv_shows show, tv_show_genres genere
JOIN genre ON show.id = genre.show_id
ORDER BY show.title ASC, genre.genre_id ASC;
