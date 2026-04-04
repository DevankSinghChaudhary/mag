from test import main
import json
niche = '{"niche": "Car","audience": "Hagemaru","Value":["gap1","gap2"]}'
niche = json.loads(niche)
print(niche)
dish = main(niche)
print(dish)