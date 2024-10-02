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

interval = [randint(-499, 0), randint(1, 500)]
mystery_number = randint(interval[0], interval[1])

all_textzone = {"answer_zone": TextZone(center[0]-150, center[1]-16, 300, "entrez un nombre", True),
                "try_counter": TextZone(screen_width-400, 10, 390, "compteur d'essais", False, "0"),
                "find_counter": TextZone(screen_width-400, 10+32+2, 390, "compteur de nombre trouvé", False, "0"),
                "interval": TextZone(center[0]-150, center[1]-16-32-2, 300, "intervalle", False,
                                     str(interval[0])+", "+str(interval[1]))}

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
            answer = all_textzone["answer_zone"].use(event, mystery_number)
            if answer == 1:
                started = current_time
                wave_color = "red"
                more_sound.play()
                tmp = list(all_textzone["try_counter"].user_text)
                tmp[len(tmp)-1] = str(int(tmp[len(tmp) - 1])+1)
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
                interval = [randint(-499, 0), randint(1, 500)]
                mystery_number = randint(interval[0], interval[1])
                all_textzone["interval"].user_text = str(interval[0])+", "+str(interval[1])
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
