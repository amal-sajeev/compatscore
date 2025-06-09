from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

@app.post("/score")
def getscore(profiles:dict,message:dict):
    print(profiles)