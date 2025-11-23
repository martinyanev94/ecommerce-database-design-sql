SELECT categories.category_name, COUNT(books.id) AS book_count
FROM categories
LEFT JOIN books ON categories.id = books.category_id
GROUP BY categories.category_name;
