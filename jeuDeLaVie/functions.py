# file for definitions of some useful functions
import pygame
import os


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


def pygame_draw_square(surface, color, top_left_pos, side_length, zoom, line_thickness=0):  # same than pygame.draw.rect ? : yes probably
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


def pygame_draw_left_arrow(surface, color, left_middle_pos, right_middle_pos, line_thickness=0):
    """draw a left arrow ;
        left_middle_pos & right_middle_pos like (x,y) & (x2,y)"""
    (x, y), x2 = left_middle_pos, right_middle_pos[0]
    d = (x2-x)//2
    pygame.draw.polygon(surface, color, [(x, y), (x2, y-d), (x2, y+d)], line_thickness)


def pygame_draw_right_arrow(surface, color, left_middle_pos, right_middle_pos, line_thickness=0):
    """draw a right arrow ;
        left_middle_pos & right_middle_pos like (x,y) & (x2,y)"""
    (x, y), x2 = left_middle_pos, right_middle_pos[0]
    d = (x2-x)//2
    pygame.draw.polygon(surface, color, [(x2, y), (x, y-d), (x, y+d)], line_thickness)


def pygame_draw_pause(surface, color, left_middle_pos, right_middle_pos, line_thickness=1):
    """draw pause symbol ;
    left_middle_pos & right_middle_pos like (x,y) & (x2,y)"""
    (x, y), x2 = left_middle_pos, right_middle_pos[0]
    d = (x2-x)//2
    pygame.draw.line(surface, color, (x+2*d//5, y-d), (x+2*d//5, y+d), line_thickness)
    pygame.draw.line(surface, color, (x2-2*d//5-1, y-d), (x2-2*d//5-1, y+d), line_thickness)


def pygame_draw_hashtag(surface, color, center_point, diameter=5, line_thickness=1):
    """draw # ;
    center_point like (x,y)"""
    (x, y), d = center_point, diameter//2
    pygame.draw.line(surface, color, (x-d//2, y-d), (x-d//2, y+d), line_thickness)
    pygame.draw.line(surface, color, (x+d//2, y-d), (x+d//2, y+d), line_thickness)
    pygame.draw.line(surface, color, (x-d, y-d//2), (x+d, y-d//2), line_thickness)
    pygame.draw.line(surface, color, (x-d, y+d//2), (x+d, y+d//2), line_thickness)


def pygame_draw_cross(surface, color, center_point, diameter=5, line_thickness=1):  # replace it by reset symbol ?
    """draw X ;
    center_point like (x,y)"""
    (x, y), d = center_point, diameter//2
    pygame.draw.line(surface, color, (x-d, y-d), (x+d, y+d), line_thickness)
    pygame.draw.line(surface, color, (x+d, y-d), (x-d, y+d), line_thickness)


def pygame_draw_check(surface, color, center_point, diameter=5, line_thickness=1):
    """draw check mark ;
    center_point like (x,y)"""
    (x, y), d = center_point, diameter//2
    pygame.draw.line(surface, color, (x+d, y-d), (x-d+d*1/2, y+d), line_thickness)
    pygame.draw.line(surface, color, (x-d*5/3+d*1/2, y), (x-d+d*1/2, y+d), line_thickness)


def old_map_size(filename):
    if os.path.exists("./"+filename+".txt"):
        temp = []
        with open("./"+filename+".txt", 'r') as f:
            line = f.readline()
            while line != "":
                if line.strip('\n').split(';') != ['0']:
                    nb_col = len(line.strip('\n').split(';'))
                temp.append(line.strip('\n').split(';'))
                line = f.readline()
        nb_row = len(temp)

        return nb_row, nb_col


def find_old_coords_topleft(filename):
    if os.path.exists("./"+filename+".txt"):
        temp = []
        non_empty_rows = []
        with open("./"+filename+".txt", 'r') as f:
            line = f.readline()
            while line != "":
                if line.strip('\n').split(';') != ['0']:
                    nb_col = len(line.strip('\n').split(';'))
                    non_empty_rows.append(line.strip('\n').split(';'))
                temp.append(line.strip('\n').split(';'))
                line = f.readline()
        nb_row = len(temp)
        i = 0
        while i < nb_row and temp[i] == ['0']:
            i += 1
        old_row = i
        for i in range(len(non_empty_rows)):
            j = 0
            while j < len(non_empty_rows[0]) and non_empty_rows[i][j] != '1':
                j += 1
            non_empty_rows[i] = len(non_empty_rows[i][:j])
        old_col = min(non_empty_rows)

        return old_row, old_col  # need in x and y (=inverse row&col) or not ??
