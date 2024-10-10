import pygame
import functions as fct


class Toggle:
    def __init__(self, x, y, name, state, width, height=32, text_color=(0, 0, 0)):
        self.name = name
        self.toggle_state = state
        self.text_font = pygame.font.Font(None, 32)
        self.rect = pygame.Rect(x, y, width, height)
        self.rect_check = pygame.Rect(self.rect.x+self.rect.w-(self.rect.h-4), self.rect.y+4, self.rect.h-8, self.rect.h-8)
        self.text_color = text_color

    def use(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect_check.collidepoint(event.pos):
                click_effect = pygame.mixer.Sound("./sounds/Pen_Clicking.mp3")
                click_effect.play()
                self.toggle_state = not self.toggle_state

    def modify_width(self, new_width):
        self.rect = pygame.Rect(self.rect.x, self.rect.y, new_width, self.rect.height)
        self.rect_check = pygame.Rect(self.rect.x+self.rect.w-(self.rect.h-4), self.rect.y+4, self.rect.h-8, self.rect.h-8)

    def print(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect, border_radius=3)  # use directly a textzone ?
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2, 3)
        text_surface = self.text_font.render(self.name, True, self.text_color)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

        pygame.draw.rect(screen, (0, 0, 100), self.rect_check, 2)
        if self.toggle_state:
            fct.pygame_draw_check(screen, (0, 255, 0), self.rect_check.center, self.rect_check.w*3/5, 3)
