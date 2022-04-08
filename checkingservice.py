#! /usr/bin/env python3
import sqlite3 
import json

#checks if guesses is the word of the day based off of the wotd.db.
#   This function opens guess.json (storage of a user's guess) 
#   and returns the last word in the file (most recent guess)
def fetch_guess():
    with open('guess.json') as file:
        data = json.loads(file.readlines()[-1])
    return data

# function opens word of the day database to get the game's answer
def get_answer():
    database_file = 'wotd.db'
    database = sqlite3.connect(database_file)
    cur = database.cursor()
    cur.execute("SELECT answer FROM answers")
    answer = cur.fetchone()
    str = ''.join(answer)
    database.close()
    return str

# function compares player's guess with game's answer.
#   Returns true if player's guess is correct
def check_word():
    guess = fetch_guess()
    answer = get_answer()
    if guess == answer:  
        print("Correct Answer")
        valid = True
    else:
        print("Wrong Answer")
        valid = False
    return valid

# this function checks each letter in the player's guess to
#   check if the letters
#   1. don't exist in the answer = grey
#   2. exists in the answer and is in the correct position = green
#   3. exists in the answer but is in wrong position = yellow
def color_answer():
    guess = fetch_guess()
    answer = get_answer()

    word_color = {0: {'letter': None, 'color': None}, 
                  1: {'letter': None, 'color': None}, 
                  2: {'letter': None, 'color': None}, 
                  3: {'letter': None, 'color': None}, 
                  4: {'letter': None, 'color': None}}   
    # Loops through the user_word and checks with the WOTD and assigning the correct color
    for character, i in zip(guess, range(0, len(guess))):
        if answer.find(character) == -1:
            word_color[i]['letter'] = character
            word_color[i]['color'] = 'Grey'
        elif answer.find(character) == guess.find(character):
            word_color[i]['letter'] = character
            word_color[i]['color'] = 'Green'
        else:
            word_color[i]['letter'] = character
            word_color[i]['color'] = 'Yellow'

    return word_color

# USE FOLLOWING FOR TESTING checkingservice.py
# if __name__ == '__main__':
    # data = fetch_guess()
    # valid = check_word()
    # print(data)
    # print(valid)
    # print(color_answer())
    # color_answer()
    
