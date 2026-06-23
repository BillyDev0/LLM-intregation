from AI_CHATBOT.DB.db_setup import get_db,History

def get_history(username):
    db=get_db()
    data=db.query(History)\
        .filter(History.username==username)\
        .order_by(History.id.desc())\
        .limit(3)\
        .all()
    db.close()
    
    data=data[::-1]

    return "\n".join([f"{i.role}: {i.pesan}"
             for i in data])
    
    