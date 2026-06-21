from fastapi import FastAPI 
from AI_CHATBOT.fitur_AI.tanya_ai import tanya_ai
from AI_CHATBOT.AUTH.regis_log import registrasi,login
app=FastAPI()

@app.post('/chatbot_ai')
def tanya(token,pesan):
    pesan=pesan.strip()
    if not pesan:
        return{'msg':'pesan input kosong'}

    jawaban=tanya_ai(token,pesan)
    return {'jawaban':jawaban}

@app.post('/regist')
def regist(username:str,password:str):
    return registrasi(username,password)

@app.post('/login')
def loginn(username:str,password:str):
    return login(username,password)