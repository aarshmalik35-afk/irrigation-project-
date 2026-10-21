def irrigate(farm, litres):
    farm.analytics.record_irrigation(litres)

    increase = litres // 2

    farm.soil.moisture += increase

    if farm.soil.moisture > 100:
        farm.soil.moisture = 100

    print(f"\n Applied {litres} litres of water.")
    print(f"Soil moisture is now {farm.soil.moisture}%")

def add_fertilizer(farm, fertilizer, amount):
    farm.analytics.record_fertilizer(fertilizer, amount)

def add_fertilizer(farm, fertilizer, amount):

    farm.analytics.record_fertilizer(fertilizer, amount)

    if fertilizer == "N":
        farm.soil.nitrogen += amount

    elif fertilizer == "P":
        farm.soil.phosphorus += amount

    elif fertilizer == "K":
        farm.soil.potassium += amount

    elif fertilizer == "NPK":
        farm.soil.nitrogen += amount
        farm.soil.phosphorus += amount
        farm.soil.potassium += amount

    print("\nUpdated Nutrients")
    print(f"Nitrogen   : {farm.soil.nitrogen}")
    print(f"Phosphorus : {farm.soil.phosphorus}")
    print(f"Potassium  : {farm.soil.potassium}")

def harvest(farm):

    if farm.crop.growth < 100:
        print("\n Crop is not ready for harvest.")
        return

    yield_amount = (
        farm.crop.health +
        farm.soil.moisture +
        farm.soil.nitrogen +
        farm.soil.phosphorus +
        farm.soil.potassium
    ) / 5

    print("\n Harvest Successful!")
    print(f"Estimated Yield : {yield_amount:.1f} kg")

    farm.crop.growth = 0
    farm.crop.health = 100
    farm.crop.stage = "Seed"