# Author: JD 04/13/2022
import math

class Circle:
    def __init__(self):
        self.radius = 3
    def get_diameter(self):
        return self.radius * 2
    def get_area(self):
        return self.radius**2 * math.pi

my_circle = Circle()

print(my_circle.get_area())