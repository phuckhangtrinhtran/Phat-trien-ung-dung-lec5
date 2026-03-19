from fastapi import FastAPI
from routers.todo_router import router as todo_router

from core.database import engine, Base
from models.todo import Todo  
from routers.auth import router as auth_router
from models import user 

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello To-Do API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

Base.metadata.create_all(bind=engine)
app.include_router(todo_router)
app.include_router(auth_router)