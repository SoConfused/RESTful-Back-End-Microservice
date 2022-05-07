from validatingservice import *
from checkingservice import *
from wotd import *
from answers import *
from valid import *
import sqlite3 
import json
import os


if __name__ == '__main__':
    # TO DO: INITIALIZE WORDS DB HERE
    wordList = word_list()
    createDBforWords(wordList)

    # initialize answers db
    answers = fetch_answers()
    createDBforAnswers(answers)

    # start new game
    user_input = 'y'
    while (user_input.lower() == 'y'):
        # initialize new word of the day for each new game
        wotd = get_wotd()
        createDB(wotd)
        # new game object
        game1 = Game("0", False, False, 6)

        # let user guess words for six tries in a game
        while game1.tries > 0: 
            game1.five = False
            game1.valid = False
            
            while game1.valid == False:
                isFive = game1.check_five() # check if player's guess is a five lettered word
                validWord = game1.validate_word() # check if player's guess is a valid word
            
            # prints out the letter and color associated to each valid guess
            word_dict = color_answer()
            for i in range(5):
                print(word_dict[i]['letter'] , " " , word_dict[i]['color'])
            
            # if user answers correct word, end the game
            if check_word() == True:
                break

            #Tracking.set_gamesPlayed(1) we got this?
    
    
        # deletes current game's files for the next game
        os.remove("guess.json")
        os.remove("wotd.db")

        # ask to play again
        '''display leaderboard'''
        print("play again? y/n")
        user_input = input()
    
    # end of game cleanup
    os.remove("answers.db") # deletes answers db
    os.remove("words.db")   # deletes words db