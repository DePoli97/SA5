from typing import List
from fastapi import FastAPI, Body,HTTPException
from pydantic import BaseModel
import uvicorn
import rank
from fastapi.middleware.cors import CORSMiddleware

class FeedbackRequestModel(BaseModel):
    feedback: List[int]


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

@app.post("/search")
async def search(query: str, feedback_data: FeedbackRequestModel = Body(...)):
    try:
        feedback = feedback_data.feedback
        results = rank.query(query,feedback)
        return results
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))



if __name__ == "__main__":
    rank.init()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)