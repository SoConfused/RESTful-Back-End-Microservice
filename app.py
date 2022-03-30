import sqlite3
import logging.config
import typing
import contextlib
import random

from typing import Optional
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
    num = random.randrange(101)
    
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

def check_answer(answer: str, db: sqlite3.Connection = Depends(get_db)): # checks if word is the answer/compares the word to the answer
    user_word = validate_word(word, db)  # 
    answer_key = random()


# columns = ['word1', 'word2', 'word3']
# chosen_column = random.choice(columns)

# #now access DB using chosen_column for example:
# Your_model.objects.raw('SELECT ' + chosen_column + ' FROM myapp_yourmodel')