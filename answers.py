#! /usr/bin/env python3
import sqlite3
import json

# this function grabs all possible answers from answers.json and saves it to a list
def fetch_answers():
    listAnswers = [] # array to store all possible game answers
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

# this function saves list of all possible answers to answers.db
def createDBforAnswers(answers):
    connection = sqlite3.connect("answers.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE answers (answerID PRIMARY KEY, answer)")
    cursor.executemany("INSERT INTO answers VALUES (?, ?)",answers) 
    connection.commit()  # adds all of answers.json into answers.db

# USE FOLLOWING FOR TESTING answers.py
if __name__ == '__main__':
    answers = fetch_answers()
    print(answers)