CREATE KEYSPACE social_media 
WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};

USE social_media;

CREATE TABLE profiles (
    user_id UUID PRIMARY KEY,
    username TEXT,
    email TEXT,
    website TEXT
);
INSERT INTO profiles (user_id, username, email) 
VALUES (uuid(), 'johndoe', 'johndoe@example.com');

INSERT INTO profiles (user_id, username, email, website) 
VALUES (uuid(), 'janesmith', 'janesmith@example.com', 'janesmith.com');
