-- mysql -u username -p  databasename  < path/example.sql to import tables to database
-- get the max temperatures
SELECT state, MAX(value) as max_temp FROM temperatures
GROUP BY state
ORDER BY state;
