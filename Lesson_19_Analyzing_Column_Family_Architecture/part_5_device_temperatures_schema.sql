CREATE TABLE device_temperatures (
    device_id UUID,
    timestamp TIMESTAMP,
    temperature FLOAT,
    status TEXT,
    PRIMARY KEY (device_id, timestamp)
);
INSERT INTO device_temperatures (device_id, timestamp, temperature, status) 
VALUES (uuid(), '2023-09-15T10:00:00', 22.5, 'ONLINE');
