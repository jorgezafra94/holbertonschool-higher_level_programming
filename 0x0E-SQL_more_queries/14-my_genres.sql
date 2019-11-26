-- double JOIN using 3 different tables
-- the idea is always get relations table-table and in that way
-- get the information that we need
-- in this example the connection is tv_show_genres.show_id because is used
-- in both JOINs
-- we dont put order by because by default use the ascendent form
SELECT tv_genres.name FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter";
