-- $ sqlite3 words.db < words.sql

PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
DROP TABLE IF EXISTS words;

CREATE TABLE words (
    wordID INTEGER NOT NULL PRIMARY KEY,
    word VARCHAR NOT NULL,   -- VARCHAR maybe?//yeah we can do that and limit it to 5 cause thats the max limit of the word

);
