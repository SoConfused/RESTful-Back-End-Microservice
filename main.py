from validatingservice import *
from checkingservice import *
from wotd import *
import sqlite3 
import json
import os

 
if __name__ == '__main__':
    user_input = 'y'
    while (user_input.lower() == 'y'):
        wotd = get_wotd()
        createDB(wotd) # everytime the program is ran a new "Word of the Day" is created

        game1 = Game("0", False, False, 6)

        while game1.tries > 0: 
            game1.five = False
            game1.valid = False
            isFive = game1.check_five()
            validWord = game1.validate_word()
            word_dict = color_answer()
            for i in range(5):  # prints out the letter and color associated to each valid guess
                print(word_dict[i]['letter'] , " " , word_dict[i]['color'])
            if check_word() == True:
                break
        
        # deletes current game's files for the next game
        os.remove("guess.json")
        os.remove("wotd.db")
        print("play again? y/n")
        user_input = input()

    