from fastapi import APIRouter

from app.api.items.items_views import router as items_router

router = APIRouter()

router.include_router(items_router)
