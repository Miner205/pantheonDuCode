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


def pygame_draw_square(surface, color, top_left_pos, side_length, line_thickness=0):
    """draw a square ;
        left_middle_pos & right_middle_pos like (x,y) & (x,y2)"""
    (x, y) = top_left_pos
    pygame.draw.polygon(surface, color, [(x, y), (x+side_length, y), (x, y+side_length),
                                         (x+side_length, y+side_length)], line_thickness)
