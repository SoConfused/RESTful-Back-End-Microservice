'''
Create a RESTful microservice for tracking user wins and losses. 

Your service should expose the following operations:
>> Posting a win or loss for a particular game, along with a timestamp and number of guesses.
>> Retrieving the statistics for a user. 
    If you visit Wordle, open your browser’s developer tools, 
    and examine local storage for the entry nyt-wordle-statistics, 
    you’ll see that it uses the following format, 
    which your service should also return:
{
    "currentStreak": 4,
    "maxStreak": 5,
    "guesses":{
        "1": 0,
        "2": 0,
        "3": 2,
        "4": 3,
        "5": 4,
        "6": 2,
        "fail": 1
    },
    "winPercentage": 90,
    "gamesPlayed": 10,
    "gamesWon": 9,
    "averageGuesses": 5
}
    Note: the names "1" through "6" are not valid identifiers for class members in Python, 
    so if you are returning a Pydantic model as a response 
    you will need to use Field customization to set an alias for each of these.
>> Retrieving the top 10 users by number of wins
>> Retrieving the top 10 users by longest streak

As with Project 2, your service should be implemented using RESTful principles.
'''

#! /usr/bin/env python3
import sqlite3 
import json
from validatingservice import Game

class Tracking:
    #def __init__(self, currentStreak, maxStreak, guesses, winPercentage, gamesPlayed, gamesWon, averageGuesses):
    def __init__(self, guesses = Game.set_numGuesses(Game), gamesWon,):
        self.guesses = guesses
        #self.currentStreak = currentStreak
        #self.maxStreak = maxStreak
        #self.winPercentage = winPercentage
        #self.gamesPlayed = gamesPlayed
        self.gamesWon = gamesWon
        #self.averageGuesses = averageGuesses

    # this function checks to see if player's guess is a valid word
    #   that exists in words.db (our database of valid words)
    def win_loss(self):
        with open("win_loss.json", "a") as outfile:
            json.dump(self.currentStreak, self.maxStreak, self.guesses, self.winPercentage, self.gamesPlayed, self.gamesWon, self.averageGuesses,)
            outfile.write("\n")
        
        return self.guesses

if __name__ == '__main__':
    bleh = Tracking()
    print(bleh.guesses)
    