#!/usr/bin/env python3

from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # zone apex
def zone_apex():
    return {"Good Day": "Sunshine!"}

@app.get("/sum/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@app.get("/multiply/{c}/{d}")
def multiply(c: int, d: int):
    return {"product": c * d}

@app.get("/square/{a}")  # New endpoint to return the square of a number
def square(a: int):
    return {"square": a * a}

