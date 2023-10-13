import turtle
import random
import math
class Rational:
    def __init__(self,num=0,den=1):
        self.numerator = num
        if den == 0:
            self.denominator = 1
        else:
            self.denominator = den
    def __str__(self):
            return str(self.numerator) + '/' + str(self.denominator) if (self.denominator != 1 and self.numerator != 0) else str(self.numerator)
class Vec2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f'<{self.x}, {self.y}>'
    def get_values(self):
        return [self.x, self.y]
    def set_values(self, lis):
        self.x = lis[0]
        self.y = lis[1]
    def __add__(self, right):
        return Vec2(self.x+right.x, self.y+right.y)
    def __mul__(self, scalar):
        return Vec2(self.x*scalar, self.y*scalar)
class Particle:
    def __init__(self, mass=0.0, position=Vec2(), velocity=Vec2()):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.particle = turtle.Turtle()
        self.particle.shape("circle")
        self.screen = turtle.Screen()
        self.particle.penup()
        self.particle.speed = 0
        self.particle.setpos(self.position.x, self.position.y)
        self.particle.pendown()
        self.force = 0
        self.force_x = 0
        self.force_y = 0
    def move(self):
        self.particle.setpos(self.position.x, self.position.y)
    def __str__(self):
        return f'mass:{self.mass}, pos:<{self.position.x}, {self.position.y}>, vel:<{self.velocity.x}, {self.velocity.y}>'
    def accelerate(self, a, t):
        self.position.x += ((self.velocity.x*t) + (.5*a.x*(t**2)))
        self.position.y += ((self.velocity.y*t) + (.5*a.y*(t**2)))
        self.velocity.x += (a.x*t)
        self.velocity.y += (a.y*t)
        self.move()

def main():
    particles = []
    turtle.tracer(0)
    g = 999 # .00000000667408
    for i in range(random.randint(10, 20)):
        particles.append(Particle(random.randint(1, 10), Vec2(random.randint(-200, 200), random.randint(-200, 200)), Vec2(random.randint(-50, 50), random.randint(-50, 50))))
    for particle in particles:
        force = 0
        ang = 0
        for particle2 in particles:
            if particle2 == particle:
                continue
            try:
                ang = math.atan((particle2.position.y-particle.position.y)/(particle2.position.x-particle.position.x))
                distance = math.sqrt(((particle2.position.x-particle.position.x)**2)+((particle2.position.y-particle.position.y)**2))
                force+=(g*((particle.mass*particle2.mass)/(distance**2)))
            except:
                pass
        particle.force = force
        particle.force_x = force*math.cos(ang)
        particle.force_y = force*math.sin(ang)
    while True:
        for particle in particles:
            for i in range(100):
                particle.accelerate(Vec2(particle.force_x/particle.mass, particle.force_y/particle.mass), .1)
                turtle.update()

    
    screen = turtle.Screen()
    screen.mainloop()

if __name__ == "__main__":
    main()