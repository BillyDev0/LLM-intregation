import requests
from AI_CHATBOT.fitur_AI.add_knowledge import add_knowledge
from AI_CHATBOT.fitur_AI.get_knowledge import get_knowledge
from AI_CHATBOT.fitur_AI.relevan import relevan_konteks


AI_server="http://localhost:11434/api/generate"

def tanya_ai(pesan):
    data_konteks=get_knowledge()
    konteks_relevan=relevan_konteks(data_konteks,pesan)

    if konteks_relevan:
       prompt=f"""
role: anda adalah seorang asisten AI
instruction: {pesan}
konteks: {konteks_relevan}
constraint: maksimal 2 kalimat, penjelasan singkat dan jelas, gunakan bahasa indonesia
"""
    else:
        prompt=f"""
role: anda adalah seorang asisten AI
instruction: {pesan}
constraint: maksimal 2 kalimat, penjelasan singkat dan jelas, gunakan bahasa indonesia
"""


    payload={
        "model":"phi3",
        "prompt":prompt,
        "stream":False
    }

    try:
        res=requests.post(AI_server,json=payload)
        jawaban=res.json()['response']
        add_knowledge(jawaban)
        return jawaban
    
    except requests.exceptions.ConnectionError:
        return {'msg':'Server ollama belum dijalankan'}
