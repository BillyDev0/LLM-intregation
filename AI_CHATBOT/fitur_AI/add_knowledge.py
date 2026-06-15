from AI_CHATBOT.db.setup import session,Knowledge
import requests
AI_server="http://localhost:11434/api/generate"

def add_knowledge(jawaban):
    prompt=f"""
role: anda adalah orang yang expert dalam summarizing
instruction: rangkum teks ini {jawaban}
constraint: maksimal 1 kalimat singkat dan jelas menggunakan bahasa indonesia.
"""
    payload={
        "model":"phi3",
        "prompt":prompt,
        "stream":False
    }

    try:
        res=requests.post(AI_server,json=payload)
        hasil=res.json()['response']
        
        new_knowledge=Knowledge(konteks=hasil)
        session.add(new_knowledge)
        session.commit()
    except requests.exceptions.ConnectionError:
        return{'msg':'Server ollama belum dijalankan'}
    
        


    