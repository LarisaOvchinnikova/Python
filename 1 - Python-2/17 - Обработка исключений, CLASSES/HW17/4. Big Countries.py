class Country:

    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.density = self.population / self.area

    def is_big(self):
        return self.population > 250000000 or self.area > 3000000

    def compare_pd(self, object):
        if self.density < object.density:
            return f"{self.name} has a smaller population density than {object.name}"
        elif self.density > object.density:
            return f"{self.name} has a larger population density than {object.name}"
        else:
            return f"{self.name} has the same population density as {object.name}"


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)
usa = Country("USA", 328915700, 9519431)
mexico = Country("Mexico", 133140936, 1972550)

print(f"{australia.name} is the big: {australia.is_big()}")
print(f"{andorra.name} is the big: {andorra.is_big()}")
print(f"{usa.name} is the big: {usa.is_big()}")
print(f"{mexico.name} is the big: {mexico.is_big()}")
print()
print(andorra.compare_pd(australia))
print(australia.compare_pd(usa))
print(usa.compare_pd(andorra))
print(usa.compare_pd(mexico))
