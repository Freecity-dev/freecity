from world import World
from city import City

# création du monde
world = World()

# création de la ville Angelica
angelica = City("Angelica", "Smart City")
world.add_city(angelica)

# simulation de 10 cycles
for day in range(1, 11):
    world.tick()
    print(f"Jour {day} :", angelica.summary())
  Add runnable game prototype
