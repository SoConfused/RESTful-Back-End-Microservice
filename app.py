import sqlite3
import logging.config
import typing
import contextlib
import random

from typing import Optional
from xml.dom.minidom import CharacterData
from fastapi import FastAPI, Depends, Response, HTTPException, status
from pydantic import BaseModel, BaseSettings


class Settings(BaseSettings):
    database: str
    logging_config: str

    class Config:
        env_file = ".env"

class words(BaseModel):
    wordID: int
    word: str

class answers(BaseModel):  
    answerID: int
    answer: str

def get_db():
    with contextlib.closing(sqlite3.connect(settings.database)) as db:
        db.row_factory = sqlite3.Row
        yield db

def get_logger():
    return logging.getLogger(__name__)

app = FastAPI()
settings = Settings()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/words/{wordid}")
def read_words(word_id: int, word_str: Optional[str] = None):
    return {"item_id": word_id, "word": word_str}

@app.get("/answers/{answerkey}")
def get_answer_key(answer: str, db: sqlite3.Connection = Depends(get_db)):
    wotd_key = random.randrange(2308) # Get value for Word of the Day
    return wotd_key
    
# The word validation service should expose the following operations:
# Checking if a guess is a valid five-letter word
# Adding and removing possible guesses   (lets focus with just words and just remove guesses user's made)

def validate_word(word: str, db: sqlite3.Connection = Depends(get_db)):  # Check valid word
    cur = db.execute("SELECT * FROM words WHERE id = ? LIMIT 1", [word])
    words = cur.fetchall()
    if not words:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Word not found"
        )
    return {"words": words}

# The answer checking service should expose the following operations:
# Checking a valid guess against the answer for the current day.
# If the guess is incorrect, the response should identify the letters that are:
# in the word and in the correct spot,
# in the word but in the wrong spot, and
# not in the word in any spot

# Changing the answers for future games.

def check_answer(word: str, answer: str, db: sqlite3.Connection = Depends(get_db)): # checks if word is the answer/compares the word to the answer
    user_word = validate_word(word, db)  # valid word user inputs 
    answer_key = get_answer_key(answer, db) #Returns WOTD key -> designate the "Answer"
    answer_word = # access answers.db and get the actual word 
    #Loop to see each character between user_word vs answer_word
    # sepeerate user_word for ecah char use a single answer
    '''my_string = "Python"
    tokens = list(my_string)
    print("String tokens are: ", tokens)
    print(tokens[0])'''
    
    for character in user_word:
        for letter in answer_word:
            if user_word[character] = answer_word[letter]: #green = 0 (right character right spot)
                user_word[len(character) = answer_word[0] -> Green
            if #yellow = 1 (right character wrong spot)
                user_word[0] = answer_word[1] or user_word[0] = answer_word[2]  -> Yellow 
            if # grey = 2 (wrong character)
    
    for character in answer_word:
        if 

        
        #check if:
        #exists and in the correct spot
        #exists and in the wrong spot
        #does not exist in the word


# for letter in answer word:
#    


# # Dictionary Built-in Functions
# squares = {0: P, 1: A, 2: T, 3: T, 4: Y, 5: Y}

# # Output: T
# print(squares.get(2))

# word_color = {
#          0 : {
#   "letter" : "A",
#     "color": 'white' # we will update with the syntax word[0]['color'] = Yellow 
#   },
#          1 : {
#    "letter": "B",
#    "color" : "white"
#   },
#           
# }

    # '''my_string = "Python"
    # tokens = list(my_string)
    # print("String tokens are: ", tokens)
    # print(tokens[0])'''
    

word[0]["letter"] = user_word[0]
word[1]["letter"] = user_word[1]
word[2]["letter"] = user_word[2]
word[3]["letter"] = user_word[3]
word[4]["letter"] = user_word[4]



  for character , i = 0  in answer_word: #"Python" 
        if word[i]["letter"] == character (P)  #grab p in first loop 
            word[i]['color'] = 'Green'
        else # word[i]["letter"] != character (P)  
            if answer_word.find(word[i]["letter"]) > 0
                word[i]['color'] = 'Yellow'
            else 
               word[i]['color'] = 'Grey'


######################## START 
    # user_word = validate_word(word, db)  # valid word user inputs 
    # answer_key = get_answer_key(answer, db) #Returns WOTD key -> designate the "Answer"
    # answer_word = # access answers.db and get the actual word 
# word_color = { } // Empty dictionary

#user word = poker
#answer_word = python
    for character in user_word
        if answer_word.find(character) == -1
            word_color[i]['color'] = 'Grey'
        else if answer_word.find(character) == user_word.index(character)
            word_color[i]['color'] = 'Green'
        else
            word_color[i]['color'] = 'Yellow'
# todo: track number of greens (counter)
# user_word = {
#     0 : {
#     "color": 'white' 
#     },
#     1 : {
#     "color" : "white"
#     },
#     2 : {
#     "color" : "white"
#     },
#     3 : {
#     "color" : "white"
#     },
#     4 : {
#     "color" : "white"
#     },
# }
# return all the colors in order at the end
# # actually we need to also do a quick check in the case if all are green and in that case we also return back like a "correct answer or soemthing idk"
# since we dont care about making sure which are green after one guess or another
# there is no need to keep another dictionary like below with "guesses"
############################ END all we need i think



# # guesses = {
# #          poker : {
# #   "letter" : "P",
# #     "color": 'green' # we will update with the syntax word[0]['color'] = Yellow 
# #   },
# #          1 : {
# #    "letter": "B",
# #    "color" : "white"
# #   },
# #           
# # }

# answer = python
# guesses = {
#             poker: {letter: P, color: green}, {letter: O, color: yellow}, {k: }, {e: }, {r: }
#             joker: {letter: , color: }, {letter: , color: }}, {letter: , color: }, {e: }, {r: }
#             ***O*: {letter: , color: }, {letter: , color: }}, {letter: , color: }, {letter: O, color: Green }, {r: }***O*: {letter: , color: }, {letter: , color: }}, {letter: , color: }, {letter: O, color: Green }, {r: }
#             *O***: {letter: , color: }, {letter: O, color: }}, {letter: , color: }, {letter: O, color: Green }, {r: }
#            }

# Output : 'Empty'
# print(myfamily[0]['color'])

# word[0]['color'] = Yellow 

# Output : 'Yellow'
# print(myfamily[0]['color'])