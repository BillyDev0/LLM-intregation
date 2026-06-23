from AI_CHATBOT.JWT_token.token import create_token
from passlib.hash import bcrypt
from AI_CHATBOT.DB.db_setup import get_db,User


def registrasi(username:str,password:str):
    db=get_db()
    # Validasi username 
    username=username.strip()
    if not username:
        return {'msg':'input username kosong'}

    # Validasi Password User
    password=password.strip()
    if not password:
        return{'msg':'input password kosong'}

    if len(password) < 8:
        return{'msg':'password terlalu singkat'}

    # Cek Username ada/tidak ada dalam database
    cek_username=db.query(User).filter(User.username==username).first()
    db.close()
    if cek_username:
        return{'msg':'username sudah tersedia'}

    # hash password dan add new user
    hashed_password=bcrypt.hash(password)
    new_user=User(username=username,password=hashed_password)
    db.add(new_user)
    db.commit()
    db.close()
    return{'msg':'Registrasi berhasil'}


def login(username:str,password:str):
        db=get_db()
    # Validasi username 
        username=username.strip()
        if not username:
            return {'msg':'input username kosong'}
    
        # Validasi Password User
        password=password.strip()
        if not password:
            return{'msg':'input password kosong'}

        # Cek Username ada/tidak ada dalam database
        cek_username=db.query(User).filter(User.username==username).first()
        db.close()
        if not cek_username:
            return{'msg':'username tidak ditemukan'}

        if not bcrypt.verify(password,cek_username.password):
            return{'msg':'password salah'}

        token=create_token(cek_username.username)
        return{'token':token}




    
