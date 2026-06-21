from jose import jwt,JWTError
from datetime import datetime,timedelta
from AI_CHATBOT.DB.db_setup import session,User

SECREAT_KEY='qy7qgsuhsq8y7ggy76g91'
ALGORITHM='HS256'

def create_token(username):
    payload={
        'username':username,
        'exp':datetime.utcnow() + timedelta(minutes=30)
    }

    token=jwt.encode(payload,SECREAT_KEY,algorithm=ALGORITHM)
    return token


def verify_token(token):
    try:
        payload=jwt.decode(token,SECREAT_KEY,algorithms=[ALGORITHM])
        user=session.query(User).filter(User.username==payload['username']).first()
        if not user:
           return None
        
        return payload['username']
    except JWTError:
        return None