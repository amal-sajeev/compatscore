from ollama import generate, GenerateResponse
from ollama import chat
from ollama import ChatResponse

def chat_parser(profiles: dict = {}, messages: dict = {}):
    """_summary_
    """
    parser_prompt = """
                    You are a conversation quality evaluator. Score this conversation on a 0-10 scale across 3 dimensions. Analyze if the scores and conversation quality is improving or degrading.

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
                      "engagement_quality": int,
                      "authenticity": int,
                      "connection": int,
                      "truthfullness": int,
                      "general trend": "positive" or "negative"
                    }                     
                   """
    chat_scorer(f"{parser_prompt}\nPROFILES:{profiles}\nCONVERSATION:{messages}")

def chat_scorer(content: str):
    """
    """
    system_prompt = """
                      Act as a conversation quality evaluator. Score this conversation between the two given profiles on a 0-10 scale across 4 dimensions. Analyze if the scores and conversation quality are improving or degrading.

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
                      - Key indicators: Stated details match profile details, stated preferences match preference details in the profile.  
                      - Scoring basis: How honest both users are willing to be in the conversation, and how comfortable they are with the other. Dishonesty suggests uncomfortableness or incompatibility.  

                      Show as this RESPONSE FORMAT:  
                      {
                        "engagement_quality": [0-10],  
                        "authenticity": [0-10],  
                        "connection": [0-10],  
                        "truthfullness": [0-10],  
                        "general_trend": ["positive" or "negative"],  
                        "conversation_analysis": "General comments about the conversation's strengths and weaknesses.",  
                        "m_comments": "Specific feedback for the male user, addressing his engagement, authenticity, connection, and truthfulness. Write it addressing him as 'you', acting as an analyzer, not as the other user.",  
                        "f_comments": "Specific feedback for the female user, addressing her engagement, authenticity, connection, and truthfulness. Write it addressing her as 'you', acting as an analyzer, not as the other user."  
                      }                
                    """

    response = chat(
        model='deepseek-r1:14b',
        messages=[
            # {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': content+system_prompt}
        ],
        options={
            'temperature': 0.4,  # Lower = more deterministic, Higher = more creative
            'top_p': 0.9,        # Optional: nucleus sampling
            'top_k': 40,         # Optional: top-k sampling
        },
        think=False,
        stream=True
    )

    for chunk in response:
        print(chunk['message']['content'], end="", flush=True)

# Example usage
with open("tests/pos_R&P_test.json", encoding="utf-8") as messages:
    with open("tests/R&P_profile.json", encoding="utf-8") as profiles:
        chat_scorer(f"PROFILES:{profiles.read()}\nMESSAGES:{messages.read()}")