from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Bin Packaging!", "message": "Welcome to FastAPI!"}