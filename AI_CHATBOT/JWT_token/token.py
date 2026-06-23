from jose import jwt,JWTError
from datetime import datetime,timedelta
from AI_CHATBOT.DB.db_setup import get_db,User
import secrets

SECRET_KEY=secrets.token_hex(32)
ALGORITHM='HS256'

def create_token(username):
    payload={
        'username':username,
        'exp':datetime.utcnow() + timedelta(minutes=30)
    }

    token=jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    return token


def verify_token(token):
    db=get_db()
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        user=db.query(User).filter(User.username==payload['username']).first()
        db.close()
        if not user:
           return None
        
        return payload['username']
    except JWTError:
        return None