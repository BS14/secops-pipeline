"""
Main FastAPI application file.
Defines the root and health check endpoints.
"""
import time
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    """Returns a simple hello message for the root endpoint."""
    return {"message": "Hello, this is a secure FastAPI app!"}


@app.get("/health")
def health():
    """Returns a health check message with the current epoch time."""
    current_epoch_time = int(time.time())
    return {
        "message": "healthy",
        "epoch_time": current_epoch_time
    }
