"""
Pygame physics simulation
http://www.petercollingridge.co.uk/pygame-physics-simulation
"""
import pygame


class Particle:
    def __init__(self, (x, y), size):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 1

    def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)

(width, height) = (300, 200)
background_colour = (255,255,255)

screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)
pygame.display.set_caption('Ph sim')

my_first_particle = Particle((150, 50), 15)
my_first_particle.display()

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False