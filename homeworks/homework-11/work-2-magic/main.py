from magicians.water import Water
from magicians.soil import Soil
from magicians.fire import Fire
from magicians.air import Air


water = Water()
fire = Fire()
air = Air()
soil = Soil()

print(f"{water.name} + {fire.name} = {water + fire}")
print(f"{water.name} + {air.name} = {air + water}")
print(f"{water.name} + {soil.name} = {water + soil}")

print(f"{fire.name} + {air.name} = {fire + air}")
print(f"{fire.name} + {soil.name} = {fire + soil}")

print(f"{air.name} + {soil.name} = {soil + air}")

