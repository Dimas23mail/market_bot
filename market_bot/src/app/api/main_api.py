from contextlib import asynccontextmanager

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import init_db

import requests as rq


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print("Bot is ready, api is running")
    yield


def run_api_application():
    app = FastAPI(title="back_API", lifespan=lifespan)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/api/products/{tg_id}")
    async def products(tg_id: int, product_name: str):
        pass
