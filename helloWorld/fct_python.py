import pygame
from random import randint


def helloworld_i(screen, i, w, h):
    font = pygame.font.SysFont("ArialBlack", randint(10, 30))
    text = font.render("Hello World n°{}".format(i), True,
                       (randint(0, 240), randint(0, 240), randint(0, 240)))
    screen.blit(text, (randint(10, w-230), randint(10, h-30)))