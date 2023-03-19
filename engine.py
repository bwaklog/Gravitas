from operator import index
import random as rd
import time
import numpy as np

NUM_PARTICLES = 2

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
        self.position = vector2(x=position[0], y=position[1]).vec()
        self.velocity = vector2(x=velocity[0], y=velocity[1]).vec()
        self.mass = mass


particles = []


def PrintParticles():
    for i in range(NUM_PARTICLES):
        particle = particles[i]
        print(
            f"Particle[{i}] {particle.position}, {particle.velocity}, {particle.mass}")
        # print(f"Particle[{i}] {particle.position}")


def InitializeParticles():
    for _ in range(NUM_PARTICLES):
        particle = Particle(
            position=vector2(x=rd.randint(0, 50), y=rd.randint(0, 50)).vec(),
            velocity=vector2(x=0, y=0).vec(),
            mass=1
        )
        particles.append(particle)


def ComputeForce(particle):
    force = vector2(x=0, y=particle.mass * -9.81)
    return force


def RunSimulation():
    totalSimulationTime = 10  # simulation length is 10 seconds
    currentTime = 0  # simulation starts at time = 0
    dt = 0.5  # each step is 1 second

    InitializeParticles()
    PrintParticles()

    while currentTime < totalSimulationTime:
        time.sleep(dt)

        for i in range(NUM_PARTICLES):
            particle = particles[i]
            force = ComputeForce(particle).vec()
            acceleration = vector2(
                x=force[0],
                y=force[1]/particle.mass
            ).vec()
            # print(acceleration)
            # print(f"x: {particle.position[0]}, {particle.velocity[0]}")
            # print(f"y: {particle.position[1], particle.velocity[1]}")
            # vel_x
            particle.velocity[0] += acceleration[0] * dt
            # vel_y
            particle.velocity[1] += acceleration[1] * dt
            # pos_x
            particle.position[0] += particle.velocity[0] * dt
            # pos_y
            particle.position[1] += particle.velocity[1] * dt

        PrintParticles()
        currentTime += dt


# RunSimulation()

NUM_RIGID_BODIES = 1

class BoxShape:
    def __init__(self, width, height, mass):
        self.width = width
        self.height = height
        self.mass = mass

        moi = mass * (width**2 * height**2) / 12
        self.momentOfInertia = moi

#def CalculateBoxInertia(boxShape):
#    m = boxShape.mass
#    w = boxShape.width
#    h = boxShape.height
#    boxShape.momentOfInertia = m * (w**2 + h**2) / 12
#    return boxShape.momentOfInertia

class RigidBody:
    def __init__(self, position, linearVelocity, angle, angularVelocity, force, torque, shape):
        self.position = vector2(x=position[0], y=position[1]).vec()
        self.linearVelocity = vector2(x=linearVelocity[0], y=linearVelocity[1]).vec()
        self.angle = angle
        self.angularVelocity = angularVelocity
        self.force = vector2(x=force[0], y=force[1]).vec()
        self.torque = torque
        self.shape = BoxShape(width=shape[0], height=shape[1], mass=1)

rigidBodies = []

def PrintRigidBodies():
    for i in range(NUM_RIGID_BODIES):
        rigidBody = rigidBodies[i]
        print(f"body[{i}] p = {rigidBody.position} | a = {rigidBody.angle}")
        print(f"    ↪ f = {rigidBody.force} | t = {rigidBody.torque}")
        
def InitializeRigidBodies():
    for _ in range(NUM_RIGID_BODIES):
        rigidBody = RigidBody(
               position=vector2(x=rd.randint(0, 50), y=rd.randint(0, 50)).vec(),
               linearVelocity=[0, 0],
               angle=(rd.randint(0, 360))/360 * np.pi,
               angularVelocity=0,
               force=vector2(x=0, y=0).vec(),
               torque=0,
               shape=[1 + rd.randint(0, 2), 1 + rd.randint(0, 2), 1]
               )
        
        rigidBodies.append(rigidBody)

def ComputeForceAndTorque(rigidBody):
    f = vector2(x=0, y=100)
    rigidBody.force[0], rigidBody.force[1] = f.x, f.y

    r = vector2(x=rigidBody.shape.width / 2, y=rigidBody.shape.height /2)
    rigidBody.torque = r.x * f.y - r.y * f.x

#InitializeRigidBodies()
#PrintRigidBodies()
#ComputeForceAndTorque(rigidBodies[0])
#PrintRigidBodies()

def RunRigidBodySimulation():
    totalSimulationTime = 10
    currentTime = 0
    dt = 0

    InitializeRigidBodies()
    PrintRigidBodies()

