from operator import index
import random as rd
import time

NUM_PARTICLES = 1

# define two dimentional vector
class vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def vec(self):
        return [self.x, self.y]

# two dimentional particle
class Particle:
    def __init__(self, position, velocity, mass):
        pos = vector2(x=position[0], y=position[1])
        self.position = pos.vec()
        vel = vector2(x=velocity[0], y=velocity[1])
        self.velocity = vel.vec()
        self.mass = mass

# particles = [[[rd.randint(0, 50), rd.randint(0, 50)], [0, 0], 1]]
particles = []

def PrintParticles():
    for i in range(NUM_PARTICLES):
        # particle = Particle(position=i[0], velocity=i[1], mass=i[2])
        particle = particles[i]
        # print(f"Particle[{i}] {particle.position}, {particle.velocity}, {particle.mass}")
        print(f"Particle[{i}] {particle.position}")

def InitializeParticles():
    for i in range(NUM_PARTICLES):
        particle = Particle(
               position=vector2(x=rd.randint(0, 50), y=rd.randint(0, 50)).vec(),
               velocity=vector2(x=0, y=0).vec(),
               mass=1
               )
        particles.append(particle)

def ComputeForce(particle):
    force = vector2(x=0, y=particle.mass * -9.81)
    return force.vec()

def RunSimulation():
    totalSimulationTime = 10 # simulation length is 10 seconds
    currentTime = 0 # simulation starts at time = 0
    dt = 1 # each step is 1 second

    InitializeParticles()
    PrintParticles()

    while currentTime < totalSimulationTime:
        time.sleep(dt)
        
        for i in range(NUM_PARTICLES):
            particle = particles[i]
            force = ComputeForce(particle)
            acceleration = vector2(
                    x=force[0],
                    y=force[1]/particle.mass
                    ).vec()
            #print(acceleration)
            #print(f"x: {particle.position[0]}, {particle.velocity[0]}")
            #print(f"y: {particle.position[1], particle.velocity[1]}")
            # vel_x
            particle.velocity[0] += acceleration[0] * dt
            #vel_y
            particle.velocity[1] += acceleration[1] * dt
            # pos_x
            particle.position[0] += particle.velocity[0] * dt
            # pos_y
            particle.position[1] += particle.velocity[1] * dt

        PrintParticles()
        currentTime += dt

RunSimulation()
