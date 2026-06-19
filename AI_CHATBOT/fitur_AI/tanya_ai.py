import requests

AI_server="http://localhost:11434/api/generate"

def tanya_ai(pesan):
    prompt=f"""
anda adalah seorang asisten AI

jawab prompt ini
{pesan}

aturan jawaban:
-jawaban menggunakan bahasa indonesia
-jawaban singkat, padat, jelas
-jawaban tidak bertele tele

bentuk output:
-wajib JSON
-key JSON "jawaban"
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
        res=requests.post(AI_server,json=payload)
        jawaban=res.json()['response']
        return jawaban
    
    except requests.exceptions.ConnectionError:
        return {'msg':'Server ollama belum dijalankan'}
