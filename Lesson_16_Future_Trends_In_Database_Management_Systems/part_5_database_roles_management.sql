CREATE ROLE data_viewer;
GRANT SELECT ON sensitive_data TO data_viewer;

CREATE ROLE data_editor;
GRANT INSERT, UPDATE, DELETE ON sensitive_data TO data_editor;
