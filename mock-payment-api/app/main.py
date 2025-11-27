from fastapi import FastAPI
from app.routes.user_routes import user_router
from app.routes.payment_routes import payment_router

app = FastAPI(title="Mock Payment API", version="1.0")

app.include_router(user_router, prefix="/api/users", tags=["Users"])
app.include_router(payment_router, prefix="/api/payments", tags=["Payments"])

@app.get("/")
def root():
    return {"message": "Mock Payment API is running 🚀"}
