from operator import index
import random as rd

NUM_PARTICLES = 1

# define two dimentional vector
class vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def vec(self):
        return (self.x, self.y)

# two dimentional particle
class Particle:
    def __init__(self, position, velocity, mass):
        pos = vector2(x=position[0], y=position[1])
        self.position = pos.vec()
        vel = vector2(x=velocity[0], y=velocity[1])
        self.velocity = vel.vec()
        self.mass = mass

particles = [[[rd.randint(0, 50), rd.randint(0, 50)], [0, 0], 1]]

def PrintParticles():
    for i in particles:
        particle = Particle(position=i[0], velocity=i[1], mass=i[2])

        print(f"Particle[{particles.index(i)}] {particle.position}")

PrintParticles()
        

