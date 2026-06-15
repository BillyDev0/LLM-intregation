from sqlalchemy import Column,Integer,String,create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

url="sqlite:///AI_CHATBOT/db/data.db"
engine=create_engine(url)
Session=sessionmaker(bind=engine)
session=Session()

base=declarative_base()

class Knowledge(base):
    __tablename__="AI_knowledge"

    id=Column(Integer,primary_key=True,autoincrement=True)
    konteks=Column(String)

base.metadata.create_all(engine)
