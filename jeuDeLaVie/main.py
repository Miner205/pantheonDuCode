import pygame
from game import Game
from button import Button
from tools_menu import ToolsMenu
import functions as fct


pygame.init()

# Define a clock
clock = pygame.time.Clock()
FPS = 60

# load sounds
# _sound = pygame.mixer.Sound("")
# load musics


nb_of_cells = 100
cell_size = 8


screen_width, screen_height = nb_of_cells*(cell_size+1), nb_of_cells*(cell_size+1)
# Create a window
pygame.display.set_caption("Jeu de la vie")
screen = pygame.display.set_mode((screen_width, screen_height))


running = True

zoom = 1.0
zoom_button = Button(screen_width-20-41*2-3, 20, 41, 41)
dezoom_button = Button(screen_width-20-41, 20, 41, 41)

go_to_center_button = Button(screen_width-20-27, 20+47, 27, 27)

game = Game((nb_of_cells, nb_of_cells), cell_size, screen_width, screen_height)

tools_menu = ToolsMenu()

k = 0



# voir pour faire que le code marche pour toute size de map..




while running:

    # display background
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, screen_width, screen_height))

    # get the current time in seconds
    current_time = pygame.time.get_ticks()//1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:  # or event.type == pygame.KEYDOWN:

            if zoom_button.use(event) and zoom < 5:
                zoom += 1
                k = 1
            if dezoom_button.use(event) and zoom > 1:
                zoom -= 1
                k = 1

            if go_to_center_button.use(event):
                game.x_slide, game.y_slide = 0, 0

            if not (zoom_button.rect.collidepoint(event.pos) or dezoom_button.rect.collidepoint(event.pos) or
                    go_to_center_button.rect.collidepoint(event.pos) or (tools_menu.which_submenu[0] != '0' and tools_menu.rect.collidepoint(event.pos))
                    or game.grille_button.rect.collidepoint(event.pos) or game.reset_button.rect.collidepoint(event.pos)
                    or game.play_pause_button.rect.collidepoint(event.pos) or game.next_button.rect.collidepoint(event.pos)):
                game.update(event, zoom)

            if game.grille_button.use(event):
                game.mode_grille += 1
                if game.mode_grille >= 3:
                    game.mode_grille = 0
            if game.reset_button.use(event):
                game.empty_map()
                game.iteration = 0
            if game.play_pause_button.use(event):
                game.play_pause_button_state = not game.play_pause_button_state
            if game.next_button.use(event):
                game.next_iteration()

            tools_menu.update(event)

        if event.type == pygame.KEYDOWN:
            game.keys_pressed[event.key] = True

        if event.type == pygame.KEYUP:
            game.keys_pressed[event.key] = False

    if running:
        game.run(zoom, k)
        k = 0

        game.print(screen, zoom)

        # print the current time :
        font = pygame.font.SysFont("ArialBlack", 20)
        text = font.render('Time : {} s'.format(current_time), True, (150, 0, 0))
        screen.blit(text, (10, 5))

        # print zoom/dezoom buttons :
        pygame.draw.rect(screen, (210, 210, 210), (screen_width - 20 - 82 - 6, 20 - 3, 82 + 9, 41 + 6), border_radius=3)
        zoom_button.print(screen)
        fct.pygame_draw_plus(screen, (130, 0, 0), zoom_button.rect.center, zoom_button.rect.w - 10, 5)
        dezoom_button.print(screen)
        fct.pygame_draw_minus(screen, (130, 0, 0), dezoom_button.rect.center, dezoom_button.rect.w - 10, 5)
        # print the zoom :
        font = pygame.font.SysFont("ArialBlack", 15)
        text = font.render('x{}'.format(zoom), True, (0, 0, 0))
        screen.blit(text, (screen_width - 85, -3))
        # print go to center button :
        go_to_center_button.print(screen)
        pygame.draw.circle(screen, (130, 0, 0), go_to_center_button.rect.center, 5)

        # print Tools menu :
        tools_menu.print(screen)

    # Update the screen
    if running:
        pygame.display.flip()
        clock.tick(FPS)
