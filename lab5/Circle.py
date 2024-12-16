class Circle:
    def __init__ (self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius
circle = Circle(3)
print(circle.get_radius())
circle.set_radius(30)
print(circle.get_radius())
