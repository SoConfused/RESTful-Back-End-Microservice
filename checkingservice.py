#! /usr/bin/env python3
import sqlite3 
import json

#checks if guesses is the word of the day based off of the wotd.db

def fetch_guess():
    with open('guess.json') as file:
        data = json.loads(file.readlines()[-1])

    return data

def validate_word():
    guess = fetch_guess()
    database_file = 'wotd.db'
    database = sqlite3.connect(database_file)
    cur = database.cursor()
    #SELECT * FROM SAMPLE_TABLE ORDER BY ROWID ASC LIMIT 1
    # cur.execute(("SELECT * FROM answers WHERE answer= ?"), [guess])
    cur.execute(("SELECT * FROM answers WHERE answer = ?"), [guess])
    #print("user_input: ", row[0])
    if cur.fetchone():  
        print("Correct Answer")
        valid = True
    else:
        print("Wrong Answer")
        valid = False
    return valid

if __name__ == '__main__':
    data = fetch_guess()
    valid = validate_word()
    print(data)
    print(valid)
    
