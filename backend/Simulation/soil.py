import random
from .constants import SOIL_TYPES

class Soil:

    def __init__(self, soil_type):

        self.type = soil_type

        profile = SOIL_TYPES[soil_type]

        self.moisture = random.randint(*profile["moisture"])

        self.ph = round(random.uniform(*profile["ph"]), 1)

        self.nitrogen = random.randint(40, 100)

        self.phosphorus = random.randint(40, 100)

        self.potassium = random.randint(40, 100)

    def to_dict(self):

        return {

            "type": self.type,

            "moisture": self.moisture,

            "ph": self.ph,

            "nitrogen": self.nitrogen,

            "phosphorus": self.phosphorus,

            "potassium": self.potassium

        }