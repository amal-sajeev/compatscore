from ollama import chat
from ollama import ChatResponse

def chat_parser(history:dict):
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
                  
                  - What it measures: How close the user's stated details about his or her life and preferences are to the details and preferences in his or her profile. 
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

response: ChatResponse = chat(model='llava:latest', messages=[
  {
    'role': 'user',
    'content': 'Mirror, mirror, on the wall, who is the strongest of them all?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)