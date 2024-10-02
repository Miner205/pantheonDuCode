# file for definitions of some useful functions
import time

import pygame


def pygame_draw_plus(surface, color, center_point, diameter=5, line_thickness=1):
    """draw + ;
    center_point like (x,y)"""
    (x, y), d = center_point, diameter//2
    pygame.draw.line(surface, color, (x, y-d), (x, y+d), line_thickness)
    pygame.draw.line(surface, color, (x-d, y), (x+d, y), line_thickness)


def pygame_draw_minus(surface, color, center_point, diameter=5, line_thickness=1):
    """draw - ;
    center_point like (x,y)"""
    (x, y), d = center_point, diameter//2
    pygame.draw.line(surface, color, (x-d, y), (x+d, y), line_thickness)


def do_a_circle(surface, color, r):
    """to do a 'wave' from the center of the screen to the border of the screen"""
    w, h = pygame.display.get_window_size()
    center = (w//2, h//2)
    pygame.draw.circle(surface, color, center, r, 5)
