BEGIN;

SELECT article_text
FROM articles
WHERE article_id = 456
FOR UPDATE;

-- Potential modification of the article's content

UPDATE articles
SET article_text = 'Updated Article Text'
WHERE article_id = 456;

COMMIT;
