from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    customer_id: int
    merchant_id: int
    payment_method_id: int
    amount: float = Field(gt=0)
    transaction_type: str
    channel: str
    city: str
    state: str


class PredictionResponse(BaseModel):
    prediction: str
    probability: float