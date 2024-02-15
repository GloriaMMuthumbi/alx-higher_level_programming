-- Displays the top 3 of cities temperature during July and Argust ordered descending temperature
SELECT cuty,
	AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7
	or MONTH = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;