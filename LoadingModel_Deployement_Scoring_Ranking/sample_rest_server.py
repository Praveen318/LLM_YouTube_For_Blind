from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import List
import search_and_rerank

app = FastAPI()

@app.get("/rerank/")

def rerank(query:str = "testvalue",count: int = 5):
    return JSONResponse(content=search_and_rerank.rerank_for_query(query, count))