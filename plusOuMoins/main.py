import pygame
import functions as fct
from textzone import TextZone
from random import randint


pygame.init()

# Define a clock
clock = pygame.time.Clock()
FPS = 60

# Create a window
screen_width, screen_height = 720, 520
center = (screen_width//2, screen_height//2)
screen = pygame.display.set_mode((screen_width, screen_height))

# load sounds
less_sound = pygame.mixer.Sound("sounds/less.mp3")
more_sound = pygame.mixer.Sound("sounds/more.mp3")
find_sound = pygame.mixer.Sound("sounds/find.mp3")


running = True

started = 0

mystery_number = None
min_i, max_i = None, None

all_textzone = {"answer_zone": TextZone(center[0]-175, center[1]+32, 350, "entrez les bornes min/max", True, answer_mode=True),
                "try_counter": TextZone(screen_width-400, 10, 390, "compteur d'essais", False, "0"),
                "find_counter": TextZone(screen_width-400, 10+32+2, 390, "compteur de nombre trouvé", False, "0"),
                "interval_min": TextZone(center[0]-150, center[1]-6-64, 300, "borne minimum", True),
                "interval_max": TextZone(center[0]-150, center[1]-4-32, 300, "borne maximum", True),
                "interval": TextZone(center[0]-150, center[1]-2, 300, "intervalle", False, "_, _")}

wave_color = "black"

while running:

    # display background
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, screen_width, screen_height))

    # get the current time in milliseconds
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            all_textzone["interval_min"].use(event)
            all_textzone["interval_max"].use(event)
            if all_textzone["interval_min"].user_text != "" and all_textzone["interval_min"].user_text != "-":
                min_i = int(all_textzone["interval_min"].user_text)
            else:
                min_i = None
            if all_textzone["interval_max"].user_text != "" and all_textzone["interval_max"].user_text != "-":
                max_i = int(all_textzone["interval_max"].user_text)
            else:
                max_i = None

            if max_i is not None and min_i is not None:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (all_textzone["interval_min"].active or all_textzone["interval_max"].active):
                    if max_i < min_i:
                        all_textzone["interval_max"].user_text, all_textzone["interval_min"].user_text = all_textzone["interval_min"].user_text, all_textzone["interval_max"].user_text
                        max_i, min_i = min_i, max_i
                    mystery_number = randint(min_i, max_i)
                    all_textzone["answer_zone"].name = "entrez un nombre"
                    all_textzone["try_counter"].user_text = "0"
                    all_textzone["interval"].user_text = str(min_i)+", "+str(max_i)
            else:
                mystery_number = None
                all_textzone["answer_zone"].name = "entrez les bornes min/max"
                all_textzone["interval"].user_text = "_, _"

            answer = all_textzone["answer_zone"].use(event, mystery_number)
            if answer == 1:
                started = current_time
                wave_color = "red"
                more_sound.play()
                tmp = list(all_textzone["try_counter"].user_text)
                tmp[len(tmp) - 1] = str(int(tmp[len(tmp) - 1]) + 1)
                all_textzone["try_counter"].user_text = "".join(tmp)

            elif answer == -1:
                started = current_time
                wave_color = "blue"
                less_sound.play()
                tmp = list(all_textzone["try_counter"].user_text)
                tmp[len(tmp) - 1] = str(int(tmp[len(tmp) - 1]) + 1)
                all_textzone["try_counter"].user_text = "".join(tmp)

            elif answer == 0:
                started = current_time
                wave_color = "green"
                find_sound.play()
                mystery_number = randint(min_i, max_i)
                all_textzone["try_counter"].user_text = "0"
                tmp = list(all_textzone["find_counter"].user_text)
                tmp[len(tmp) - 1] = str(int(tmp[len(tmp) - 1]) + 1)
                all_textzone["find_counter"].user_text = "".join(tmp)

    if running:

        # to do a wave
        if started and current_time-started < max(screen_width, screen_height):
            fct.do_a_circle(screen, wave_color, current_time-started)
        elif current_time-started >= max(screen_width, screen_height):
            started = 0

        # print the current time :
        font = pygame.font.SysFont("ArialBlack", 20)
        text = font.render('Time : {} s'.format(current_time//1000), True, (0, 0, 0))
        screen.blit(text, (10, 5))

        for txt_z in all_textzone.values():
            txt_z.draw(screen)

    # Update the screen
    if running:
        pygame.display.flip()
        clock.tick(FPS)
