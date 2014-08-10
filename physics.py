"""
Pygame physics simulation
http://www.petercollingridge.co.uk/pygame-physics-simulation
"""
import random
import math

import pygame


background_colour = (255,255,255)
(width, height) = (400, 400)

# Sim constants
gravity = (math.pi, 0.002)
number_of_particles = 1
drag = 0.999  # air resistance - the faster a particle is moving, the more speed is lost.
elasticity = 0.75 # loss of speed a particle experiences when it hits a boundary.

def addVectors((angle1, length1), (angle2, length2)):
    """ Takes two vectors (each an angle and a length), and returns single, combined a vector."""
    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.cos(angle2) * length2
    length = math.hypot(x, y)
    angle = 0.5 * math.pi - math.atan2(y, x)
    return angle, length


class Particle():
    def __init__(self, (x, y), size):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 1
        self.speed = 0
        self.angle = 0

    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    def move(self):
        (self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
        self.speed *= drag
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

    def bounce(self):
        """
         check whether particle move beyond the window boundary,
         and change it coordinates appropriately.
         """
        # Calculate by how much particle has exceeded the boundary
        # d = self.x - (width - self.size)
        # then reflect the position in the boundary (i.e. bounce it)
        # self.x = (width - self.size) - d
        # This simplifies to:
        # self.x = 2*(width - self.size) - self.x

        if self.x > width - self.size:
            self.speed *= elasticity
            self.x = 2*(width - self.size) - self.x
            self.angle = - self.angle

        elif self.x < self.size:
            self.speed *= elasticity
            self.x = 2*self.size - self.x
            self.angle = - self.angle

        if self.y > height - self.size:
            self.speed *= elasticity
            self.y = 2*(height - self.size) - self.y
            self.angle = math.pi - self.angle

        elif self.y < self.size:
            self.speed *= elasticity
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pygame')

my_particles = []

for n in range(number_of_particles):
    size = random.randint(10, 20)
    x = random.randint(size, width-size)
    y = random.randint(size, height-size)

    particle = Particle((x, y), size)
    particle.speed = random.random()
    particle.angle = random.uniform(0, math.pi*2)

    my_particles.append(particle)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_colour)

    for particle in my_particles:
        particle.move()
        particle.bounce()
        particle.display()
    pygame.display.flip()