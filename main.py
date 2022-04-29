# from fastapi import FastAPI, Request

# app = FastAPI()

# @app.get("/app")
# def read_main(request: Request):
#     return {"message": "Hello World", "root_path": request.scope.get("root_path")}

from typing import Optional
from fastapi import FastAPI, Request

from pydantic import BaseModel

app = FastAPI(root_path="/api/v1")


class Words(BaseModel):
    wordID: int
    word: str

@app.get("/")
def read_root(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}


@app.get("/words/{word_id}")
def read_word(word_id: int, word: Optional[str] = None):
    return {"word_id": word_id, "word": word}   

@app.put("/words/{word_id}")
def update_word(word_id: int, words: Words):
    return {"words": words.word, "word_id": word_id}
