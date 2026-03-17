from fastapi import FastAPI
from routers.todo_router import router as todo_router

from core.database import engine, Base
from models.todo import Todo   # import để SQLAlchemy biết model

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello To-Do API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(todo_router)