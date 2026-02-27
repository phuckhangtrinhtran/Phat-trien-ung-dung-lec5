from fastapi import FastAPI
from core.config import settings
from routers.todo_router import router as todo_router

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

@app.get("/")
def read_root():
    return {"message": "Hello To-Do API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(todo_router)