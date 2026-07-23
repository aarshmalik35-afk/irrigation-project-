import random

SOIL_TYPES = {
    "Loamy": {
        "moisture": (55, 75),
        "ph": (6.2, 7.2),
        "water_loss": 4
    },

    "Sandy": {
        "moisture": (30, 55),
        "ph": (5.5, 6.8),
        "water_loss": 8
    },

    "Clay": {
        "moisture": (60, 85),
        "ph": (6.5, 8.0),
        "water_loss": 2
    }
}

CROPS = {

    "Rice": {
        "ideal_moisture": 70,
        "daily_water": 30
    },

    "Wheat": {
        "ideal_moisture": 55,
        "daily_water": 18
    },

    "Tomato": {
        "ideal_moisture": 60,
        "daily_water": 15
    },

    "Cotton": {
        "ideal_moisture": 45,
        "daily_water": 12
    }
}

WEATHER = [

    "Sunny",
    "Cloudy",
    "Rainy"
]