from math import pi
class Circle:
    def __init__(self, radius):
        self.radius=radius
    def __eq__(self, other):
        return self.radius==other.radius
    def getRadius(self):
        return self.radius
    def setRadius(self, rad):
        self.radius=rad
    def getArea(self):
        return pi*(self.radius**2)
    def getDiameter(self):
        return 2*self.radius
    def getCircumference(self):
        return 2*self.radius*pi
    
