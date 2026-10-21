from .constants import SOIL_TYPES

def next_day(farm):

    print("next_day() called")
    print("Farm object:", id(farm))
    print("Current day:", farm.day)

    farm.day += 1
    farm.analytics.next_day()

    print("New day:", farm.day)

    farm.weather.generate()

    loss = SOIL_TYPES[farm.soil.type]["water_loss"]

    if farm.weather.condition == "Sunny":
        farm.soil.moisture -= loss

    elif farm.weather.condition == "Cloudy":
        farm.soil.moisture -= loss // 2

    elif farm.weather.condition == "Rainy":
        farm.soil.moisture += farm.weather.rainfall // 2

    farm.soil.moisture = max(0, min(100, farm.soil.moisture))

    farm.soil.nitrogen = max(0, farm.soil.nitrogen - 1)
    farm.soil.phosphorus = max(0, farm.soil.phosphorus - 1)
    farm.soil.potassium = max(0, farm.soil.potassium - 1)

    # ----------------------------
    # Crop growth
    # ----------------------------

    if farm.soil.moisture >= 40 and farm.soil.nitrogen >= 40:
        farm.crop.growth += 5
    else:
        farm.crop.health -= 5

    # ----------------------------
    # Growth stages
    # ----------------------------

    if farm.crop.growth >= 100:
        farm.crop.stage = "Ready to Harvest"

    elif farm.crop.growth >= 75:
        farm.crop.stage = "Mature"

    elif farm.crop.growth >= 50:
        farm.crop.stage = "Flowering"

    elif farm.crop.growth >= 25:
        farm.crop.stage = "Vegetative"

    else:
        farm.crop.stage = "Seed"

    farm.crop.growth = min(100, farm.crop.growth)
    farm.crop.health = max(0, farm.crop.health)