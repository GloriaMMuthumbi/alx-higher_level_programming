-- Displays the avaerage temperature by sity ordered by temperature (descending)
SELECT city,
	AVG(value) AS avg_temp
FROM temperatures
GROUP by CITY
ORDER BY avg_temp DESC;
