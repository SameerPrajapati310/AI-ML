from fastapi import FastAPI, Depends
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from sqlalchemy import Column, Integer, String, select
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from pydantic import BaseModel
from dotenv import load_dotenv
from celery import Celery
from sqlalchemy import DateTime, Boolean
from datetime import datetime


load_dotenv()


celery_app = Celery(
    "reminder_app",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

llm = init_chat_model(model="gpt-4o", model_provider="openai")

DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost:5432/mydb"

engine = create_async_engine(url=DATABASE_URL, echo=True)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SYNC_DATABASE_URL = "postgresql://postgres:1234@localhost:5432/mydb"

sync_engine = create_engine(SYNC_DATABASE_URL)

SyncSession = sessionmaker(bind=sync_engine)

Localsession = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String)
    remind_at = Column(DateTime)
    is_sent = Column(Boolean, default=False)


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

@celery_app.task
def send_reminder(reminder_id, message):
    print(f"🔔 Reminder: {message}")

    db = SyncSession()
    try:
        reminder = db.query(Reminder).filter(Reminder.id == reminder_id).first()
        if reminder:
            reminder.is_sent = True
            db.commit()
    finally:
        db.close()

@app.on_event("startup")
async def startup():
    await init_db()

from datetime import datetime, timedelta

@tool(description="Use this tool to set reminder")
async def remind(msg: str, count_down: int):
    """
    msg : short description
    count_down : seconds
    """

    async with Localsession() as db:
        remind_time = datetime.utcnow() + timedelta(seconds=count_down)

        reminder = Reminder(
            message=msg,
            remind_at=remind_time
        )

        db.add(reminder)
        await db.commit()
        await db.refresh(reminder)

    send_reminder.apply_async(
        args=[reminder.id, msg],
        countdown=count_down
    )

    return f"Reminder set for '{msg}' in {count_down} seconds"

llm = init_chat_model(model="gpt-5.2",model_provider="openai")

SYSTEM_PROMPT="""
You are a help full assistant your task is to set reminder for the user. Based on the user query.
You have the access of the following tool:

Remind : Use this tool to set the reminder.

User Query:
{query}
"""
llm_with_tools = llm.bind_tools([remind])

import asyncio

async def main():
    while True:
        user = input("[YOU] : ")
        if user in ("q","exit"):
            break

        result = llm_with_tools.invoke(user)

        if result.tool_calls:
            for tool_call in result.tool_calls:
                tool_result = await remind.ainvoke(tool_call["args"])
                print(tool_result)
        else:
            print(result.content)

if __name__ == "__main__":
    asyncio.run(main())