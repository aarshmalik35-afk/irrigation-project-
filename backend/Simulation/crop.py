class Crop:

    def __init__(self, name):
        self.name = name
        self.stage = "Seed"
        self.growth = 0
        self.health = 100

        # Predicted crop yield (%)
        self.yield_prediction = 0
    def update_yield(self):
        """Yield depends mostly on growth, adjusted by health."""

        prediction = self.growth * (self.health / 100)
        # Clamp to 0-100 and round
        self.yield_prediction = round(max(0, min(100, prediction)))

    def to_dict(self):
        self.update_yield()
        return {
            "name": self.name,
            "stage": self.stage,
            "growth": self.growth,
            "health": self.health,
            "yield_prediction": self.yield_prediction,
        }