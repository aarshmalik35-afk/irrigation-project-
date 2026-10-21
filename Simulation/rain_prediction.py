import random

def predict_rain(farm):

    probability = 0

    # Current weather
    if farm.weather.condition == "Rainy":
        probability += 45

    elif farm.weather.condition == "Cloudy":
        probability += 25

    # Humidity
    if farm.weather.humidity > 80:
        probability += 30

    elif farm.weather.humidity > 60:
        probability += 15

    # Temperature
    if farm.weather.temperature < 28:
        probability += 15

    elif farm.weather.temperature > 35:
        probability -= 10

    probability += random.randint(-5, 5)

    probability = max(0, min(100, probability))

    if probability >= 70:
        forecast = "Heavy Rain Expected"

    elif probability >= 40:
        forecast = "Light Rain Possible"

    else:
        forecast = "No Significant Rain"

    return {
        "probability": probability,
        "forecast": forecast
    }