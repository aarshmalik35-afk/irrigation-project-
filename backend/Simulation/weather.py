import random

class Weather:

    def __init__(self):

        self.generate()

    def generate(self):

        self.condition = random.choice(

            ["Sunny", "Cloudy", "Rainy"]

        )

        self.temperature = random.randint(20, 40)

        self.humidity = random.randint(35, 90)

        self.rainfall = 0

        if self.condition == "Rainy":

            self.rainfall = random.randint(10, 40)

    def to_dict(self):

        return {

            "condition": self.condition,

            "temperature": self.temperature,

            "humidity": self.humidity,

            "rainfall": self.rainfall

        }