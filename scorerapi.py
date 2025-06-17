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
    """Get scores and analysis for a conversation, given the profiles and the messages. Currently uses Gemma 8B.

    Args:
        scoredat (ScoreInput): JSON format: {
                                                profiles: [list of profiles in JSON format],
                                                messages: [list of messages or messages in JSON format]
                                                detail: Bool = If set to True, returns detailed analysis and takes more time, otherwise returns quick analysis. Default = True
                                            }

    Raises:
        HTTPException: _description_
    """
    try:
        return(convoscore.chat_parser(scoredat.profiles, scoredat.messages,scoredat.detail))
    except Exception as e:
        raise HTTPException(500,f"Error,{str(e.__traceback__)}")

