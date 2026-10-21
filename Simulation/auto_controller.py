from .actions import irrigate, add_fertilizer


def log(farm, message):
    """Store AI activity log (keep last 20 entries)."""

    farm.ai_logs.append(message)

    if len(farm.ai_logs) > 12:
        farm.ai_logs.pop(0)


def autonomous_control(farm):

    actions = []

    soil = farm.soil
    weather = farm.weather

    MOISTURE_MIN = 40
    MOISTURE_TARGET = 70

    NUTRIENT_MIN = 40
    NUTRIENT_TARGET = 60

    # ==========================
    # SMART IRRIGATION
    # ==========================

    if weather.condition == "Rainy":

        message = "🌧 Rain expected. Irrigation skipped."

        actions.append(message)
        log(farm, message)

    elif soil.moisture < MOISTURE_MIN:

        current = soil.moisture

        litres = int((MOISTURE_TARGET - current) * 2)

        litres = max(10, min(litres, 40))

        irrigate(farm, litres)

        message = (
            f" Soil moisture was {current:.1f}%. "
            f"AI irrigated with {litres}L."
        )

        actions.append(message)
        log(farm, message)

    elif soil.moisture > 85:

        message = " Soil already has sufficient water. Irrigation skipped."

        actions.append(message)
        log(farm, message)

    else:

        message = " Soil moisture is within the optimal range."

        actions.append(message)
        log(farm, message)

    # ==========================
    # SMART FERTILIZATION
    # ==========================

    if weather.condition == "Rainy":

        message = "🌧 Fertilizer application postponed due to rain."

        actions.append(message)
        log(farm, message)

    else:

        nutrients = [
            ("N", soil.nitrogen, "Nitrogen"),
            ("P", soil.phosphorus, "Phosphorus"),
            ("K", soil.potassium, "Potassium"),
        ]

        for code, value, name in nutrients:

            if value < NUTRIENT_MIN:

                amount = int((NUTRIENT_TARGET - value) / 2)

                amount = max(5, min(amount, 15))

                add_fertilizer(farm, code, amount)

                message = (
                    f" {name} level was {value:.1f}. "
                    f"AI applied {amount}% {name} fertilizer."
                )

                actions.append(message)
                log(farm, message)

            elif value > 85:

                message = f" {name} level is already high. No fertilizer applied."

                actions.append(message)
                log(farm, message)

            else:

                message = f" {name} level is optimal."

                actions.append(message)
                log(farm, message)

    # ==========================
    # SUMMARY
    # ==========================

    summary = " Autonomous control cycle completed."

    actions.append(summary)
    log(farm, summary)

    return actions