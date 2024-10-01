import pygame
from random import randint

print("HelloWorld!")


def helloworld_i(screen, i, w, h):
    font = pygame.font.SysFont("ArialBlack", randint(10, 30))
    text = font.render("Hello World n°{}".format(i), True, (0, 0, 0))
    screen.blit(text, (randint(10, w-230), randint(10, h-30)))


pygame.init()

w, h = pygame.display.get_desktop_sizes()[0]
w, h = w-100, h-100
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
running = True
do_once = 1

while running:

    if do_once:
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, w, h))
        for j in range(1, 101):
            helloworld_i(screen, j, w, h)
            do_once = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            pygame.quit()

    if running:
        pygame.display.flip()
        clock.tick(60)
