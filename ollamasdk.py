from ollama import generate, GenerateResponse
from ollama import chat
from ollama import ChatResponse
from typing import Union

def chat_parser(profiles: Union[dict,str] = "", messages: Union[dict,str] = ""):
    """Given the profiles and the messages, parse them into strings that can be added to the prompt for scoring.

    
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
    summarize_prompt = """Act as an profile summarizer. Given two profiles, summarize each profile into a paragraph that captures all given information in a concise manner. Make sure no detail is omitted. Seperate the preferences from the profile so you can include all the details for both.

    Show as this RESPONSE FORMAT:
    {
        "profile1":{
            "name": Full name of the profile
            "gender": Male or Female
            "profile": Summary of the profile
            "preferences" : Summary of the user's preferences
        }
        "profile2":{
            "name": Full name of the profile
            "gender": Male or Female
            "profile": Summary of the profile
            "preferences" : Summary of the user's preferences
        }
    }
    """
    
    summarized = chat(
        model= 'deepseek-r1:14b',
        messages=[
            # {'role': 'system', 'content': system_prompt},ssssssssssssssssssssssssss
            {'role': 'user', 'content': str(profiles)+summarize_prompt}
        ],
        options={
            'temperature': 0.4,  
            'top_p': 0.9,        # Union: nucleus sampling
            'top_k': 40,         # Union: top-k sampling
        },
        think=False
    )
    print(summarized["message"]["content"])
    chat_scorer(f"CONVERSATION:{messages}\nPROFILES:{summarized["message"]["content"]}")

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

                      TRUTHFULNESS (0-10)ddd

                      - What it measures: How accurately each user's stated details and preferences in the conversation match the data in their respective profiles in the PROFILES section. Specifically look at locations, ages, incomes, and professions.

                      - Key indicators: Direct alignment between spoken claime
                      - Scoring basis: This score reflects factual consistency — not plausibility. A high score requires no contradictions between conversation content and profile data. Any discrepancies, exaggerations, or omissions should reduce the score. Truthfulness also suggests user comfort and transparency in the interaction.
                      
                      
                      Show as this RESPONSE FORMAT:  
                      {
                        "engagement_quality": [0-10],  
                        "authenticity": [0-10],  
                        "connection": [0-10],  
                        "truthfullness": [0-10],  
                        "general_trend": ["positive" or "negative"],  
                        "conversation_analysis": "General comments about the conversation's strengths and weaknesses.",   
                        "m_comments": "Specific feedback and advice for the male user, addressing his engagement, authenticity, connection, and truthfulness. If either the male or female user is dishonest about a detail, mention it. Write it addressing him as 'you', acting as an analyzer, not as the other user.",
                        "f_comments": "Specific feedback and advice      for the female user, addressing her engagement, authenticity, connection, and truthfulness. If either the male or female user is dishonest about a detail, mention it. Write it addressing her as 'you', acting as an analyzer, not as the other user.",
                        "contradictions": "Any contradictions between the details on the profile and the details the users shared in their messages." 
                      }                
                    """

    print(content)
    response = chat(
        
        model='deepseek-r1:14b',
        messages=[
            # {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': content+system_prompt}
        ],
        options={
            'temperature': 0.5,  
            'top_p': 0.95,        # Union: nucleus samplings
            'top_k': 50,         # Union: top-k sampling
        },
        # think=True,
        stream=True
    )
    for chunk in response:
        print(chunk['message']['content'], end="", flush=True)

# Example usage
with open("tests/pos_R&P_test.json", encoding="utf-8") as messages:
    with open("tests/R&P_profile.json", encoding="utf-8") as profiles:
        # chat_scorer(f"PROFILES:{profiles.read()}\nMESSAGES:{messages.read(e)}")
        chat_parser(profiles.read(),messages.read())