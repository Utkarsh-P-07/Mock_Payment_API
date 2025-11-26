from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import get_settings
from .routes.order_routes import router as order_router
from .routes.payment_routes import router as payment_router
from .routes.user.routes import router as user_router


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        description="Mock Razorpay-like payment API built with FastAPI and MongoDB.",
    )

    # CORS
    origins = [
        *(settings.backend_cors_origins or []),
        "http://localhost",
        "http://localhost:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routers
    app.include_router(user_router, prefix="/api/users", tags=["users"])
    app.include_router(order_router, prefix="/api/orders", tags=["orders"])
    app.include_router(payment_router, prefix="/api/payments", tags=["payments"])

    @app.get("/health", tags=["health"])
    async def health_check():
        return {"status": "ok"}

    return app


app = create_app()


