SELECT AVG(temperature) FROM device_temperatures 
WHERE device_id = <your_device_id>
AND timestamp >= '2023-09-01' AND timestamp <= '2023-09-30';
