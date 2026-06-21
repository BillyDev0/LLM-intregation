from AI_CHATBOT.DB.db_setup import History,session

def save_chat(pesan):
    data=History(pesan=pesan)
    session.add(data)
    session.commit()
