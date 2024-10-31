import pygame
from game import Game
from button import Button
from textezone import TextZone


pygame.init()

# Define a clock
clock = pygame.time.Clock()
FPS = 60


screen_width, screen_height = 720, 720
# Create a window
pygame.display.set_caption("Jeu d'échecs")
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)


start_local_multi_textzone = TextZone(screen_width//2-125, screen_height//2-25-75, 250, False, "local multi/1v1")
start_local_solo_textzone = TextZone(screen_width//2-125, screen_height//2-25, 250, False, "local solo (WIP)")
start_online_multi_textzone = TextZone(screen_width//2-125, screen_height//2-25+75, 250, False, "online multi/1v1 (WIP)")
start_local_multi_button = Button(start_local_multi_textzone.rect.x, start_local_multi_textzone.rect.y, start_local_multi_textzone.rect.w, start_local_multi_textzone.rect.h)
start_local_solo_button = Button(start_local_solo_textzone.rect.x, start_local_solo_textzone.rect.y, start_local_solo_textzone.rect.w, start_local_solo_textzone.rect.h)
start_online_multi_button = Button(start_online_multi_textzone.rect.x, start_online_multi_textzone.rect.y, start_online_multi_textzone.rect.w, start_online_multi_textzone.rect.h)


running = True

zoom = 1

game = Game(screen_width, screen_height)

which_scene = 0  # 0 for main_menu, 1 for game, -1 for win/loose screen

while running:

    # get the current time in seconds
    current_time = pygame.time.get_ticks()//1000

    # screen_width, screen_height = pygame.display.get_window_size() !!!!!! (to update everywhere ; also in piece)

    if which_scene == 0:
        # background
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, screen_width, screen_height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            pygame.quit()

        if which_scene == 1 and event.type == pygame.MOUSEBUTTONDOWN:  # or event.type == pygame.KEYDOWN:
            game.update(event, zoom)

        elif which_scene == 0 and event.type == pygame.MOUSEBUTTONDOWN:
            if start_local_multi_button.use(event, False):
                game.game_mode = 0  # by default
                which_scene = 1
                sound_game_start = pygame.mixer.Sound("./sounds/game-start.mp3")
                sound_game_start.play()
            elif start_local_solo_button.use(event):
                game.game_mode = 1
                #which_scene = 1
            elif start_online_multi_button.use(event):
                game.game_mode = 2
                #which_scene = 1

    if running:

        if which_scene == 1:
            game.print(screen, zoom)

        elif which_scene == 0:
            start_local_multi_textzone.draw(screen)
            start_local_solo_textzone.draw(screen)
            start_online_multi_textzone.draw(screen)

        # print the current time :
        font = pygame.font.SysFont("ArialBlack", 20)
        text = font.render('Time : {} s'.format(current_time), True, (150, 0, 0))
        screen.blit(text, (10, 5))

    # Update the screen
    if running:
        pygame.display.flip()
        clock.tick(FPS)
