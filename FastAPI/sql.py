from fastapi import FastAPI, Depends
from langchain.chat_models import init_chat_model
from sqlalchemy import Column, Integer, String, select
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model(model="gpt-4o", model_provider="openai")

DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost:5432/mydb"

engine = create_async_engine(url=DATABASE_URL, echo=True)

Localsession = sessionmaker(
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


class CreateUser(BaseModel):
    name: str
    age: int


app = FastAPI()


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all) #try block



async def get_db():
    async with Localsession() as db:
        yield db

# async def get_db():
#     db = Localsession()

#     try:
#         yield db

#     finally:
#         await db.close()

@app.on_event("startup")
async def startup():
    await init_db()

@app.post("/user")
async def create_user(user: CreateUser, db: AsyncSession = Depends(get_db)):
    new_user = User(name=user.name, age=user.age)

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user


@app.get("/user")
async def get_user(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    return result.scalars().all()


@app.delete("/user/{user_id}")
async def remove_user(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()

    if not user:
        return {"error": "User not found"}

    await db.delete(user)
    await db.commit()

    return {"message": f"User {user_id} deleted"}