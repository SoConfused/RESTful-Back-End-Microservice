from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, BaseSettings, Field
import contextlib
import logging.config
import sqlite3


#Professor's code
class Settings(BaseSettings):
    database: str
    logging_config: str

    class Config:
        env_file = ".env"

class Words(BaseModel):
    wordID: int
    word: str

def get_db():
    with contextlib.closing(sqlite3.connect(settings.database)) as db:
        db.row_factory = sqlite3.Row
        yield db

settings = Settings()
app = FastAPI()

logging.config.fileConfig(settings.logging_config)


@app.get("/words/")
def list_words(db: sqlite3.Connection = Depends(get_db)):
    words = db.execute("SELECT * FROM words")
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