from fastapi import FastAPI
import uvicorn
import pyterrier as pt
import pandas as pd
import rank
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/search")
async def query(query: str = ""):
    return rank.query(query)



if __name__ == "__main__":
    rank.init()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)