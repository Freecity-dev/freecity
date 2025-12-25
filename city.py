class City:
    def __init__(self, name, city_type):
        self.name = name
        self.city_type = city_type
        self.population = 1000
        self.happiness = 70
        self.budget = 50000

    def update(self):
        # croissance naturelle
        self.population += int(self.population * 0.01)

        # revenus basés sur la population
        self.budget += int(self.population * 2)

        # évolution du bonheur
        if self.budget > 0:
            self.happiness = min(100, self.happiness + 0.1)
        else:
            self.happiness = max(0, self.happiness - 0.5)

    def summary(self):
        return {
            "name": self.name,
            "type": self.city_type,
            "population": self.population,
            "happiness": round(self.happiness, 1),
            "budget": self.budget
        }
