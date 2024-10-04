import pygame


class TextZone:
    def __init__(self, x, y, width, editing=True, starter_txt="", name=""):
        super().__init__()
        self.text_font = pygame.font.Font(None, 32)
        self.user_text = starter_txt
        self.rect = pygame.Rect(x, y, width, 32)
        self.active = False
        self.editing = editing
        self.name = name

    def use(self, event):

        if self.editing and event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if not self.active:
                    click_effect = pygame.mixer.Sound("sounds/Pen_Clicking.mp3")
                    click_effect.play()
                self.active = True
            else:
                self.active = False

        if self.editing and event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                else:
                    if len(event.unicode) != 0:   # Pour éviter que les touches comme maj ou alt fasse crasher le jeu.
                        self.user_text += event.unicode

    def modify_width(self, new_width):
        self.rect = pygame.Rect(self.rect.x, self.rect.y, new_width, self.rect.height)

    def draw(self, screen):
        if self.active:
            pygame.draw.rect(screen, (255, 255, 255), self.rect, border_radius=3)
            pygame.draw.rect(screen, (255, 220, 0), self.rect, 2, 3)
        else:
            pygame.draw.rect(screen, (255, 255, 255), self.rect, border_radius=3)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2, 3)
        if self.name:
            text_surface = self.text_font.render(self.name + " : " + self.user_text, True, (0, 0, 0))
        else:
            text_surface = self.text_font.render(self.user_text, True, (0, 0, 0))
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
