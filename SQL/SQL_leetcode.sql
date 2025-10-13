--197. Rising Temperature
SELECT w1.id
FROM Weather w1
JOIN Weather w2
  ON w1.recordDate = DATEADD(DAY, 1, w2.recordDate)
WHERE w1.temperature > w2.temperature;


--511. Game Play Analysis I
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;