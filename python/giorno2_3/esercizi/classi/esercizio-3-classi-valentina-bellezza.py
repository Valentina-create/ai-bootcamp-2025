class Country:
    def __init__(self, name):
        self.name = name
        self.region = []

    def add_region(self, region):
        self.region.append(region)

italy = Country("Italy")

assert italy.name == "Italy"


class Region:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def add_city(self, city):
        self.city.append(city)


sicily = Region ("Sicily", "Palermo, Catania")

italy.add_region(sicily)

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    @property
    def pop(self):
        return self.population

catania = City("Catania", 300_000)
palermo = City("Palermo", 600_000)

sicily.add_city (catania)
sicily.add_city (palermo)

total_population = catania.pop + palermo.pop
print(f"La popolazione totale di Catania e Palermo è: {total_population}")

assert sicily.pop == 900_000

calabria = Region("Calabria")

reggio_calabria = City("Reggio Calabria", 170_000)
calabria.add_city(reggio_calabria)

italy.add_region(calabria)

