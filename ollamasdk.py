from ollama import generate, GenerateResponse
from ollama import chat
from ollama import ChatResponse
from typing import Optional

def chat_parser(profiles: Optional[dict,str] = "", messages: Optional[dict,str] = ""):
    """_summary_
    """
    scorer_prompt = """
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
                      - What it measures: How close the details shared by each user match the preferences on the other user's profile from the PROFILES section.  
                      - Key indicators: Identifies shared interests, shows empathy, discusses compatibility  
                      - Scoring basis: Analysis of closeness between the details shared by one user and the preferences in the other user's profile.  

                      TRUTHFULNESS (0-10)

                      - What it measures: How accurately each user's stated details and preferences in the conversation match the data in their respective profiles in the PROFILES section.

                      - Key indicators: Direct alignment between spoken claims (e.g., age, profession, habits, interests, preferences) and structured profile fields.

                      - Scoring basis: This score reflects factual consistency — not plausibility. A high score requires no contradictions between conversation content and profile data. Any discrepancies, exaggerations, or omissions should reduce the score. Truthfulness also suggests user comfort and transparency in the interaction.
                      
                      
                      Show as this RESPONSE FORMAT:  
                      {
                        "engagement_quality": [0-10],  
                        "authenticity": [0-10],  
                        "connection": [0-10],  
                        "truthfullness": [0-10],  
                        "general_trend": ["positive" or "negative"],  
                        "conversation_analysis": "General comments about the conversation's strengths and weaknesses.",   
                        "m_comments": "Specific feedback and advice for the male user, addressing his engagement, authenticity, connection, and truthfulness. If the other user is dishonest about a detail, mention it. Write it addressing him as 'you', acting as an analyzer, not as the other user.",  
                        "f_comments": "Specific feedback and advice for the female user, addressing her engagement, authenticity, connection, and truthfulness. If the other user is dishonest about a detail, mention it. Write it addressing her as 'you', acting as an analyzer, not as the other user."  
                      }                
                    """
    summarize_prompt = """You are a profile summarizer. Given two profiles, summarize each profile into a paragraph that captures all given information in a concise manner, and return them in the following format:
    {
        "profile1":{
            "name": Full name of the profile.
            "profile": Summary of the profile.
        }
        "profile2":{
            "name": Full name of the profile.
            "profile": Summary of the profile.
        }
    }
    """
    chat_scorer(f"{parser_prompt}\nCONVERSATION:{messages}\nPROFILES:{profiles}")

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
                      - What it measures: How close the details shared by each user match the preferences on the other user's profile from the PROFILES section.  
                      - Key indicators: Identifies shared interests, shows empathy, discusses compatibility  
                      - Scoring basis: Analysis of closeness between the details shared by one user and the preferences in the other user's profile.  

                      TRUTHFULNESS (0-10)

                      - What it measures: How accurately each user's stated details and preferences in the conversation match the data in their respective profiles in the PROFILES section.

                      - Key indicators: Direct alignment between spoken claims (e.g., age, profession, habits, interests, preferences) and structured profile fields.

                      - Scoring basis: This score reflects factual consistency — not plausibility. A high score requires no contradictions between conversation content and profile data. Any discrepancies, exaggerations, or omissions should reduce the score. Truthfulness also suggests user comfort and transparency in the interaction.
                      
                      
                      Show as this RESPONSE FORMAT:  
                      {
                        "engagement_quality": [0-10],  
                        "authenticity": [0-10],  
                        "connection": [0-10],  
                        "truthfullness": [0-10],  
                        "general_trend": ["positive" or "negative"],  
                        "conversation_analysis": "General comments about the conversation's strengths and weaknesses.",   
                        "m_comments": "Specific feedback and advice for the male user, addressing his engagement, authenticity, connection, and truthfulness. If the other user is dishonest about a detail, mention it. Write it addressing him as 'you', acting as an analyzer, not as the other user.",  
                        "f_comments": "Specific feedback and advice for the female user, addressing her engagement, authenticity, connection, and truthfulness. If the other user is dishonest about a detail, mention it. Write it addressing her as 'you', acting as an analyzer, not as the other user."  
                      }                
                    """

    # system_prompt = "Summarize the profiles of Rajesh and Priya only from the profile details. "
    
    response = chat(
        model='deepseek-r1:14b',
        messages=[
            # {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': content+system_prompt}
        ],
        options={
            'temperature': 0.4,  
            'top_p': 0.9,        # Optional: nucleus sampling
            'top_k': 40,         # Optional: top-k sampling
        },
        # think=True,
        stream=True
    )
    for chunk in response:
        print(chunk['message']['content'], end="", flush=True)

# Example usage
with open("tests/pos_R&P_test.json", encoding="utf-8") as messages:
    with open("tests/R&P_profile.json", encoding="utf-8") as profiles:
        chat_scorer(f"PROFILES:{profiles.read()}\nMESSAGES:{messages.read()}")