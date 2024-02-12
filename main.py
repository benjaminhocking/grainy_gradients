import pygame
import math
from utils import decay, draw_circle, clear, white, poppy, dim_gray, lerp_colour, uranian_blue, cherry_blossom, granular_c_1, granular_c_2, c_1, c_2, c_3, c_4, c_5
import random

class Nucleus:
    def __init__(self, near_colour, far_colour, x, y, radius):
        self.near_colour = near_colour
        self.far_colour = far_colour
        self.x = x
        self.y = y
        self.radius = radius
    
    def euclidean_dist(self, x_1, y_1):
        return math.sqrt((x_1-self.x)**2 + (y_1-self.y)**2)
        
    def p(self, dist):
        return decay(dist)

    def sample(self, x_1, y_1, surface):
        dist = self.euclidean_dist(x_1, y_1)
        prob = self.p(dist)
        if surface.get_at((x_1, y_1))!=white:
            currently = surface.get_at((x_1, y_1))
            if random.random()<prob:
                blended = lerp_colour(currently, self.near_colour, 0.5)
            else:
                blended = lerp_colour(currently, self.far_colour, 0.5)
            #blended = lerp_colour(self.near_colour, currently, 0.2)
            surface.set_at((x_1, y_1), blended)
        else:            
            #we want to always draw a circle, but if prob pass, it is close colour, else far.
            if random.random()<prob:
                surface.set_at((x_1, y_1), self.near_colour)
            else:
                surface.set_at((x_1, y_1), self.far_colour)
        

width = 500
height = 500

pygame.init()
surface = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running = True


n = Nucleus(c_1, c_4, 100,100, 5)
n_1 = Nucleus(c_2, c_3, 300, 300, 5)
n_2 = Nucleus(c_3, c_1, 400, 400, 5)
n_3 = Nucleus(c_4, cherry_blossom, 100, 400, 5)
n_4 = Nucleus(c_5, c_2, 400, 100, 5)


clear(surface, white)

for x in range(width):
    for y in range(height):
        #surface.set_at((x,y), n.sample(x,y))
        n.sample(x,y,surface)
        n_1.sample(x,y,surface)
        n_2.sample(x,y,surface)
        n_3.sample(x,y,surface)
        n_4.sample(x,y,surface)

pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



clock.tick(60)
    
#pygame.quit()