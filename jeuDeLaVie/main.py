import pygame
from game import Game
from button import Button
from tools_menu import ToolsMenu
import functions as fct


pygame.init()

# Define a clock
clock = pygame.time.Clock()
FPS = 60

# Create a window
screen_width, screen_height = 801, 801
center = (screen_width//2, screen_height//2)
screen = pygame.display.set_mode((screen_width, screen_height))

# load sounds
# _sound = pygame.mixer.Sound("")
# load musics

keys_pressed = {}

running = True

zoom = 1.0
zoom_button = Button(screen_width-20-41*2-3, 20, 41, 41)
dezoom_button = Button(screen_width-20-41, 20, 41, 41)

x_slide = 0
y_slide = 0
go_to_center_button = Button(screen_width-20-21-6, 20+47, 27, 27)

game = Game((100, 100))
# game.load_map()

tools_menu = ToolsMenu()



# voir pour faire que le code marche pour toute size de map..

# me : do slides avec les touches flèches directionnels

# draw nb x y on map to verify the nb of cells


while running:

    # display background
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, screen_width, screen_height))

    # // faire un quadrillage
    for w in range(0-int(200*zoom), screen_width+1+int(200*zoom), int(16 * zoom)):
        pygame.draw.line(screen, (0, 0, 0), (w, 0), (w, 1000*zoom), max(1, int(1*zoom)))
        for h in range(0-int(200*zoom), screen_height+1+int(200*zoom), int(16 * zoom)):
            pygame.draw.line(screen, (0, 0, 0), (0, h), (1000*zoom, h), max(1, int(1*zoom)))

        font = pygame.font.SysFont("ArialBlack", int(7*zoom))
        text = font.render('{}'.format((w+int(200*zoom))//int(16 * zoom)), True, (250, 0, 0))
        screen.blit(text, (w+2+x_slide, 403+y_slide))
        screen.blit(text, (403+x_slide, w+2+y_slide))

    pygame.draw.circle(screen, "green", (center[0] + int(x_slide), center[1] + int(y_slide)),
                       5 * zoom)  # to visualize the center

    # get the current time
    current_time = pygame.time.get_ticks()//1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            game.save_map()
            pygame.quit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            game.save_map()
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:  # or event.type == pygame.KEYDOWN:
            tools_menu.update(event)
            # game.update(event)

            if zoom_button.use(event) and zoom < 5.0:
                zoom += 0.5
            if dezoom_button.use(event) and zoom > 0.5:
                zoom -= 0.5
                if x_slide > (1600 * zoom - 800):
                    x_slide = (1600 * zoom - 800)
                if x_slide < -(1600 * zoom - 800):
                    x_slide = -(1600 * zoom - 800)
                if y_slide > (1600 * zoom - 800):
                    y_slide = (1600 * zoom - 800)
                if y_slide < -(1600 * zoom - 800):
                    y_slide = -(1600 * zoom - 800)

            if go_to_center_button.use(event):
                x_slide, y_slide = 0, 0

        if event.type == pygame.KEYDOWN:
            keys_pressed[event.key] = True

        if event.type == pygame.KEYUP:
            keys_pressed[event.key] = False

    if running:
        if keys_pressed.get(pygame.K_DOWN):
            y_slide -= 16*zoom
        if keys_pressed.get(pygame.K_UP):
            y_slide += 16*zoom
        if keys_pressed.get(pygame.K_RIGHT):
            x_slide -= 16*zoom
        if keys_pressed.get(pygame.K_LEFT):
            x_slide += 16*zoom

        if keys_pressed.get(pygame.K_UP) or keys_pressed.get(pygame.K_DOWN) or keys_pressed.get(pygame.K_RIGHT) or keys_pressed.get(pygame.K_LEFT):
            if x_slide > (1600*zoom-800):
                x_slide = (1600*zoom-800)
            if x_slide < -(1600*zoom-800):
                x_slide = -(1600*zoom-800)
            if y_slide > (1600*zoom-800):
                y_slide = (1600*zoom-800)
            if y_slide < -(1600*zoom-800):
                y_slide = -(1600*zoom-800)


        # game.print(screen, zoom)

        # print the current time :
        font = pygame.font.SysFont("ArialBlack", 20)
        text = font.render('Time : {} s'.format(current_time), True, (0, 0, 0))
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
