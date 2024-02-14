-- Script that lists all shows
SELECT tv_show.title, tv_show_genre.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genre.genre_id ASC;
