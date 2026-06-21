from AI_CHATBOT.DB.db_setup import session,History

def get_history(username):
    data=session.query(History)\
        .filter(History.username==username)\
        .order_by(History.id.desc())\
        .limit(3)\
        .all()
    
    data=data[::-1]

    return [f"{i.role}: {i.pesan}" for i in data]