#! /usr/bin/env python3
import sqlite3
import json
import re
import os

# this function goes through a master word file,
#   removes invalid words,
#   and saves each word in a list
def word_list():
     listWords = []
     wordID = 1
     file = open("/usr/share/dict/words") # opens master list
     for line in file.readlines():
        lowerLine = line.lower() # change word in master list to lowercase
        # currentWord = re.findall(r'\b(\w{6})\b', lowerLine)
        # eachWord = (wordID , currentWord)
        # listWords.append(eachWord)
        # wordID += 1
        listWords += re.findall(r'\b(\w{6})\b', lowerLine)
     print(listWords)
     return listWords


# this function saves the final word list with all invalid words removed
#   to answers.db database
def createDBforWords(wordList):
    connection = sqlite3.connect("words.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE words (word)")
    cursor.executemany("INSERT INTO words VALUES (?)",wordList) ######
    connection.commit()  
    connection.close()

# USE FOLLOWING FOR TESTING answers.py
if __name__ == '__main__':
    os.remove("words.db")
    wordList = word_list()
    createDBforWords (wordList)





