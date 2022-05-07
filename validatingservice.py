#! /usr/bin/env python3
import sqlite3 
import json

class Game:
    def __init__(self, guess, five, valid, tries):
        self.guess = guess.lower()
        self.five = five
        self.valid = valid
        self.tries = tries


    # this function asks the player for their guess
    def set_guess(self):
        print('Enter a 5 Letter Word')
        self.guess = input()
        return self.guess

    # this function checks to see if player's guess is a five lettered word
    def check_five(self):
        self.five = False
        while(self.five == False):
            self.guess = self.set_guess()
            if (len(self.guess) != 5):
                self.five = False
            else:
                self.five = True
        return self.five


    # this function checks to see if player's guess is a valid word
    #   that exists in words.db (our database of valid words)
    def validate_word(self):
        database_file = 'words.db'
        database = sqlite3.connect(database_file)
        cur = database.cursor()
        cur.execute(("SELECT * FROM words WHERE word= ?"), [self.guess])       
        if cur.fetchone():  
            print("Found!")
            self.valid = True
            self.tries -= 1
            with open("guess.json", "a") as outfile:
                json.dump(self.guess, outfile)
                outfile.write("\n")
        else:
            print("Not a valid word!")
            self.valid = False
        return self.valid


# USE FOLLOWING FOR TESTING validatingservice.py
# if __name__ == '__main__':
    # game1 = Game("0", False, False, 6)

    # isFive = game1.check_five()
    # validWord = game1.validate_word()
    # print(validWord)
    # print(game1.tries)

