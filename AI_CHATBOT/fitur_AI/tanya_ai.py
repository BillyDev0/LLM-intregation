import requests
from AI_CHATBOT.fitur_AI.get_history import get_history
from AI_CHATBOT.fitur_AI.save_history import save_chat
from AI_CHATBOT.JWT_token.token import verify_token

AI_server="http://localhost:11434/api/generate"

def tanya_ai(token,pesan):
    username=verify_token(token)
    if not username:
        return{'msg':'token error'}
    
    history=get_history(username)

    prompt=f"""
anda adalah seorang asisten AI

jawab prompt ini:
{pesan}

gunakan konteks ini jika relevan:
{history}

aturan jawaban:
-jawaban hanya menggunakan bahasa indonesia
-gunakan bahasa yang baku
-jawaban tidak bertele tele
-jika prompt user tidak ada yang nyambung terhadap data konteks maka jawab sesuai pengetahuan anda

"""

    payload={
        "model":"gemma:2b",
        "prompt":prompt,
        "stream":False,
        "options":{
            "temperature":0.3, #opsi memilih konteks
            "num_predict":150, #max_token
            "top_p":0.5 #luas konteks
        }
    }
    
    try:
        save_chat(username,"user",pesan)
        
        res=requests.post(AI_server,json=payload)
        jawaban=res.json()['response']
        save_chat(username,"AI",jawaban)
        return jawaban
    
    except requests.exceptions.ConnectionError:
        return {'msg':'Server ollama belum dijalankan'}
