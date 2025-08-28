# superhero.py

# Base class: Superhero
class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.__power = power  # Encapsulated attribute

    def show_power(self):
        print(f"{self.name}'s power is {self.__power}")

# Derived class: FlyingHero
class FlyingHero(Superhero):
    def __init__(self, name, power, speed):
        super().__init__(name, power)
        self.speed = speed

    def show_power(self):
        print(f"{self.name} flies at {self.speed} km/h using {self._Superhero__power}!")

# Derived class: StrongHero
class StrongHero(Superhero):
    def lift_heavy(self):
        print(f"{self.name} is lifting a huge object using {self._Superhero__power}!")

# Create objects
hero1 = FlyingHero("SkyWing", "Flight", 500)
hero2 = StrongHero("MegaMuscle", "Super Strength")

# Demonstrate methods
hero1.show_power()
hero2.show_power()
hero2.lift_heavy()
