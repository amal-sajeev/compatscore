from ollama import generate,GenerateResponse
from ollama import chat
from ollama import ChatResponse

def chat_parser(profiles:dict={}, messages:dict={}):
  """_summary_
  """
  parser_prompt= """
                  You are a conversation quality evaluator. Score this conversation on a 0-100 scale across 3 dimensions. Analyze if the scores and conversation quality is improving or degrading. 

                  ENGAGEMENT QUALITY (0-10):
                  - What it measures: Active participation, asking questions, building on partner's responses
                  - Key indicators: References previous messages, asks follow-ups, shows curiosity
                  - Why essential: Predicts conversation sustainability and mutual interest

                  AUTHENTICITY (0-10):
                  - What it measures: Genuine self-expression vs generic/scripted responses
                  - Key indicators: Personal stories, consistent voice, appropriate vulnerability
                  - Scoring basis: Distinguishes real connection potential from surface-level chat

                  CONNECTION (0-10)

                  - What it measures: How close the details shared by each user match the preferences on the other user's profile.
                  - Key indicators: Identifies shared interests, shows empathy, discusses compatibility
                  - Scoring basis: Analysis of closeness between the details shared by one user and the preferences in the other user's profile.

                  TRUTHFULLNESS (0-10)
                  
                  - What it measures: How close the user's stated details about his o r her life and preferences are to the details and preferences in his or her profile. 
                  - Key indicators: Stated details match profile details, stated preferences matches preference details in the profile.
                  - Scoring basis: How honest both users are willing to be in the conversation, and how comfortable they are with the other. Dishonesty suggest uncomfortableness or incompatbility.


                  REQUIRED RESPONSE FORMAT:
                  {
                    "engagement_quality": [0-10],
                    "authenticity": [0-10],
                    "connection": [0-10],
                    "truthfullness": [0-10],
                    "general trend": ["positive" or "negative"]
                  }                     
                 """
  chat_scorer(f"{parser_prompt}\nPROFILES:{profiles}\nCONVERSATION:{messages}")

def chat_scorer(content:str):
  """
  """

  response= generate(model='gemma3:latest', system= """
                 Act as a conversation quality evaluator. Score this conversation between the two given profiles on a 0-100 scale across 4 dimensions. Analyze if the scores and conversation quality is improving or degrading.  

                  ENGAGEMENT QUALITY (0-10):
                  - What it measures: Active participation, asking questions, building on partner's responses
                  - Key indicators: References previous messages, asks follow-ups, shows curiosity
                  - Why essential: Predicts conversation sustainability and mutual interest

                  AUTHENTICITY (0-10):
                  - What it measures: Genuine self-expression vs generic/scripted responses
                  - Key indicators: Personal stories, consistent voice, appropriate vulnerability
                  - Scoring basis: Distinguishes real connection potential from surface-level chat

                  CONNECTION (0-10)

                  - What it measures: How close the details shared by each user match the preferences on the other user's profile.
                  - Key indicators: Identifies shared interests, shows empathy, discusses compatibility
                  - Scoring basis: Analysis of closeness between the details shared by one user and the preferences in the other user's profile.

                  TRUTHFULLNESS (0-10)
                  
                  - What it measures: How close the user's stated details about his or her life and preferences are to the details and preferences in his or her profile. 
                  - Key indicators: Stated details match profile details, stated preferences matches preference details in the profile.
                  - Scoring basis: How honest both users are willing to be in the conversation, and how comfortable they are with the other. Dishonesty suggest uncomfortableness or incompatbility.


                  Show as this RESPONSE FORMAT:
                  {
                    "engagement_quality": [0-10],
                    "authenticity": [0-10],
                    "connection": [0-10],ee
                    "truthfullness": [0-10],
                    "general trend": ["positive" or "negative"]
                  }                
                  """,
                  prompt=content,
                  template="{{ if .System }}system<|end_header_id|>\n\n{{ .System }}<|eot_id|>{{ end }}{{ if .Prompt }}<|start_header_id|>user<|end_header_id|>\n\n{{ .Prompt }}<|eot_id|>{{ end }}<|start_header_id|>assistant<|end_header_id|>\n\n{{ .Response }}<|eot_id|>",
                  stream= True)

  for chunk in response:
    print(chunk.response,end="", flush=True)
  # print(response['message']['content'])
  # # or access fields directly from the response object
  # print(response.message.content)

with open("tests/neg_R&P_test.json",encoding="utf-8") as messages:
  with open("tests/R&P_profile.json",encoding="utf-8") as profiles:
    chat_scorer(f"PROFILES:{profiles.read()}\nMESSAGES:{messages.read()}")