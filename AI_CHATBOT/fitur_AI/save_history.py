from AI_CHATBOT.DB.db_setup import History,get_db

def save_chat(username,role,pesan):
    db=get_db()
    data=History(username=username,role=role,pesan=pesan)
    try:
       db.add(data)
       db.commit()
    except:
        db.rollback()
        
    db.close()
