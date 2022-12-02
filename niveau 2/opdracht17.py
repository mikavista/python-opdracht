import random
print("lootbox opent nu")
print("................")
box = ("common", "uncommon", "rare", "ultra rare", "epic", "legendary", "god tier")
print(random.choices(box, weights=(49, 30 ,10, 5, 3, 2, 1,)))