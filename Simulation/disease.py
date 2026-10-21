def disease_analysis(farm):

    risk = 0
    diseases = []

    # High humidity increases fungal disease risk
    if farm.weather.humidity > 80:
        risk += 25
        diseases.append("High humidity may cause fungal diseases.")

    # Excess water
    if farm.soil.moisture > 85:
        risk += 20
        diseases.append("Overwatering can lead to root rot.")

    # Dry soil
    if farm.soil.moisture < 35:
        risk += 20
        diseases.append("Dry soil increases plant stress.")

    # High temperature
    if farm.weather.temperature > 35:
        risk += 15
        diseases.append("High temperature may reduce crop immunity.")

    # Weak crop
    if farm.crop.health < 60:
        risk += 20
        diseases.append("Weak crop health increases disease susceptibility.")

    # Long rainy period
    if farm.weather.condition == "Rainy":
        risk += 10
        diseases.append("Rainy conditions favour fungal growth.")

    risk = min(risk, 100)

    if risk >= 70:
        level = "High"

    elif risk >= 40:
        level = "Moderate"

    else:
        level = "Low"

    return {
        "risk": risk,
        "level": level,
        "causes": diseases
    }