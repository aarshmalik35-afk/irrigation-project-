from .soil import Soil
from .weather import Weather
from .crop import Crop
from .analytics import Analytics


class Farm:

    def __init__(self, crop_name, soil_type):

        self.day = 1

        self.crop = Crop(crop_name)

        self.soil = Soil(soil_type)

        self.weather = Weather()

        # Analytics
        self.analytics = Analytics()

        # AI Activity Log
        self.ai_logs = []

    def to_dict(self):

        return {

            "day": self.day,

            "crop": self.crop.to_dict(),

            "soil": self.soil.to_dict(),

            "weather": self.weather.to_dict(),

            "analytics": self.analytics.report(),

            "ai_logs": self.ai_logs

        }