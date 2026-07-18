from fastapi import FastAPI
from fastapi.responses import JSONResponse, Response
from policy import evaluate

app = FastAPI()


@app.get("/")
def health():
    return {"status": "ok"}


@app.head("/")
def health_head():
    return Response(status_code=200)


@app.post("/")
def guardrail(request: dict):
    return JSONResponse(content=evaluate(request))


@app.post("/check")
def guardrail_check(request: dict):
    return JSONResponse(content=evaluate(request))