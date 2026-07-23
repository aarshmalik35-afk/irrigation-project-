from .soil_health import calculate_soil_health
from .disease import disease_analysis
from .rain_prediction import predict_rain
from .yield_prediction import predict_yield
from .sensor_monitor import check_sensor_status
def generate_recommendations(farm):

    recommendations = []

    soil = farm.soil
    crop = farm.crop
    weather = farm.weather

    # ---------------------------------
    # Soil Moisture
    # ---------------------------------

    if soil.moisture < 40:
        recommendations.append(" Soil moisture is LOW. Irrigate with 25-30 litres.")

    elif soil.moisture > 90:
        recommendations.append(" Soil is waterlogged. Stop irrigation immediately.")

    else:
        recommendations.append(" Soil moisture is optimal.")

    # ---------------------------------
    # Weather Analysis
    # ---------------------------------

    if weather.condition == "Rainy":
        recommendations.append(" Rain detected. Skip irrigation today.")

    elif weather.temperature > 35:
        recommendations.append(" High temperature. Increase moisture monitoring.")

    elif weather.temperature < 18:
        recommendations.append(" Low temperature may slow crop growth.")

    if weather.humidity > 80:
        recommendations.append(" High humidity detected. Watch for fungal diseases.")

    # ---------------------------------
    # Nutrient Analysis
    # ---------------------------------

    if soil.nitrogen < 40:
        recommendations.append(" Nitrogen is low. Apply Nitrogen fertilizer.")

    if soil.phosphorus < 40:
        recommendations.append(" Phosphorus is low. Apply Phosphorus fertilizer.")

    if soil.potassium < 40:
        recommendations.append(" Potassium is low. Apply Potassium fertilizer.")

    if (
        soil.nitrogen >= 40 and
        soil.phosphorus >= 40 and
        soil.potassium >= 40
    ):
        recommendations.append(" Nutrient levels are balanced.")

    # ---------------------------------
    # Soil Health
    # ---------------------------------

    health = calculate_soil_health(soil)

    if health >= 80:
        recommendations.append(" Soil health is GOOD.")

    elif health >= 60:
        recommendations.append(" Soil health is MODERATE.")

    else:
        recommendations.append(" Soil health is POOR. Improve soil conditions.")

    # ---------------------------------
    # Crop Health
    # ---------------------------------

    if crop.health >= 90:
        recommendations.append(" Crop health is EXCELLENT.")

    elif crop.health >= 70:
        recommendations.append(" Crop health is GOOD.")

    elif crop.health >= 50:
        recommendations.append(" Crop health is declining.")

    else:
        recommendations.append(" Crop health is CRITICAL.")

    # ---------------------------------
    # Growth Stage
    # ---------------------------------

    recommendations.append(f" Current Stage: {crop.stage}")

    if crop.stage == "Ready to Harvest":
        recommendations.append(" Crop is ready for harvest!")

    # ---------------------------------
    # Yield Prediction
    # ---------------------------------

    prediction = predict_yield(farm)

    recommendations.append(
        f" Estimated Yield: {prediction['yield']} tons/hectare ({prediction['grade']})"
    )

    if prediction["grade"] == "Poor":
        recommendations.append(" Improve irrigation and nutrients to increase yield.")

    elif prediction["grade"] == "Excellent":
        recommendations.append(" Excellent growing conditions detected.")

    # ---------------------------------
    # Disease Analysis
    # ---------------------------------

    disease = disease_analysis(farm)

    recommendations.append(
        f" Disease Risk: {disease['level']} ({disease['risk']}%)"
    )

    if disease["level"] == "High":
        recommendations.append(
            " Immediate crop inspection recommended."
        )

    elif disease["level"] == "Moderate":
        recommendations.append(
            " Monitor crops regularly for disease symptoms."
        )

    else:
        recommendations.append(
            " Disease risk is low."
        )

    # ---------------------------------
    # Water Efficiency
    # ---------------------------------

    efficiency = farm.analytics.water_efficiency()

    if efficiency >= 90:
        recommendations.append(" Water usage is highly efficient.")

    elif efficiency >= 75:
        recommendations.append(" Water efficiency is acceptable.")

    else:
        recommendations.append(" Water consumption is higher than recommended.")

    sensor = check_sensor_status(farm)

    if sensor["status"] == "Healthy":
        recommendations.append(
            " All sensors are functioning normally."
        )
    else:
        recommendations.append(
            " Sensor fault detected."
        )

    for alert in sensor["alerts"]:
        recommendations.append(alert)

    # ---------------------------------
    # Overall Farm Status
    # ---------------------------------

    score = 0

    if health >= 80:
        score += 1

    if crop.health >= 80:
        score += 1

    if disease["risk"] < 40:
        score += 1

    if prediction["grade"] in ["Excellent", "Good"]:
        score += 1

    if score == 4:
        recommendations.append(" Overall Farm Status: Excellent")

    elif score == 3:
        recommendations.append(" Overall Farm Status: Good")

    elif score == 2:
        recommendations.append(" Overall Farm Status: Fair")

    else:
        recommendations.append(" Overall Farm Status: Needs Immediate Attention")

    return recommendations