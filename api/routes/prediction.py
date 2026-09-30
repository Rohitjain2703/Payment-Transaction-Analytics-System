from fastapi import APIRouter

from api.schemas import PredictionRequest, PredictionResponse


router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"]
)


@router.post("/", response_model=PredictionResponse)
def predict(request: PredictionRequest):

    # Temporary response.
    # Actual ML model will be connected later.

    prediction = "LOW_RISK"
    probability = 0.90

    return PredictionResponse(
        prediction=prediction,
        probability=probability
    )