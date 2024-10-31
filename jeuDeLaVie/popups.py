import pygame
from button import Button
from textezone import TextZone
from toggle import Toggle


class ConfirmationPopup:  # SaveMapSecurityPopup
    def __init__(self, x, y, info_msg):
        self.active = 0
        self.all_button = {"Yes": Button(),
                           "No": Button()}
        self.all_textzone = {"Yes": TextZone(),
                             "No": TextZone(),
                             "InfoMessage": TextZone()}

    def use(self):

    def print(self, screen):
        if self.active:
            pygame.draw.rect(screen, (230, 230, 230), self.rect)

            for textzone in self.all_textzone.values():
                textzone.draw(screen)

class IntegrationOptionsPopup:
    def __init__(self, x, y, ):
        self.active = 0
        self.all_button = {"DefaultCoords_topleft": Button(),
                           "CustomCoords_topleft": Button()}
        self.all_textzone = {"DefaultCoords": TextZone(),
                             "CustomCoords": TextZone()}
        self.all_toggle = {"ResetMap": Toggle(),
                           "100x100": Toggle(),
                           "200x200": Toggle(),
                           "500x500": Toggle()}
        self.all_toggle_state = {"ResetMap": True, "100x100": True, "200x200": False, "500x500": False}
