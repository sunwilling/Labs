class Vehicle:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
    def get_info(self):
        return self.marka, self.model
class Car(Vehicle):
    def __init__(self, marka, model, fuel_type):
        super().__init__(marka, model)
        self.fuel_type = fuel_type
    def get_info(self):
        return self.marka, self.model, self.fuel_type
car = Car('TAYOTA', 'Bobcat', 95)
print(car.get_info())
