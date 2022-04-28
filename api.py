from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, BaseSettings, Field
import contextlib
import logging.config
import sqlite3
import re


#Professor's code
class Settings(BaseSettings):
    database: str
    logging_config: str

    class Config:
        env_file = ".env"

class Words(BaseModel):
    wordID: int
    word: str

#db open--------------------------------------------------------
# this function goes through a master word file,
#   removes invalid words,
#   and saves each word in a list

def word_list():
     listWords = []
     wordID = 1
     file = open("/usr/share/dict/words") # opens master list
     for line in file.readlines():
        lowerLine = line.lower() # change word in master list to lowercase
        # currentWord = re.findall(r'\b(\w{6})\b', lowerLinewordList)
        # eachWord = (wordID , currentWord)
        # listWords.append(eachWord)
        # wordID += 1
        listWords += re.findall(r"\b([a-z]{5}$)\b", lowerLine)

# this function saves the final word list with all invalid words removed
#   to answers.db database
def createDBforWords():
    listWords = word_list()
    connection = sqlite3.connect("words.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE words (word)")
    for item in listWords:
        cursor.execute("INSERT INTO words VALUES(?)", (item, )) 
    connection.commit()  
    connection.close()

def get_db():
    with contextlib.closing(sqlite3.connect('/share/words.db')) as db:
        db.row_factory = sqlite3.Row
        yield db

# db open end---------------------------------------------------------------

settings = Settings()
app = FastAPI()

logging.config.fileConfig(settings.logging_config)


@app.get("/words/")
def list_words(db: sqlite3.Connection = Depends(get_db)):
    words = db.execute("SELECT * FROM words")
    #wotd = cur.fetchall()
    return {"words": words.fetchall()}

#end professor's code


'''
app = FastAPI()
# Example Hello World to get us started. This is localhost:8000/
@app.get("/")
async def root():
    return {"message": "Hello World"}

class Wotd(BaseModel):
    wordID: int
    word: str
    



#http://127.0.0.1:8000/docs
#navigate your browser to http://localhost:8000/words/
@app.get("/words/{word_ID}")
async def create_item(word_ID: int, word: Wotd):
    return {"word_ID": word_ID, **word.dict()}


'''