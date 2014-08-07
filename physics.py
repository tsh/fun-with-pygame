"""
Pygame physics simulation
http://www.petercollingridge.co.uk/pygame-physics-simulation
"""
import pygame

(width, height) = (300, 200)
background_colour = (255,255,255)

screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)
pygame.display.set_caption('Tutorial 1')

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False