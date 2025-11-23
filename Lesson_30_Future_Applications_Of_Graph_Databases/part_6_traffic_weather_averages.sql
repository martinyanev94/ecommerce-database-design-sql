SELECT ts.device_id, ws.device_id, AVG(ts.data_reading) AS average_traffic, AVG(ws.data_reading) AS average_weather
FROM traffic_sensors ts
JOIN weather_sensors ws ON ts.location = ws.location
GROUP BY ts.device_id, ws.device_id;
