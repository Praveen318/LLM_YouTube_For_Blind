from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import search_and_rerank
from pydantic import BaseModel

# app = FastAPI()

# @app.get("/rerank/")

# def rerank(query:str = "testvalue",count: int = 5):
#     return JSONResponse(content=search_and_rerank.rerank_for_query(query, count))



app = FastAPI()

class Item(BaseModel):
    query: str
    count: int

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/rerank/")
def rerank(item: Item):
    return JSONResponse(content=search_and_rerank.rerank_for_query(item.query, item.count))