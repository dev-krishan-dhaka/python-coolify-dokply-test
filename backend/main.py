from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend Running 🚀"}

@app.get("/todos")
def get_todos():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM todos"))
        todos = [dict(row._mapping) for row in result]
        return todos

@app.post("/todos")
def add_todo(todo: dict):
    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO todos(text) VALUES (:text)"),
            {"text": todo["text"]}
        )
        conn.commit()

    return {"success": True}
