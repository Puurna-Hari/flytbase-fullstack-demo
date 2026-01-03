from fastapi import APIRouter
from models.schemas import InputData
from services.logic import predict_logic

router = APIRouter()

@router.post("/predict")
def predict(data: InputData):
    return predict_logic(data.name, data.age)
