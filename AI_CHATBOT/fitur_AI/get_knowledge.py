from AI_CHATBOT.db.setup import session,Knowledge
from fastapi import FastAPI

app=FastAPI()

@app.get('/data_knowledge')
def get_knowledge():
    data=session.query(Knowledge).all()
    konteks=[d.konteks for d in data]
    return konteks
