from AI_CHATBOT.DB.db_setup import session,History

def get_history(username):
    data=session.query(History).filter(History.username==username).all()
    hasil=[]

    for d in data:
        if d.pesan:
            hasil.append(f"{d.role}: {d.pesan}")

    return hasil[-3:]