CREATE TABLE system_metrics (
    id SERIAL PRIMARY KEY,
    metric_name VARCHAR(50),
    metric_value NUMERIC,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
