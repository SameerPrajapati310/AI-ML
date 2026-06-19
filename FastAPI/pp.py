from fastapi import FastAPI,Depends
from langchain.chat_models import init_chat_model
from sqlalchemy import Column,Integer,String,select
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
import asyncio
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
engine = create_async_engine(url="")
LocalSession = sessionmaker(
    bind=engine,
    class_=AsyncSession
)

base = declarative_base()

class User(base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)

class UserPayload(BaseModel):
    name : str
    age : int

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(base.metadata.create_all)

async def get_db():
    async with LocalSession() as db:
        yield db

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.post("/user")
async def create_user(user_data:UserPayload, db : AsyncSession = Depends(get_db)):
    new_user = User(name =user_data.name, age =user_data.age)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@app.get("/get_user/{user_id}")
async def get_user(user_id : int, db : AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id==user_id))
    return result.scalar_one_or_none()