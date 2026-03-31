#this is the file for ai chat
from groq import Groq
from dotenv import load_dotenv
import os 

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "llama-3.3-70b-versatile"


def AI_CHAT(user_message,history):
    message= [{ 
        "role":"system",
        "content": '''You are AIVidCodex Assistant, created by Monu Verma.
                        Help users with reel content ideas, descriptions, and creative suggestions.
                         Be friendly, conversational, and occasionally add light humor.
                        Offer options like reel ideas or voiceover descriptions when relevant.'''

     }]
    #saving the history of current text 
    for h in history:
        message.append({"role":"user","content":h["user"]})
        message.append({"role":"assistant","content":h["assistant"]})
    
    message.append({"role":"user","content":user_message})

    response = client.chat.completions.create(
        model = MODEL,
        messages = message,
        max_tokens=1024
    )#for getting the response of the ai 
    return response.choices[0].message.content




