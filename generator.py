import math

class Seed:
    def __init__(self, name, rank, grade, stat_items):
        self.name = name
        self.rank = rank
        self.grade = grade
        self.stat_items = stat_items

    def __str__(self):
        return self.name + " " + str(self.rank) + " " + ("*"*self.grade)

seeds = [
        Seed("Mixed Herb Seeds",      27, 1, ["Str"]),
        Seed("Western Fodlan Seeds",   9, 1, ["Hp"]),
        Seed("Root Vegetable Seed",   49, 1, ["Def"]),
        Seed("Vegetable Seeds",       33, 1, ["Res"]),
        Seed("Northern Fodlan Seeds", 53, 2, ["Cha"]),
        Seed("Southern Fodlan Seeds", 37, 2, ["Mag"]),
        Seed("Morfis Seeds",          23, 2, ["Dex"]),
        Seed("Boa-Fruit Seeds",       31, 5, ["Lck"]),
        Seed("Albinean Seeds",        20, 2, ["Cha"]),
        Seed("Eastern Fodlan Seeds",  42, 2, ["Def"]),
        Seed("Mixed Fruit Seeds",     44, 1, ["Lck"]),
        Seed("Red Flower Seeds",      24, 3, ["Res"]),
        Seed("White Flower Seeds",     5, 3, ["Cha"]),
        Seed("Blue Flower Seeds",     38, 3, ["Hp"]),
        Seed("Purple Flower Seeds",   16, 3, ["Str"]),
        Seed("Yellow Flower Seeds",   55, 3, ["Mag"]),
        Seed("Green Flower Seeds",    10, 3, ["Dex"]),
        Seed("Angelica Seeds",        34, 1, ["Str"]),
        Seed("Morfis-Plum Seeds",     18, 1, ["Dex"]),
        Seed("Nordsalat Seeds",        3, 1, ["Spd"]),
        Seed("Pale-Blue Flower Seeds", 1, 3, ["Spd"])
        ]


def yieldValue(seeds, cultivation):
    sum_of_ranks = 0
    sum_of_grades = 0
    for seed in seeds:
        sum_of_ranks += seed.rank
        sum_of_grades += seed.grade

    A = (12 - sum_of_ranks % 12) * 5
    B = math.floor(sum_of_grades / 0.8)
    C = (cultivation + 4) * 2
    return A + B + C

def yieldClass(value):
    if value <= 20:
        return 0.5
    if value <= 40:
        return 1.0
    if value <= 60:
        return 1.5
    if value <= 80:
        return 2.0
    if value <= 90:
        return 2.5
    return 3.0

def explore(current_seeds, max_seeds, last_seed_index, found_combinations):
    for cultivation_level in range(1, 7):
        if yieldClass(yieldValue(current_seeds, cultivation_level)) >= 2.7:
            found_combinations.append([[i for i in current_seeds], cultivation_level])
            break

    if len(current_seeds) < max_seeds:
        for i in range(last_seed_index, len(seeds)):
            current_seeds.append(seeds[i])
            explore(current_seeds, max_seeds, i, found_combinations)
            current_seeds.pop()

results = []
explore([], 5, 0, results)

for result in results:
    for seed in result[0]:
        print(str(seed) + ", ", end="")
    print("Min cult:", result[1])

