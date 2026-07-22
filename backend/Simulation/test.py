from .farm import Farm
from .simulator import next_day

farm = Farm("Rice", "Loamy")

for i in range(5):
    print("=" * 40)
    print(f"Day {farm.day}")
    print(farm.to_dict())
    next_day(farm)