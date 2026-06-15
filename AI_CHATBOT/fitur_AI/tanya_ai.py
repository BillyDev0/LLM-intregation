import requests
from AI_CHATBOT.db.setup import session,Knowledge
AI_server="http://localhost:11434/api/generate"

def tanya_ai(pesan):
    prompt=f"""
role: anda adalah seorang asisten AI
instruction: {pesan}
konteks: saya seorang pemula yang baru belajar
constraint: maksimal 3 poin, penjelasan singkat dan jelas, gunakan bahasa indonesia
"""
    payload={
        "model":"phi3",
        "prompt":prompt,
        "stream":False
    }

    try:
        res=requests.post(AI_server,json=payload)
        jawaban=res.json()['response']
        return jawaban
    
    except requests.exceptions.ConnectionError:
        return {'msg':'Server ollama belum dijalankan'}
