from city import City
from ai import PopulationAI, EconomyAI

class World:
    def __init__(self):
        self.cities = []
        self.population_ai = PopulationAI()
        self.economy_ai = EconomyAI()

    def add_city(self, city):
        self.cities.append(city)

    def tick(self):
        for city in self.cities:
            self.population_ai.apply(city)
            self.economy_ai.apply(city)
            city.update()
          Add world simulation engine
