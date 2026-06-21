from AI_CHATBOT.DB.db_setup import History,session

def save_chat(username,role,pesan):
    data=History(username=username,role=role,pesan=pesan)
    session.add(data)
    session.commit()
