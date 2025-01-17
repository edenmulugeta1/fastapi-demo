#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os

app = FastAPI()

# Root endpoint returning a friendly message
@app.get("/")  # zone apex
def zone_apex():
    return {"Good Day": "Sunshine!"}

# Endpoint to sum two numbers
@app.get("/sum/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

# Endpoint to multiply two numbers
@app.get("/multiply/{c}/{d}")
def multiply(c: int, d: int):
    return {"product": c * d}

# New endpoint to subtract two numbers
@app.get("/subtract/{x}/{y}")
def subtract(x: int, y: int):
    return {"difference": x - y}

# New endpoint to divide two numbers
@app.get("/divide/{m}/{n}")
def divide(m: int, n: int):
    if n == 0:
        return {"error": "Cannot divide by zero"}
    return {"quotient": m / n}

# New endpoint to square a number
@app.get("/square/{a}")
def square(a: int):
    return {"square": a ** 2}

@app.get("/new-endpoint")
def read_new_endpoint():
    return {"message": "This is a new endpoint!"}
