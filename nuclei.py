import pygame
import math
from utils import decay, draw_circle, clear, white, poppy, dim_gray, lerp_colour, uranian_blue, cherry_blossom, granular_c_1, granular_c_2, c_1, c_2, c_3, c_4, c_5, get_colour, noise
import random
from pygame import Color

nuclei = [
    {
        "x": 100,
        "y": 100,
        "colour": Color(43, 69, 96)
    },
    {
        "x":250,
        "y":250,
        "colour": Color(190,126,116)
    },
    {
        "x": 400,
        "y": 400,
        "colour": Color(185,86,112)
    }
]

width = 1000
height = 1000

pygame.init()
surface = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running = True

for x in range(width):
    for y in range(height):
        c = get_colour(nuclei, x, y)
        surface.set_at((x,y), c)

noise(surface)

pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.image.save(surface, "my_image.jpeg")
"""
img = Image.fromstring('RGBA', (width,height), data)
zdata = StringIO()
img.save(zdata, 'JPEG')
print(zdata.getvalue())"""