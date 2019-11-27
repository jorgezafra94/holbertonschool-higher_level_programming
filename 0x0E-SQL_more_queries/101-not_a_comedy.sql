-- using sub queries
-- in this case sub query "sub_q"
-- the sub query gets as atribute name as it is printed in the subprocess
-- like in this case titulo
SELECT tv_shows.title FROM tv_shows
LEFT JOIN
(SELECT tv_shows.title FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = "Comedy") sub_q ON tv_shows.title = sub_q.title
WHERE sub_q.title IS NULL
ORDER BY tv_shows.title ASC;
