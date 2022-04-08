#! /usr/bin/env python3
import sqlite3
import json

def fetch_answers():
    listAnswers = [] # array to store game words
    answerID = 1
    file = open('answers.json')
    data = json.load(file)
    for i, answer in enumerate(data):
        # print(answer)
        eachAnswer = (answerID, answer)
        listAnswers.append(eachAnswer) # adds each answer to array
        answerID += 1
    # print(listAnswers)
    return listAnswers

def createDB(answers):
    connection = sqlite3.connect("answers.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE answers (answerID PRIMARY KEY, answer)")
    cursor.executemany("INSERT INTO answers VALUES (?, ?)",answers) 
    connection.commit()  # adds all of answers.json into answers.db


if __name__ == '__main__':
    answers = fetch_answers()
    createDB (answers)

