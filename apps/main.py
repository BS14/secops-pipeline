from fastapi import FastAPI
import time

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello, this is a secure FastAPI app!"}


@app.get("/health")
def health():
    current_epoch_time = int(time.time())
    return {
        "message": "healthy",
        "epoch_time": current_epoch_time
    }
