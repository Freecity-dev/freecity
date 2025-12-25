import random

class PopulationAI:
    def apply(self, city):
        if city.happiness < 50:
            city.population -= random.randint(5, 20)
        else:
            city.population += random.randint(5, 25)

class EconomyAI:
    def apply(self, city):
        variation = random.randint(-1000, 2000)
        city.budget += variation
