from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel
import convoscore

app = FastAPI()
class ScoreInput(BaseModel):
    profiles: Union[list,dict,str]
    messages: Union[list,dict,str]
    detail: Bool = True

@app.post("/score")
def getdetailscore(scoredat: ScoreInput):
    try:
        return(convoscore.chat_parser(scoredat.profiles, scoredat.messages,scoredat.detail))
    except Exception as e:
        raise HTTPException(500,f"Error,{str(e.__traceback__)}")

