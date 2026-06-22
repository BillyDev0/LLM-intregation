from sqlalchemy import Column,Integer,String,create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

url="sqlite:///AI_CHATBOT/DB/data.db"
engine=create_engine(url)
Session=sessionmaker(bind=engine)
session=Session()
base=declarative_base()

class History(base):
    __tablename__="data_history"

    id=Column(Integer,primary_key=True,autoincrement=True)
    username=Column(String)
    role=Column(String)
    pesan=Column(String)

class User(base):
    __tablename__='data_user'

    username=Column(String,primary_key=True)
    password=Column(String)

base.metadata.create_all(engine)

