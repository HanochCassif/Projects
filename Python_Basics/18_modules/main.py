# first method - import the whole module

import converters
print(converters.kg_to_lbs(45))


# second method - import only relevant functions from module
from converters import lbs_to_kg
print(lbs_to_kg(100))
