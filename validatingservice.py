#! /usr/bin/env python3
import sqlite3 
import json

# use answers.db

class Game:
    def __init__(self, guess, five, valid, tries):
        self.guess = guess
        self.five = five
        self.valid = valid
        self.tries = tries

    def set_guess(self):
        print('Enter a 5 Letter Word')
        self.guess = input()
        return self.guess
#this looks familiar, we will need self in every function

    def check_five(self):
        while(self.five == False):
            self.guess = self.set_guess()
            if (len(self.guess) != 5):
                self.five = False
            else:
                self.five = True
        return self.five

    def validate_word(self):
        database_file = 'answers.db'
        database = sqlite3.connect(database_file)
        cur = database.cursor()
        cur.execute(("SELECT * FROM answers WHERE answer= ?"), [self.guess])
        if cur.fetchone():  
            print("Found!")
            self.valid = True
            self.tries -= 1
            with open("guess.json", "a") as outfile:
                json.dump(self.guess, outfile)
                outfile.write("\n")
        else:
            print("Not a valid word, loser!")
            self.valid = False
        #asdf = cur.fetchone()
        #if (asdf == guess)
        return self.valid


if __name__ == '__main__':
    game1 = Game("0", False, False, 6)

    isFive = game1.check_five()
    validWord = game1.validate_word()
    print(validWord)
    print(game1.tries)
