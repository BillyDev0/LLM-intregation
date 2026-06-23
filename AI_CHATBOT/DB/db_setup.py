from sqlalchemy import Column,Integer,String,create_engine,Text,DateTime
from sqlalchemy.orm import declarative_base,sessionmaker
from datetime import datetime

url="sqlite:///AI_CHATBOT/DB/data.db"
engine=create_engine(url)
session_local=sessionmaker(bind=engine)
base=declarative_base()

def get_db():
    return session_local()

class History(base):
    __tablename__="data_history"

    id=Column(Integer,primary_key=True,autoincrement=True)
    username=Column(String)
    role=Column(String)
    pesan=Column(Text)

    create_at=Column(DateTime,default=datetime.utcnow)

class User(base):
    __tablename__='data_user'

    username=Column(String,primary_key=True)
    password=Column(String)

base.metadata.create_all(engine)

