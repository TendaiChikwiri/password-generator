from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models import custom
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return "Password generator home"


@app.get("/api/generate")
async def random_password():
    from scripts import generate
    password = generate.generate_password(10, True, True, True)
    response = {"password": password}
    return JSONResponse(response)


@app.post("/api/generate")
async def custom_password(custom: custom.CustomPassword):
    print(custom)
    from scripts import generate
    password = generate.generate_password(
        custom.length, custom.symbols, custom.numbers, custom.letters)
    response = {"password": password}
    return JSONResponse(response)
