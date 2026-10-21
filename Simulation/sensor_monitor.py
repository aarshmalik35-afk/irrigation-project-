def check_sensor_status(farm):

    alerts = []

    # Soil Moisture
    if farm.soil.moisture < 0 or farm.soil.moisture > 100:
        alerts.append("❌ Soil moisture sensor malfunction.")

    # pH
    if farm.soil.ph < 0 or farm.soil.ph > 14:
        alerts.append("❌ Soil pH sensor malfunction.")

    # Temperature
    if farm.weather.temperature < -10 or farm.weather.temperature > 60:
        alerts.append("❌ Temperature sensor malfunction.")

    # Humidity
    if farm.weather.humidity < 0 or farm.weather.humidity > 100:
        alerts.append("❌ Humidity sensor malfunction.")

    # Nutrients
    if farm.soil.nitrogen < 0:
        alerts.append("❌ Nitrogen sensor error.")

    if farm.soil.phosphorus < 0:
        alerts.append("❌ Phosphorus sensor error.")

    if farm.soil.potassium < 0:
        alerts.append("❌ Potassium sensor error.")

    if len(alerts) == 0:
        status = "Healthy"
    else:
        status = "Fault Detected"

    return {
        "status": status,
        "alerts": alerts
    }