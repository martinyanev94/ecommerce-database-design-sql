ALTER TABLE books
ALTER COLUMN title SET NOT NULL;

ALTER TABLE books
ADD CONSTRAINT valid_year CHECK (published_year > 0);
