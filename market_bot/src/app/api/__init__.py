from fastapi import APIRouter

from .items.items_views import router as items_router
from .users.users_views import router as users_router
from .users.users_history_views import router as users_history_router
from .products.products_views import router as products_router
from .products.product_type_view import router as product_types_router
from .delivery.delivery_status_view import router as delivery_status_router
from .delivery.delivery_type_views import router as delivery_type_router
from .orders.orders_views import router as orders_router
from .rooms.rooms_views import router as rooms_router
from .promo.promo_views import router as promo_router


router = APIRouter()

router.include_router(items_router, prefix="/items")
router.include_router(users_router, prefix="/users")
router.include_router(users_history_router, prefix="/users_history")
router.include_router(products_router, prefix="/products")
router.include_router(product_types_router, prefix="/product-types")
router.include_router(delivery_status_router, prefix="/delivery-status")
router.include_router(delivery_type_router, prefix="/delivery-type")
router.include_router(orders_router, prefix="/order")
router.include_router(rooms_router, prefix="/room")
router.include_router(promo_router, prefix="/promo")
