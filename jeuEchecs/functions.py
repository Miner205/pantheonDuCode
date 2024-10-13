# file for definitions of some useful functions
import pygame


def pygame_draw_hashtag(surface, color, center_point, diameter=5, line_thickness=1):
    """draw # ;
    center_point like (x,y)"""
    (x, y), d = center_point, diameter//2
    pygame.draw.line(surface, color, (x-d//2, y-d), (x-d//2, y+d), line_thickness)
    pygame.draw.line(surface, color, (x+d//2, y-d), (x+d//2, y+d), line_thickness)
    pygame.draw.line(surface, color, (x-d, y-d//2), (x+d, y-d//2), line_thickness)
    pygame.draw.line(surface, color, (x-d, y+d//2), (x+d, y+d//2), line_thickness)
