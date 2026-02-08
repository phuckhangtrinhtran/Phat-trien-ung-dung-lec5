from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello To-Do API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
