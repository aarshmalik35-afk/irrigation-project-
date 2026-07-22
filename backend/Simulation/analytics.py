from typing import Self


class Analytics:

    def __init__(self):

        self.total_water_used = 0
        self.irrigation_count = 0

        self.total_nitrogen_used = 0
        self.total_phosphorus_used = 0
        self.total_potassium_used = 0

        self.days_simulated = 1

    # -------------------------
    # Water
    # -------------------------

    def record_irrigation(self, litres):
        print(f"Recording irrigation: {litres} L")
        self.total_water_used += litres
        self.irrigation_count += 1

    # -------------------------
    # Fertilizer
    # -------------------------

    def record_fertilizer(self, fertilizer, amount):
        if fertilizer == "N":
            self.total_nitrogen_used += amount

        elif fertilizer == "P":
            self.total_phosphorus_used += amount

        elif fertilizer == "K":
            self.total_potassium_used += amount

        elif fertilizer == "NPK":
            self.total_nitrogen_used += amount
            self.total_phosphorus_used += amount
            self.total_potassium_used += amount
    # -------------------------
    # Days
    # -------------------------

    def next_day(self):

        self.days_simulated += 1

    # -------------------------
    # Water Efficiency
    # -------------------------

    def water_efficiency(self):

        if self.irrigation_count == 0:
            return 100

        average = self.total_water_used / self.irrigation_count

        if average <= 20:
            return 100

        elif average <= 30:
            return 90

        elif average <= 40:
            return 80

        else:
            return 65

    # -------------------------
    # Report
    # -------------------------

    def report(self):

        return {

            "days": self.days_simulated,

            "water_used": self.total_water_used,

            "irrigations": self.irrigation_count,

            "nitrogen": self.total_nitrogen_used,

            "phosphorus": self.total_phosphorus_used,

            "potassium": self.total_potassium_used,

            "efficiency": self.water_efficiency()

        }