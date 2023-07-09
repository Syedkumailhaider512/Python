class Car():

    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year
        # Fuel capacity and level in gallons.
        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")

    def drive(self):
        print("The car is moving.")


car = Car('Ferrai', '2X', 2023)

print(car.fill_tank())