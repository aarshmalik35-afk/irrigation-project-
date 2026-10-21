from .soil_health import calculate_soil_health

def predict_yield(farm):

    soil_health = calculate_soil_health(farm.soil)

    score = (
        crop_score(farm.crop.health) +
        soil_score(soil_health) +
        moisture_score(farm.soil.moisture) +
        nutrient_score(farm)
    )

    # Maximum score = 100

    predicted_yield = round((score / 100) * 10, 2)

    confidence = round(60 + (score * 0.4), 1)

    if predicted_yield >= 8:
        grade = "Excellent"

    elif predicted_yield >= 6:
        grade = "Good"

    elif predicted_yield >= 4:
        grade = "Average"

    else:
        grade = "Poor"

    return {
        "yield": predicted_yield,
        "confidence": confidence,
        "grade": grade
    }


# -----------------------------
# Helper Functions
# -----------------------------

def crop_score(health):

    return health * 0.30


def soil_score(health):

    return health * 0.30


def moisture_score(moisture):

    if 50 <= moisture <= 80:
        return 20

    elif 40 <= moisture < 50:
        return 15

    elif 80 < moisture <= 90:
        return 15

    else:
        return 5


def nutrient_score(farm):

    average = (
        farm.soil.nitrogen +
        farm.soil.phosphorus +
        farm.soil.potassium
    ) / 3

    return average * 0.20