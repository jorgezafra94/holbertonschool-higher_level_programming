-- using sub queries
-- in this case sub query "sub_q"
-- the sub query gets as atribute name as it is printed in the subprocess
-- like in this case titulo
SELECT tv_shows.title from tv_shows
LEFT JOIN
(SELECT tv_shows.title as titulo from tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = "Comedy"
GROUP BY tv_shows.title) sub_q ON tv_shows.title = sub_q.titulo
WHERE sub_q.titulo IS NULL
ORDER BY tv_shows.title ASC;
