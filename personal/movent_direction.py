"""
http://thepythongamebook.com/en:pygame:step017
"""
import math
import pygame

GRAD = math.pi / 180

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

class Player(object):
    def __init__(self):
        self.x = 25
        self.y = 25
        self.speed = 2.0
        self.turning = 2
        self.angle = 1
        self.dx = 0
        self.dy = 0

    def calculate_position(self):
        dx = math.sin(self.angle) * self.speed
        dy = math.cos(self.angle) * self.speed
        self.x += dx
        self.y += dy
        print 'dx: ', dx, ';   dy: ', dy,';   x: ', self.x, ';   y: ', self.y

p = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ddx = -math.cos(p.angle*GRAD)
                ddy = +math.sin(p.angle*GRAD)

                p.dx += ddx * p.speed
                p.dy += ddy * p.speed

                p.x += p.dx
                p.y += p.dy

            if event.key == pygame.K_RIGHT:
                ddx = +math.cos(p.angle*GRAD)
                ddy = -math.sin(p.angle*GRAD)

                p.dx += ddx * p.speed
                p.dy += ddy * p.speed

                p.x += p.dx
                p.y += p.dy


    # screen, coordinates, x, y, size, thickness
    pygame.draw.circle(screen, (0,0,255), (int(p.x), int(p.y)), 20, 2)
    pygame.display.flip()


    screen.fill((255, 255, 255))

