import pygame


class TextZone:
    def __init__(self, x, y, width, name, editing=True, starter_txt="", answer_mode=False):
        super().__init__()
        self.text_font = pygame.font.Font(None, 32)
        self.name = name
        self.user_text = starter_txt
        self.rect = pygame.Rect(x, y, width, 32)
        self.active = False
        self.editing = editing
        self.answer_mode = answer_mode

    def use(self, event, mystery_number=None):

        if self.editing and event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if not self.active:
                    click_effect = pygame.mixer.Sound("sounds/Pen_Clicking.mp3")
                    click_effect.set_volume(0.5)
                    click_effect.play()
                self.active = True
            else:
                self.active = False

        if self.editing and event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                elif self.answer_mode and event.key == pygame.K_RETURN and len(self.user_text) != 0:
                    if mystery_number is None:
                        self.name = "entrez les bornes min/max"
                    elif mystery_number == int(self.user_text):
                        self.user_text = ""
                        self.name = "entrez un nombre"
                        return 0
                    elif mystery_number > int(self.user_text):
                        self.user_text = ""
                        self.name = "c'est plus"
                        return 1
                    else:
                        self.user_text = ""
                        self.name = "c'est moins"
                        return -1
                else:
                    if len(event.unicode) != 0:   # Pour éviter que les touches comme maj ou alt fasse crasher le jeu.
                        if ord('0') <= ord(event.unicode) <= ord('9') or (event.unicode == '-' and len(self.user_text) == 0):
                            self.user_text += event.unicode

    def draw(self, screen):
        if self.active:
            pygame.draw.rect(screen, (255, 255, 255), self.rect, border_radius=3)
            pygame.draw.rect(screen, (255, 220, 0), self.rect, 2, 3)
        else:
            pygame.draw.rect(screen, (255, 255, 255), self.rect, border_radius=3)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2, 3)
        if self.answer_mode:
            text_surface = self.text_font.render(self.name + " : " + self.user_text, True, (180, 0, 0))
        else:
            text_surface = self.text_font.render(self.name+" : "+self.user_text, True, (0, 0, 0))
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
