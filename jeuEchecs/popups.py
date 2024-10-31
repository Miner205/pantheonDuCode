import pygame
from button import Button
from textezone import TextZone


class PawnPromotion:
    def __init__(self, x=0, y=0, color="w"):
        self.active = 0
        self.color = color
        self.border_margin = 3
        self.queen_image = pygame.image.load("./images/queen_" + self.color + ".png")
        self.knight_image = pygame.image.load("./images/knight_" + self.color + ".png")
        self.rook_image = pygame.image.load("./images/rook_" + self.color + ".png")
        self.bishop_image = pygame.image.load("./images/bishop_" + self.color + ".png")
        if self.color == "w":
            k = 1
        else:
            k = -1
        self.rect = pygame.Rect(min(self.queen_image.get_width()*8-self.queen_image.get_width()*4-self.border_margin*5, max(0, x-self.queen_image.get_width()*2-self.border_margin*3+self.queen_image.get_width()//2)), y+self.queen_image.get_height()*k+self.border_margin*k,
                                4*self.queen_image.get_width()+self.border_margin*5, self.queen_image.get_height()+self.border_margin*2)
        self.queen_rect = pygame.Rect(self.rect.x+self.border_margin, self.rect.y+self.border_margin, self.queen_image.get_width(), self.rect.h-self.border_margin*2)
        self.knight_rect = pygame.Rect(self.rect.x+self.border_margin*2+self.knight_image.get_width(), self.rect.y+self.border_margin, self.knight_image.get_width(), self.rect.h-self.border_margin*2)
        self.rook_rect = pygame.Rect(self.rect.x+self.border_margin*3+self.rook_image.get_width()*2, self.rect.y+self.border_margin, self.rook_image.get_width(), self.rect.h-self.border_margin*2)
        self.bishop_rect = pygame.Rect(self.rect.x+self.border_margin*4+self.bishop_image.get_width()*3, self.rect.y+self.border_margin, self.bishop_image.get_width(), self.rect.h-self.border_margin*2)

    def update(self, event):
        if self.active and event.type == pygame.MOUSEBUTTONDOWN:
            if self.queen_rect.collidepoint(event.pos):
                self.active = 0
                sound_promote = pygame.mixer.Sound("./sounds/promote.mp3")
                sound_promote.play()
                return "queen"
            elif self.knight_rect.collidepoint(event.pos):
                self.active = 0
                sound_promote = pygame.mixer.Sound("./sounds/promote.mp3")
                sound_promote.play()
                return "knight"
            elif self.rook_rect.collidepoint(event.pos):
                self.active = 0
                sound_promote = pygame.mixer.Sound("./sounds/promote.mp3")
                sound_promote.play()
                return "rook"
            elif self.bishop_rect.collidepoint(event.pos):
                self.active = 0
                sound_promote = pygame.mixer.Sound("./sounds/promote.mp3")
                sound_promote.play()
                return "bishop"

    def print(self, screen):
        if self.active:
            pygame.draw.rect(screen, (230, 230, 230), self.rect)

            pygame.draw.rect(screen, "red", self.queen_rect)
            pygame.draw.rect(screen, "orange", self.knight_rect)
            pygame.draw.rect(screen, "green", self.rook_rect)
            pygame.draw.rect(screen, "blue", self.bishop_rect)

            screen.blit(self.queen_image, self.queen_rect)
            screen.blit(self.knight_image, self.knight_rect)
            screen.blit(self.rook_image, self.rook_rect)
            screen.blit(self.bishop_image, self.bishop_rect)


class ConfirmationPopup:
    def __init__(self, x, y, info_msg):
        self.active = 0
        self.all_button = {"Yes": Button(), "No": Button()}
        self.all_textzone = {"Yes": TextZone(), "No": TextZone(), "InfoMessage": TextZone()}
