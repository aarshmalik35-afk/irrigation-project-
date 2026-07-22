from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .farm import Farm
from .simulator import next_day
from .actions import irrigate, add_fertilizer
from .yield_prediction import predict_yield
from .rain_prediction import predict_rain
from .disease import disease_analysis
from .ai_engine import generate_recommendations
from .auto_controller import autonomous_control

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title="AI Smart Irrigation Digital Twin API",
    description="Backend API for an AI-powered Smart Irrigation Digital Twin simulation.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class FertilizerRequest(BaseModel):
    fertilizer: str
    amount: int


# Persistent farm instance
farm = Farm("Rice", "Loamy")


# =========================
# System
# =========================

@app.get(
    "/",
    tags=["System"],
    summary="Welcome endpoint"
)
def home():
    return {
        "message": "AI Smart Irrigation Digital Twin API is running."
    }


@app.get(
    "/health",
    tags=["System"],
    summary="API Health Check"
)
def health():
    return {
        "status": "healthy",
        "version": "1.0.0"
    }


# =========================
# Farm
# =========================

@app.get(
    "/farm",
    tags=["Farm"],
    summary="Get complete farm state"
)
def get_farm():
    return farm.to_dict()


@app.get(
    "/weather",
    tags=["Farm"],
    summary="Get current weather"
)
def get_weather():
    return farm.weather.to_dict()


@app.get(
    "/soil",
    tags=["Farm"],
    summary="Get soil information"
)
def get_soil():
    return farm.soil.to_dict()


@app.get(
    "/crop",
    tags=["Farm"],
    summary="Get crop information"
)
def get_crop():
    return farm.crop.to_dict()


@app.get(
    "/analytics",
    tags=["Farm"],
    summary="Get farm analytics"
)
def get_analytics():
    return farm.analytics.report()


# =========================
# Simulation
# =========================

@app.post(
    "/next-day",
    tags=["Simulation"],
    summary="Advance simulation by one day"
)
def advance_day():

    # Advance the simulation
    next_day(farm)

    # Let the AI make autonomous decisions
    actions = autonomous_control(farm)

    return {
        "message": "Simulation advanced successfully.",
        "actions": actions,
        "farm": farm.to_dict()
    }

# =========================
# Actions
# =========================

@app.post(
    "/irrigate/{litres}",
    tags=["Actions"],
    summary="Irrigate the farm"
)
def irrigate_farm(litres: int):

    if litres <= 0:
        raise HTTPException(
            status_code=400,
            detail="Water amount must be greater than zero."
        )

    irrigate(farm, litres)

    return {
        "message": f"{litres} litres applied successfully.",
        "farm": farm.to_dict()
    }


@app.post(
    "/fertilize",
    tags=["Actions"],
    summary="Apply fertilizer"
)
def fertilize(data: FertilizerRequest):

    if data.amount <= 0:
        raise HTTPException(
            status_code=400,
            detail="Fertilizer amount must be greater than zero."
        )

    add_fertilizer(
        farm,
        data.fertilizer,
        data.amount
    )

    return {
        "message": "Fertilizer applied successfully.",
        "farm": farm.to_dict()
    }


# =========================
# AI Predictions
# =========================

@app.get(
    "/yield",
    tags=["AI"],
    summary="Predict crop yield"
)
def get_yield():
    return predict_yield(farm)


@app.get(
    "/rain-forecast",
    tags=["AI"],
    summary="Predict rainfall"
)
def get_rain_forecast():
    return predict_rain(farm)


@app.get(
    "/disease",
    tags=["AI"],
    summary="Analyze crop disease risk"
)
def get_disease():
    return disease_analysis(farm)


@app.get(
    "/recommendations",
    tags=["AI"],
    summary="Generate AI farming recommendations"
)
def get_recommendations():
    return generate_recommendations(farm)