import pygame
from game import Game


pygame.init()

# Define a clock
clock = pygame.time.Clock()
FPS = 60


screen_width, screen_height = 720, 720
# Create a window
pygame.display.set_caption("Jeu d'échecs")
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)


running = True

zoom = 1.0

game = Game(screen_width, screen_height)

game_started = 0

while running:

    # get the current time in seconds
    current_time = pygame.time.get_ticks()//1000

    if not game_started:
        # background
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, screen_width, screen_height))
        start_solo_button_button.print(screen)
        start_local_multi_button.print(screen)
        start_online_multi_button.print(screen)
        #+ reprendre partie en cours button ?

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            pygame.quit()

        if game_started and event.type == pygame.MOUSEBUTTONDOWN:  # or event.type == pygame.KEYDOWN:

            game.update(event, zoom)

    if running:

        game.print(screen, zoom)

        # print the current time :
        font = pygame.font.SysFont("ArialBlack", 20)
        text = font.render('Time : {} s'.format(current_time), True, (150, 0, 0))
        screen.blit(text, (10, 5))

    # Update the screen
    if running:
        pygame.display.flip()
        clock.tick(FPS)
