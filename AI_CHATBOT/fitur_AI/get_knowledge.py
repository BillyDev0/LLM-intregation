from AI_CHATBOT.db.setup import session,Knowledge

def get_knowledge():
    data=session.query(Knowledge).all()
    konteks=[d.konteks for d in data]
    return konteks