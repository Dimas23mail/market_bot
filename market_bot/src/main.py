from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app import api_routers


@asynccontextmanager
async def lifespan(app: FastAPI):

    yield


app = FastAPI(lifespan=lifespan)
app.include_router(api_routers)


@app.get("/")
def hello_index():
    return {
        "message": "Hello, index!",
    }


@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello, {name}!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
