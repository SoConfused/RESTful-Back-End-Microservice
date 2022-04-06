import sqlite3
import logging.config
import typing
import contextlib
import random
import json

from typing import Optional
from xml.dom.minidom import CharacterData
from fastapi import FastAPI, Depends, Response, HTTPException, status
from pydantic import BaseModel, BaseSettings

# class Settings(BaseSettings):
#     database: str
#     logging_config: str

#     class Config:
#         env_file = ".env"


# class words(BaseModel):
#     wotd_key: int
#     wotd: str

# app = FastAPI()
# settings = Settings()

# logging.config.fileConfig(settings.logging_config)
# cursor.execute("CREATE TABLE answers (answerID PRIMARY KEY, answer)")
#database_file = 'answers.db'
#database = sqlite3.connect(database_file)


#def get_db():
#    with contextlib.closing(sqlite3.connect(settings.database)) as db:
#        db.row_factory = sqlite3.Row
#        yield db

# @app.get("/answers/{wotd}")
# def get_wotd():
#     db = get_db()
#     wotd_key = random.randrange(2308) # Get value for Word of the Day
#     cur = db.execute("SELECT * FROM answers WHERE wotd_key = ? LIMIT 1", [wotd_key])
#     wotd = cur.fetchall()
#     if not wotd:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Word not found")
#     # need to access datab
#     return {"wotd": wotd}

database_file = 'answers.db'
database = sqlite3.connect(database_file)
cur = database.cursor()
cur.execute("SELECT * FROM answers WHERE answerID = 5")
print(cur.fetchall())

# if __name__ == '__main__':
#     #answer = get_db()
#     # test = get_wotd()
#     #print(answer)
#     database_file = 'answers.db'
#     database = sqlite3.connect(database_file)

#     cur.execute("select * from answers where answer=:answerID", {"answerID": 1})
#     print(cur.fetchall())


database.close()
