from fastapi import FastAPI
from policy import evaluate

app = FastAPI()


@app.post("/")
def guardrail(request: dict):
    return evaluate(request)