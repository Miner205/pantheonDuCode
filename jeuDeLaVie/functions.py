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


def pygame_draw_square(surface, color, top_left_pos, side_length, zoom, line_thickness=0):
    """draw a square ;
        top_left_pos like (x,y)"""
    (x, y) = top_left_pos[0]+max(1, 1*zoom/2), top_left_pos[1]+max(1, 1*zoom/2)
    side_length -= max(2, 2*zoom/2)
    pygame.draw.polygon(surface, color, [(x, y), (x, y+side_length), (x+side_length, y+side_length),
                                         (x+side_length, y)], line_thickness)


def pygame_rect_square(top_left_pos, side_length):
    """rect og a square ;
        top_left_pos like (x,y)"""
    (x, y) = top_left_pos
    return pygame.Rect(x, y, side_length, side_length)
