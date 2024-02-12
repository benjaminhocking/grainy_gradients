import numpy as np
import pygame
from pygame import Color
import random
import math

white = Color(255, 255, 255, 255)
black = Color(0,0,0,255)
poppy = Color(211, 62, 67, 255)
dim_gray = Color(102, 99, 112, 100)
uranian_blue = Color(184, 225, 255, 255)
cherry_blossom = Color(232, 174, 183, 100)
granular_c_1 = Color(81,177,176,255)
granular_c_2 = Color(37,96,164,255)

c_1 = Color(127, 17, 224, 255)
c_2 = Color(144, 124, 255,255)
c_3 = Color(242, 55, 31,255)
c_4 = Color(255, 199, 0,255)
c_5 = Color(0, 197, 223,255)

def normal(d, mu, sig):
    #make a normal distribution with mu, sig, and then take generate a probability of d
    pass

def decay(d):
    if d==0:
        return 1
    else:
        return 1/(d**0.5)
    
def draw_circle(surface, r, x, y, colour):
    for x_r in range(-r, r):
        for y_r in range(-r, r):
            if(x_r**2+y_r**2<r**2):
                surface.set_at((x+x_r, y+y_r), colour)
    return

def clear(surface, colour):
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            surface.set_at((x,y), colour)
            
def lerp_colour(c1, c2, k):
    return c1.lerp(c2, k)

def euclidean_dist(x, y, x_1, y_1):
    return math.sqrt((x_1-x)**2+(y_1-y)**2)

def total_dist(cdp):
    s = 0
    for p in cdp:
        s+=p["dist"]
    return s

def get_colour(nuclei, x, y):
    #initially we will ignore the problems that arise with averaging RGB colours. later we can move to lab space.
    #core idea of this function:
    #   set colour to weighted (by distance) average of all colours of nuclei.
    cdp = [] #[{"colour":<> ,"dist":<>},...]
    for nucleus in nuclei:
        dist_m = euclidean_dist(nucleus["x"], nucleus["y"], x, y)
        cdp.append({"colour":nucleus["colour"], "dist":dist_m})
    tot = total_dist(cdp)
    #now add some noise to the colour generation
    #many ways of doing this: 
    #   preferentially increase contibution of one colour
    #   small probability of choosing the colour randomly from all nuclei
    if random.random()<0.05:
        # build proximity weighted distribution and pick one colour
        probs = [x["dist"]/tot for x in cdp]
        draw = np.random.choice([i for i in range(len(nuclei))], 1, p=probs)
        c = nuclei[draw[0]]["colour"]
        c.a = 150
        return c
    c = [0,0,0]
    for p in cdp:
        c[0]+=(p["colour"].r)*(p["dist"]/tot)
        c[1]+=(p["colour"].g)*(p["dist"]/tot)
        c[2]+=(p["colour"].b)*(p["dist"]/tot)
    return Color(int(c[0]), int(c[1]), int(c[2]), 255)

def noise(surface):
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            if random.random()<0.5:
                c = surface.get_at((x,y))
                c.a = 0
                surface.set_at((x,y), c)