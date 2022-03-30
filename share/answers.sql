sqlite3 answers.db < answers.sql

PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
DROP TABLE IF EXISTS answers;

CREATE TABLE answers (
    answerID INTEGER NOT NULL PRIMARY KEY,
    answer Char NOT NULL   -- VARCHAR maybe?//yeah we can do that and limit it to 5 cause thats the max limit of the word

);
