CREATE TABLE devices (
    id SERIAL PRIMARY KEY,
    device_name VARCHAR(50) NOT NULL,
    device_type VARCHAR(20) NOT NULL
);

CREATE TABLE connections (
    device_id_a INT REFERENCES devices(id),
    device_id_b INT REFERENCES devices(id),
    PRIMARY KEY (device_id_a, device_id_b)
);
WITH RECURSIVE reachable_devices AS (
    SELECT device_id_b
    FROM connections
    WHERE device_id_a = (SELECT id FROM devices WHERE device_name = 'Router1')
    
    UNION ALL
    
    SELECT c.device_id_b
    FROM connections c
    JOIN reachable_devices rd ON c.device_id_a = rd.device_id_b
)
SELECT d.device_name
FROM reachable_devices rd
JOIN devices d ON rd.device_id_b = d.id;
