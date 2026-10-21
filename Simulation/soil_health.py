def calculate_soil_health(soil):

    score = 100

    # Moisture

    if soil.moisture < 40:
        score -= 25

    elif soil.moisture > 90:
        score -= 15

    # pH

    if soil.ph < 6:
        score -= 15

    elif soil.ph > 8:
        score -= 15

    # Nitrogen

    if soil.nitrogen < 40:
        score -= 10

    # Phosphorus

    if soil.phosphorus < 40:
        score -= 10

    # Potassium

    if soil.potassium < 40:
        score -= 10

    return max(score,0)