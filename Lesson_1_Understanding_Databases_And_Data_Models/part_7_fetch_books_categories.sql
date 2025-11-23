SELECT books.title, categories.category_name
FROM books
JOIN categories ON books.category_id = categories.id;
