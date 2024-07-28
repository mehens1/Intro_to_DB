-- -- Use the specified database
-- USE alx_book_store;

-- -- Print the full description of the table books
-- SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA
-- FROM information_schema.COLUMNS
-- WHERE TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'Books';

-- Use the specified database
USE alx_book_store;

-- Print the full description of the table books
SHOW CREATE TABLE Books;
