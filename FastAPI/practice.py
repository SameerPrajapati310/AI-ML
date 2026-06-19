from fastapi import FastAPI, Depends
from langchain.chat_models import init_chat_model
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, select
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
import asyncio
import time
from dotenv import load_dotenv

load_dotenv()

# ---------------- DB CONFIG ----------------
DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost:5432/mydb"

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)



async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)



app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_db()

llm = init_chat_model(model="gpt-5.2", model_provider="openai")


async def get_db():
    async with AsyncSessionLocal() as db:
        yield db


class UserCreate(BaseModel):
    name: str
    age: int


@app.post("/user")
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    new_user = User(name=user.name, age=user.age)

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user


@app.get("/get_user")
async def get_user(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    return result.scalars().all()


@app.delete("/user/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()

    if not user:
        return {"error": "User not found"}

    await db.delete(user)
    await db.commit()

    return {"status": f"User deleted: {user_id}"}


# ---------------- CHAT ----------------
class Payload(BaseModel):
    name: str
    userid: int


async def vector_search(userid):
    await asyncio.sleep(0.2)
    return ["Hi my name is sameer", "I Like to play cricket"]


async def user_details(userid):
    await asyncio.sleep(0.3)
    return {"user_age": 30}


async def memory_details(userid):
    await asyncio.sleep(0.1)
    return "User is a good boy."


@app.post("/chat")
async def chat_api(payload: Payload):
    name = payload.name
    userid = payload.userid

    vector, user, memory = await asyncio.gather(
        vector_search(userid),
        user_details(userid),
        memory_details(userid)
    )

    final_prompt = f"""
You are a helpful assistant. Respond politely.

User Name: {name}

Vector search:
{vector}

Memory:
{memory}
"""

    try:
        start = time.time()
        response = await llm.ainvoke(final_prompt)
        total = time.time() - start
        answer = response.content
    except Exception as e:
        print("Error:", e)
        answer = "Error!!!!!!!"
        total = 0

    return {
        "reply": answer,
        "response_time": total
    }