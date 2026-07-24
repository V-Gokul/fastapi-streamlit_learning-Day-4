from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Calculator API")


class CalculationRequest(BaseModel):
    a: float
    b: float


@app.get("/")
def home():
    return {
        "message": "Welcome to the FastAPI Calculator API",
        "endpoints": [
            "/add",
            "/subtract",
            "/multiply",
            "/divide"
        ]
    }


@app.post("/add")
def add(data: CalculationRequest):
    return {
        "operation": "addition",
        "result": data.a + data.b
    }


@app.post("/subtract")
def subtract(data: CalculationRequest):
    return {
        "operation": "subtraction",
        "result": data.a - data.b
    }


@app.post("/multiply")
def multiply(data: CalculationRequest):
    return {
        "operation": "multiplication",
        "result": data.a * data.b
    }


@app.post("/divide")
def divide(data: CalculationRequest):
    if data.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")

    return {
        "operation": "division",
        "result": data.a / data.b
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("calculator:app", host="0.0.0.0", port=8000, reload=True)
