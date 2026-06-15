from fastapi import FastAPI 
from AI_CHATBOT.fitur_AI.tanya_ai import tanya_ai
app=FastAPI()

@app.post('/chatbot_ai')
def tanya(pesan):
    pesan=pesan.strip()
    if not pesan:
        return{'msg':'pesan input kosong'}

    jawaban=tanya_ai(pesan)
    return{'jawaban':jawaban}