from .farm import Farm
from .ai_engine import generate_recommendations
from .actions import irrigate, add_fertilizer, harvest
from .yield_prediction import predict_yield
import simulator
from .disease import disease_analysis
from .soil_health import calculate_soil_health
from .rain_prediction import predict_rain

farm = Farm("Rice", "Loamy")

while True:

    print("\n" + "=" * 55)
    print("        SMART IRRIGATION DIGITAL TWIN")
    print("=" * 55)

    print(f"\nDAY : {farm.day}")

    print("\n------------ CROP ------------")

    print(f"Name : {farm.crop.name}")
    print(f"Stage : {farm.crop.stage}")
    print(f"Growth : {farm.crop.growth}%")
    print(f"Health : {farm.crop.health}%")

    print("\n------------ SOIL ------------")

    print(f"Type : {farm.soil.type}")
    print(f"Moisture : {farm.soil.moisture}%")
    print(f"pH : {farm.soil.ph}")

    print(f"Nitrogen : {farm.soil.nitrogen}")
    print(f"Phosphorus : {farm.soil.phosphorus}")
    print(f"Potassium : {farm.soil.potassium}")

    print("\n---------- WEATHER -----------")

    print(f"Condition : {farm.weather.condition}")
    print(f"Temperature : {farm.weather.temperature}°C")
    print(f"Humidity : {farm.weather.humidity}%")
    print(f"Rainfall : {farm.weather.rainfall} mm")

    rain = predict_rain(farm)

    print("\n RAIN FORECAST")
    print("-" * 30)

    print(f"Probability : {rain['probability']}%")
    print(f"Forecast    : {rain['forecast']}")

    rain = predict_rain(farm)

    recommendations = []

    recommendations.append(
        f" Rain Probability: {rain['probability']}%"
    )

    recommendations.append(
        f" Forecast: {rain['forecast']}"
    )

    if rain["probability"] >= 70:
        recommendations.append(
            " Delay irrigation. Rain is likely."
        )

    elif rain["probability"] >= 40:
        recommendations.append(
            " Consider reducing irrigation due to possible rainfall."
        )

    else:
        recommendations.append(
            " No rainfall expected. Irrigation can continue if required."
        )

    # Soil Health
    health = calculate_soil_health(farm.soil)

    print("\n SOIL HEALTH")
    print(f"{health}%")

    # AI Recommendations
    print("\n AI RECOMMENDATIONS")
    print("-" * 30)

    recommendations = generate_recommendations(farm)

    for recommendation in recommendations:
        print(recommendation)

    # Analytics
    report = farm.analytics.report()

    print("\n ANALYTICS")
    print("-" * 30)
    print(f"Days Simulated   : {report['days']}")
    print(f"Water Used       : {report['water_used']} L")
    print(f"Irrigations      : {report['irrigations']}")
    print(f"Nitrogen Added   : {report['nitrogen']}")
    print(f"Phosphorus Added : {report['phosphorus']}")
    print(f"Potassium Added  : {report['potassium']}")
    print(f"Water Efficiency : {report['efficiency']}%")

    # Yield Prediction
    prediction = predict_yield(farm)

    print("\n YIELD PREDICTION")
    print("-" * 30)
    print(f"Expected Yield : {prediction['yield']} tons/hectare")
    print(f"Confidence     : {prediction['confidence']}%")
    print(f"Grade          : {prediction['grade']}")

    # Menu
    print("\n==============================")
    print("1. Next Day")
    print("2. Irrigate")
    print("3. Add Fertilizer")
    print("4. Harvest")
    print("5. Exit")

    disease = disease_analysis(farm)

    print("\n DISEASE ANALYSIS")
    print("-" * 30)

    print(f"Risk Level : {disease['level']}")
    print(f"Risk Score : {disease['risk']}%")

    if disease["causes"]:
     print("\nPossible Causes:")
    for cause in disease["causes"]:
        print(f"- {cause}")
    else:
     print("No disease risks detected.")
    choice = input("\nChoice : ")

    if choice == "1":
        simulator.next_day(farm)

    elif choice == "2":
        litres = int(input("\nEnter water amount (litres): "))
        irrigate(farm, litres)

    elif choice == "3":

        print("\nChoose Fertilizer")
        print("1. Nitrogen")
        print("2. Phosphorus")
        print("3. Potassium")

        option = input("\nChoice : ")
        amount = int(input("Amount : "))

        if option == "1":
            add_fertilizer(farm, "N", amount)

        elif option == "2":
            add_fertilizer(farm, "P", amount)

        elif option == "3":
            add_fertilizer(farm, "K", amount)

        else:
            print("Invalid choice!")

    elif choice == "4":
        harvest(farm)

    elif choice == "5":
        break

    else:
        print("Invalid choice!")