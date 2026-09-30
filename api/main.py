from fastapi import FastAPI

from api.routes.prediction import router as prediction_router


app = FastAPI(
    title="Payment Transaction Analytics API",
    description="API for payment transaction risk prediction",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "payment-transaction-analytics-api"
    }


app.include_router(prediction_router)