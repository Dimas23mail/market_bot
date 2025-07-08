from fastapi import APIRouter

from app.api.users.users_views import router as users_router

router = APIRouter()

router.include_router(users_router)
