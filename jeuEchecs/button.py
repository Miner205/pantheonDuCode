import pygame


class Button:
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)

    def use(self, event, click_sound=True):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if click_sound:
                    click_effect = pygame.mixer.Sound("./sounds/Pen_Clicking.mp3")
                    click_effect.play()
                return True

    def modify_width(self, new_width):
        self.rect = pygame.Rect(self.rect.x, self.rect.y, new_width, self.rect.height)

    def print(self, screen, opacity=255):
        pygame.draw.rect(screen, (0, 140, 190, opacity), self.rect, border_radius=3)
